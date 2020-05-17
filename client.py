import json
import pygame
pygame.font.init()
from network import Network
from player import Player
from obstacles import Obstacle, Eatable, VictoryWindow

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

def redrawWindow(win, player, player2, eatable, eatable2, obstacles, victory):
    win.fill((255,255,255))
    for obs in obstacles:
        obs.draw(win)
    player.draw(win)
    player2.draw(win)
    if not eatable.eaten:
        eatable.draw(win)
    if not eatable2.eaten:
        eatable2.draw(win)
    if player2.won == True:
        victory.draw(win)
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
    things = json.loads(n.getServerObjectList())
    p = Player(**things[0])# expanding the dictionary
    e1 = Eatable(**things[1])
    e2 = Eatable(**things[2])

    clientObjectList = [p, e1, e2]

    clock = pygame.time.Clock()

    while run:
        clock.tick(100)

        clientObjectList = [p,e1,e2]

        other_things_net = n.send(json.dumps(list(map(lambda item: item.__dict__, clientObjectList))))
        other_things_json = json.loads(other_things_net)
        p2 = Player(**other_things_json[0])
        e1 = Eatable(**other_things_json[1])
        e2 = Eatable(**other_things_json[2])

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
        #plockar upp eatable
        if (p.x < e1.x < p.x+30) and (p.y < e1.y < p.y+30) and p.hungry == True:
            e1.getEaten()
            p.notHungry()

        elif (p.x < e2.x < p.x+30) and (p.y < e2.y < p.y+30) and p.hungry == True:
            e2.getEaten()
            p.notHungry()

        victory = VictoryWindow("You won!!", 130, 130, 250, 150, (0,150,0))

        redrawWindow(win, p, p2, e1, e2, obstacles, victory)

main()