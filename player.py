import os

import pygame as pg

from projectile import Projectile
from util import audio, image as img
from util import constants as cons

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.transform.scale(img.spaceship, (cons.SPACESHIP_WIDTH, cons.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom=pos)
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 300
        self.lasers = pg.sprite.Group()
        self.laser_sound = audio.laser_sound
        self.was_hit = False
        self.death_current = 0
        self.death_img_list = img.death_sprite[self.death_current].convert_alpha()
        self.hit_countdown = 0
        self.rocket = Rocket(pos)

    # Method for handling player movement
    def get_input(self):
        keys_pressed = pg.key.get_pressed()

        if keys_pressed[pg.K_a] and self.rect.x - cons.VEL > 0:  # LEFT
            self.rect.x -= cons.VEL
            self.image = pg.transform.scale(img.moving_spaceship, (
                cons.SPACESHIP_WIDTH, cons.SPACESHIP_HEIGHT))
        else:
            self.image = pg.transform.scale(img.spaceship, (cons.SPACESHIP_WIDTH, cons.SPACESHIP_HEIGHT))

        if keys_pressed[pg.K_d] and self.rect.x + cons.VEL + self.rect.width < cons.WIDTH:  # RIGHT
            self.rect.x += cons.VEL
            self.image = pg.transform.scale(pg.transform.flip(img.moving_spaceship, True, False), (
                cons.SPACESHIP_WIDTH, cons.SPACESHIP_HEIGHT))

        if keys_pressed[pg.K_w] and self.rect.y + cons.VEL > 0:  # UP
            self.rect.y -= cons.VEL

        if keys_pressed[pg.K_s] and self.rect.y + cons.VEL + self.rect.height < cons.HEIGHT:  # DOWN
            self.rect.y += cons.VEL

        if keys_pressed[pg.K_SPACE] and self.ready:  # SHOOT
            self.shoot_laser()
            self.ready = False
            self.laser_time = pg.time.get_ticks()
            self.laser_sound.play()

    # Method for setting laser cooldown to 0.3 seconds
    def recharge(self):
        if not self.ready:
            current_time = pg.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True
                self.rect.y -= cons.VEL

    def shoot_laser(self):
        self.lasers.add(
            Projectile(self.rect.midtop, velocity=cons.LASER_VEL, img=img.laser_bullet.convert_alpha(), damage=15))
        self.rect.y += cons.VEL

    def update(self, screen):
        self.recharge()
        self.lasers.update()
        if self.was_hit:
            self.rocket.kill()
            audio.ship_explode.play()
            if self.death_current == 30:
                self.__init__((cons.WIDTH / 2, cons.HEIGHT - 100), screen)
                self.was_hit = False
            self.death_current += 0.25
            self.image = pg.transform.scale(img.death_sprite[int(self.death_current)].convert_alpha(), (100, 85))
        else:
            self.get_input()
            self.rocket.draw(self, screen)
            self.rocket.update()


# Class for adding engine trail to spaceship
class Rocket(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.sprites = img.flying_sprite
        self.current_image = 0
        self.rocket_image = self.sprites[self.current_image]
        self.rect = self.rocket_image.get_rect(center=pos)

    def update(self):
        self.current_image += 0.25

        if self.current_image >= len(self.sprites) - 1:
            self.current_image = 0

        self.rocket_image = self.sprites[int(self.current_image)]

    def draw(self, ship, screen):
        keys_pressed = pg.key.get_pressed()

        if keys_pressed[pg.K_a] and self.rect.x - cons.VEL > 0:
            screen.blit(self.rocket_image,
                        [ship.rect.x + (cons.SPACESHIP_WIDTH - self.rocket_image.get_width()) // 2 + 6,
                         ship.rect.y + cons.SPACESHIP_HEIGHT - 18])
        if keys_pressed[pg.K_d] and self.rect.x + cons.VEL + self.rect.width < cons.WIDTH:
            screen.blit(self.rocket_image,
                        [ship.rect.x + (cons.SPACESHIP_WIDTH - self.rocket_image.get_width()) // 2 - 6,
                         ship.rect.y + cons.SPACESHIP_HEIGHT - 18])
        else:
            screen.blit(self.rocket_image, [ship.rect.x + (cons.SPACESHIP_WIDTH - self.rocket_image.get_width()) // 2,
                                            ship.rect.y + cons.SPACESHIP_HEIGHT - 18])
