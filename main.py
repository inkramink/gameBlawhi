import os
import sys
import pygame

size = 800, 600


def terminate():
    pygame.quit()
    sys.exit()


def start_end_screen(intro_text, button_text):
    FPS = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    from class_blawhi import load_image
    fon = load_image('background.png')
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('serif', 40)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, 1, (70, 70, 70))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = screen.get_width() / 2 - string_rendered.get_width() / 2
        text_coord += 50
        screen.blit(string_rendered, intro_rect)
    start_btn = font.render(button_text, 1, (70, 70, 70))
    start_rect = start_btn.get_rect()
    start_rect.top = 500
    start_rect.x = screen.get_width() / 2 - start_btn.get_width() / 2
    screen.blit(start_btn, start_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.left <= event.pos[0] <= start_rect.right \
                        and start_rect.top <= event.pos[1] <= start_rect.bottom:
                    return
        pygame.display.flip()
        clock.tick(FPS)


def levels_init(LEVELS):
    platform_hor_coords = [[], [(450, 430)], [(300, 200), (500, 200)], ]
    platform_ver_coords = [[], [(150, 300)], [(400, 410), (950, 300)], ]
    platform_coords = [
        [(250, 540), (400, 470), (560, 360), (370, 300), (680, 390)],
        [(50, 560), (160, 500), (280, 430), (740, 430), (330, 380), (300, 200)],
        [(250, 500), (1300, 410), (750, 300), (200, 300), (1100, 150)],
    ]
    RGB_coords = [
        [button(platform_coords[0], 2), button(platform_coords[0], 3), button(platform_coords[0], 4)],
        [button(platform_coords[1], 3), button(platform_coords[1], 4), button(platform_coords[1], 5)],
        [button(platform_coords[2], 2), button(platform_coords[2], 3), button(platform_coords[2], 1)],
    ]

    level_borders = [size[0] * 2] * LEVELS
    botom_platforms = [[(i, 595) for i in range(0, level_borders[j], 60)] for j in range(LEVELS)]
    for i in range(len(platform_coords)):  # во всех уровнях пол выложен платформами
        for platform in botom_platforms[i]:
            platform_coords[i].append(platform)

    return platform_coords[:LEVELS], RGB_coords[:LEVELS], platform_hor_coords, \
           platform_ver_coords, level_borders


def button(platform_coords, platform):
    # рассчитывает положение кнопки относительно платформы
    return platform_coords[platform][0] + 20, platform_coords[platform][1] - 20


def level(screen, platform_coords, RGB_coords, platform_hor_coords,
          platform_ver_coords, level_borders):
    from class_blawhi import load_image
    bg_image = load_image('background.png')
    background = pygame.Surface(screen.get_size())
    background.blit(bg_image, (0, 0))
    all_sprites = pygame.sprite.Group()
    from class_buttonsForBlawhi import FlagButtons, flagRGB, Buttons, RGButtons

    RGB = pygame.sprite.Group()
    RGB_list = []
    for i in range(3):
        FlagButtons(i)
        RGB_list.append(Buttons(RGB, num=i, location=RGB_coords[i]))

    from class_blawhi import Blawhi

    blawhi_player = Blawhi(all_sprites)
    platforms = pygame.sprite.Group()
    platforms_hor = pygame.sprite.Group()
    platforms_ver = pygame.sprite.Group()
    from class_platform import Platform, PlatformHor, PlatformVer

    for i in platform_coords:
        Platform(platforms, location=i)
    for i in platform_hor_coords:
        PlatformHor(platforms_hor, location=i)
    for i in platform_ver_coords:
        PlatformVer(platforms_ver, location=i)

    all_sprites.add(*platforms.sprites())
    all_sprites.add(*platforms_hor.sprites())
    all_sprites.add(*platforms_ver.sprites())
    all_sprites.add(*RGB.sprites())

    running = True
    left, right, up = False, False, False
    RGButtons[0], RGButtons[1], RGButtons[2] = 0, 0, 0  # так надо.
    FPS = 60
    clock = pygame.time.Clock()

    from class_camera import Camera
    camera = Camera(level_borders)
    count = 0

    from class_particle import Particle, particles

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
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

        copy = RGButtons[::]

        screen.blit(background, (0, 0))
        blawhi_player.update(left, right, up, platforms, RGB_list, RGB_coords, platforms_hor, platforms_ver, camera,
                             all_sprites)

        # if RGButtons != copy:
        for i in range(3):
            if RGButtons[i] != copy[i]:
                what = i
                Particle.create_particles((790, 20 * what - 10))
        if sum(RGButtons) != 0:
            particles.draw(screen)
            particles.update()
        platforms_hor.update()
        platforms_ver.update()

        flagRGB.empty()
        for i in range(3):
            FlagButtons(i)

        RGB.update(RGButtons, all_sprites)
        flagRGB.draw(screen)

        all_sprites.draw(screen)
        if blawhi_player.all_buttons_collected:
            count += 1
            if count == 20:
                running = False
        pygame.display.flip()
        clock.tick(FPS)


def win_bild(screen, i):
    text1 = 'Уровень ' + str(i + 1) + ' пройден'
    text2 = 'Нажмите ENTER, чтобы продолжить'
    ft1_font = pygame.font.SysFont('serif', 60)
    ft1_surf = ft1_font.render(text1, True, (70, 70, 70))
    ft2_font = pygame.font.SysFont('serif', 40)
    ft2_surf = ft2_font.render(text2, True, (70, 70, 70))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False

        screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])
        screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 170])
        pygame.display.flip()


def main():
    pygame.init()
    LEVELS = 3
    screen = pygame.display.set_mode(size)
    platform_coords, RGB_coords, platform_hor_coords, \
    platform_ver_coords, level_borders = levels_init(LEVELS)
    start_game_text = ['ДОБРО ПОЖАЛОВАТЬ В ИГРУ BLAWHI!',
                       'Нажмите СТАРТ, чтобы начать']
    while True:
        start_end_screen(start_game_text, 'СТАРТ')
        for i in range(LEVELS):
            level(screen, platform_coords[i], RGB_coords[i],
                  platform_hor_coords[i], platform_ver_coords[i],
                  level_borders[i])
            win_bild(screen, i)
        end_game_text = ['Поздравляем! Вы прошли игру!']
        start_end_screen(end_game_text, 'ВЕРНУТЬСЯ')


if __name__ == '__main__':
    main()
