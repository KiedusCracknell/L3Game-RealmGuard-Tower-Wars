import pygame
from menu.menu import Menu
import os
import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/gui/", "box_square.png")), (125, 70))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/gui/", "upgrade.png")), (50, 50))

class Tower:
    """
    Abstract class for Towers
    """
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.upg_price = [1232]
        self.level = 1
        self.selected = False

        
        self.tower_imgs = []
        self.damage = 1
        self.original_damage = 0
        self.moving = False
        
    
    def draw(self, win):
        """
        draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_imgs[0]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))
        
        #draw menu
        if self.selected:
        # define menu and buttons
            self.menu = Menu(self, self.x, self.y, menu_bg)
            self.menu.add_btn(upgrade_btn, "Upgrade")
            self.menu.draw(win)
        
    def draw_radius(self,win,radius,r,g,b):
        if self.selected:
            surface = pygame.Surface((radius * 4, radius * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (r,g,b, 100), (radius, radius), radius, 0)
            
            win.blit(surface, (self.x-radius, self.y-radius))
            
    def draw_placement(self,win):
        surface = pygame.Surface((40 * 4, 40 * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (255,0,0, 100), (40, 40), 40, 0)
        
        win.blit(surface, (self.x-40, self.y-40))
    
    def click(self,X,Y):
        """
        returns if the tower has been clicked on and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: Bool
        """
        img = self.tower_imgs[0]
        if X <= self.x-img.get_width()//2 + img.get_width() and X >= self.x-img.get_width()//2:
            if Y <= self.y-img.get_height()//2 + img.get_height() and Y >= self.y-img.get_height()//2:
                return True
        return False
    
    def sell(self):
        """
        call to sell the selected tower, return sell price
        :return: int
        """
        return self.sell_price[self.level-1]
    
    def upgrade(self):
        """
        upgrades the selected tower for a given cost
        :return: None
        """
        if isinstance(self.menu.item_costs[self.level-1],(float,int)):
            self.level += 1
            self.damage += 1
            self.original_damage += 1
        else:
            print("max level")
            print("dmg:", self.damage, "level:", self.level, "range:", self.range)
    
    def get_upgrade_cost(self):
        """
        returns the upgrade cost for the selected tower, if 0 then upgrade isn't available
        :return: int
        """
        return self.price[self.level-1]
    
    def move(self,x,y):
        """
        Makes tower follow the mouse position when placing a new tower
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y 
        
    def collide(self, otherTower):
        x2 = otherTower.x 
        y2 = otherTower.y + 45
        
        dis = math.sqrt((x2-self.x)**2 + (y2-self.y)**2)
        
        if dis <= 82:
            return True
        else:
            return False
        
    def collide_path(self, otherTower):
        x = otherTower.x
        y = otherTower.y
        h = otherTower.height//2
        if x >= 73 and x <= 177 and y >= 0 - h and y <= 220:
            return True
        if x >= 73 and x <= 1240 and y >= 130 - h and y <= 220:
            return True
        if x >= 1139 and x <= 1269 and y >= 130 - h and y <= 412:
            return True
        if x >= 961 and x <= 1138 and y >= 324  - h and y <= 505:
            return True
        if x >= 536 and x <= 960 and y >= 415 - h and y <= 507:
            return True
        if x >= 535 and x <= 634 and y >= 418 - h and y <= 700:
            return True
        else:
            return False