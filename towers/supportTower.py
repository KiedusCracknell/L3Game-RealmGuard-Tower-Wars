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
        self.radius = 150
        self.tower_imgs = range_img[:]
        self.effect = [0.2,0.4]
        
    def draw(self,win):
        super().draw_radius(win,self.radius,128,255,128)
        super().draw(win)
        
    def support(self,towers):
        """
        buffs towers in radius with extra range
        :param towers: list
        :return: None
        """
        pass

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
        pass