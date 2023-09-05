import pygame

class Enemy:
    imgs = []
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.img = None
        
    def draw(self, win):
        """
        Draw the enemy with the given images
        :param win: surface
        :return: None
        """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        win.blit(self.img, (self.x, self.y))
        self.move()
        
    def collide(self, X, Y):
        """
        Returns if position hits the enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    
    def move(self):
        """
        Move the enemy
        :return: None
        """
        pass
        
    def hit(self):
        """
        Returns if an enemy has died and removes one health each call
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True