import pygame

class Enemy:
    imgs = []
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
        
    def collide(self, x, y):
        """
        Returns if position hits the enemy
        :param x: int
        :param y: int
        :return: Bool
        """
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