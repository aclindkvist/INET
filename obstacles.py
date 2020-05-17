import pygame
pygame.font.init()

class Obstacle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

class Eatable:
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

class VictoryWindow:
    def __init__(self,text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = 300
        self.height = 200
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render(self.text, 1, (40,40,0))
        win.blit(text,(self.x + round(self.width/2)-round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))