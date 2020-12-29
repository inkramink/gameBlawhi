import os
import sys
import pygame

FPS = 60

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    from class_blawhi import Blawhi
    blawhi_player = Blawhi(all_sprites)
    # from class_walls import Border
    # Border(0, 0, width, 0)
    # Border(0, height, width, height)
    # Border(0, 0, 0, height)
    # Border(width, 0, width, height)
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
        blawhi_player.update(left, right, up)
        screen.blit(blawhi_player.image, blawhi_player.rect)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()

