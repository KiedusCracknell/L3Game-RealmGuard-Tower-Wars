import pygame
import os

pygame.font.init()

diamond = pygame.transform.scale(pygame.image.load(os.path.join('game_assets/gui', 'diamond.png')),(48,48))

class Button:
    """
    button class for menu objects
    """
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        
    def click(self,X,Y):
        """
        returns if the click event pos has collided with the menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x and Y <= self.y + self.height and Y >= self.y:
            return True
        return False
        
    def draw(self,win):
        win.blit(self.img, (self.x, self.y))

class Menu:
    """
    menu for holding items
    """
    def __init__(self, tower, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_costs = tower.upg_price[:]
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont(None, 25)
        self.tower = tower
        
    def add_btn(self, img, name):
        """
        adds button to the menu
        :param img: surface
        :param name: str
        :return: None 
        """
        self.items += 1
        inc_x = self.width/self.items
        btn_x = self.x - self.bg.get_width()/2 + 10
        btn_y = self.y - 120 + 30
        self.buttons.append(Button(btn_x, btn_y, img, name))
    
    
    def draw(self,win):
        """
        draw btns and menu bg
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y -100))
        for item in self.buttons:
            item.draw(win)
            win.blit(diamond, (item.x + item.width + 7, item.y - 7))
            upg_text = self.font.render(str(self.item_costs[self.tower.level-1]), 1, (255,255,255))
            win.blit(upg_text, (item.x + item.width + 30 - upg_text.get_width()/2, item.y + diamond.get_height() - 7))
    
    def get_clicked(self, X, Y):
        """
        returns the clicked item from the menu
        :param X: int
        :param Y: int
        :return: str
        """
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name
            return None
        
class VerticalButton(Button):
    """
    button class for vertical menu objects
    """
    def __init__(self, x, y, img, name, cost):
        super().__init__(x, y, img, name)
        self.cost = cost
         
            
class VerticalMenu(Menu):
    """
    vertical menu for sidebar of game
    """
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont(None, 25)

    def add_btn(self, img, name, cost):
        """
        adds button to the menu
        :param img: surface
        :param name: str
        :return: None 
        """
        self.items += 1
        btn_x = 1242
        btn_y = self.y + 10 + (self.items-1)*80
        self.buttons.append(VerticalButton(btn_x, btn_y, img, name, cost))
        print(str(self.items))
        
    def draw(self,win):
        """
        draw btns and menu bg
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y -100))
        for item in self.buttons:
            item.draw(win)
            win.blit(item.img, (item.x + item.width + 7, item.y - 7))
            upg_text = self.font.render((str(item.cost)), 1, (255,255,255))
            win.blit(upg_text, (item.x + item.width + 30 - upg_text.get_width()/2, item.y + diamond.get_height() - 7))        
    