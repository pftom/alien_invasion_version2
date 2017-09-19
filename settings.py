class Settings():
    """store <<alien_invasion>> all settings class"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (0, 0, 255)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 100

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

        # 最高分写入文件
        self.highest_score_filename = 'history_highest_score.txt'

    def initialize_dynamic_settings(self):
        """初始化随游戏变化而进行的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右； 为-1表示向左
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)