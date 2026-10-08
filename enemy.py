import random

import pygame as pg
import random as rnd
from util import audio, image as img, constants as cons
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Chicken(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.current_sprite = rnd.randint(0, 21)
        self.image = img.chicken_sprite[self.current_sprite].convert()
        self.rect = pg.Rect((x, y), (120, 110))
        self.hp = 27
        self.was_hit = False
        self.current_death = 0

    def update(self, direction, screen, wave):
        self.current_sprite += 0.25
        if self.current_sprite >= len(img.chicken_sprite):
            self.current_sprite = 0
        self.image = pg.transform.scale(img.chicken_sprite[int(self.current_sprite)].convert_alpha(), (122, 117))
        self.rect.x += direction
        if self.was_hit:
            self.current_death += 0.25
            if self.current_death == 8:
                self.kill()
            self.image = img.death_img[int(self.current_death)].convert_alpha()


class Feather(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.sprite_list = img.feather_list
        self.current_image = 0
        self.image = self.sprite_list[self.current_image]
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.current_image += 0.20
        self.rect.y += 3
        if self.current_image >= 15:
            self.kill()
        self.image = self.sprite_list[int(self.current_image)].convert_alpha()


class Drumstick(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = (pg.image.load('assets/chicken/meat.png').convert_alpha())
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.velocity = 0
        self.image_copy = self.image
        self.angle = 0
        self.direction = -1
        self.rect.x = pos_x
        self.acceleration = 0.09

    def move(self):
        # If drumstick hits the ground it will change its direction
        if self.direction == -1 and self.rect.y > cons.HEIGHT:
            self.velocity *= -1
            # Limiting velocity
            if self.velocity > 2:
                self.velocity = 2

        # Adding acceleration to velocity and updating the y-coordinate with current velocity
        self.velocity += self.acceleration
        self.rect.y += self.velocity + 3

        # if velocity is lesser than 0, change drumstick's direction
        if self.velocity < 0:
            self.direction = 1
        else:
            self.direction = -1

    def update(self):
        self.rect.x -= random.choice((0.3, -0.3))
        self.move()
        self.angle += -3
        self.rotate(self.angle)

    def rotate(self, angle):
        img_center = self.rect.center
        self.image = pg.transform.rotate(self.image_copy, angle)
        self.rect = self.image.get_rect(center=img_center)


class Boss(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.current_sprite = rnd.randint(0, 13)
        self.image = pg.transform.scale(img.darth_img[self.current_sprite].convert(), (430, 409))
        self.rect = self.image.get_rect(center=(x, y))
        self.hp = 250
        self.was_hit = False
        self.current_death = 0
        self.die_sound = pg.mixer.Sound('assets/audio/(bossexplosion).ogg')
        self.die_sound.set_volume(0.60)
        pg.mixer.music.load('assets/audio/henperorBreathe.ogg')
        pg.mixer.music.play(-1)

    def update(self, direction, screen, wave):
        self.current_sprite += 0.15
        if self.current_sprite >= len(img.darth_img) - 1:
            self.current_sprite = 0
        self.image = pg.transform.scale(img.darth_img[int(self.current_sprite)].convert_alpha(), (430, 409))

        if self.was_hit:
            pg.mixer.music.stop()
            self.die_sound.play()
            self.current_death += 0.5
            if self.current_death >= 45:
                self.kill()
            self.image = img.darth_explode[int(self.current_death)].convert_alpha()
        else:
            self.rect.x += direction
