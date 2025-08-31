/*
    Controle via Socket com LBML - Enki
    
    Este exemplo demonstra como controlar um robô E-Puck via socket TCP usando LBML.
    O programa cria uma simulação gráfica onde o robô se move em um plano
    e recebe comandos de movimento de um cliente externo via socket.
    
    Comandos aceitos via socket (formato LBML):
    - "D<valor><direção>;" - deslocamento em centímetros (D40F; = 40cm frente)
    - "R<valor><direção>;" - rotação em graus (R90L; = 90° esquerda)
    Direções para D: F=Frente, B=Trás, L=Esquerda, R=Direita
    Direções para R: L=Esquerda, R=Direita
    - "stop" - para o robô
    - "status" - retorna posição e orientação atual
    - "quit" - encerra o programa
    
    Exemplos LBML:
    - "D40F;" - desloca 40cm para frente
    - "D100B;" - desloca 100cm (1 metro) para trás
    - "R90R;" - gira 90 graus à direita
    - "R180L;" - gira 180 graus à esquerda
    - "D25F;R90L;D25F;" - sequência de comandos
*/

#include "enkiSocketControl.h"
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;
using namespace Enki;

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
    pendingMoveDistance(0.0)
{
    // Criar e configurar o robô E-Puck
    setupRobot(world);
    
    // Configurar servidor TCP
    setupTcpServer();
    
    // Timer para enviar status periodicamente
    statusTimer = new QTimer(this);
    connect(statusTimer, &QTimer::timeout, this, &SocketControlExample::sendStatus);
    statusTimer->start(1000); // Enviar status a cada 1 segundo
    
    cout << "=== Controle via Socket com LBML - Enki ===" << endl;
    cout << "Servidor TCP rodando na porta 9999" << endl;
    cout << "Conecte um cliente para controlar o robô" << endl;
    cout << "Comandos LBML: D40F; (deslocamento), R90L; (rotação), stop, status, quit" << endl;
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
             << ") Ângulo: " << robot->angle * 180.0 / M_PI << "°" << endl;
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
        sendResponse("OK: Robot stopped");
        return;
    }
    
    // Processar comandos de movimento LBML
    QStringList movements = cmd.split(';', Qt::SkipEmptyParts);
    if (movements.isEmpty()) {
        sendResponse("ERROR: Invalid command format. Use LBML: D<value><dir>; or R<value><dir>; (e.g., D40F;R90L;)");
        return;
    }
    
    executeMovementSequence(movements);
    
    if (verbose) {
        cout << "Comando LBML executado: " << command.toStdString() << endl;
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
    QString status = QString("STATUS: pos=(%1,%2) angle=%3° left_speed=%4 right_speed=%5")
                    .arg(robot->pos.x, 0, 'f', 2)
                    .arg(robot->pos.y, 0, 'f', 2)
                    .arg(robot->angle * 180.0 / M_PI, 0, 'f', 2)
                    .arg(robot->leftSpeed, 0, 'f', 2)
                    .arg(robot->rightSpeed, 0, 'f', 2);
    sendResponse(status);
}

void SocketControlExample::executeMovementSequence(const QStringList& movements)
{
    // Limpar fila anterior e adicionar novos comandos
    commandQueue.clear();
    
    for (const QString& movement : movements) {
        if (!movement.trimmed().isEmpty()) {
            commandQueue.enqueue(movement.trimmed());
        }
    }
    
    // Se já está em movimento, parar primeiro
    if (isMoving) {
        stopRobot();
    }
    
    // Começar execução da sequência
    processNextCommand();
}

void SocketControlExample::processNextCommand()
{
    // Se não há mais comandos na fila, terminar
    if (commandQueue.isEmpty()) {
        sendResponse("OK: All movements completed");
        return;
    }
    
    // Pegar próximo comando da fila
    QString movement = commandQueue.dequeue();
    executeSingleMovement(movement);
}

void SocketControlExample::executeSingleMovement(const QString& movement)
{
    const double DEFAULT_SPEED = 5.0;
    const double CM_TO_UNITS = 0.3; // Conversão: 1cm = 0.3 unidades do simulador
    
    QString cleanMove = movement.toUpper();
    if (cleanMove.length() < 3) {
        sendResponse("ERROR: Invalid LBML format: " + movement);
        processNextCommand();
        return;
    }
    
    // Extrair prefixo (D ou R)
    QChar prefix = cleanMove[0];
    
    // Extrair direção (último caractere)
    QChar direction = cleanMove.right(1)[0];
    
    // Extrair valor numérico (entre prefixo e direção)
    QString numberStr = cleanMove.mid(1, cleanMove.length() - 2);
    
    bool ok;
    double value = numberStr.toDouble(&ok);
    if (!ok || value < 0) {
        sendResponse("ERROR: Invalid value in LBML command: " + movement);
        processNextCommand();
        return;
    }
    
    // Processar comando baseado no prefixo
    if (prefix == 'D') {
        // Deslocamento linear em centímetros
        double distance = value * CM_TO_UNITS;
        
        if (direction == 'F' || direction == 'B') {
            // Movimento linear para frente ou para trás
            startPosition = robot->pos;
            targetDistance = distance;
            currentDistance = 0.0;
            isMoving = true;
            currentMovementType = (direction == 'F') ? "forward" : "backward";
            
            double speed = (direction == 'F') ? DEFAULT_SPEED : -DEFAULT_SPEED;
            robot->leftSpeed = speed;
            robot->rightSpeed = speed;
            
            sendResponse(QString("OK: Moving %1 %2 cm")
                        .arg(direction == 'F' ? "forward" : "backward")
                        .arg(value, 0, 'f', 1));
        }
        else if (direction == 'L' || direction == 'R') {
            // Virar 90° e depois mover lateralmente
            startAngle = robot->angle;
            targetDistance = M_PI / 2; // 90 graus em radianos
            currentDistance = 0.0;
            isMoving = true;
            currentMovementType = (direction == 'L') ? "turn_left_then_move" : "turn_right_then_move";
            pendingMoveDistance = distance;
            
            // Girar primeiro
            double turnSpeed = (direction == 'L') ? -DEFAULT_SPEED * 0.6 : DEFAULT_SPEED * 0.6;
            robot->leftSpeed = turnSpeed;
            robot->rightSpeed = -turnSpeed;
            
            sendResponse(QString("OK: Turning %1 90° then moving %2 cm")
                        .arg(direction == 'L' ? "left" : "right")
                        .arg(value, 0, 'f', 1));
        }
        else {
            sendResponse("ERROR: Invalid direction for D command. Use F, B, L, or R");
            processNextCommand();
        }
    }
    else if (prefix == 'R') {
        // Rotação em graus
        if (direction != 'L' && direction != 'R') {
            sendResponse("ERROR: Invalid direction for R command. Use L or R");
            processNextCommand();
            return;
        }
        
        startAngle = robot->angle;
        targetDistance = value * M_PI / 180.0; // Converter graus para radianos
        currentDistance = 0.0;
        isMoving = true;
        currentMovementType = (direction == 'L') ? "rotation_left" : "rotation_right";
        
        double turnSpeed = (direction == 'L') ? -DEFAULT_SPEED * 0.6 : DEFAULT_SPEED * 0.6;
        robot->leftSpeed = turnSpeed;
        robot->rightSpeed = -turnSpeed;
        
        sendResponse(QString("OK: Rotating %1 degrees %2")
                    .arg(value, 0, 'f', 1)
                    .arg(direction == 'L' ? "left" : "right"));
    }
    else {
        sendResponse("ERROR: Invalid LBML prefix. Use D (displacement) or R (rotation)");
        processNextCommand();
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
            stopCurrentMovement();
            sendResponse(QString("OK: Completed %1 movement of %2 cm")
                        .arg(currentMovementType)
                        .arg(targetDistance / 0.3, 0, 'f', 1)); // Converter de volta para cm
            
            // Processar próximo comando da fila
            processNextCommand();
        }
    } 
    else if (currentMovementType == "rotation_left" || currentMovementType == "rotation_right") {
        // Rotação pura (comando R)
        double angleDiff = abs(robot->angle - startAngle);
        if (angleDiff > M_PI) {
            angleDiff = 2*M_PI - angleDiff;
        }
        currentDistance = angleDiff;
        
        if (currentDistance >= targetDistance) {
            stopCurrentMovement();
            sendResponse(QString("OK: Completed rotation of %1 degrees")
                        .arg(targetDistance * 180.0 / M_PI, 0, 'f', 1));
            processNextCommand();
        }
    }
    else if (currentMovementType == "turn_left_then_move" || currentMovementType == "turn_right_then_move") {
        // Comando D com direção L ou R: primeiro girar, depois mover
        double angleDiff = abs(robot->angle - startAngle);
        if (angleDiff > M_PI) {
            angleDiff = 2*M_PI - angleDiff;
        }
        currentDistance = angleDiff;
        
        if (currentDistance >= targetDistance) {
            // Terminou a rotação, agora começar o movimento linear
            startPosition = robot->pos;
            targetDistance = pendingMoveDistance;
            currentDistance = 0.0;
            currentMovementType = "forward";
            
            // Começar movimento para frente
            robot->leftSpeed = DEFAULT_SPEED;
            robot->rightSpeed = DEFAULT_SPEED;
            
            sendResponse(QString("OK: Rotation complete, now moving forward %1 cm")
                        .arg(pendingMoveDistance / 0.3, 0, 'f', 1));
            
            pendingMoveDistance = 0.0;
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
    
    // Limpar fila de comandos se estiver parando manualmente
    commandQueue.clear();
}

void SocketControlExample::stopCurrentMovement()
{
    robot->leftSpeed = 0.0;
    robot->rightSpeed = 0.0;
    isMoving = false;
    targetDistance = 0.0;
    currentDistance = 0.0;
    currentMovementType = "";
}

void SocketControlExample::onNewConnection()
{
    clientSocket = server->nextPendingConnection();
    
    connect(clientSocket, &QTcpSocket::readyRead, this, &SocketControlExample::onDataReceived);
    connect(clientSocket, &QTcpSocket::disconnected, this, &SocketControlExample::onClientDisconnected);
    
    cout << "Cliente conectado!" << endl;
    sendResponse("HELLO: Connected to Enki Robot Controller (LBML)");
    sendResponse("COMMANDS: Use LBML format - D40F; (move 40cm forward), R90L; (turn 90° left)");
    sendResponse("COMMANDS: Multiple commands: D25F;R90L;D25F; or use stop, status, quit");
}

void SocketControlExample::onDataReceived()
{
    if (!clientSocket) return;
    
    QByteArray data = clientSocket->readAll();
    QString command = QString::fromUtf8(data).trimmed();
    
    if (!command.isEmpty()) {
        cout << "Comando LBML recebido: " << command.toStdString() << endl;
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
    viewer.setWindowTitle("Controle via Socket com LBML - Enki Robotics");
    viewer.resize(800, 600);
    viewer.show();
    
    cout << "\nFeche a janela ou envie 'quit' via socket para sair." << endl;
    cout << "Exemplo de comando LBML: D40F;R90L;D25F; (40cm frente, gira 90° esquerda, 25cm frente)" << endl;
    
    return app.exec();
}

#include "enkiSocketControl.moc"