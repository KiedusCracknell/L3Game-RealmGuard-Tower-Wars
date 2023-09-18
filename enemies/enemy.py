import pygame
import math

class Enemy:
    imgs = []
    
    def __init__(self):
        self.width = 48
        self.height = 48
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(107, 15), (111, 171), (1062, 174), (1060, 365), (934, 395), (862, 465), (746, 461), (525, 462), (524, 553), (523, 689)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.dis = 0
        
    def draw(self, win):
        """
        Draws the with the given images
        :param win: surface
        :return: none
        """
        self.img = self.imgs[self.animation_count//3]
        self.animation_count += 1
        print(self.imgs)
        
        if self.animation_count >= len(self.imgs)*3:
            self.animation_count = 0
            
        win.blit(self.img, (self.x, self.y))
        #pygame.draw.rect, (win, (255,0,0), (self.x, self.y, 48, 48))
        
        self.move()
        
        
    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: bool   
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def move(self):
        """
        moves enemy position to next path position
        :return: None
        """
        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-100000, -100000)
        else:
            x2,y2 = self.path[self.path_pos+1]
            
        move_dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            
        self.move_count += 1 
        dirn = (x2 - x1, y2 - y1)
                
        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x-x1)**2 + (move_y-y1)**2)
        
        #go to next point
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                self.path_pos = 0
        
        self.x = move_x
        self.y = move_y
    
    def hit(self):
        """
        decreases enemy health by 1 each call and returns true when enemy health is less than or equal to 0
        :return: bool
        
        """
        self.health -= 1
        if self.health <= 0:
            return True
        
    
        