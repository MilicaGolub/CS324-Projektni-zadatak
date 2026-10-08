import pygame as pg
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# SHIP ASSETS
spaceship = pg.image.load('../assets/spaceship/ship.png')
moving_spaceship = pg.image.load("../assets/spaceship/lship.png")
flying_sprite = [
    pg.image.load('../assets/spaceship/rocket/1_1.png'),
    pg.image.load('../assets/spaceship/rocket/2_1.png'),
    pg.image.load('../assets/spaceship/rocket/3_1.png'),
    pg.image.load('../assets/spaceship/rocket/4_1.png'),
    pg.image.load('../assets/spaceship/rocket/5_1.png'),
    pg.image.load('../assets/spaceship/rocket/6_1.png'),
    pg.image.load('../assets/spaceship/rocket/7_1.png'),
    pg.image.load('../assets/spaceship/rocket/8_1.png'),
    pg.image.load('../assets/spaceship/rocket/9_1.png'),
    pg.image.load('../assets/spaceship/rocket/10_1.png'),
    pg.image.load('../assets/spaceship/rocket/11_1.png'),
    pg.image.load('../assets/spaceship/rocket/12_1.png')
]
laser_bullet = pg.transform.scale(pg.image.load("../assets/spaceship/green_strong.png"), (25, 100))
death_sprite = [
    pg.image.load('../assets/spaceship/death/1.png'),
    pg.image.load('../assets/spaceship/death/2.png'),
    pg.image.load('../assets/spaceship/death/3.png'),
    pg.image.load('../assets/spaceship/death/4.png'),
    pg.image.load('../assets/spaceship/death/5.png'),
    pg.image.load('../assets/spaceship/death/6.png'),
    pg.image.load('../assets/spaceship/death/7.png'),
    pg.image.load('../assets/spaceship/death/8.png'),
    pg.image.load('../assets/spaceship/death/9.png'),
    pg.image.load('../assets/spaceship/death/10.png'),
    pg.image.load('../assets/spaceship/death/11.png'),
    pg.image.load('../assets/spaceship/death/12.png'),
    pg.image.load('../assets/spaceship/death/13.png'),
    pg.image.load('../assets/spaceship/death/14.png'),
    pg.image.load('../assets/spaceship/death/15.png'),
    pg.image.load('../assets/spaceship/death/16.png'),
    pg.image.load('../assets/spaceship/death/17.png'),
    pg.image.load('../assets/spaceship/death/18.png'),
    pg.image.load('../assets/spaceship/death/19.png'),
    pg.image.load('../assets/spaceship/death/20.png'),
    pg.image.load('../assets/spaceship/death/21.png'),
    pg.image.load('../assets/spaceship/death/22.png'),
    pg.image.load('../assets/spaceship/death/23.png'),
    pg.image.load('../assets/spaceship/death/24.png'),
    pg.image.load('../assets/spaceship/death/25.png'),
    pg.image.load('../assets/spaceship/death/26.png'),
    pg.image.load('../assets/spaceship/death/27.png'),
    pg.image.load('../assets/spaceship/death/28.png'),
    pg.image.load('../assets/spaceship/death/29.png'),
    pg.image.load('../assets/spaceship/death/30.png'),
    pg.image.load('../assets/spaceship/death/31.png'),
    pg.image.load('../assets/spaceship/death/32.png'),
    pg.image.load('../assets/spaceship/death/33.png'),
    pg.image.load('../assets/spaceship/death/34.png'),
]

# UI


btn_img = pg.image.load('../assets/ui/—Pngtree—button button colorful _3911001.png')

title_img = pg.image.load('../assets/ui/Logo.png')
title_img = pg.transform.scale(title_img, (title_img.get_width() * 0.7, title_img.get_height() * 0.7))


# CHICKEN
chicken_sprite = [pg.image.load("../assets/chicken/0.png"),
                  pg.image.load("../assets/chicken/1.png"),
                  pg.image.load("../assets/chicken/2.png"),
                  pg.image.load("../assets/chicken/3.png"),
                  pg.image.load("../assets/chicken/4.png"),
                  pg.image.load("../assets/chicken/5.png"),
                  pg.image.load("../assets/chicken/6.png"),
                  pg.image.load("../assets/chicken/7.png"),
                  pg.image.load("../assets/chicken/8.png"),
                  pg.image.load("../assets/chicken/9.png"),
                  pg.image.load("../assets/chicken/10.png"),
                  pg.image.load("../assets/chicken/11.png"),
                  pg.image.load("../assets/chicken/12.png"),
                  pg.image.load("../assets/chicken/13.png"),
                  pg.image.load("../assets/chicken/14.png"),
                  pg.image.load("../assets/chicken/15.png"),
                  pg.image.load("../assets/chicken/16.png"),
                  pg.image.load("../assets/chicken/17.png"),
                  pg.image.load("../assets/chicken/18.png"),
                  pg.image.load("../assets/chicken/19.png"),
                  pg.image.load("../assets/chicken/20.png"),
                  pg.image.load("../assets/chicken/21.png")
                  ]
egg_img = pg.transform.scale(pg.image.load("../assets/chicken/egg.png"), (32, 41))
egg_crack = [
    pg.image.load('../assets/chicken/crack/egg_1-removebg-preview.png'),
    pg.image.load('../assets/chicken/crack/egg_2-removebg-preview.png'),
    pg.image.load('../assets/chicken/crack/egg_3-removebg-preview.png'),
    pg.image.load('../assets/chicken/crack/egg_4-removebg-preview.png'),
    pg.image.load('../assets/chicken/crack/egg_5-removebg-preview.png'),
    pg.image.load('../assets/chicken/crack/egg_6-removebg-preview.png'),
    pg.image.load('../assets/chicken/crack/egg_7-removebg-preview.png'),
    pg.image.load('../assets/chicken/crack/egg_8-removebg-preview.png'),
]

death_img = [
    pg.image.load('../assets/chicken/chicken death/1.png'),
    pg.image.load('../assets/chicken/chicken death/2.png'),
    pg.image.load('../assets/chicken/chicken death/3.png'),
    pg.image.load('../assets/chicken/chicken death/4.png'),
    pg.image.load('../assets/chicken/chicken death/5.png'),
    pg.image.load('../assets/chicken/chicken death/6.png'),
    pg.image.load('../assets/chicken/chicken death/7.png'),
    pg.image.load('../assets/chicken/chicken death/8.png'),
    pg.image.load('../assets/chicken/chicken death/9.png')
]
feather_list = [
    pg.image.load('../assets/chicken/feather/16.png'),
    pg.image.load('../assets/chicken/feather/17.png'),
    pg.image.load('../assets/chicken/feather/18.png'),
    pg.image.load('../assets/chicken/feather/19.png'),
    pg.image.load('../assets/chicken/feather/20.png'),
    pg.image.load('../assets/chicken/feather/21.png'),
    pg.image.load('../assets/chicken/feather/22.png'),
    pg.image.load('../assets/chicken/feather/23.png'),
    pg.image.load('../assets/chicken/feather/24.png'),
    pg.image.load('../assets/chicken/feather/25.png'),
    pg.image.load('../assets/chicken/feather/26.png'),
    pg.image.load('../assets/chicken/feather/27.png'),
    pg.image.load('../assets/chicken/feather/28.png'),
    pg.image.load('../assets/chicken/feather/29.png'),
    pg.image.load('../assets/chicken/feather/30.png'),
    pg.image.load('../assets/chicken/feather/31.png'),
]

# BOSS
darth_img = [
    pg.image.load('../assets/boss/1.png'),
    pg.image.load('../assets/boss/2.png'),
    pg.image.load('../assets/boss/3.png'),
    pg.image.load('../assets/boss/4.png'),
    pg.image.load('../assets/boss/5.png'),
    pg.image.load('../assets/boss/6.png'),
    pg.image.load('../assets/boss/7.png'),
    pg.image.load('../assets/boss/8.png'),
    pg.image.load('../assets/boss/9.png'),
    pg.image.load('../assets/boss/10.png'),
    pg.image.load('../assets/boss/11.png'),
    pg.image.load('../assets/boss/12.png'),
    pg.image.load('../assets/boss/13.png'),
    pg.image.load('../assets/boss/14.png'),
    pg.image.load('../assets/boss/15.png'),
    pg.image.load('../assets/boss/16.png'),
]

darth_explode = [
    pg.image.load('../assets/boss/boss explosion/1.png'),
    pg.image.load('../assets/boss/boss explosion/2.png'),
    pg.image.load('../assets/boss/boss explosion/3.png'),
    pg.image.load('../assets/boss/boss explosion/4.png'),
    pg.image.load('../assets/boss/boss explosion/5.png'),
    pg.image.load('../assets/boss/boss explosion/6.png'),
    pg.image.load('../assets/boss/boss explosion/7.png'),
    pg.image.load('../assets/boss/boss explosion/8.png'),
    pg.image.load('../assets/boss/boss explosion/9.png'),
    pg.image.load('../assets/boss/boss explosion/10.png'),
    pg.image.load('../assets/boss/boss explosion/11.png'),
    pg.image.load('../assets/boss/boss explosion/12.png'),
    pg.image.load('../assets/boss/boss explosion/13.png'),
    pg.image.load('../assets/boss/boss explosion/14.png'),
    pg.image.load('../assets/boss/boss explosion/15.png'),
    pg.image.load('../assets/boss/boss explosion/16.png'),
    pg.image.load('../assets/boss/boss explosion/17.png'),
    pg.image.load('../assets/boss/boss explosion/18.png'),
    pg.image.load('../assets/boss/boss explosion/19.png'),
    pg.image.load('../assets/boss/boss explosion/20.png'),
    pg.image.load('../assets/boss/boss explosion/21.png'),
    pg.image.load('../assets/boss/boss explosion/22.png'),
    pg.image.load('../assets/boss/boss explosion/23.png'),
    pg.image.load('../assets/boss/boss explosion/24.png'),
    pg.image.load('../assets/boss/boss explosion/25.png'),
    pg.image.load('../assets/boss/boss explosion/26.png'),
    pg.image.load('../assets/boss/boss explosion/27.png'),
    pg.image.load('../assets/boss/boss explosion/28.png'),
    pg.image.load('../assets/boss/boss explosion/29.png'),
    pg.image.load('../assets/boss/boss explosion/30.png'),
    pg.image.load('../assets/boss/boss explosion/31.png'),
    pg.image.load('../assets/boss/boss explosion/32.png'),
    pg.image.load('../assets/boss/boss explosion/33.png'),
    pg.image.load('../assets/boss/boss explosion/34.png'),
    pg.image.load('../assets/boss/boss explosion/35.png'),
    pg.image.load('../assets/boss/boss explosion/36.png'),
    pg.image.load('../assets/boss/boss explosion/37.png'),
    pg.image.load('../assets/boss/boss explosion/38.png'),
    pg.image.load('../assets/boss/boss explosion/39.png'),
    pg.image.load('../assets/boss/boss explosion/40.png'),
    pg.image.load('../assets/boss/boss explosion/41.png'),
    pg.image.load('../assets/boss/boss explosion/42.png'),
    pg.image.load('../assets/boss/boss explosion/43.png'),
    pg.image.load('../assets/boss/boss explosion/44.png'),
    pg.image.load('../assets/boss/boss explosion/45.png'),
    pg.image.load('../assets/boss/boss explosion/46.png'),
]

boss_laser = pg.image.load('../assets/boss/laserBoss.png')