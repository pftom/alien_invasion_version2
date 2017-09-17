import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """init the ship and set the initial setting"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船都放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center种存储小数值
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # 移动标志
        # 横向
        self.moving_right = False
        self.moving_left = False
        # 纵向
        self.moving_up = False
        self.moving_down = False

    def update_x(self):
        """根据移动标志调整飞船横向的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor

        # 根据self.center 更新rect对象
        self.rect.centerx = self.center_x

    def update_y(self):
        """根据移动标志调整飞船纵向的位置"""
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        # 根据self.center 更新rect对象
        self.rect.centery = self.center_y
    
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)