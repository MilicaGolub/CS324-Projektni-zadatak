import pygame as pg

import scoreboard
from util import func, image as img, constants as cons


pg.init()

COLOR_INACTIVE = pg.Color('white')
COLOR_ACTIVE = pg.Color('dodgerblue2')
font = pg.font.Font('../assets/ui/thundernova.ttf', 50)


class Button:

    def __init__(self, x, y, scale, text):
        image = img.btn_img
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image.convert_alpha(), (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.text = text
        self.font = font
        self.text_surface = self.font.render(self.text, True, 'white').convert_alpha()
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    # Method for checking button was clicked
    def check_clicked(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0]:
                return True
            else:
                return False


class InputBox:

    def __init__(self, w, h, text=''):
        self.rect = pg.Rect((cons.WIDTH / 2 - w / 2, cons.HEIGHT / 2 - 275, w, h))
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    # Method for receiving input when entering player's name
    def handle_event(self, event, score):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    scoreboard.scoreboard = scoreboard.load_scores()
                    scoreboard.check_new_score([self.text, score])
                    self.text = ''
                    return True
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 2)


# Functions for creating menu buttons
def create_play_btn():
    return Button(func.get_hcenter_btn(img.btn_img), 500, 0.45, "PLAY")


def create_scoreboard_btn():
    return Button(func.get_hcenter_btn(img.btn_img), 650, 0.45, "SCOREBOARD")


def create_exit_btn():
    return Button(func.get_hcenter_btn(img.btn_img), 800, 0.45, "EXIT")


def create_back_to_menu_btn():
    return Button(func.get_hcenter_btn(img.btn_img), 900, 0.40, "BACK")


# Function for drawing main menu in game  loop
def draw_menu(screen):
    command = -1
    screen.blit(img.title_img.convert_alpha(), ((cons.WIDTH / 2) - img.title_img.get_width() / 2, 55))

    play = create_play_btn()
    play.draw(screen)

    score = create_scoreboard_btn()
    score.draw(screen)

    exit = create_exit_btn()
    exit.draw(screen)

    if play.check_clicked():
        command = 0
    if score.check_clicked():
        command = 1
    if exit.check_clicked():
        command = 2
    return command



