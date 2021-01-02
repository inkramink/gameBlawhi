import os
import sys
import pygame


def levels_init(LEVELS):
    platform_coords = [
        [(50, 580), (150, 500), (280, 426), (440, 430), (330, 380), (160, 300)],
        [(250, 540), (400, 470), (560, 360), (370, 300), (680, 390)]
        ]
    RGB_coords = [
        [button(platform_coords[0], 3), button(platform_coords[0], 4), button(platform_coords[0], 5)],
        [button(platform_coords[1], 2), button(platform_coords[1], 3), button(platform_coords[1], 4)],
        ]

    botom_platforms = [(i, 595) for i in range(0, 800, 60)]    
    for i in range(len(platform_coords)):  # во всех уровнях пол выложен платформами
        for platform in botom_platforms:
            platform_coords[i].append(platform)
    
    return platform_coords[:LEVELS], RGB_coords[:LEVELS]


def button(platform_coords, platform):
    # рассчитывает положение кнопки относительно платформы
    return platform_coords[platform][0] + 20, platform_coords[platform][1] - 20


def level(screen, platform_coords, RGB_coords, RGB):
    screen.fill((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    from class_buttonsForBlawhi import FlagButtons, flagRGB, Buttons, RGButtons

    for i in range(3):
        FlagButtons(i)
        Buttons(RGB, num=i, location=RGB_coords[i])
    from class_blawhi import Blawhi

    blawhi_player = Blawhi(all_sprites)
    platforms = pygame.sprite.Group()
    from class_platform import Platform

    for i in platform_coords:
        my_platform = Platform(platforms, location=i)
    running = True
    left, right, up = False, False, False
    RGButtons[0], RGButtons[1], RGButtons[2] = 0, 0, 0  # так надо.
    FPS = 60
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = True
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                right = False
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                left = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                up = True
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                up = False

        screen.fill((255, 255, 255))
        blawhi_player.update(left, right, up, platforms, RGB, RGB_coords)
        for my_platform in platforms:
            screen.blit(my_platform.image, my_platform.rect)
        screen.blit(blawhi_player.image, blawhi_player.rect)
        all_sprites.draw(screen)
        platforms.draw(screen)

        RGB = pygame.sprite.Group()
        for i in range(3):
            FlagButtons(i)
            if RGButtons[i] == 0:
                Buttons(RGB, num=i, location=RGB_coords[i])
        flagRGB.draw(screen)
        RGB.draw(screen)
        if blawhi_player.all_buttons_collected:
            running = False

        pygame.display.flip()
        clock.tick(FPS)


def win_bild(i):
    # показывается картинка с поздравлением и позможностью
    # перехода либо в меню либо на след уровень
    pass


def main():
    pygame.init()
    size = width, height = 800, 600
    LEVELS = 2
    screen = pygame.display.set_mode(size)
    platform_coords, RGB_coords = levels_init(LEVELS)

    for i in range(LEVELS):
        RGB = pygame.sprite.Group()
        level(screen, platform_coords[i], RGB_coords[i], RGB)
        win_bild(i)

    pygame.quit()


if __name__ == '__main__':
    main()
