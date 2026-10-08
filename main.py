import pygame as pg
import game_setup as gs
import ctypes


def main():
    ctypes.windll.user32.SetProcessDPIAware()
    pg.init()
    gs.start_game()


if __name__ == '__main__':
    main()
