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

players = [Player(30, 30, 30, 30, (255, 0, 0)), Player(450, 30, 30, 30, (0, 0, 255))]
eatables = [Eatable(90, 400, 10, 10, (0, 255, 0)), Eatable(160, 120, 10, 10, (0, 255, 0))]


def threaded_client(conn, player):
    # dict = (key, value). gör om complex object till ett dictionary som kan json encodas.
    things = [players[player]]
    things = things + eatables
    print(json.dumps(list(map(lambda item: item.__dict__, things))))
    conn.send(str.encode(json.dumps(list(map(lambda item: item.__dict__, things)))))
    reply = ""
    while True:
        try:

            data = json.loads(conn.recv(2048).decode())
            player_data = Player(**data[0])
            if not eatables[0].eaten:
                eatables[0] = Eatable(**data[1])
            if not eatables[1].eaten:
                eatables[1] = Eatable(**data[2])

            if eatables[0].eaten == True and eatables[1].eaten == True:
                player_data.won = True
                print("Victory!")

            players[player] = player_data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = [players[0], eatables[0], eatables[1]]
                else:
                    reply = [players[1], eatables[0], eatables[1]]

                print("Received: ", data)
                print("Sending : ", reply)

            dictified_reply = list(map(lambda item: item.__dict__, reply))

            conn.sendall(str.encode(json.dumps(dictified_reply)))
        except:
            print("Could not load client data.")
            break

    print("Lost connection")
    conn.close()


currenteatable = 0
currentPlayer = 0
while True:
    conn, addr = s.accept()  # Accepts blocks for incoming connections. New socket object that you will use to communicate with the client.
    print("Connected to:", addr)

    start_new_thread(threaded_client,
                     (conn, currentPlayer))  # import thread. Vaje gång det kommer en conn så startas det en ny thread.
    currentPlayer += 1
