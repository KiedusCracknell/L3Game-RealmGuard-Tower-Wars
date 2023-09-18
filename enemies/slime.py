import pygame
import os
from enemies.enemy import Enemy   

class Slime(Enemy): 
    imgs = []
    
    for x in range(6):
        imgs.append(pygame.image.load(os.path.join("game_assets/1/", "1_Walk00" + str(x) + ".png")))
    
    def __init__(self):
        super().__init__()