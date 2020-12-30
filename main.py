import os
import sys
import pygame

FPS = 60
platform_coords = [(50, 580), (150, 500), (0, 595), (50, 595)]
RGB_coords = [(300, 525), (400, 500), (500, 550)]
RGB = pygame.sprite.Group()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
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
        blawhi_player.update(left, right, up, platforms)
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
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
