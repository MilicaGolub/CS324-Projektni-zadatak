import csv

import pygame as pg

import ui as btn
from util import constants as cons

pg.init()

font = pg.font.Font('../assets/ui/thundernova.ttf', 50)
font_title = pg.font.Font('../assets/ui/thundernova.ttf', 125)

scoreboard = []


# Function for drawing scoreboard UI
def render_scores(screen):
    global scoreboard
    scoreboard = load_scores()

    y_offset = cons.HEIGHT / 2 - 400
    text = font_title.render(f'HALL OF FAME', True, 'white')
    screen.blit(text, ((cons.WIDTH / 2) - text.get_width() / 2, y_offset))
    y_offset += 75

    for item in scoreboard:
        y_offset += 100
        text = font.render(f'{item[0]}...........................{item[1]}\n', True, 'white')
        screen.blit(text, ((cons.WIDTH / 2) - text.get_width() / 2, y_offset))

    back = btn.create_back_to_menu_btn()
    back.draw(screen)

    if back.check_clicked():
        return True


def save_scores(scores):
    with open("scores.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score"])
        for score in scores:
            writer.writerow(score)


def load_scores():
    scores = []
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            scores.append(row)
    return scores


def check_new_score(new_score):
    global scoreboard
    scoreboard.append(new_score)
    scoreboard.sort(key=lambda x: int(x[1]), reverse=True)
    scores = scoreboard[:5]
    save_scores(scores)

