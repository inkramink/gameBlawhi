import pygame
from class_blawhi import load_image


class Platform(pygame.sprite.Sprite):
    image = pygame.transform.scale2x(load_image("platform.jpg", colorkey=-1))

    def __init__(self, *group, location=(0, 0)):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
