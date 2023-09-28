import pygame

class Tower:
    """
    Abstract class for Towers
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.price = [0,0,0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.tower_imgs
        
        
    
    def draw(self, win):
        """
        draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_imgs[self.level - 1]
        win.blit(img, self.x-img.get_width()//2, self.y-img.get_height()//2)
    
    def click(self,X,Y):
        """
        returns if the tower has been clicked on and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
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
        self.level += 1
    
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
    