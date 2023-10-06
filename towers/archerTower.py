import pygame
from towers.tower import Tower
import os

class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(self,x,y)
        
        self.tower_img = pygame.transform.scale((pygame.image.load(os.path.join("game_assets/Towers", "long_range_tower.png")), (64,64)))
        self.archer_1_img = []
        self.archer_2_img = []
        self.archer_3_img = []
        self.archer_imgs = []
        self.archer_count = 0
        
        for x in range(6):
            self.archer_1_img.append(pygame.img.load(os.path.join("game_assets/Towers", "level_l", "a_attack00" + str(x) + ".png")))
        for x in range(6):
            self.archer_2_img.append(pygame.img.load(os.path.join("game_assets/Towers", "level_2", "a_attack00" + str(x) + ".png")))
        for x in range(6):
            self.archer_3_img.append(pygame.img.load(os.path.join("game_assets/Towers", "level_3", "a_attack00" + str(x) + ".png")))
        
    
    def draw(self, win):
        if self.level == 1:
            self.archer_imgs = self.archer_1_img
        elif self.level == 2:
            self.archer_imgs = self.archer_2_img
        elif self.level == 3:
            self.archer_imgs = self.archer_3_img
    
    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: enemy list
        :return: None
        """
        
            
    
    