import pygame
import os
from enemies.enemy import Enemy   

class Orc(Enemy): 
    imgs = []
    
    for x in range(6):
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/2/", "2_Walk00" + str(x) + ".png")), (64, 64)))
    
    def __init__(self):
        super().__init__()