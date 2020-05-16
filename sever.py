import json
import socket
from _thread import *
from player import Player
from obstacles import Eatable
import sys

server = "192.168.10.123"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection, Server Started")


players = [Player(30,30,30,30,(255,0,0)), Player(450,30, 30,30, (0,0,255))]




def threaded_client(conn, player):
    #dict = (key, value). gör om complex object till ett dictionary som kan json encodas.
    conn.send(str.encode(json.dumps(players[player].__dict__)))
    reply = ""
    while True:
        try:
            data = Player(**json.loads(conn.recv(2048).decode()))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(json.dumps(reply.__dict__)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept() #Accepts blocks for incoming connections. New socket object that you will use to communicate with the client.
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1