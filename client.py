import json
import pygame
import player
from network import Network
from player import Player
from obstacles import Obstacle

width = 510
height = 510
win = pygame.display.set_mode((width, height))
# Title on the game
pygame.display.set_caption("Client")

obstacles = [Obstacle(0,0,510,30,(0,0,0)),
             Obstacle(0,480,510,30,(0,0,0)),
             Obstacle(0,0,30,510,(0,0,0)),
             Obstacle(480,0,30,510,(0,0,0)),
             Obstacle(225,205,30,100,(0,0,0)),
             ]

def redrawWindow(win, player, player2, obstacles):
    win.fill((255,255,255))
    for obs in obstacles:
        obs.draw(win)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    p = Player(**json.loads(n.getP())) #expanding the dictionary
    clock = pygame.time.Clock()

    while run:
        clock.tick(100)
        p2net = n.send(json.dumps(p.__dict__))
        p2json = json.loads(p2net)
        p2 = Player(**p2json)

        #Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        #om spelare krockar med hinder i mitten
        if (p.x+30 > obstacles[4].x and p.x < obstacles[4].x + 30) and (p.y+30 > obstacles[4].y and p.y < obstacles[4].y + 100):
            p.plzstopgo()
        #om spelarna krockar med varandra ska de stanna
        if (p.x+30 > p2.x and p.x < p2.x+30) and (p.y+30 > p2.y and p.y < p2.y+30):
            p.plzstopgo()
        else:
            p.update()
        redrawWindow(win, p, p2, obstacles)

main()