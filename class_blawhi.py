import pygame
import os
import sys
JUMP_POWER = 5
GRAVITY = 0.35


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Blawhi(pygame.sprite.Sprite):
    image = load_image("blawhi1.png", colorkey=-1)

    def __init__(self, *group, pos_x=0, pos_y=0):
        super().__init__(*group)
        self.image = Blawhi.image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.yvel = 0  # Скорость по оси y
        self.xvel = 0  # Скорость по оси x
        self.speed = 5
        self.onGround = False  # Нахождение на земле

    def update(self, left, right, up):
        if left:
            self.xvel = -self.speed
        if right:
            self.xvel = self.speed
        if not (left or right):
            self.xvel = 0
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.onGround = False
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.collide()

    def collide(self):
        if self.rect.right >= 800:
            self.rect.right = 800
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= 600:
            self.yvel = 0
            self.onGround = True

