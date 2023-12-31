import pygame
import os
from enemies.enemy import Enemy   

imgs = []
for x in range(6):
    imgs.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/1/", "1_Walk00" + str(x) + ".png")), (64, 64)), False, False))


class Slime(Enemy): 
    def __init__(self):
        super().__init__()
        self.name = "slime"
        self.money = 5
        self.imgs = imgs[:]
        self.max_health = 2
        self.health = self.max_health
        