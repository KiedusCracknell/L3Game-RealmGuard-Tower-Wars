import pygame
from towers.tower import Tower
import os

class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(x,y)
        
        self.tower_imgs = []
        self.archer_1_img = []
        self.archer_2_img = []
        self.archer_3_img = []
        self.archer_imgs = []
        self.archer_count = 0
        
        self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers", "long_range_tower.png")), (64,64)))
        
        for x in range(6):
            self.archer_1_img.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers/level_1", "a_Attack00" + str(x) + ".png")), (64,64)))
        for x in range(6):
            self.archer_2_img.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers/level_2", "a_Attack00" + str(x) + ".png")), (64,64)))
        for x in range(6):
            self.archer_3_img.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers/level_3", "a_Attack00" + str(x) + ".png")), (64,64)))
        
    
    def draw(self, win):
        super().draw(win)
        if self.level == 1:
            self.archer_imgs = self.archer_1_img
        elif self.level == 2:
            self.archer_imgs = self.archer_2_img
        elif self.level == 3:
            self.archer_imgs = self.archer_3_img
        if self.archer_count >= len(self.archer_imgs)*3:
            self.archer_count = 0
        
        archer = self.archer_imgs[self.archer_count//3]
        win.blit(archer, ((self.x + self.width/2) - (archer.get_width()/2), (self.y - archer.get_height())))
        
    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: enemy list
        :return: None
        """
        pass
        
            
    
    