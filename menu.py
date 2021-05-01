import pygame
import time
import sys


class Menu():
    def __init__(self, klasa_mainGame):
        self.game = klasa_mainGame  # dostep do klasy MAIN
        self.mid_w = 300  # polowa szerokosci
        self.mid_h = 400  # polowa wysokosci
        self.run_display = True  # czy ma pokazywac menu
        # self.run_Controldisplay = False  # czy ma pokazywac menu Poruszania sie
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)  # tworzy kwadrat kursora
        self.offset = -100  # do wyswietlania kursora

    def draw_cursor(self):
        self.game.draw_text('*', 20, self.cursor_rect.x,
                            self.cursor_rect.y, 'white', 'center')  # tworzy kursor

    def screen_blit(self):
        # wyswietla ekran menu
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, klasa_mainGame):
        Menu.__init__(self, klasa_mainGame)
        self.state = 'Play'  # aktualnie wybrana pozycja w menu
        # kordynaty do napisow oraz umiejscowanie kursora po lewej od tekstu
        self.startx, self.starty = self.mid_w, self.mid_h
        self.mutex, self.mutey = self.mid_w, self.mid_h + 50
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 100
        self.quitx, self.quity = self.mid_w, self.mid_h + 150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()  # sprawdza ktora opcja zostala wybrana
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Main menu', 50, 300, 280, 'white', 'center')
            self.game.draw_text('Play', 30, self.startx,
                                self.starty, 'white', 'center')
            if self.game.play_sound == True:
                self.game.draw_text('Sound: ON', 30, self.mutex,
                                    self.mutey, 'green', 'center')
            else:
                self.game.draw_text('Sound: OFF', 30, self.mutex,
                                    self.mutey, 'red', 'center')
            self.game.draw_text('Controls', 30, self.controlsx,
                                self.controlsy, 'white', 'center')
            self.game.draw_text('Quit', 30, self.quitx,
                                self.quity, 'white', 'center')
            self.draw_cursor()
            self.screen_blit()

    def move_cursor(self):
        if self.game.DOWN_KEY:  # w dol przechodzi na opcje nizej
            if self.state == 'Play':
                self.cursor_rect.midtop = (
                    self.mutex + self.offset, self.mutey)
                self.state = 'Sound'
            elif self.state == 'Sound':
                self.cursor_rect.midtop = (
                    self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (
                    self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Play'
        if self.game.UP_KEY:  # w gore przechodzi na x[-1]
            if self.state == 'Play':
                self.cursor_rect.midtop = (
                    self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Sound':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Play'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (
                    self.mutex + self.offset, self.mutey)
                self.state = 'Sound'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (
                    self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'

    def check_input(self):
        self.move_cursor()  # ruszanie kursorem
        if self.game.START_KEY:
            if self.state == "Play":
                self.run_display = False
                self.game.playing = True
            elif self.state == "Sound":
                if self.game.play_sound == True:
                    self.game.play_sound = False
                elif self.game.play_sound == False:
                    self.game.sound.play()
                    self.game.play_sound = True
            elif self.state == "Controls":
                self.game.current_menu = self.game.controls_menu
            elif self.state == "Quit":
                pygame.QUIT()
                sys.exit()
        self.run_display = False


class ControlMenu(Menu):
    def __init__(self, klasa_mainGame):
        Menu.__init__(self, klasa_mainGame)
        # ---------800/5 = 160
        self.enterx, self.entery = self.mid_w-100, 80
        self.escx, self.escy = self.mid_w-100, 120
        self.arrowx, self.arrowy = self.mid_w-100, 160
        self.spacex, self.spacey = self.mid_w-100, 350
        self.esc2x, self.esc2y = self.mid_w-100, 390
        # ====================================currentmenu musi sie zmieniac przy zmianie menu==============================================

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False
            # self.check_input()  # sprawdza ktora opcja zostala wybrana
            self.game.display.fill((0, 0, 0))
            # --------------------------menu
            self.game.draw_text('To navigate in Menu', 50,
                                300, 30, 'white', 'center')
            self.game.draw_text('ENTER/RETURN', 20, self.enterx-100,
                                self.entery, 'white', 'left')
            self.game.draw_text('to choose an option', 20, self.enterx + 100,
                                self.entery, 'white', 'left')
            self.game.draw_text('ESCAPE', 20, self.escx-100,
                                self.escy, 'white', 'left')
            self.game.draw_text('to go back', 20, self.escx + 100,
                                self.escy, 'white', 'left')
            self.game.draw_text('ARROW UP/DOWN', 20, self.arrowx-100,
                                self.arrowy, 'white', 'left')
            self.game.draw_text('to go up or down in menu', 20, self.arrowx + 100,
                                self.arrowy, 'white', 'left')
            # ------------------------------granie
            self.game.draw_text('To play the game', 50,
                                300, 300, 'white', 'center')
            self.game.draw_text('SPACE/ARROW UP', 20, self.spacex-100,
                                self.spacey, 'white', 'left')
            self.game.draw_text('to fly a bird', 20, self.spacex + 100,
                                self.spacey, 'white', 'left')
            self.game.draw_text('ESCAPE', 20, self.esc2x-100,
                                self.esc2y, 'white', 'left')
            self.game.draw_text('to open menu', 20, self.esc2x + 100,
                                self.esc2y, 'white', 'left')
            self.screen_blit()
