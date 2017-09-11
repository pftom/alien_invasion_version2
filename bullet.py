import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """在飞船所在位置创建一个子弹对象"""
    
    def __init__(self, ai_settings, screen, ship):
        """在飞船所在位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)处创建一个子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.conterx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示的子弹位置