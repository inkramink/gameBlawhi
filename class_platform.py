import pygame
from math import sqrt
from class_blawhi import load_image, Blawhi
from main import size


class Platform(pygame.sprite.Sprite):
    image = load_image('platform.png')

    def __init__(self, *group, location=(0, 0)):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class PlatformHor(pygame.sprite.Sprite):
    image = load_image('platform.png')

    def __init__(self, *group, location=(0, 0), lenn=100):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.orig = location[0]
        self.lenn = lenn
        self.fl = 1
        self.rect.left, self.rect.top = location

    def update(self):
        if self.rect.left == self.orig:
            self.fl = 1
        if self.rect.left == self.orig + self.lenn:
            self.fl = -1
        if not (self.orig <= self.rect.left <= self.orig + self.lenn):
            self.fl *= -1
        self.rect.left += self.fl * 1


class PlatformVer(pygame.sprite.Sprite):
    image = load_image('platform.png')

    def __init__(self, *group, location=(0, 0), lenn=100):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.orig = location[1]
        self.lenn = lenn
        self.fl = 1
        self.rect.left, self.rect.top = location

    def update(self):
        if self.rect.top == self.orig:
            self.fl = -1
        if self.rect.top == self.orig - self.lenn:
            self.fl = 1
        self.rect.top += self.fl * 1
