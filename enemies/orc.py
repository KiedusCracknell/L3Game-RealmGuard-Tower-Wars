import pygame
import os
from enemies.enemy import Enemy   

imgs = []
for x in range(6):
    imgs.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/2/", "2_Walk00" + str(x) + ".png")), (64, 64)), True, False))
    

class Orc(Enemy): 
    def __init__(self):
        super().__init__()
        self.name = "orc"
        self.money = 12
        self.imgs = imgs[:]
        self.max_health = 4
        self.health = self.max_health
    
        