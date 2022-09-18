import pygame
from plane_sprites import *

# 敌机出现事件（pygame.USEREVENT,set_timer 可以创建一个 事件,可以在 游戏循环 的 事件监听 方法中捕获到该事件,第 1 个参数 事件代号 需要基于常量 pygame.USEREVENT 来指定USEREVENT 是一个整数，再增加的事件可以使用 USEREVENT + 1 指定，依次类推…）
CREATE_ENEMY_EVENT = pygame.USEREVENT#第 2 个参数是 事件触发 间隔的 毫秒值通过 pygame.event.get() 可以获取当前时刻所有的 事件列表,遍历列表 并且判断 event.type 是否等于 eventid，如果相等，表示 定时器事件 发生
# boss出现事件
BOSS_ENEMY_EVENT =pygame.USEREVENT + 1
# 子弹自动射击事件
FIRE = pygame.USEREVENT + 2
class PlaneGame(object):
    """飞机大战游戏类"""

    def __init__(self):

        # 1. pygame 初始化
        pygame.init()

        # 2. 创建游戏屏幕
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 3. 创建游戏时钟
        self.clock = pygame.time.Clock()

        # 4. 创建精灵组
        self.__create_sprites()

        # 5. 创建用户事件
        PlaneGame.__create_user_events()

    def __create_sprites(self):
        """创建精灵组"""

        # 背景组
        bg1 = Background()
    
        self.back_group = pygame.sprite.Group(bg1)

        # 敌机组
        enemy = Diren()
        self.Diren_group = pygame.sprite.Group(enemy)
        #boss组
        boss = Boss()
        self.Boss_group = pygame.sprite.Group(boss)
        # 青龙组
        self.Qinglong = Qinglong()
        self.Qinglong_group = pygame.sprite.Group(self.Qinglong)

        #朱雀组
        self.Zhuque = Zhuque()
        self.Zhuque_group = pygame.sprite.Group(self.Zhuque)

        #白虎组
        self.Baihu =Baihu()
        self.Baihu_group = pygame.sprite.Group(self.Baihu)

    @staticmethod
    def __create_user_events():
        """创建用户事件"""

        # 每零点三秒添加一架敌机，（python.time.set_timer()）添加定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1 * 300)
        pygame.time.set_timer(FIRE, 250)
        # 每三秒添加一架boss，定时器添加boss
        pygame.time.set_timer(BOSS_ENEMY_EVENT, 3000)

    def start_game(self):
        """开始游戏"""
        #循环播放载入音乐
        pygame.mixer.init()
        pygame.mixer.music.load("./图片/背景音乐.mp3")
        pygame.mixer.music.play(-1)
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(60)
            # 2. 事件监听
            self.__event_handler()
            # 3. 更新精灵组
            self.__update_sprites()
            # 碰撞检测
            self.__check_collide()
            # 4. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self,):
        """事件监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print("退出游戏...")
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机，并且添加到敌机组
                self.Diren_group.add(Diren())

                # 测试敌机精灵数量
                # enemy_count = len(self.enemy_group.sprites())
                # print("敌机精灵数量 %d" % enemy_count)
            elif event.type == FIRE:
                self.Qinglong.fire()
                self.Baihu.fire()
                self.Zhuque.fire()
            elif event.type == BOSS_ENEMY_EVENT:
                self.Boss_group.add(Boss())

                

        # 通过 pygame.key 获取用户按键
        keys_pressed = pygame.key.get_pressed()
        dir = keys_pressed[pygame.K_d] - keys_pressed[pygame.K_a]
        dir2 = keys_pressed[pygame.K_s] - keys_pressed[pygame.K_w]
        dir3 = keys_pressed[pygame.K_l] - keys_pressed[pygame.K_j]
        dir4 = keys_pressed[pygame.K_k] - keys_pressed[pygame.K_i]
        dir5 = keys_pressed[pygame.K_RIGHT] - keys_pressed[pygame.K_LEFT]
        dir6 = keys_pressed[pygame.K_DOWN] - keys_pressed[pygame.K_UP]
        if keys_pressed[pygame.K_e]:
            self.Qinglong.jineng()
        if keys_pressed[pygame.K_o]:
            self.Zhuque.jineng()
        if keys_pressed[pygame.K_PERIOD]:
            self.Baihu.jineng()
        if keys_pressed[pygame.K_q]:
            self.Qinglong.fire()
        if keys_pressed[pygame.K_u]:
            self.Zhuque.fire()
        if keys_pressed[pygame.K_COMMA]:
            self.Baihu.fire()
        # 根据移动方向设置英雄的速度
        self.Qinglong.speed = dir * 3
        self.Qinglong.sspeed = dir2 * 3
        self.Zhuque.speed = dir3 * 3
        self.Zhuque.sspeed = dir4 * 3
        self.Baihu.speed = dir5 * 3
        self.Baihu.sspeed = dir6 * 3
        

    def __update_sprites(self):
        """更新精灵组"""

        for group in [self.back_group, self.Diren_group,
                      self.Boss_group, self.Qinglong_group,
                      self.Zhuque_group, self.Baihu_group,
                      self.Qinglong.bullets1,self.Qinglong.jinengs1,
                      self.Zhuque.bullets2,self.Zhuque.jinengs2,
                      self.Baihu.bullets3,self.Baihu.jinengs3]:

            group.update()
            group.draw(self.screen)

    def __check_collide(self):
        """碰撞检测"""

        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.Qinglong.bullets1, self.Diren_group, True, True)
        pygame.sprite.groupcollide(self.Zhuque.bullets2, self.Diren_group, True, True)
        pygame.sprite.groupcollide(self.Baihu.bullets3, self.Diren_group, True, True)
        pygame.sprite.groupcollide(self.Qinglong.bullets1, self.Boss_group, True, True)
        pygame.sprite.groupcollide(self.Zhuque.bullets2, self.Boss_group, True, True)
        pygame.sprite.groupcollide(self.Baihu.bullets3, self.Boss_group, True, True)
        # 2. 技能摧毁敌机
        pygame.sprite.groupcollide(self.Qinglong.jinengs1, self.Diren_group, True, True)
        pygame.sprite.groupcollide(self.Zhuque.jinengs2, self.Diren_group, True, True)
        pygame.sprite.groupcollide(self.Baihu.jinengs3, self.Diren_group, True, True)
        pygame.sprite.groupcollide(self.Qinglong.jinengs1, self.Boss_group, True, True)
        pygame.sprite.groupcollide(self.Zhuque.jinengs2, self.Boss_group, True, True)
        pygame.sprite.groupcollide(self.Baihu.jinengs3, self.Boss_group, True, True)
        # 3. 神兽被撞毁
        collide_list = pygame.sprite.spritecollide(self.Qinglong, self.Diren_group, False)
        collide_list2 = pygame.sprite.spritecollide(self.Zhuque, self.Diren_group, False)
        collide_list3 = pygame.sprite.spritecollide(self.Baihu, self.Diren_group, False)
        collide_list4 = pygame.sprite.spritecollide(self.Qinglong, self.Boss_group, False)
        collide_list5 = pygame.sprite.spritecollide(self.Zhuque, self.Boss_group, False)
        collide_list6 = pygame.sprite.spritecollide(self.Baihu, self.Boss_group, False)
        
        if len(collide_list) > 0:
            self.Qinglong.kill()

            print("青龙牺牲...")

            pygame.quit()
            exit()
        if len(collide_list2) > 0:
            self.Zhuque.kill()

            print("朱雀牺牲...")

            pygame.quit()
            exit()
        if len(collide_list3) > 0:
            self.Baihu.kill()

            print("白虎牺牲...")

            pygame.quit()
            exit()
        if len(collide_list4) > 0:
            self.Qinglong.kill()

            print("青龙牺牲...")

            pygame.quit()
            exit()
        if len(collide_list5) > 0:
            self.Zhuque.kill()

            print("朱雀牺牲...")

            pygame.quit()
            exit()
        if len(collide_list6) > 0:
            self.Baihu.kill()

            print("白虎牺牲...")

            pygame.quit()
            exit()
if __name__ == '__main__':
    # 1. 创建游戏对象
    game = PlaneGame()

    # 2. 开始游戏
    game.start_game()