import pygame
from towers.tower import Tower, menu_bg, upgrade_btn
from menu.menu import Menu
import os
import math
import time

#loads long range tower images
tower_imgs_1 = []
tower_imgs_1.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers", "long_range_tower.png")), (90,180)))

#loads short range tower images
tower_imgs_2 = []
tower_imgs_2.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers", "short_range_tower.png")), (90,180)))


#loads archer images
archer_1_img = []
archer_2_img = []
archer_3_img = []

for x in range(6):
    archer_1_img.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers/level_1", "a_Attack00" + str(x) + ".png")), (72,72)))
for x in range(6):
    archer_2_img.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers/level_2", "a_Attack00" + str(x) + ".png")), (72,72)))
for x in range(6):
    archer_3_img.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers/level_3", "a_Attack00" + str(x) + ".png")), (72,72)))


class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(x,y)
        
        self.tower_imgs = tower_imgs_1[:]
        self.archer_1_img = archer_1_img[:]
        self.archer_2_img = archer_2_img[:]
        self.archer_3_img = archer_3_img[:]
        self.archer_imgs = []
        self.upg_price = [1000,5000,"MAX"]
        self.archer_count = 0
        self.range = 250
        self.original_range = self.range
        self.inRange = False
        self.right = False
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.tower_imgs[0].get_width()
        self.height = self.tower_imgs[0].get_height()
        #def menu
        self.menu = Menu(self, self.x, self.y, menu_bg)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "archer"
        
    
    def draw(self, win):
        super().draw_radius(win, self.range,128,128,128)
        super().draw(win)
        
        # self.width = self.tower_imgs[0].get_width()
        # self.height = self.tower_imgs[0].get_height()
        
        if self.level == 1:
            self.archer_imgs = self.archer_1_img
        elif self.level == 2:
            self.archer_imgs = self.archer_2_img
        elif self.level == 3:
            self.archer_imgs = self.archer_3_img
        
        if self.inRange and not self.moving:
            self.archer_count += 1
        else:
             self.archer_count = 0

        if self.archer_count >= len(self.archer_imgs)*10:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count//10 - 1]
        win.blit(archer, ((self.x) - 35, (self.y - archer.get_height() + 35)))
        

        
    def change_range(self, r):
        """
        change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r
        
    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: enemy list
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
          x = enemy.x
          y = enemy.y
          
          dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
          if dis < self.range:
              self.inRange = True
              enemy_closest.append(enemy)
        
        enemy_closest.sort(key=lambda x: x.x)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.archer_count == 3:
                if first_enemy.hit(self.damage) == True:
                    enemies.remove(first_enemy)
                    money = first_enemy.money
            
            if first_enemy.x > self.x and not(self.right):
                self.right = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.right and first_enemy.x < self.x:
                self.right = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
        return money
            
        
class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        
        self.archer_1_img = archer_1_img[:]
        self.archer_2_img = archer_2_img[:]
        self.archer_3_img = archer_3_img[:]
        self.tower_imgs = tower_imgs_2[:]
        self.archer_imgs = []
        self.upg_price = [2000,6000,"MAX"]
        self.archer_count = 0
        self.range = 150
        self.inRange = False
        self.right = False
        self.damage = 2
        self.original_range = self.range
        self.original_damage = self.damage
        self.width = self.tower_imgs[0].get_width()
        self.height = self.tower_imgs[0].get_height()
        #def menu
        self.menu = Menu(self, self.x, self.y, menu_bg)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "archer2"
