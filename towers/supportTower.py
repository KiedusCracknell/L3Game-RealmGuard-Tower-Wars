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

            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            
            if dis <= self.range + tower.height / 2:
                effected.append(tower)
                
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
            
            
            
            dis = math.sqrt((self.x-x)**2 + (self.y-y)**2)
            
            if dis <= self.range  + tower.height / 2:
                effected.append(tower)
                
        for tower in effected:
            tower.damage += round(tower.damage * self.effect[self.level-1])