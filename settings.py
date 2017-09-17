class Settings():
    """store <<alien_invasion>> all settings class"""

    def __init__(self):
        """init game setting"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (0, 0, 255)

        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

        # 飞船设置
        self.ship_speed_factor = 15
        self.ship_limit = 3
