import pygame
import os
from enemies.slime import Slime
from enemies.orc import Orc
from enemies.bee import Bee
from towers.archerTower import ArcherTowerLong, ArcherTowerShort
from towers.supportTower import RangeTower, DamageTower
import time
import random

pygame.font.init()

live_img = pygame.image.load(os.path.join("game_assets/gui", "heart.png"))


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.attack_towers = [ArcherTowerLong(300,200), ArcherTowerShort(700,500)]
        self.support_towers = [RangeTower(410, 330), DamageTower(620, 500)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets/Map", "OLD-map.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        #self.clicks = []
        self.timer = time.time()
        self.life_font = pygame.font.SysFont(None, 55)
        self.selected_tower = None
        
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            if time.time() - self.timer > random.randrange(1,5)/2:
                self.timer = time.time()
                self.enemys.append(random.choice([Slime(), Orc(), Bee()]))
            #pygame.time.delay(500) REMOVE
            clock.tick(200) #fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False #script stops if pygame window is closed
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    btn_clicked = None
                    #check if click is on upgrade/sell buttons
                    if self.selected_tower:
                        btn_clicked = self.selected_tower.menu.get_clicked(pos[0],pos[1])
                        if btn_clicked:
                            if btn_clicked == "Upgrade":
                                self.selected_tower.upgrade()
                                
                    #if not clicked on upgrade/sell buttons
                    if not btn_clicked:
                        #check if click is on attack tower
                        for tw in self.attack_towers:
                            if tw.click(pos[0],pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False
                        #check if click is on support tower
                        for tw in self.support_towers:
                            if tw.click(pos[0],pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False
                
            # loop through enemies
            to_del = []
            for en in self.enemys:
                if en.y > 720:
                    to_del.append(en)
                    
            # deltete enemies
            for d in to_del:
                self.lives -= 1 #removes a life when enemy makes it offscreen
                self.enemys.remove(d) #removes enemies that are in to_del
            
            # loop through attack towers to find targets etc.
            for tw in self.attack_towers:
                tw.attack(self.enemys)  
                
            # loop through support towers to find targets etc.
            for tw in self.support_towers:
                tw.support(self.attack_towers)
                
            if self.lives <= 0:
                print("you lose")
                run = False
                
            self.draw()
        
        pygame.quit()
                    
    def draw(self):
        self.win.blit(self.bg, (0, 0)) # draws pygame window
        
        # draw  attack towers 
        for tw in self.attack_towers:
            tw.draw(self.win)
            
        #draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)
            
        #draw enemies    
        for en in self.enemys:
            en.draw(self.win)
        
        #draw lives
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        
        life = pygame.transform.scale(live_img, (45,45))
        start_x = self.width - life.get_width() - 10
        
        self.win.blit(text, (start_x - text.get_width() - 10, 15))
        self.win.blit(life, (start_x, 10))
        
        pygame.display.update()
        
    def draw_menu(self):
        pass
        
g = Game()
g.run()
