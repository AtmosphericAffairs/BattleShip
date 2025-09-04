import pygame
import game_function as gf

class Position_ship():
    def __init__(self, screen):
        self.screen = screen

    def position(self):
        self.ships = [
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[0][2], self.copy_coords_ship[0][3], self.copy_coords_ship[0][1], 0)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[1][2], self.copy_coords_ship[1][3], self.copy_coords_ship[1][1], 1)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[2][2], self.copy_coords_ship[2][3], self.copy_coords_ship[2][1], 1)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[3][2], self.copy_coords_ship[3][3], self.copy_coords_ship[3][1], 2)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[4][2], self.copy_coords_ship[4][3], self.copy_coords_ship[4][1], 2)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[5][2], self.copy_coords_ship[5][3], self.copy_coords_ship[5][1], 2)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[6][2], self.copy_coords_ship[6][3], self.copy_coords_ship[6][1], 3)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[7][2], self.copy_coords_ship[7][3], self.copy_coords_ship[7][1], 3)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[8][2], self.copy_coords_ship[8][3], self.copy_coords_ship[8][1], 3)),
        pygame.draw.rect(self.screen, (0, 0, 105), gf.data_ship(self.copy_coords_ship[9][2], self.copy_coords_ship[9][3], self.copy_coords_ship[9][1], 3))
        ]