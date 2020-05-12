import pygame
from network import Network
from player import Player
from obstacles import Obstacles

width = 500
height = 500
win = pygame.display.set_mode((width, height))
# Title on the game
pygame.display.set_caption("Client")

obstacle = [Obstacles(0,100,150,30,(0,0,0)),Obstacles(200,150,30,150,(0,0,0)),Obstacles(300, 300,30,100,(0,0,0)),Obstacles(300,100,200,30,(0,0,0))]

def redrawWindow(win,player, player2, obstacle):
    win.fill((255,255,255))
    for obs in obstacle:
        obs.draw(win)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        #Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2, obstacle)

main()