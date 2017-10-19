#!/usr/bin/python
# Akkas Haider
import json
import random
import socket
import sys
import time

import thread


# function to read config file
def readConfigFile(filename):
    with open(filename) as f:
        lines = [line.strip() for line in open(filename)]
        return lines


# fucntion to get port of specific host
def getPortFromIndex(line):
    if line < 1 or line > totalNodes:
        print
        "line out of bound"
        sys.exit()
    nodeConfig = str(configurations[line - 1]).split()
    port = nodeConfig[2]
    return port


# function to get host/ip from index
def getHostFromIndex(line):
    # check line if within bounds
    nodeConfig = str(configurations[line - 1]).split()
    host = nodeConfig[1]
    return host


# function to get id from index
def getIdFromIndex(line):
    # check line if within bounds
    nodeConfig = str(configurations[line - 1]).split()
    nodeId = nodeConfig[0]
    return nodeId


# start and listen to socket
def startSockerListener(port):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.settimeout(120)
    serverSocket.bind((socket.gethostname(), int(port)))
    serverSocket.listen(5)

    # loop to receive messages
    while 1:
        c, addr = serverSocket.accept()
        message = c.recv(1024)
        msg = message.split('.')
        senderId = msg[0]
        senderClock = json.loads(msg[1])
        updateClock(vectorClock, senderClock)
        print
        'r', senderId, str(senderClock).replace(",", ""), str(vectorClock).replace(",", "")
        c.close()
    return


# update vector clock
def updateClock(vectorClock, senderClock):
    for i in range(0, len(vectorClock)):
        vectorClock[i] = max(vectorClock[i], senderClock[i])
    vectorClock[myIndex - 1] += 1;


# send message to remote node
def sendMessage():
    # choose random node excluding your own
    r = range(1, myIndex) + range(myIndex + 1, totalNodes + 1)
    randomIndex = random.choice(r)
    nodePort = getPortFromIndex(randomIndex)
    nodeHost = getHostFromIndex(randomIndex)
    nodeId = getIdFromIndex(randomIndex)
    socketId = socket.socket()
    socketId.connect((nodeHost, int(nodePort)))
    vectorClock[myIndex - 1] += 1;
    print
    's', nodeId, str(vectorClock).replace(",", "");
    sendMessage = str(myId) + '.' + json.dumps(vectorClock)
    socketId.send(sendMessage)
    socketId.close();
    return


# check number of arguments
if (len(sys.argv) < 3):
    print
    "usage:[program] [configuration_file] [line]"
    sys.exit()

configFileName = str(sys.argv[1])
myIndex = int(sys.argv[2])

configurations = readConfigFile(configFileName)
totalNodes = len(configurations)

myPort = getPortFromIndex(myIndex)
myId = getIdFromIndex(myIndex)

# initialize vector clock
vectorClock = [0] * totalNodes

# thread for listening
thread.start_new_thread(startSockerListener, (myPort,))
# wait for 15 seconds to make sure all nodes are running
time.sleep(15)
eventCount = 0
while eventCount < 100:
    event = random.randint(1, 2)
    # localevent
    if event == 1:
        increment = random.randint(1, 5)
        vectorClock[myIndex - 1] += increment
        print
        'l', increment
    if event == 2:
        sendMessage()
    eventCount += 1
time.sleep(10)
