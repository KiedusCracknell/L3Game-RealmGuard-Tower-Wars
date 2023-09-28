import pygame
from towers.tower import Tower

class ArcherTower(Tower):
    def __init__(self,x,y):
        super().__init__(self,x,y)
        
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        
    def draw(self, win):
        super().draw(win)
    
    def attacl(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: enemy list
        :return: None
        """
        
            
    
    