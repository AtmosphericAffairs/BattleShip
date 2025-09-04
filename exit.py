import pygame
import sys
import game_function as gf
import random

def mouse_click(position_ship, territory_gamer, button, position_ship_computer, shoting, level):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if level == 1:
                if event.button == 1:
                    if gf.element_capture_check(position_ship.copy_coords_ship) == None:
                        position_ship.change_of_position(pygame.mouse.get_pos())
                    else:
                        x = gf.element_capture_check(position_ship.copy_coords_ship)
                        position_ship.coords_flag(x, position_ship.ships[x])
                    if button.bt1.collidepoint(pygame.mouse.get_pos()):
                        if gf.start_game(position_ship, territory_gamer):
                            position_ship_computer.go()
                            level = 2
                if event.button == 3:
                    position_ship.turn_ship()
            elif level > 1:
                if button.bt1.collidepoint(pygame.mouse.get_pos()):
                    shoting.stop_game()
                    position_ship.stop_game()
                    position_ship_computer.stop_game()
                    level = 1
                if level == 2:
                    shoting.shot_gamer(pygame.mouse.get_pos())