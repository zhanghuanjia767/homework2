import random
import pygame


# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 1000, 700)


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵基类"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed
        #增加主机的竖速度
        self.sspeed = speed
    def update(self, *args):

        # 默认在垂直方向移动
        self.rect.top += self.speed


class Background(GameSprite):
    """背景精灵"""

    def __init__(self):

        image_name = "./图片/背景.jpg"
        super().__init__(image_name, 0)
        
    def update(self, *args):

        # 调用父类方法
        super().update(args)



class Diren(GameSprite):
    """敌机精灵"""

    def __init__(self):

        image_name = "./图片/小怪.png"
        super().__init__(image_name)

        # 随机敌机出现位置
        width = SCREEN_RECT.width - self.rect.width
        self.rect.left = random.randint(0, width)
        self.rect.bottom = 0

        # 随机速度
        self.speed = random.randint(1, 3)

    def update(self, *args):
        super().update(args)

        # 判断敌机是否移出屏幕
        if self.rect.top >= SCREEN_RECT.height:
            # 将精灵从所有组中删除
            self.kill()

class Boss(GameSprite):
    """Boss精灵"""

    def __init__(self):

        image_name = "./图片/boss.png"
        super().__init__(image_name)

        # 随机敌机出现位置
        width = SCREEN_RECT.width - self.rect.width
        self.rect.left = random.randint(0, width)
        self.rect.bottom = 0

        # 随机速度
        self.speed = random.randint(3, 5)

    def update(self, *args):
        super().update(args)

        # 判断敌机是否移出屏幕
        if self.rect.top >= SCREEN_RECT.height:
            # 将精灵从所有组中删除
            self.kill()

class Qinglong(GameSprite):
    """青龙精灵"""

    def __init__(self):

        image_name = "./图片/青龙.png"
        super().__init__(image_name, 0)

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 140

        # 创建子弹组
        self.bullets1 = pygame.sprite.Group()
        self.jinengs1 = pygame.sprite.Group()

    def update(self, *args):

        # 飞机水平竖直移动
        self.rect.left += self.speed
        self.rect.bottom += self.sspeed
        # 超出屏幕检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.bottom > 700:
            self.rect.bottom = 700
        if self.rect.top < 0:
            self.rect.top = 0
    def fire(self):

        # bullet_count = len(self.bullets.sprites())
        # print("子弹数量 %d" % bullet_count)

       
            # 创建子弹精灵
        bullet = Bullet1()


        bullet.rect.bottom = self.rect.top
        bullet.rect.centerx = self.rect.centerx

            # 将子弹添加到精灵组
        self.bullets1.add(bullet)
    def jineng(self):
        jineng = jineng1()
        jineng.rect.bottom = self.rect.top
        jineng.rect.centerx = self.rect.centerx
        #将技能添加到精灵组
        self.jinengs1.add(jineng)
class Zhuque(GameSprite):
    """朱雀精灵"""

    def __init__(self):

        image_name = "./图片/朱雀.png"
        super().__init__(image_name, 0)

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx - 140
        self.rect.bottom = SCREEN_RECT.bottom - 140
        # 创建子弹组
        self.bullets2 = pygame.sprite.Group()
        self.jinengs2 = pygame.sprite.Group()
    def update(self, *args):

        # 飞机水平竖直移动
        self.rect.left += self.speed
        self.rect.bottom += self.sspeed
        # 超出屏幕检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.bottom > 700:
            self.rect.bottom = 700
        if self.rect.top < 0:
            self.rect.top = 0

    def fire(self):

        # bullet_count = len(self.bullets.sprites())
        # print("子弹数量 %d" % bullet_count)

       
            # 创建子弹精灵
        bullet = Bullet2()

            # 设置子弹位置
        bullet.rect.bottom = self.rect.top
        bullet.rect.centerx = self.rect.centerx

            # 将子弹添加到精灵组
        self.bullets2.add(bullet)
    def jineng(self):
        jineng = jineng2()
        jineng.rect.bottom = self.rect.top
        jineng.rect.centerx = self.rect.centerx
        #将技能添加到精灵组
        self.jinengs2.add(jineng)
class Baihu(GameSprite):
    """白虎精灵"""

    def __init__(self):

        image_name = "./图片/白虎.png"
        super().__init__(image_name, 0)

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx + 140
        self.rect.bottom = SCREEN_RECT.bottom - 140
        # 创建子弹组
        self.bullets3 = pygame.sprite.Group()
        self.jinengs3 = pygame.sprite.Group()
    def update(self, *args):

        # 飞机水平竖直移动
        self.rect.left += self.speed
        self.rect.bottom += self.sspeed
        # 超出屏幕检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.bottom > 700:
            self.rect.bottom = 700
        if self.rect.top < 0:
            self.rect.top = 0

    def fire(self):

        # bullet_count = len(self.bullets.sprites())
        # print("子弹数量 %d" % bullet_count)


            # 创建子弹精灵
        bullet = Bullet3()
            # 设置子弹位置
        bullet.rect.bottom = self.rect.top
        bullet.rect.centerx = self.rect.centerx

            # 将子弹添加到精灵组
        self.bullets3.add(bullet)
    def jineng(self):
        jineng = jineng3()
        jineng.rect.bottom = self.rect.top
        jineng.rect.centerx = self.rect.centerx
        self.jinengs3.add(jineng)


class Bullet1(GameSprite):
    """青龙子弹精灵"""

    def __init__(self):

        image_name = "./图片/青龙子弹.png"
        super().__init__(image_name, -5)

    def update(self, *args):

        super().update(args)

        # 判断是否超出屏幕
        if self.rect.bottom < 0:
            self.kill()
class Bullet2(GameSprite):
    """朱雀子弹精灵"""

    def __init__(self):

        image_name = "./图片/朱雀子弹.png"
        super().__init__(image_name, -5)

    def update(self, *args):

        super().update(args)

        # 判断是否超出屏幕
        if self.rect.bottom < 0:
            self.kill()
class Bullet3(GameSprite):
    """白虎子弹精灵"""

    def __init__(self):

        image_name = "./图片/白虎子弹.png"
        super().__init__(image_name, -5)

    def update(self, *args):

        super().update(args)

        # 判断是否超出屏幕
        if self.rect.bottom < 0:
            self.kill()
class jineng1(GameSprite):
    """青龙技能精灵"""

    def __init__(self):

        image_name = "./图片/青龙技能.png"
        super().__init__(image_name, -50)

    def update(self, *args):

        super().update(args)

        # 判断是否超出屏幕
        if self.rect.bottom < 0:
            self.kill()

class jineng2(GameSprite):
    """朱雀技能精灵"""

    def __init__(self):

        image_name = "./图片/朱雀技能.png"
        super().__init__(image_name, -50)

    def update(self, *args):

        super().update(args)

        # 判断是否超出屏幕
        if self.rect.bottom < 0:
            self.kill()
class jineng3(GameSprite):
    """白虎技能精灵"""

    def __init__(self):

        image_name = "./图片/白虎技能.png"
        super().__init__(image_name, -50)

    def update(self, *args):

        super().update(args)

        # 判断是否超出屏幕
        if self.rect.bottom < 0:
            self.kill()
