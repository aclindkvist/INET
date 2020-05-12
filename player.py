import pygame

class Player():

    # Constructor for recreating encoded player
    def __init__(self, x, y, width, height, color, rect=None, vel=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        if rect is not None:
            self.rect = rect
        else:
            self.rect = (x, y, width, height)
        if vel is not None:
            self.vel = vel
        else:
            self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x < 500-30:
            self.x += self.vel

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y < 500-30:
            self.y += self.vel

        if keys[pygame.K_SPACE]:
            pass

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)