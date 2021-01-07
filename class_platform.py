import pygame
from math import sqrt
from class_blawhi import load_image


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


class PlatformKr(pygame.sprite.Sprite):
    image = load_image('platform.png')

    def __init__(self, *group, location=(0, 0), rad=100):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.orig = location
        self.rad = rad
        self.fl = 1
        self.rect.left, self.rect.top = location
        self.rect.top += 100

    def update(self):
        if self.orig[0] <= self.rect.left < self.orig[0] + 100 and \
                self.orig[1] < self.rect.top <= self.orig[1] + 100 and self.rect.left != self.orig[0] + 100:
            self.rect.left += 1
            self.rect.top = self.orig[1] + sqrt(self.rad ** 2 - (self.rect.left - self.orig[0]) ** 2)
        if self.orig[0] < self.rect.left <= self.orig[0] + 100 and \
                self.orig[1] >= self.rect.top > self.orig[1] - 100:
            self.rect.top -= 1
            self.rect.left = self.orig[1] + sqrt(self.rad ** 2 - (self.rect.top - self.orig[1]) ** 2)
        if self.orig[0] >= self.rect.left > self.orig[0] - 100 and \
                self.orig[1] > self.rect.top >= self.orig[1] - 100:
            self.rect.left -= 1
            self.rect.top = self.orig[0] - sqrt(self.rad ** 2 - (self.rect.left - self.orig[1]) ** 2)
        if self.orig[0] > self.rect.left >= self.orig[0] - 100 and \
                self.orig[1] <= self.rect.top < self.orig[1] + 100:
            self.rect.top += 1
            self.rect.left = self.orig[0] - sqrt(self.rad ** 2 - (self.rect.top - self.orig[1]) ** 2)
