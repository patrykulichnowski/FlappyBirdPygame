import pygame
import random


class WALL():
    def __init__(self, x):
        self.new_wall(x)  # x przyjmuje gdzie generowac sciane

    def create_walls(self):
        # =============gorna===========
        # plaszczyzna gornej sciany
        self.wall_up = pygame.Surface((self.width, self.height_up))
        self.wall_up_rect = self.wall_up.get_rect(  # kwadrat kordynatow gornej sciany
            topleft=(self.movement, 0))
        # ============dolna==========
        # plaszczyzna dolnej sciany
        self.wall_down = pygame.Surface((self.width, self.height_down))
        self.wall_down_rect = self.wall_down.get_rect(  # kwadrat kordynatow dolnej sciany
            topleft=(self.movement, 800 - self.height_down))

    def new_wall(self, x):
        self.height_up = random.randint(100, 530)  # wysokosc gornej sciany
        self.width = 40  # szerokosc obu scian
        # wysokosc dolnej 170 zeby ptak przelecial
        self.height_down = 800 - self.height_up - 170
        self.movement = x   # przesuwanie scian w prawo
        # grafiki do scian
        self.wall_graph = pygame.image.load('grafika/pipe.png')
        self.wall_graph2 = pygame.image.load('grafika/pipe.png')
