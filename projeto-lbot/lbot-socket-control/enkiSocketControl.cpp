/*
    Exemplo de Con#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace Enki; via Socket - Enki
    
    Este exemplo demonstra como controlar um robô E-Puck via socket TCP.
    O programa cria uma simulação gráfica onde o robô se move em um plano
    e recebe comandos de movimento de um cliente externo via socket.
    
    Comandos aceitos via socket:
    - "XF;YB;ZL;WR" - sequência de movimentos (ex: "10F;5R" = 10 unidades frente + 5 unidades direita)
        F = Forward (frente), B = Backward (trás), L = Left (esquerda), R = Right (direita)
    - "stop" - para o robô
    - "status" - retorna posição e orientação atual
    - "quit" - encerra o programa
    
    Exemplos:
    - "10F" - move 10 unidades para frente
    - "5B;3L" - move 5 para trás e 3 para esquerda
    - "10F;30R" - move 10 para frente e 30 para direita
*/

#include "enkiSocketControl.h"
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

SocketControlExample::SocketControlExample(World *world, QWidget *parent) :
    ViewerWidget(world, parent),
    robot(nullptr),
    server(nullptr),
    clientSocket(nullptr),
    stepCounter(0),
    verbose(true),
    isMoving(false),
    targetDistance(0.0),
    currentDistance(0.0),
    startPosition(0, 0),
    startAngle(0.0),
    currentMovementType(""),
    pendingMoveDistance(0.0),
    executingQueue(false)
{
    // Criar e configurar o robô E-Puck
    setupRobot(world);
    
    // Configurar servidor TCP
    setupTcpServer();
    
    // Timer para enviar status periodicamente
    statusTimer = new QTimer(this);
    connect(statusTimer, &QTimer::timeout, this, &SocketControlExample::sendStatus);
    statusTimer->start(1000); // Enviar status a cada 1 segundo
    
    cout << "=== Controle via Socket - Enki ===" << endl;
    cout << "Servidor TCP rodando na porta 9999" << endl;
    cout << "Conecte um cliente para controlar o robô" << endl;
    cout << "Comandos: XF;YB;ZL;WR (ex: 10F;5R), stop, status, quit" << endl;
}

void SocketControlExample::setupRobot(World* world)
{
    // Criar robô E-Puck no centro do mundo
    robot = new EPuck;
    robot->pos = Point(60, 60);     // Posição central
    robot->angle = 0;               // Orientação inicial
    robot->setColor(Color(0.2, 0.7, 0.2)); // Verde
    
    // Inicialmente parado
    robot->leftSpeed = 0.0;
    robot->rightSpeed = 0.0;
    
    world->addObject(robot);
    
    if (verbose) {
        cout << "Robô criado em (" << robot->pos.x << ", " << robot->pos.y << ")" << endl;
    }
}

void SocketControlExample::setupTcpServer()
{
    server = new QTcpServer(this);
    
    // Conectar sinais
    connect(server, &QTcpServer::newConnection, this, &SocketControlExample::onNewConnection);
    
    // Iniciar servidor na porta 9999
    if (!server->listen(QHostAddress::Any, 9999)) {
        cout << "Erro: Não foi possível iniciar o servidor TCP: " 
             << server->errorString().toStdString() << endl;
    } else {
        cout << "Servidor TCP iniciado na porta 9999" << endl;
    }
}

void SocketControlExample::timerEvent(QTimerEvent * event)
{
    stepCounter++;
    
    // Verificar progresso do movimento se estiver em movimento
    if (isMoving) {
        checkMovementProgress();
    }
    
    // Log ocasional da posição
    if (verbose && stepCounter % 500 == 0) {
        cout << "Passo " << stepCounter << " - Posição: (" 
             << robot->pos.x << ", " << robot->pos.y 
             << ") Ângulo: " << robot->angle << endl;
    }
    
    ViewerWidget::timerEvent(event);
}

void SocketControlExample::processCommand(const QString& command)
{
    QString cmd = command.trimmed();
    
    // Comandos especiais
    if (cmd.toLower() == "status") {
        sendRobotStatus();
        return;
    } else if (cmd.toLower() == "quit") {
        sendResponse("OK: Goodbye!");
        QApplication::quit();
        return;
    } else if (cmd.toLower() == "stop") {
        stopRobot();
        commandQueue.clear();
        executingQueue = false;
        sendResponse("OK: Robot stopped and command queue cleared");
        return;
    }
    
    // Processar comandos de movimento (formato: 10F;30R;23B;7L)
    QStringList movements = cmd.split(';', Qt::SkipEmptyParts);
    if (movements.isEmpty()) {
        sendResponse("ERROR: Invalid command format. Use: XF;YB;ZL;WR (e.g., 10F;5R)");
        return;
    }
    
    executeMovementSequence(movements);
    
    if (verbose) {
        cout << "Comando executado: " << command.toStdString() << endl;
    }
}

void SocketControlExample::sendResponse(const QString& message)
{
    if (clientSocket && clientSocket->state() == QTcpSocket::ConnectedState) {
        clientSocket->write((message + "\n").toUtf8());
        clientSocket->flush();
    }
}

void SocketControlExample::sendRobotStatus()
{
    QString status = QString("STATUS: pos=(%1,%2) angle=%3 left_speed=%4 right_speed=%5")
                    .arg(robot->pos.x, 0, 'f', 2)
                    .arg(robot->pos.y, 0, 'f', 2)
                    .arg(robot->angle, 0, 'f', 2)
                    .arg(robot->leftSpeed, 0, 'f', 2)
                    .arg(robot->rightSpeed, 0, 'f', 2);
    sendResponse(status);
}

void SocketControlExample::executeMovementSequence(const QStringList& movements)
{
    if (movements.isEmpty()) {
        sendResponse("ERROR: No movements provided");
        return;
    }
    
    // Se já há comandos sendo executados, adicionar à fila
    if (isMoving) {
        for (const QString& movement : movements) {
            if (!movement.trimmed().isEmpty()) {
                commandQueue.append(movement.trimmed());
            }
        }
        sendResponse(QString("INFO: Added %1 commands to queue").arg(movements.size()));
        return;
    }
    
    // Iniciar execução da nova sequência
    commandQueue.clear();
    for (const QString& movement : movements) {
        if (!movement.trimmed().isEmpty()) {
            commandQueue.append(movement.trimmed());
        }
    }
    
    executingQueue = true;
    executeNextCommand();
}

void SocketControlExample::executeNextCommand()
{
    if (commandQueue.isEmpty()) {
        executingQueue = false;
        sendResponse("OK: All commands completed");
        return;
    }
    
    QString movement = commandQueue.takeFirst();
    executeSingleCommand(movement);
}

void SocketControlExample::executeSingleCommand(const QString& movement)
{
    const double DEFAULT_SPEED = 5.0;
    
    if (movement.isEmpty()) {
        executeNextCommand(); // Pular para o próximo comando
        return;
    }
    
    // Extrair número e direção (ex: "10F", "30R", "D50F", "R90L")
    QString cleanMove = movement.trimmed().toUpper();
    if (cleanMove.length() < 2) {
        sendResponse("ERROR: Invalid movement format: " + movement);
        executeNextCommand();
        return;
    }
    
    // Determinar se é comando de rotação (R) ou deslocamento (D)
    bool isRotationCommand = false;
    bool isDisplacementCommand = false;
    
    QChar direction = cleanMove.right(1)[0];
    QString numberStr = cleanMove.left(cleanMove.length() - 1);
    
    // Se o comando começa com uma letra (prefixo como "D" ou "R"), remover
    if (!numberStr.isEmpty() && numberStr[0].isLetter()) {
        QChar prefix = numberStr[0];
        if (prefix == 'R') {
            isRotationCommand = true;
        } else if (prefix == 'D') {
            isDisplacementCommand = true;
        }
        numberStr = numberStr.mid(1); // Remove o primeiro caractere (prefixo)
        
        if (verbose) {
            cout << "Executando comando - Prefixo: " << prefix.toLatin1() << ", número: " << numberStr.toStdString() << ", direção: " << direction.toLatin1() << endl;
        }
    } else {
        // Sem prefixo, assumir deslocamento por padrão
        isDisplacementCommand = true;
    }
    
    bool ok;
    double distance = numberStr.toDouble(&ok);
    if (!ok || distance < 0) {
        sendResponse("ERROR: Invalid distance in movement: " + movement + " (parsed: " + numberStr + ")");
        executeNextCommand();
        return;
    }
    
    // Se já está em movimento, parar primeiro
    if (isMoving) {
        stopRobot();
    }
    
    // Executar movimento baseado no tipo de comando e direção
    if (isRotationCommand) {
        // Comando de rotação pura (R90L, R90R)
        startAngle = robot->angle;
        targetDistance = distance * M_PI / 180.0; // Converter graus para radianos
        currentDistance = 0.0;
        isMoving = true;
        
        switch (direction.toLatin1()) {
            case 'L':
                currentMovementType = "rotate_left";
                robot->leftSpeed = -DEFAULT_SPEED * 0.6;
                robot->rightSpeed = DEFAULT_SPEED * 0.6;
                sendResponse(QString("OK: Rotating left %1 degrees").arg(distance, 0, 'f', 1));
                break;
            case 'R':
                currentMovementType = "rotate_right";
                robot->leftSpeed = DEFAULT_SPEED * 0.6;
                robot->rightSpeed = -DEFAULT_SPEED * 0.6;
                sendResponse(QString("OK: Rotating right %1 degrees").arg(distance, 0, 'f', 1));
                break;
            default:
                sendResponse("ERROR: Invalid rotation direction '" + QString(direction) + "'. Use L or R for rotation");
                return;
        }
    } else if (isDisplacementCommand) {
        // Comando de deslocamento (D10F, D10B, D10L, D10R)
        switch (direction.toLatin1()) {
            case 'F':
                // Mover para frente
                startPosition = robot->pos;
                targetDistance = distance;
                currentDistance = 0.0;
                isMoving = true;
                currentMovementType = "forward";
                
                robot->leftSpeed = DEFAULT_SPEED;
                robot->rightSpeed = DEFAULT_SPEED;
                
                sendResponse(QString("OK: Moving forward for %1 units").arg(distance, 0, 'f', 1));
                break;
                
            case 'B':
                // Mover para trás
                startPosition = robot->pos;
                targetDistance = distance;
                currentDistance = 0.0;
                isMoving = true;
                currentMovementType = "backward";
                
                robot->leftSpeed = -DEFAULT_SPEED;
                robot->rightSpeed = -DEFAULT_SPEED;
                
                sendResponse(QString("OK: Moving backward for %1 units").arg(distance, 0, 'f', 1));
                break;
                
            case 'L':
                // Virar 90° à esquerda E mover nessa direção
                startAngle = robot->angle;
                targetDistance = M_PI / 2; // 90 graus em radianos
                currentDistance = 0.0;
                isMoving = true;
                currentMovementType = "turn_left_then_move";
                pendingMoveDistance = distance; // Armazenar distância para depois
                
                // Primeiro virar à esquerda
                robot->leftSpeed = -DEFAULT_SPEED * 0.6;
                robot->rightSpeed = DEFAULT_SPEED * 0.6;
                
                sendResponse(QString("OK: Turning left 90° then moving %1 units").arg(distance, 0, 'f', 1));
                break;
                
            case 'R':
                // Virar 90° à direita E mover nessa direção
                startAngle = robot->angle;
                targetDistance = M_PI / 2; // 90 graus em radianos
                currentDistance = 0.0;
                isMoving = true;
                currentMovementType = "turn_right_then_move";
                pendingMoveDistance = distance; // Armazenar distância para depois
                
                // Primeiro virar à direita
                robot->leftSpeed = DEFAULT_SPEED * 0.6;
                robot->rightSpeed = -DEFAULT_SPEED * 0.6;
                
                sendResponse(QString("OK: Turning right 90° then moving %1 units").arg(distance, 0, 'f', 1));
                break;
                
            default:
                sendResponse("ERROR: Invalid displacement direction '" + QString(direction) + "'. Use F, B, L, R");
                executeNextCommand();
                return;
        }
    } else {
        sendResponse("ERROR: Unknown command type for: " + movement);
        executeNextCommand();
        return;
    }
}

void SocketControlExample::checkMovementProgress()
{
    if (!isMoving) return;
    
    const double DEFAULT_SPEED = 5.0;
    
    if (currentMovementType == "forward" || currentMovementType == "backward") {
        // Calcular distância percorrida desde o início
        double dx = robot->pos.x - startPosition.x;
        double dy = robot->pos.y - startPosition.y;
        currentDistance = sqrt(dx*dx + dy*dy);
        
        if (currentDistance >= targetDistance) {
            stopRobot();
            sendResponse(QString("OK: Completed %1 movement of %2 units")
                        .arg(currentMovementType)
                        .arg(targetDistance, 0, 'f', 1));
            
            // Se estamos executando uma fila de comandos, executar o próximo
            if (executingQueue) {
                executeNextCommand();
            }
        }
    } else if (currentMovementType == "rotate_left" || currentMovementType == "rotate_right") {
        // Calcular ângulo rotacionado para rotação pura
        double angleDiff = abs(robot->angle - startAngle);
        if (angleDiff > M_PI) {
            angleDiff = 2*M_PI - angleDiff; // Ajustar para ângulo menor
        }
        currentDistance = angleDiff;
        
        if (currentDistance >= targetDistance) {
            stopRobot();
            sendResponse(QString("OK: Completed %1 rotation of %2 degrees")
                        .arg(currentMovementType)
                        .arg(targetDistance * 180.0 / M_PI, 0, 'f', 1));
            
            // Se estamos executando uma fila de comandos, executar o próximo
            if (executingQueue) {
                executeNextCommand();
            }
        }
    } else if (currentMovementType == "turn_left_then_move" || currentMovementType == "turn_right_then_move") {
        // Calcular ângulo rotacionado
        double angleDiff = abs(robot->angle - startAngle);
        if (angleDiff > M_PI) {
            angleDiff = 2*M_PI - angleDiff; // Ajustar para ângulo menor
        }
        currentDistance = angleDiff;
        
        if (currentDistance >= targetDistance) {
            // Terminou a rotação, agora começar o movimento linear
            startPosition = robot->pos;
            targetDistance = pendingMoveDistance;
            currentDistance = 0.0;
            
            // Determinar novo tipo de movimento
            if (currentMovementType == "turn_left_then_move") {
                currentMovementType = "forward";
            } else {
                currentMovementType = "forward";
            }
            
            // Começar movimento para frente
            robot->leftSpeed = DEFAULT_SPEED;
            robot->rightSpeed = DEFAULT_SPEED;
            
            sendResponse(QString("OK: Rotation complete, now moving forward %1 units")
                        .arg(pendingMoveDistance, 0, 'f', 1));
            
            pendingMoveDistance = 0.0; // Limpar
        }
    }
}

void SocketControlExample::stopRobot()
{
    robot->leftSpeed = 0.0;
    robot->rightSpeed = 0.0;
    isMoving = false;
    targetDistance = 0.0;
    currentDistance = 0.0;
    currentMovementType = "";
    
    // Não limpar a fila aqui, pois queremos continuar a execução
    // commandQueue.clear();
    // executingQueue = false;
}

void SocketControlExample::onNewConnection()
{
    clientSocket = server->nextPendingConnection();
    
    connect(clientSocket, &QTcpSocket::readyRead, this, &SocketControlExample::onDataReceived);
    connect(clientSocket, &QTcpSocket::disconnected, this, &SocketControlExample::onClientDisconnected);
    
    cout << "Cliente conectado!" << endl;
    sendResponse("HELLO: Connected to Enki Robot Controller");
    sendResponse("COMMANDS: Use format XF;YB;ZL;WR (e.g., 10F;5R) or stop, status, quit");
}

void SocketControlExample::onDataReceived()
{
    if (!clientSocket) return;
    
    QByteArray data = clientSocket->readAll();
    QString command = QString::fromUtf8(data).trimmed();
    
    if (!command.isEmpty()) {
        cout << "Comando recebido: " << command.toStdString() << endl;
        processCommand(command);
    }
}

void SocketControlExample::onClientDisconnected()
{
    cout << "Cliente desconectado." << endl;
    clientSocket = nullptr;
}

void SocketControlExample::sendStatus()
{
    // Enviar status periodicamente apenas se há cliente conectado
    if (clientSocket && clientSocket->state() == QTcpSocket::ConnectedState) {
        // Enviar apenas se solicitado, para não sobrecarregar
        // sendRobotStatus();
    }
}

SocketControlExample::~SocketControlExample()
{
    if (server) {
        server->close();
    }
    cout << "Simulação finalizada após " << stepCounter << " passos." << endl;
}

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    
    // Criar o mundo da simulação (120x120 unidades)
    World world(120, 120, Color(0.9, 0.9, 0.9));
    
    // Criar o visualizador com controle via socket
    SocketControlExample viewer(&world);
    viewer.setWindowTitle("Controle via Socket - Enki Robotics");
    viewer.resize(800, 600);
    viewer.show();
    
    cout << "\nFeche a janela ou envie 'quit' via socket para sair." << endl;
    cout << "Exemplo de comando: 10F;5R (10 unidades frente + 5 unidades direita)" << endl;
    
    return app.exec();
}

#include "enkiSocketControl.moc"
