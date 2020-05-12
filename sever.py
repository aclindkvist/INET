import socket
from _thread import *
from player import Player
import sys
from obstacles import Obstacles

server = "192.168.10.123"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))


print(s)
s.listen(2)
print("Waiting for a connection, Server Started")


players = [Player(0,0,30,30,(255,0,0)), Player(470,470, 30,30, (0,0,255))]


def threaded_client(conn, player):
    conn.send(str.encode(players[player]))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
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

            conn.sendall(str.encode(reply))
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