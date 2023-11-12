'''太空狙击（二）'''
import random

import pygame
from pygame.locals import *
# 初始化
pygame.init()

# 定义飞机类
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 加载飞机图片
        self.image = pygame.image.load('img/img_plane.png')
        # 设置飞机初始位置
        self.rect = self.image.get_rect()
        # 设置飞机长方形中心的X的值
        self.rect.centerx = WIDTH / 2

        # 设置飞机长方形底边的值
        self.rect.bottom = HEIGHT - 10

    def update(self):
        # 初始化速度为 0
        self.speedx = 0
        # 获取按键状态
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -8
        if keys[pygame.K_RIGHT]:
            self.speedx = 8
        # 根据速度改变飞机位置
        self.rect.centerx += self.speedx
        # 飞机左右移动限制
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shout(self):
        bullet =Bullet(self.rect.centerx,self.rect.top)
        all_sprite.add(bullet)
class Mete(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('img/img_meteorite.png')
        self.rect=self.image.get_rect()
        self.rect.left=random.randrange(0,WIDTH-self.rect.width)
        self.rect.bottom=random.randrange(-100,0)
        self.speedy=random.randrange(1,5)
        self.speedx=random.randrange(-3,3)
    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > HEIGHT or self.rect.right <0 or self.rect.left>WIDTH:
            self.rect.left = random.randrange(0, WIDTH - self.rect.width)
            self.rect.bottom = random.randrange(-100, 0)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('img/img_bullet.png')
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.speedy=-10
        if self.rect.top > HEIGHT or self.rect.right <0 or self.rect.left>WIDTH:
            self.rect.left = random.randrange(0, WIDTH - self.rect.width)
            self.rect.bottom = random.randrange(-100, 0)
    def update(self):

        self.rect.y+=self.speedy
        if self.rect.bottom <0 :
            self.kill()
# 定义屏幕宽，高
WIDTH = 480
HEIGHT = 600

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 加载背景图片
bg = pygame.image.load('img/img_bg.jpg')
# 定义飞机
plane = Plane()
all_sprite=pygame.sprite.Group()

all_sprite.add(plane)
for i in range(8):
    mete=Mete()
    all_sprite.add(mete)
# 控制帧速率
clock = pygame.time.Clock()
# 帧速率为60，即每秒执行60次循环
FPS = 60

running = True
while running:
    # 控制帧速率也就是每秒内循环执行的次数
    clock.tick(FPS)
    # 调用角色组移动的方法
    all_sprite.update()
    # 绘制背景
    screen.blit(bg, (0, 0))
    # 绘制角色组
    all_sprite.draw(screen)
    # 重绘界面，相当于刷新
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 点击叉号结束游戏
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # 按下ESC键结束游戏
                running = False
            if event.key ==pygame.K_SPACE:
                plane.shout()

# 彻底退出
pygame.quit()
