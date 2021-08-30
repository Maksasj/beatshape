import pygame, sys
WIDTH, HEIGHT = 400, 400
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        #self.color = (color_r,color_g,color_b)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
    
    def draw(self, win,color_r,color_g,color_b):
        pygame.draw.rect(win, (color_r,color_g,color_b), self.rect)
    
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (242, 53, 31)
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    def col(self,player):
        col = pygame.sprite.collide_rect(self, player)
        if col == True:
            return True

class Point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.color = (66, 245, 90)
    def draw(self, win):
        #glowing = pygame.Rect(self.x, self.y, 32, 32)
        #pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, self.color, self.rect)
    def col(self,player):
        col = pygame.sprite.collide_rect(self, player)
        if col == True:
            return True

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.color = (236, 245, 66)
    def draw(self, win):
        #glowing = pygame.Rect(self.x, self.y, 32, 32)
        #pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, self.color, self.rect)
    def col(self,player):
        col = pygame.sprite.collide_rect(self, player)
        if col == True:
            return True

class Shield_Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 80, 90)
        
    def draw(self, win , color):
        #glowing = pygame.Rect(self.x, self.y, 32, 32)
        #pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, color, self.rect)