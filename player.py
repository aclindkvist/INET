import pygame

class Player:
    # Constructor for recreating encoded player
    def __init__(self, x, y, width, height, color, rect=None, vel=None, hungry=True, won=False):
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
            self.vel = 1
        self.hungry = hungry
        self.won = won

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        if keys[pygame.K_SPACE]:
            self.pickUp()

        #self.update()

    def babyPlzDontGo(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= -1

        if keys[pygame.K_RIGHT]:
            self.x += -1

        if keys[pygame.K_UP]:
            self.y -= -1

        if keys[pygame.K_DOWN]:
            self.y += -1

        if keys[pygame.K_SPACE]:
            pass

    def pickUp(self):
        print("picked")

    def notHungry(self):
        self.hungry = False


    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
