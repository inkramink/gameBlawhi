import pygame
import os
import sys

JUMP_POWER = 12
GRAVITY = 0.65
ANIMATION_SPEED = 15


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
    images = [pygame.transform.scale2x(load_image(f"blawhi{i}.png", colorkey=-1)) for i in range(1, 10)]

    def __init__(self, *group, pos_x=0, pos_y=0):
        super().__init__(*group)
        self.image = Blawhi.images[0]
        self.image_i = 0
        self.animation_counter = 0
        self.left = True
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.yvel = 0  # Скорость по оси y
        self.xvel = 0  # Скорость по оси x
        self.speed = 5
        self.onGround = False  # Нахождение на земле

    def update(self, left, right, up, platforms):
        from class_buttonsForBlawhi import Buttons, RGButtons
        from main import RGB, RGB_coords
        for i in range(3):
            if pygame.sprite.collide_mask(self, Buttons(RGB, num=i, location=RGB_coords[i])) and \
                    RGButtons[i] == 0:
                RGButtons[i] = 1
        if left or right:  # смена кадра при ходьбе
            self.animation_counter += 1
            if self.animation_counter >= ANIMATION_SPEED:
                self.image_i += 1
                if self.image_i >= len(Blawhi.images):
                    self.image_i = 0
        if left:
            self.xvel = -self.speed
            self.left = True  # отражение спрайта
        if right:
            self.xvel = self.speed
            self.left = False  # отражение спрайта
        if not (left or right):
            self.xvel = 0
            self.image_i = 0
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.onGround = False
                self.image_i = 0
        if not self.onGround:
            self.yvel += GRAVITY
            # self.image_i = len(Blawhi.images) // 2

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        if not (self.left):
            self.image = Blawhi.images[self.image_i]
        else:
            self.image = pygame.transform.flip(Blawhi.images[self.image_i], 1, 0)

    def collide(self, xvel, yvel, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if xvel > 0:
                    self.rect.right = platform.rect.left
                if xvel < 0:
                    self.rect.left = platform.rect.right
                if yvel > 0:
                    self.rect.bottom = platform.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = platform.rect.bottom
                    self.yvel = 0
        if self.rect.right >= 800:
            self.rect.right = 800
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= 600 and self.yvel > 0:
            self.rect.bottom = 600
            self.yvel = 0
            self.onGround = True
