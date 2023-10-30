import pygame
import os
from enemies.enemy import Enemy   

imgs = []
for x in range(6):
    imgs.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/3/", "3_Walk00" + str(x) + ".png")), (64, 64)), True, False))
    

class Bee(Enemy): 
    def __init__(self):
        super().__init__()
        self.imgs = imgs[:]
        self.max_health = 8
        self.health = self.max_health