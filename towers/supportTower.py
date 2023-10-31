import pygame
from towers.tower import Tower
import os
import math
import time

range_img = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/towers", "support_range_tower.png")),(90,180))]

class RangeTower(Tower):
    """
    Add extra range to nearby towers
    """
    def __init__(self,x,y):
        super().__init__(x,y)
        self.range = 75
        self.tower_imgs = range_img[:]
        self.effect = [0.2,0.4]
        self.width = self.tower_imgs[0].get_width()
        self.height = self.tower_imgs[0].get_height()
        
    def draw(self,win):
        super().draw_radius(win,self.range,128,255,128)
        super().draw(win)
        
    def support(self,towers):
        """
        buffs towers in radius with extra range
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y
            w = tower.width
            h = tower.height

            r = self.range
            range_center = [self.x+self.width/2, self.y+self.height/2]
            #vertices of the outer bounding box of tower plus the range of the support
            rect_x = [(x-r), (x+w+r), (x-r), (x+w+r)]
            rect_y = [(y-r), (y-r), (y+h+r), (y+h+r)]

            min_x = min(rect_x[0], rect_x[1], rect_x[2], rect_x[3])
            max_x = max(rect_x[0], rect_x[1], rect_x[2], rect_x[3])
            min_y = min(rect_y[0], rect_y[1], rect_y[2], rect_y[3])
            max_y = max(rect_y[0], rect_y[1], rect_y[2], rect_y[3])
            
            #print("X=",x,"Y=",y,"w=",w,"h=",h,"r=",r,"rangecenter=",range_center, "mx=",min_x, "mxx=",max_x, "my=",min_y, "myy=", max_y)
            
            if range_center[0] >= min_x and range_center[0] <= max_x and range_center[1] >= min_y and range_center[1] <= max_y:
                effected.append(tower)
                #print("done")
            
        for tower in effected:
            tower.range = round(tower.original_range + tower.original_range * self.effect[self.level-1])

damage_img = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/towers", "support_damage_tower.png")),(80,170))]

class DamageTower(RangeTower):
    """
    add extra damage to nearby towers
    """
    def __init__(self,x,y):
        super().__init__(x,y)
        self.tower_imgs = damage_img[:]
        self.effect = [1,2]
        
    def support(self,towers):
        """
        buffs towers in radius with extra damage
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y
            w = tower.width
            h = tower.height

            r = self.range
            range_center = [self.x+self.width/2, self.y+self.height/2]
            #vertices of the outer bounding box of tower plus the range of the support
            rect_x = [(x-r), (x+w+r), (x-r), (x+w+r)]
            rect_y = [(y-r), (y-r), (y+h+r), (y+h+r)]

            min_x = min(rect_x[0], rect_x[1], rect_x[2], rect_x[3])
            max_x = max(rect_x[0], rect_x[1], rect_x[2], rect_x[3])
            min_y = min(rect_y[0], rect_y[1], rect_y[2], rect_y[3])
            max_y = max(rect_y[0], rect_y[1], rect_y[2], rect_y[3])
            
            #print("X=",x,"Y=",y,"w=",w,"h=",h,"r=",r,"rangecenter=",range_center, "mx=",min_x, "mxx=",max_x, "my=",min_y, "myy=", max_y)
            
            if range_center[0] >= min_x and range_center[0] <= max_x and range_center[1] >= min_y and range_center[1] <= max_y:
                effected.append(tower)
                #print("done")
        for tower in effected:
            tower.damage = round(tower.original_damage + tower.original_damage * self.effect[self.level-1])