import pygame
from class_blawhi import load_image

all_sprites = pygame.sprite.Group()
from class_blawhi import Blawhi

blawhi_player = Blawhi(all_sprites)
flagRGB = pygame.sprite.Group()
RGButtons = [0, 0, 0]


class FlagButtons(pygame.sprite.Sprite):
    images = [load_image('button.png', colorkey=-1), load_image('buttonRed.png', colorkey=-1),
              load_image('buttonGreen.png', colorkey=-1), load_image('buttonBlue.png', colorkey=-1)]

    def __init__(self, num=0):
        super().__init__(all_sprites)
        self.add(flagRGB)
        if RGButtons[num] == 1:
            self.image = FlagButtons.images[num + 1]
        else:
            self.image = FlagButtons.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 780
        self.rect.y = 20 * num


class Buttons(pygame.sprite.Sprite):
    images = [load_image('buttonRed.png', colorkey=-1), load_image('buttonGreen.png', colorkey=-1),
              load_image('buttonBlue.png', colorkey=-1)]

    def __init__(self, *group, num=0, location=(0, 0)):
        super().__init__(*group)
        self.image = Buttons.images[num]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = location
