import pygame
import copy
from settings import Setting
from territory_computer import Territory_computer
from territory_gamer import Territory_gamer
from position_ship_gamer import Position_ship_gamer
from position_ship_computer import Position_ship_Computer
from event_handler import EventHandler
from button import Button
from shooting import Shoting
from window_message import Window_message
import game_function as gf


coords_ship = [[False, 1, 60, 250], [False, 1, 90, 250], [False, 1, 120, 250], [False, 1, 150, 250], [False, 1, 180, 250],
        [False, 1, 210, 250], [False, 1, 60, 340], [False, 1, 90, 340], [False, 1, 120, 340], [False, 1, 150, 340]]

coords_ship_comp = [[False, 1, 332, 250], [False, 1, 362, 250], [False, 1, 392, 250], [False, 1, 422, 250], [False, 1, 452, 250],
        [False, 1, 482, 250], [False, 1, 332, 340], [False, 1, 362, 340], [False, 1, 392, 340], [False, 1, 422, 340]]

copy_coords_ship = copy.deepcopy(coords_ship)
copy_coords_ship_comp = copy.deepcopy(coords_ship_comp)

def run_game():
    pygame.init()
    level = 1
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Морской бой')
    territory_computer = Territory_computer(screen)
    territory_gamer = Territory_gamer(screen)
    position_ship_gamer = Position_ship_gamer(screen, copy_coords_ship, coords_ship, territory_gamer)
    position_ship_computer = Position_ship_Computer(screen, copy_coords_ship_comp, coords_ship_comp, territory_computer, level)
    window_message = Window_message(screen)
    shoting = Shoting(screen, territory_gamer, territory_computer, position_ship_gamer, position_ship_computer, window_message)
    while True:
        screen.fill(ai_setting.bg_color)
        button = Button(screen, level)
        territory_computer.fill_battle()
        territory_gamer.fill_battle()
        position_ship_computer.position()
        position_ship_gamer.position()
        EventHandler(position_ship_gamer, territory_gamer, button, position_ship_computer, position_ship_gamer, shoting, level)
        gf.change_of_list_coords(position_ship_gamer.copy_coords_ship)
        if level > 1:
                shoting.shot_comp()
                territory_computer.fog_activation(level)
                shoting.winner()
                shoting.fill()
                window_message.message_output(level)
        level = position_ship_computer.level
        pygame.display.flip()

run_game()