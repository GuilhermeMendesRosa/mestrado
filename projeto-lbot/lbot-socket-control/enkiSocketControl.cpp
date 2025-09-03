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
    executingQueue(false),
    accumulatedRotation(0.0),
    lastAngle(0.0)
{
    setupRobot(world);
    
    setupTcpServer();
    
    statusTimer = new QTimer(this);
    connect(statusTimer, &QTimer::timeout, this, &SocketControlExample::sendStatus);
    statusTimer->start(1000);
    
    cout << "=== Controle via Socket - Enki ===" << endl;
    cout << "Servidor TCP rodando na porta 9999" << endl;
    cout << "Conecte um cliente para controlar o robô" << endl;
    cout << "Comandos: XF;YB;ZL;WR (ex: 10F;5R), stop, status, quit" << endl;
}

void SocketControlExample::setupRobot(World* world)
{
    robot = new EPuck;
    robot->pos = Point(60, 60);
    robot->angle = 0;
    robot->setColor(Color(0.2, 0.7, 0.2));
    
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
    
    connect(server, &QTcpServer::newConnection, this, &SocketControlExample::onNewConnection);
    
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
    
    if (isMoving) {
        checkMovementProgress();
    }
    
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
    
    if (isMoving) {
        for (const QString& movement : movements) {
            if (!movement.trimmed().isEmpty()) {
                commandQueue.append(movement.trimmed());
            }
        }
        sendResponse(QString("INFO: Added %1 commands to queue").arg(movements.size()));
        return;
    }
    
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
        executeNextCommand();
        return;
    }
    
    QString cleanMove = movement.trimmed().toUpper();
    if (cleanMove.length() < 2) {
        sendResponse("ERROR: Invalid movement format: " + movement);
        executeNextCommand();
        return;
    }
    
    bool isRotationCommand = false;
    bool isDisplacementCommand = false;
    
    QChar direction = cleanMove.right(1)[0];
    QString numberStr = cleanMove.left(cleanMove.length() - 1);
    
    if (!numberStr.isEmpty() && numberStr[0].isLetter()) {
        QChar prefix = numberStr[0];
        if (prefix == 'R') {
            isRotationCommand = true;
        } else if (prefix == 'D') {
            isDisplacementCommand = true;
        }
        numberStr = numberStr.mid(1);
        
        if (verbose) {
            cout << "Executando comando - Prefixo: " << prefix.toLatin1() << ", número: " << numberStr.toStdString() << ", direção: " << direction.toLatin1() << endl;
        }
    } else {
        isDisplacementCommand = true;
    }
    
    bool ok;
    double distance = numberStr.toDouble(&ok);
    if (!ok || distance < 0) {
        sendResponse("ERROR: Invalid distance in movement: " + movement + " (parsed: " + numberStr + ")");
        executeNextCommand();
        return;
    }
    
    if (isMoving) {
        stopRobot();
    }
    
    if (isRotationCommand) {
        startAngle = robot->angle;
        targetDistance = distance * M_PI / 180.0;
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
        
        resetRotationTracking();
    } else if (isDisplacementCommand) {
        switch (direction.toLatin1()) {
            case 'F':
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
                startAngle = robot->angle;
                targetDistance = M_PI / 2;
                currentDistance = 0.0;
                isMoving = true;
                currentMovementType = "turn_left_then_move";
                pendingMoveDistance = distance;
                
                robot->leftSpeed = -DEFAULT_SPEED * 0.6;
                robot->rightSpeed = DEFAULT_SPEED * 0.6;
                
                resetRotationTracking();
                
                sendResponse(QString("OK: Turning left 90° then moving %1 units").arg(distance, 0, 'f', 1));
                break;
                
            case 'R':
                startAngle = robot->angle;
                targetDistance = M_PI / 2;
                currentDistance = 0.0;
                isMoving = true;
                currentMovementType = "turn_right_then_move";
                pendingMoveDistance = distance;
                
                robot->leftSpeed = DEFAULT_SPEED * 0.6;
                robot->rightSpeed = -DEFAULT_SPEED * 0.6;
                
                resetRotationTracking();
                
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
        double dx = robot->pos.x - startPosition.x;
        double dy = robot->pos.y - startPosition.y;
        currentDistance = sqrt(dx*dx + dy*dy);
        
        if (currentDistance >= targetDistance) {
            stopRobot();
            sendResponse(QString("OK: Completed %1 movement of %2 units")
                        .arg(currentMovementType)
                        .arg(targetDistance, 0, 'f', 1));
            
            if (executingQueue) {
                executeNextCommand();
            }
        }
    } else if (currentMovementType == "rotate_left" || currentMovementType == "rotate_right") {
        
        double angleDiff = robot->angle - lastAngle;
        
        while (angleDiff > M_PI) angleDiff -= 2*M_PI;
        while (angleDiff < -M_PI) angleDiff += 2*M_PI;
        
        if (currentMovementType == "rotate_left") {
            if (angleDiff > 0) {
                accumulatedRotation += angleDiff;
            } else if (angleDiff < -M_PI/2) {
                accumulatedRotation += (2*M_PI + angleDiff);
            }
        } else {
            if (angleDiff < 0) {
                accumulatedRotation += abs(angleDiff);
            } else if (angleDiff > M_PI/2) {
                accumulatedRotation += (2*M_PI - angleDiff);
            }
        }
        
        lastAngle = robot->angle;
        currentDistance = accumulatedRotation;
        
        if (currentDistance >= targetDistance) {
            stopRobot();
            accumulatedRotation = 0.0;
            sendResponse(QString("OK: Completed %1 rotation of %2 degrees")
                        .arg(currentMovementType)
                        .arg(targetDistance * 180.0 / M_PI, 0, 'f', 1));
            
            if (executingQueue) {
                executeNextCommand();
            }
        }
    } else if (currentMovementType == "turn_left_then_move" || currentMovementType == "turn_right_then_move") {
        double angleDiff = robot->angle - lastAngle;

        while (angleDiff > M_PI) angleDiff -= 2*M_PI;
        while (angleDiff < -M_PI) angleDiff += 2*M_PI;

        if (currentMovementType == "turn_left_then_move") {
            if (angleDiff > 0) {
                accumulatedRotation += angleDiff;
            } else if (angleDiff < -M_PI/2) {
                accumulatedRotation += (2*M_PI + angleDiff);
            }
        } else {
            if (angleDiff < 0) {
                accumulatedRotation += abs(angleDiff);
            } else if (angleDiff > M_PI/2) {
                accumulatedRotation += (2*M_PI - angleDiff);
            }
        }
        
        lastAngle = robot->angle;
        currentDistance = accumulatedRotation;
        
        if (currentDistance >= targetDistance) {
            accumulatedRotation = 0.0;
            startPosition = robot->pos;
            targetDistance = pendingMoveDistance;
            currentDistance = 0.0;

            if (currentMovementType == "turn_left_then_move") {
                currentMovementType = "forward";
            } else {
                currentMovementType = "forward";
            }

            robot->leftSpeed = DEFAULT_SPEED;
            robot->rightSpeed = DEFAULT_SPEED;

            sendResponse(QString("OK: Rotation complete, now moving forward %1 units")
                        .arg(pendingMoveDistance, 0, 'f', 1));

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
    
    
}

void SocketControlExample::resetRotationTracking()
{
    accumulatedRotation = 0.0;
    lastAngle = startAngle;
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
    if (clientSocket && clientSocket->state() == QTcpSocket::ConnectedState) {
        
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
    
    World world(120, 120, Color(0.9, 0.9, 0.9));

    SocketControlExample viewer(&world);
    viewer.setWindowTitle("Controle via Socket - Enki Robotics");
    viewer.resize(800, 600);
    viewer.show();
    
    cout << "\nFeche a janela ou envie 'quit' via socket para sair." << endl;
    cout << "Exemplo de comando: 10F;5R (10 unidades frente + 5 unidades direita)" << endl;
    
    return app.exec();
}

#include "enkiSocketControl.moc"
