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
score = 0

obstacles = [Obstacle(0, 0, 510, 30, (0, 0, 0)),
             Obstacle(0, 480, 510, 30, (0, 0, 0)),
             Obstacle(0, 0, 30, 510, (0, 0, 0)),
             Obstacle(480, 0, 30, 510, (0, 0, 0)),
             Obstacle(225, 205, 20, 100, (0, 0, 0)),
             Obstacle(70, 70, 150, 20, (0, 0, 0)),
             Obstacle(300, 150, 20, 200, (0, 0, 0)),
             Obstacle(90, 350, 300, 20, (0, 0, 0))]

def redrawWindow(win, player, player2, obstacles):
    win.fill((255,255,255))
    for obs in obstacles:
        obs.draw(win)
    player.draw(win)
    player2.draw(win)

    pygame.display.update()

def krock(p):
    for i in obstacles:
        # stående hinder
        if (p.x + 30 > i.x and p.x < i.x + i.width) and (p.y + 30 > i.y and p.y < i.y + i.height):
            p.babyPlzDontGo()
        else:
            p.update()


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
        #om spelare krockar med hinder
        krock(p)
        #om spelarna krockar med varandra ska de stanna
        if (p.x+30 > p2.x and p.x < p2.x+30) and (p.y+30 > p2.y and p.y < p2.y+30):
            p.babyPlzDontGo()
        else:
            p.update()
        redrawWindow(win, p, p2, obstacles)

main()