import pygame
import math

class Enemy:    
    def __init__(self):
        self.width = 48
        self.height = 48
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(108, -10), (108, 1), (108, 173), (455, 173), (712, 173), (1062, 173), (1062, 365), (966, 365), (936, 397), (866, 459), (748, 463), (550, 461), (550, 558), (550, 696), (550, 800)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.move_dis = 0
        self.dis = 0
        self.imgs = []
        self.flipped = False
        
    def draw(self, win):
        """
        Draws the with the given images
        :param win: surface
        :return: none
        """
        self.img = self.imgs[(self.animation_count)//10]
        self.animation_count += 1
        
        if ((self.animation_count)//10) >= len(self.imgs):
            self.animation_count = 0
            
        win.blit(self.img, (self.x-self.img.get_width()/2, self.y-self.img.get_height()/2))
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
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 710)
        else:
            x2,y2 = self.path[self.path_pos+1]
            
        dirn = ((x2 - x1)*2, (y2 - y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)
        
        if dirn[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

                
        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))
        #self.dis += (math.sqrt((move_x-x1)**2 + (move_y-y1)**2))
        
        self.x = move_x
        self.y = move_y
        
        #go to next point
        if dirn[0] >= 0: # Moving right
            if dirn[1] >= 0: # Moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else: # Moving up
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else: # Moving left
            if dirn[1] >= 0: # Moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else: # Moving up
                if self.x <= x2 and self.y <= y2:
                    self.path_pos += 1
        
    
    def hit(self):
        """
        decreases enemy health by 1 each call and returns true when enemy health is less than or equal to 0
        :return: bool
        
        """
        self.health -= 1
        if self.health <= 0:
            return True
        
    
        