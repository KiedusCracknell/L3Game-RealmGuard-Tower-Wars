import pygame
import os
from enemies.slime import Slime
from enemies.orc import Orc
from enemies.bee import Bee
from towers.archerTower import ArcherTowerLong


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Bee()]
        self.towers = [ArcherTowerLong(300,200)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets/Map", "OLD-map.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            #pygame.time.delay(500) REMOVE
            clock.tick(30) #fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False #script stops if pygame window is closed
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)
                
            # loop through enemies
            to_del = []
            for en in self.enemys:
                if en.y > 720:
                    to_del.append(en)
                    
            # deltete enemies
            for d in to_del:
                self.enemys.remove(d) #removes enemies that are in to_del
            
            # loop through towers to find targets etc.
            for tw in self.towers:
                tw.attack(self.enemys)
                
            self.draw()
        
        pygame.quit()
                    
    def draw(self):
        self.win.blit(self.bg, (0, 0)) # draws pygame window
        
        # draw enemies 
        
        for tw in self.towers:
            tw.draw(self.win)
            
        for en in self.enemys:
            en.draw(self.win)
        
        pygame.display.update()
        
g = Game()
g.run()
