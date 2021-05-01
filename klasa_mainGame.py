from klasa_bird import BIRD
from klasa_wall import WALL
from menu import MainMenu
from menu import ControlMenu
import pygame
import sys


class MAIN_GAME():
    pygame.mixer.pre_init(44120, -16, 2, 512)
    pygame.init()

    def __init__(self):
        self.new_game()
        self.screen = pygame.display.set_mode((600, 800))
        self.game_font = pygame.font.Font(None, 25)
        self.clock = pygame.time.Clock()
        # ----do MAIN menu
        self.play_sound = True
        self.font_name = 'NewTegomin-Regular.ttf'
        self.display = pygame.Surface((600, 800))
        self.running = True  # dzialanie programu
        self.playing = False  # granie
        # do poruszania sie w menu
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.main_menu = MainMenu(self)
        self.controls_menu = ControlMenu(self)
        self.current_menu = self.main_menu  # aktualnie wybrane menu

    def auto_draw_walls(self, x):
        wall = x
        # ---------------grafiki do scian---------------
        self.screen.blit(wall.wall_graph, wall.wall_down_rect)
        self.screen.blit(wall.wall_graph2,  # gorna sciana musi byc docieta
                         (wall.movement, 0 - (800-wall.height_up)))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_display = False
                # do testowania
                pygame.QUIT()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    self.bird.jump_bird()
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.current_menu = self.main_menu
                    self.current_menu.run_display = True
                    self.BACK_KEY = True
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

    def check_colision(self):
        # sprawdza czy ptak nie wylecial za ekran
        if self.bird.y-30 <= 0 or self.bird.y + 30 >= 800:
            if self.play_sound == True:
                self.game_over_sound.play()
            self.new_game()
            # self.game_over
        # sprawdza kolizje ze scianami
        self.check_points(self.wall)
        self.check_points(self.wall2)

    def check_points(self, x):
        wall = x
        if wall.movement <= self.bird.x + 30 and wall.movement + wall.width >= self.bird.x - 30:
            if self.bird.y - 30 <= wall.height_up or self.bird.y + 30 >= 800 - wall.height_down:
                if self.play_sound == True:
                    self.game_over_sound.play()
                self.new_game()
                # self.game_over
            elif self.bird.x - 30 >= wall.movement + wall.width:
                if self.play_sound == True:
                    self.sound.play()
            else:
                self.points += 1

    def create_elements(self):
        self.bird.create_bird()
        self.wall.create_walls()
        self.wall2.create_walls()
        self.create_score()

    def create_score(self):
        # tworzy napis do wyniku
        self.score_text = str('Points: ' + str(int(self.points/25)))
        # w render podaje sie co ma byc wyswietlone, kolor i AA
        self.score_surface = self.game_font.render(
            self.score_text, True, (0, 0, 0))
        self.score_x = int(100)
        self.score_y = int(750)
        # -------tlo dla wyniku,ramka i sam wynik
        self.score_rect = self.score_surface.get_rect(
            center=(self.score_x, self.score_y))  # kwadrat kordynatow tekstu
        self.background_rect = pygame.Rect(  # kwadrat kordynatow tła
            self.score_rect.left-5, self.score_rect.top-5, self.score_rect.width + 10, self.score_rect.height+10)  # tlo

    def draw_elements(self):
        self.screen.blit(self.bg, (0, 0))  # rysuje tlo
        self.screen.blit(self.bird.bird, self.bird.bird_rect)  # rysuje ptaka
        self.auto_draw_walls(self.wall)  # sciana 600
        self.auto_draw_walls(self.wall2)  # sciana 940
        pygame.draw.rect(self.screen, (255, 255, 255),
                         self.background_rect)  # tlo za wynikiem
        pygame.draw.rect(self.screen, (255, 0, 0),
                         self.background_rect, 2)  # ramka
        self.screen.blit(self.score_surface, self.score_rect)  # wynik

    def draw_text(self, text, size, x, y, kolor, typ):  # funkcja do menu - napisow
        font = pygame.font.Font(self.font_name, size)
        color = kolor
        if color == 'white':
            color = (255, 255, 255)
        elif color == 'red':
            color = (255, 0, 0)
        elif color == 'green':
            color = (0, 255, 0)
        text_surface = font.render(text, True, kolor)
        text_rect = text_surface.get_rect()
        if typ == 'center':
            text_rect.center = (x, y)
        elif typ == 'left':
            text_rect.topleft = (x, y)
        self.display.blit(text_surface, text_rect)

    def game_over(self):  # ----------do napisania od 0 bo tu kurwa nic nie działa
        self.playing = False
        # self.draw_elements()
        # for event in pygame.event.get():
        #    if event.type == pygame.KEYDOWN:
        #        self.playing = True

    def move_elements(self):
        self.bird.fall_bird()
        if(self.wall.movement <= 0 - self.wall.width):
            self.wall.new_wall(600)
        else:
            self.wall.movement -= 4
        if(self.wall2.movement <= 0 - self.wall2.width):
            self.wall2.new_wall(600)
        else:
            self.wall2.movement -= 4

    def main_loop(self):
        while self.playing:
            self.check_events()
            self.create_elements()
            self.move_elements()
            self.draw_elements()
            self.check_colision()
            self.reset_keys()
            pygame.display.update()
            self.clock.tick(60)

    def new_game(self):
        self.game_over()
        self.bird = BIRD()
        self.wall = WALL(600)
        self.wall2 = WALL(940)  # 940 zeby byly rowne odstepy
        self.bg = pygame.image.load('grafika/bg3.png')
        self.points = 0
        self.sound = pygame.mixer.Sound('dzwiek/dzwiek.wav')
        self.game_over_sound = pygame.mixer.Sound('dzwiek/GO.wav')

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
