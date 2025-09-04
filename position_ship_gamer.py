import pygame
import copy
from position_ship import Position_ship
import game_function as gf

class Position_ship_gamer(Position_ship):
    def __init__(self, screen, copy_coords_ship, coords_ship, territory_gamer):
        super().__init__(screen)
        self.copy_coords_ship = copy_coords_ship
        self.coords_ship = coords_ship
        self.territory_gamer = territory_gamer
        
    def coords_flag(self, a, name_ship):
        if self.copy_coords_ship[a][0]:
            self.copy_coords_ship[a][0] = False
            gf.coordinate_matching_check(self.territory_gamer, a, self.copy_coords_ship, self.coords_ship, name_ship, self.ships)
        else:
            self.copy_coords_ship[a][0] = True

    def change_of_position(self, pos):
        if self.ships[0].collidepoint(pos):
            self.coords_flag(0, self.ships[0])
        elif self.ships[1].collidepoint(pos):
            self.coords_flag(1, self.ships[1])
        elif self.ships[2].collidepoint(pos):
            self.coords_flag(2, self.ships[2])
        elif self.ships[3].collidepoint(pos):
            self.coords_flag(3, self.ships[3])
        elif self.ships[4].collidepoint(pos):
            self.coords_flag(4, self.ships[4])
        elif self.ships[5].collidepoint(pos):
            self.coords_flag(5, self.ships[5])
        elif self.ships[6].collidepoint(pos):
            self.coords_flag(6, self.ships[6])
        elif self.ships[7].collidepoint(pos):
            self.coords_flag(7, self.ships[7])
        elif self.ships[8].collidepoint(pos):
            self.coords_flag(8, self.ships[8])
        elif self.ships[9].collidepoint(pos):
            self.coords_flag(9, self.ships[9])

    def turn_ship(self):
        for i in self.copy_coords_ship:
            if i[0]:
                if i[1] == 1:
                    i[1] = 0
                else:
                    i[1] = 1

    def stop_game(self):
        self.copy_coords_ship = copy.deepcopy(self.coords_ship)

    def auto(self):
        rect_ships = []
        turns = []
        gf.coordinate_matching_check_comp(self.copy_coords_ship, self.territory_gamer, rect_ships, turns)
        gf.copy_coords(self.copy_coords_ship, turns, rect_ships)





