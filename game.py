import pygame
import os
from enemies.slime import Slime
from enemies.orc import Orc
from enemies.bee import Bee
from towers.archerTower import ArcherTowerLong, ArcherTowerShort
from towers.supportTower import RangeTower, DamageTower
from menu.menu import VerticalMenu
import time
import random

pygame.font.init()

live_img = pygame.image.load(os.path.join("game_assets/gui", "heart.png"))
diamond = pygame.image.load(os.path.join("game_assets/gui", "diamond.png"))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/gui", "box_square.png")),(120,500))

buy_archer_long = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/towers", "long_range_tower.png")),(45,90))
buy_archer_short = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/towers", "short_range_tower.png")),(45,90))
buy_support_range = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/towers", "support_range_tower.png")),(45,90))
buy_support_damage = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/towers", "support_damage_tower.png")),(45,90))

attack_tower_names = ["archer", "archer2"]
support_tower_names = ["support", "support2"]



class Game:
    def __init__(self):
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.attack_towers = [ArcherTowerLong(300,200), ArcherTowerShort(700,500)]
        self.support_towers = [RangeTower(410, 330), DamageTower(620, 500)]
        self.lives = 10
        self.money = 1000
        self.bg = pygame.image.load(os.path.join("game_assets/Map", "OLD-map.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        #self.clicks = []
        self.timer = time.time()
        self.life_font = pygame.font.SysFont(None, 45)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - side_img.get_width()+ 70, 220, side_img)
        self.menu.add_btn(buy_archer_long, "Long Range", 400)
        self.menu.add_btn(buy_archer_short, "Short Range", 600)
        self.menu.add_btn(buy_support_range, "Support Range", 300)
        self.menu.add_btn(buy_support_damage, "Support Damage", 600)
        self.moving_object = None
        self.cost = 0
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(200) #fps
            
            # gen monsters
            if time.time() - self.timer > random.randrange(1,5)/2:
                self.timer = time.time()
                self.enemys.append(random.choice([Slime(), Orc(), Bee()]))
            
            pos = pygame.mouse.get_pos()
            # check for moving object
            if self.moving_object is not None:
                self.moving_object.move(pos[0], pos[1])
            
            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False #script stops if pygame window is closed
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #if you're moving an object and you click
                    if self.moving_object and event.button == 3:
                        self.moving_object.moving = False
                        self.moving_object = None
                                               
                    if self.moving_object is not None:
                        if self.moving_object.name in attack_tower_names:
                            self.attack_towers.append(self.moving_object)
                            self.money -= self.cost
                            self.cost = 0
                        elif self.moving_object.name in support_tower_names:
                            self.support_towers.append(self.moving_object)
                            self.money -= self.cost
                            self.cost = 0
                        self.moving_object.moving = False
                        self.moving_object = None
                        
                    else:
                        #check if you click on side menu
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            self.cost = self.menu.get_item_cost(side_menu_button)
                            if self.cost <= self.money:
                                self.add_tower(side_menu_button)
                        btn_clicked = None
                        #check if click is on upgrade/sell buttons
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0],pos[1])
                            if btn_clicked:
                                if btn_clicked == "Upgrade":
                                    if self.money >= self.selected_tower.upg_price[self.selected_tower.level-1]:
                                        self.money -= self.selected_tower.upg_price[self.selected_tower.level-1]
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
                self.money += tw.attack(self.enemys)
                
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
            
        #draw moving object
        if self.moving_object is not None:
            self.moving_object.draw(self.win)
            
        #draw menu
        self.menu.draw(self.win)
        
        #draw lives
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = pygame.transform.scale(live_img, (45,45))
        start_x = self.width - life.get_width() - 10
        
        self.win.blit(text, (start_x - text.get_width() - 10, 15))
        self.win.blit(life, (start_x, 10))
        
        #draw money
        text = self.life_font.render(str(self.money), 1, (255,255,255))
        money = pygame.transform.scale(diamond, (45,45))
        start_x = self.width - money.get_width() - 10
        
        self.win.blit(text, (start_x - text.get_width() - 10, 70))
        self.win.blit(money, (start_x, 65))    
        
        pygame.display.update()
    
    def add_tower(self, name):
        x,y = pygame.mouse.get_pos()
        name_list = ["Long Range", "Short Range", "Support Range", "Support Damage"]
        object_list = [ArcherTowerLong(x,y), ArcherTowerShort(x,y), RangeTower(x,y), DamageTower(x,y)]
        
        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")
    
    
        
g = Game()
g.run()
