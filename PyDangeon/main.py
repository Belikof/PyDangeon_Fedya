import pygame
from settings import *
from tilemap import *
from player import *

pygame.init()  # инициализация pygame

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))  # создаем окно
pygame.display.set_caption("PyDangeon")  # название окна

clock = pygame.time.Clock()  # контроль фпс

tilemap = TileMap()  # создание карты
player = Player(tilemap, start_x=1, start_y=1)  # создание игрока

running = True
# основной цикл игры
while running:
    clock.tick(FPS)  # ограничение фпс

    # обработка событий
    for event in pygame.event.get():

        # пользователь нажимает на крестик - цикл завершается
        if event.type == pygame.QUIT:
            running = False

        player.handle_event(event)

    # заливка экрана цветом
    screen.fill(DARK_GREY)

    # отрисовка карты
    tilemap.draw(screen, player)

    # отрисовка игрока
    player.draw(screen)

    # убираем мерцание
    pygame.display.flip()

pygame.quit()


