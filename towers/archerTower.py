import pygame
from towers.tower import Tower
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
        self.archer_count = 0
        self.range = 250
        self.inRange = False
        self.right = False
        self.timer = time.time()
        self.damage = 1
        
    
    def draw(self, win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128,128,128, 100), (self.range, self.range), self.range, 0)
        
        win.blit(surface, (self.x-self.range, self.y-self.range))
        super().draw(win)
        
        # self.width = self.tower_imgs[0].get_width()
        # self.height = self.tower_imgs[0].get_height()
        
        if self.level == 1:
            self.archer_imgs = self.archer_1_img
        elif self.level == 2:
            self.archer_imgs = self.archer_2_img
        elif self.level == 3:
            self.archer_imgs = self.archer_3_img
        
        if self.inRange:
            self.archer_count += 1
        else:
             self.archer_count = 0

        if self.archer_count >= len(self.archer_imgs)*3:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count//3]
        win.blit(archer, ((self.x + self.width/2) - 35, (self.y - archer.get_height() + 35)))
        

        
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
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.hit(self.damage) == True:
                    enemies.remove(first_enemy)
            
            if first_enemy.x > self.x and not(self.right):
                self.right = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.right and first_enemy.x < self.x:
                self.right = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            
        
class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        
        self.archer_1_img = archer_1_img[:]
        self.archer_2_img = archer_2_img[:]
        self.archer_3_img = archer_3_img[:]
        self.tower_imgs = tower_imgs_2[:]
        self.archer_imgs = []
        self.archer_count = 0
        self.range = 150
        self.inRange = False
        self.right = False
        self.timer = time.time()
        self.damage = 2