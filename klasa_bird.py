import pygame


class BIRD():
    def __init__(self):
        self.width = 60  # obrazek ptaka ma 60x60
        self.height = 60
        self.x = 150
        self.y = 400
        self.gravity = 0.25  # zwieksza predkosc spadania ptaka w dol
        self.bird_movement = 0
        self.go_var = 5
        self.jump = 12

    def create_bird(self):
        self.bird = pygame.image.load(
            'grafika/ptak_outline.png')  # wczytuje grafike
        # tworzy kwadrat koordynatowy ptaka i daje go na srodek
        self.bird_rect = self.bird.get_rect(center=(self.x, self.y))

    def jump_bird(self):
        self.bird_movement = 0  # zeruje wektor w dol
        self.bird_movement -= self.jump

    def fall_bird(self):
        self.bird_movement += self.gravity  # przyspiesza spadanie
        self.y += self.bird_movement + self.go_var
