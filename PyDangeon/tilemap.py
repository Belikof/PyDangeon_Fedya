import pygame
from settings import *

# Эти числа — "тип" каждой клетки на карте
# Мы используем числа, потому что компьютеру легче сравнивать числа чем текст
TILE_WALL  = 0   # стена
TILE_FLOOR = 3   # пол

# Карта нашего подземелья — список строк
# '#' = стена, '.' = пол
# Это удобно читать глазами — сразу видно как выглядит уровень!
MAP_DATA = [
    "####################",
    "#..................#",
    "#..................#",
    "#.....##...........#",
    "#..................#",
    "#..................#",
    "#..######..........#",
    "#.........##.......#",
    "#..................#",
    "....................",
    "#...........######.#",
    "#..................#",
    "#..................#",
    "#....#######.......#",
    "#...................",
    "#..................#",
    "#.......####.......#",
    "#..................#",
    "#..................#",
    "####################",
]

class TileMap:
    def __init__(self):
        # Превращаем строки с '#' и '.' в числа (0 и 3)
        # Так потом проще проверять — стена это или пол
        self.tiles = []
        for row in MAP_DATA:
            tile_row = []
            for char in row:
                if char == '#':
                    tile_row.append(TILE_WALL)
                else:
                    tile_row.append(TILE_FLOOR)
            self.tiles.append(tile_row)

    def is_wall(self, x, y):
        # Проверяем: является ли клетка (x, y) стеной?
        # Это нужно чтобы игрок не мог пройти сквозь стену
        return self.tiles[y][x] == TILE_WALL

    def draw(self, screen, player):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                tile = self.tiles[y][x]

                px = x * TILE_SIZE
                py = y * TILE_SIZE

                if tile == TILE_WALL:
                    color = GREY
                else:
                    color = BROWN

                pygame.draw.rect(screen, color, (px, py, TILE_SIZE, TILE_SIZE))

                # Рисуем сетку — тёмная рамка вокруг каждой клетки
                # Это делает карту похожей на настоящий данжен!
                # pygame.draw.rect с последним аргументом 1 — рисует только контур
                pygame.draw.rect(screen, BLACK, (px, py, TILE_SIZE, TILE_SIZE), 1)
