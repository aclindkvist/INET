import pygame

class Obstacle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

class Eatable():
    def __init__(self, x, y, width, height, color, rect = None, eaten = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        if rect is not None:
            self.rect = rect
        else:
            self.rect = (x, y, width, height)
        self.eaten = eaten

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def getEaten(self):
        self.eaten = True

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

class Scoreboard():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)