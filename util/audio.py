import pygame as pg
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pg.mixer.init()

# PLAYER
eat = pg.mixer.Sound('../assets/audio/chomp.wav')
eat.set_volume(0.25)

laser_sound = pg.mixer.Sound('../assets/audio/(defaultweapon).ogg')
laser_sound.set_volume(0.25)

ship_explode = pg.mixer.Sound('../assets/audio/explosion.ogg')
ship_explode.set_volume(0.25)

# CHICKEN

egg_drop = pg.mixer.Sound('../assets/audio/(eggdrop).ogg')
egg_drop.set_volume(0.25)

chicken_hurt = pg.mixer.Sound('../assets/audio/chickenhurt.wav')

chicken_die = pg.mixer.Sound('../assets/audio/chickendie.ogg')
chicken_die.set_volume(0.25)

boss_shoot = pg.mixer.Sound('../assets/audio/bossShoots.ogg')

breathe = pg.mixer.Sound('../assets/audio/henperorBreathe.ogg')

# UI

game_start = pg.mixer.Sound('../assets/audio/startgame.wav')
game_start.set_volume(0.80)



