import ctypes
import os
import sys
from random import choice

import pygame as pg

import scoreboard
import ui as btn
from enemy import Chicken, Drumstick, Feather, Boss
from player import Player
from projectile import Projectile
from util import audio, constants as cons, image as img

os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = 0
duration = 0
invincible_times = 0
counter = 0

# Disabling screen stretching
ctypes.windll.user32.SetProcessDPIAware()
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

# Initializing display and setting it full-screen
screen = pg.display.set_mode(true_res, pg.FULLSCREEN)

# Loading background image
bg_img = pg.image.load('assets/background/Galaxy-Background.png').convert()
bg_img = pg.transform.scale(bg_img, (cons.WIDTH, cons.HEIGHT))


# Class for updating game display (wave, player, lasers, etc...)
class Game:

    # Initial setup(drawing player, wave, setting score and lives system)
    def __init__(self):
        # Player setup
        player_sprite = Player((cons.WIDTH / 2, cons.HEIGHT - 100))
        self.player = pg.sprite.GroupSingle(player_sprite)
        self.has_played = False
        self.won = False
        self.text = ''
        self.invincible = 0

        # Health and scoring setup
        self.lives = 3
        self.live_surf = pg.transform.scale(pg.image.load('assets/small/heart-3.png').convert_alpha(), (50, 50))
        self.live_x = cons.WIDTH - (self.live_surf.get_width())
        self.score = 0
        self.font = pg.font.Font('assets/ui/thundernova.ttf', 30)

        # Chicken setup
        self.wave = 1
        global duration
        duration = pg.time.get_ticks() + 4500
        self.chicken = pg.sprite.Group()
        self.wave_setup(4, 7)
        self.chicken_direction = 1
        self.chicken_projectile = pg.sprite.Group()
        self.drumsticks = pg.sprite.Group()
        self.feathers = pg.sprite.Group()

    # Method for updating player, chicken, laser pos
    def run(self):
        # Play music when starting the game
        if not self.has_played:
            audio.game_start.play()
            self.has_played = True

        # Player
        self.player.draw(screen)
        self.player.update(screen)
        self.player.sprite.lasers.draw(screen)

        # Collision
        self.collision_check()

        # Chicken
        self.chicken_projectile.draw(screen)
        self.chicken_projectile.update()

        self.drumsticks.draw(screen)
        self.drumsticks.update()

        self.feathers.draw(screen)
        self.feathers.update()

        self.chicken.draw(screen)
        self.chicken.update(self.chicken_direction, screen, self.wave)

        # Wave
        self.chicken_position()
        self.check_waves()

        # Game UI
        self.display_lives()
        self.show_hint()
        self.display_score()
        self.display_message(self.text)

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x - (live * (self.live_surf.get_width()))
            screen.blit(self.live_surf, (x, 10))

    def display_score(self):
        score_surf = self.font.render(f'score: {self.score}', True, 'white')
        score_rect = score_surf.get_rect(topleft=(15, 20))
        screen.blit(score_surf, score_rect)

    def show_hint(self):
        hint_surf = self.font.render(f'Press esc to go back to main menu', True, 'white')
        hint_rect = hint_surf.get_rect(bottomleft=(15, cons.HEIGHT - 20))
        screen.blit(hint_surf, hint_rect)

    def chicken_shoot(self):
        if self.chicken.sprites():
            random_chicken = choice(self.chicken.sprites())
            if not self.player.sprite.was_hit and not self.wave == 4:
                laser_sprite = Projectile(pos=random_chicken.rect.center, velocity=2, img=img.egg_img, damage=15)
                self.chicken_projectile.add(laser_sprite)
                audio.egg_drop.play()

    def boss_shoot(self):
        if self.chicken.sprites():
            random_chicken = choice(self.chicken.sprites())
            laser_sprite = Projectile(pos=random_chicken.rect.center, velocity=3, img=img.boss_laser.convert_alpha(),
                                      damage=15)
            self.chicken_projectile.add(laser_sprite)
            audio.boss_shoot.play()

    def chicken_position(self):
        all_chicken = self.chicken.sprites()
        for chicken in all_chicken:
            if chicken.rect.right >= cons.WIDTH:
                self.chicken_direction = -1
            elif chicken.rect.left <= 0:
                self.chicken_direction = 1

    def wave_setup(self, rows, cols, x_distance=200, y_distance=120, x_offset=10, y_offset=50):
        if self.wave == 1:
            for row_index, row in enumerate(range(rows)):
                for col_index, col in enumerate(range(cols)):
                    x = col_index * x_distance + x_offset
                    y = row_index * y_distance + y_offset
                    chicken_sprite = Chicken(x + 1900, y)
                    self.chicken.add(chicken_sprite)
        if self.wave == 2:
            for row_index, row in enumerate(range(rows)):
                for col_index, col in enumerate(range(cols)):
                    if col_index % 2 == 0:
                        x = col_index * x_distance + x_offset
                        y = row_index * y_distance + y_offset
                        chicken_sprite = Chicken(x - 1500, y)
                        self.chicken.add(chicken_sprite)
        if self.wave == 3:
            for row_index, row in enumerate(range(rows)):
                for col_index, col in enumerate(range(cols)):
                    if not col_index == 3:
                        x = col_index * x_distance + x_offset
                        y = row_index * y_distance + y_offset
                        chicken_sprite = Chicken(x + 1900, y)
                        self.chicken.add(chicken_sprite)
        if self.wave == 4:
            self.chicken.add(Boss(2200, cons.HEIGHT / 2 - 250))
            if not self.chicken.sprites():
                self.won = True

    def check_waves(self):
        global duration
        if self.wave == 1 and not self.chicken.sprites():
            self.wave = 2
            duration = pg.time.get_ticks() + 4500
            self.wave_setup(4, 7)
        elif self.wave == 2 and not self.chicken.sprites():
            self.wave = 3
            duration = pg.time.get_ticks() + 4500
            self.wave_setup(4, 7)
        elif self.wave == 3 and not self.chicken.sprites():
            self.wave = 4
            duration = pg.time.get_ticks() + 4500
            self.wave_setup(1, 1)
        elif self.wave == 4 and not self.chicken.sprites():
            self.won = True

    def check_escape(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_ESCAPE]:
            return True

    def collision_check(self):
        global invincible_times

        # EGG HITS PLAYER
        if self.chicken_projectile and not self.player.sprite.was_hit:
            for laser in self.chicken_projectile:
                if pg.sprite.spritecollide(laser, self.player, False) and self.invincible == 0:
                    self.lives -= 1
                    self.player.sprite.was_hit = True
                    invincible_times = pg.time.get_ticks() + 5000
                    self.invincible = 1
                    laser.kill()
                    if self.lives == 0:
                        self.wave = 4
                        self.chicken.empty()

        # PLAYER HITS CHICKEN
        if self.player.sprite.lasers.sprites():
            for laser in self.player.sprite.lasers.sprites():
                got_hit = pg.sprite.spritecollideany(laser, self.chicken)
                if got_hit:
                    laser.kill()
                    self.score += 100
                    got_hit.hp -= laser.dmg
                    if got_hit.hp < 0:
                        audio.chicken_die.play()
                        got_hit.was_hit = True
                        self.score += 550
                        self.drumsticks.add(Drumstick(got_hit.rect[0], got_hit.rect[1]))
                    elif not self.wave == 4:
                        audio.chicken_hurt.play()
                        self.feathers.add(Feather((got_hit.rect[0], got_hit.rect[1])))

        # PLAYER EATS DRUMSTICK
        if self.drumsticks:
            for drumstick in self.drumsticks:
                if pg.sprite.spritecollide(drumstick, self.player, False):
                    drumstick.kill()
                    audio.eat.play()
                    self.score += 550

        # PLAYER RUNS INTO CHICKEN
        if self.chicken:
            for chicken in self.chicken:
                if pg.sprite.spritecollide(chicken, self.player, False):
                    self.lives -= 1
                    self.player.sprite.was_hit = True
                    if self.lives == 0:
                        self.wave = 4
                        self.chicken.empty()

    def display_message(self, text):
        if not self.chicken.sprites():
            font_victory = pg.font.Font('assets/ui/thundernova.ttf', 175)
            victory_surf = font_victory.render(text, True, 'white')
            victory_rect = victory_surf.get_rect(center=(cons.WIDTH / 2, cons.HEIGHT / 2))
            screen.blit(victory_surf, victory_rect)


def show_text(text):
    font = pg.font.Font('assets/ui/thundernova.ttf', 50)
    text_surface = font.render(text, True, 'white')
    text_rect = text_surface.get_rect(center=(cons.WIDTH / 2, cons.HEIGHT / 2 - 300))
    screen.blit(text_surface, text_rect)


def start_game():
    global duration
    game = Game()
    menu = True
    # Seamless background counter
    i = 0
    # Setting clock for frame
    clock = pg.time.Clock()

    ALIENLASER = pg.USEREVENT + 1
    pg.time.set_timer(ALIENLASER, 1200)

    BOSSLASER = pg.USEREVENT + 2
    pg.time.set_timer(BOSSLASER, 900)

    input_box = btn.InputBox(200, 70)

    # Game loop
    run = True
    while run:
        # Seamless background
        rel_i = i % bg_img.get_rect().height
        screen.blit(bg_img, (0, rel_i - bg_img.get_rect().height))
        if rel_i < cons.HEIGHT:
            screen.blit(bg_img, (0, rel_i))
        i += 1

        # Event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == ALIENLASER and not menu and menu_command == 0:
                game.chicken_shoot()
            if event.type == BOSSLASER and game.wave == 4:
                game.boss_shoot()
            if input_box.handle_event(event, game.score):
                menu = True
                menu_command = btn.draw_menu(screen)

        # Drawing menu and initializing new game instance
        if menu:
            game.__init__()
            input_box.__init__(200, 70)
            menu_command = btn.draw_menu(screen)
            if not menu_command == -1:
                menu = False
            if menu_command == 2:
                pg.quit()
                sys.exit()

        # Blinking spaceship to indicate player's invincibility
        if game.invincible == 1 and not game.player.sprite.was_hit:
            if pg.time.get_ticks() % 250 < 125:
                game.player.sprite.image.set_alpha(10)
                game.player.sprite.rocket.rocket_image.set_alpha(10)
            else:
                game.player.sprite.image.set_alpha(255)
                game.player.sprite.rocket.rocket_image.set_alpha(255)
        else:
            game.player.sprite.image.set_alpha(255)
            game.player.sprite.rocket.rocket_image.set_alpha(255)

        if not menu:
            # Displaying scored and drawing 'Go back' button
            if menu_command == 1:
                if scoreboard.render_scores(screen):
                    menu = True
                    menu_command = btn.draw_menu(screen)
            # Starting the game and checking if player has pressed esc to go back to menu
            if menu_command == 0:
                game.run()
                if game.check_escape():
                    menu = True
                    menu_command = btn.draw_menu(screen)
                # Displaying wave count
                if pg.time.get_ticks() < duration:
                    if not game.wave == 4:
                        show_text(f"Wave {game.wave}")
                    else:
                        show_text("Henperor's apprentice")
                # Checking if player was invincible for 4.5 seconds
                if pg.time.get_ticks() > invincible_times:
                    game.invincible = 0

            # Display message if player has won
            if game.won and game.lives != 0:
                input_box.draw(screen)
                show_text(f"Enter your name: ")
                input_box.update()
                game.display_message(text="You won!")
            # Display message if player lost the game
            elif game.lives == 0:
                input_box.draw(screen)
                show_text(f"Enter your name: ")
                input_box.update()
                game.display_message(text="You lost!")

        pg.display.update()
        clock.tick(cons.FPS)
    pg.quit()
