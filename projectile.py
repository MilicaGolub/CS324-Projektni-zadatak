import pygame as pg
from util import constants as cons


class Projectile(pg.sprite.Sprite):
    def __init__(self, pos, img, velocity, damage):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(center=pos)
        self.velocity = velocity
        self.dmg = damage

    # Method for destroying laser off-screen
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= cons.HEIGHT + 60:
            self.kill()

    def update(self):
        self.rect.y += self.velocity
        self.destroy()
