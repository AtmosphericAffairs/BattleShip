import pygame
import random


def data_ship(x, y, turn, type_ship):
        if type_ship == 0:
            if turn == 1:
                return (x, y, 18, 78)
            else:
                return (x, y, 78, 18)
        if type_ship == 1:
            if turn == 1:
                return (x, y, 18, 58)
            else:
                return (x, y, 58, 18)
        if type_ship == 2:
            if turn == 1:
                return (x, y, 18, 38)
            else:
                return (x, y, 38, 18)
        if type_ship == 3:
                return (x, y, 18, 18)

def change_of_list_coords(lists):
    for i in lists:
        if i[0]:
            i[2] = pygame.mouse.get_pos()[0]
            i[3] = pygame.mouse.get_pos()[1]

def coordinate_matching_check(terrytory_gamer, a, copy_coord_ship, coords_ship, name_ship, ships):
    rect_ship = pygame.Rect((name_ship.x-22, name_ship.y-22, name_ship.width+25, name_ship.height+25))
    if terrytory_gamer.terrytory.collidepoint(pygame.mouse.get_pos()) and len(rect_ship.collidelistall(ships)) < 2:
        copy_coord_ship[a][2] = terrytory_gamer.coords[name_ship.collidelistall(terrytory_gamer.coords)[0]].x+2
        copy_coord_ship[a][3] = terrytory_gamer.coords[name_ship.collidelistall(terrytory_gamer.coords)[0]].y+2
        if not terrytory_gamer.terrytory.contains(pygame.Rect(copy_coord_ship[a][2], copy_coord_ship[a][3], name_ship.width, name_ship.height)):
            copy_coord_ship[a] = coords_ship[a].copy()
    else:
        copy_coord_ship[a] = coords_ship[a].copy()


def element_capture_check(list_ship):
        for i in range(len(list_ship)):
            if list_ship[i][0]:
                return i
        return None

def coordinate_matching_check_comp(copy_coords_ship_comp, territory_computer, rect_ships, turns):
        for i in range(10):
            if i == 0: type_ship = 0
            elif i < 3: type_ship = 1
            elif i < 6: type_ship = 2
            else: type_ship = 3
            setting_to_position = True
            while(setting_to_position):
                turn = random.randint(0, 1)
                coord = random.randint(0, 99)
                x = territory_computer.coords[coord].x
                y = territory_computer.coords[coord].y
                rc = pygame.Rect((data_ship(x, y, turn, type_ship)))
                rect_ship = pygame.Rect((x-20, y-20, rc.width + 40 , rc.height + 40))
                if len(rect_ship.collidelistall(rect_ships)) == 0 and territory_computer.terrytory.contains(rc):
                    rect_ships.append(rc)
                    turns.append(turn)
                    setting_to_position = False

def copy_coords(copy_coords_ship_comp, turns, rect_ships):
        for i in range(10):
            copy_coords_ship_comp[i][1] = turns[i]
            copy_coords_ship_comp[i][2] = rect_ships[i].x+2
            copy_coords_ship_comp[i][3] = rect_ships[i].y+2

def start_game(position_ship, territory_gamer):
    if len(territory_gamer.terrytory.collidelistall(position_ship.ships)) == 10:
        return True
    else: return False
