import pygame
from class_blawhi import load_image


class Platform(pygame.sprite.Sprite):
    image = load_image('platform.png')

    def __init__(self, *group, location=(0, 0)):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
