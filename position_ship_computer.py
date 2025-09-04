import pygame
import copy
from position_ship import Position_ship
import game_function as gf

class Position_ship_Computer(Position_ship):
    def __init__(self, screen, copy_coords_ship_comp, coords_ship_comp, territory_computer, level):
        super().__init__(screen)
        self.copy_coords_ship = copy_coords_ship_comp
        self.coords_ship_comp = coords_ship_comp
        self.territory_computer = territory_computer
        self.level = level
    
    def go(self):
        rect_ships = []
        turns = []
        gf.coordinate_matching_check_comp(self.copy_coords_ship, self.territory_computer, rect_ships, turns)
        gf.copy_coords(self.copy_coords_ship, turns, rect_ships)
        self.level = 2

    def stop_game(self):
        self.copy_coords_ship = copy.deepcopy(self.coords_ship_comp)
        self.level = 1

    def result(self):
        self.level = 3

            
                
                

                
