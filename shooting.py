import pygame
import random
import time

class Shoting():
    def __init__(self, screen, territory_gamer, territory_computer, position_ship_gamer, position_ship_computer, window_message):
        self.screen = screen
        self.territory_gamer = territory_gamer
        self.territory_computer = territory_computer
        self.position_ship_gamer = position_ship_gamer
        self.position_ship_computer = position_ship_computer
        self.window_message = window_message

        self.hit_point_ship = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.hit_point_ship_gamer = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.shotted = []
        self.dots = []
        self.crosses = []
        self.shotted_comp = []
        self.dots_comp = []
        self.crosses_comp = []
        self.shoot_direction = ''
        self.target = False
        self.count = 0
        self.shooter = False
        self.target_selection = [i for i in range(0, 100)]

    def winner(self):
        if sum(self.hit_point_ship) == 0:
            self.position_ship_computer.result()
            self.window_message.number_message = 6
        elif sum(self.hit_point_ship_gamer) == 0:
            self.window_message.number_message = 5
            self.position_ship_computer.result()

    def shot_gamer(self, pos):    
        if self.territory_computer.terrytory.collidepoint(pos):
            shot = pygame.Rect((pos[0], pos[1], 1, 1))
            coord = shot.collidelist(self.territory_computer.coords)
            number_ship = self.territory_computer.coords[coord].collidelist(self.position_ship_computer.ships)
            if coord in self.shotted:
                self.window_message.number_message = 4
            else:
                self.shotted.append(coord)
                if number_ship != -1:
                    self.crosses.append((self.territory_computer.coords[coord].x+2, self.territory_computer.coords[coord].y+2))
                    self.hit_point_ship[number_ship] -= 1
                    if self.hit_point_ship[number_ship] == 0:
                        self.window_message.number_message = 3
                        rc = pygame.Rect((self.position_ship_computer.ships[number_ship].x - 18, self.position_ship_computer.ships[number_ship].y - 18, self.position_ship_computer.ships[number_ship].width + 36, self.position_ship_computer.ships[number_ship].height + 36))
                        for i in rc.collidelistall(self.territory_computer.coords):
                            if not i in self.shotted:
                                self.shotted.append(i)
                                self.dots.append((self.territory_computer.coords[i].centerx, self.territory_computer.coords[i].centery))
                    else: 
                        self.window_message.number_message = 2
                else: 
                    self.window_message.number_message = 1
                    self.dots.append((self.territory_computer.coords[coord].centerx, self.territory_computer.coords[coord].centery))
                    self.shooter = True

    def drawing_dots(self, dots):
        for i in dots:
            pygame.draw.circle(self.screen, (10, 10, 10 ,10), i, 3)

    def drawing_crosses(self, crosses):
        for i in crosses:
            pygame.draw.aaline(self.screen, (250, 10, 10), (i), (i[0] + 18, i[1] + 18))
            pygame.draw.aaline(self.screen, (250, 10, 10), (i[0] + 18, i[1]), (i[0], i[1] + 18))

    def fill(self):
        self.drawing_dots(self.dots)
        self.drawing_crosses(self.crosses)
        self.drawing_dots(self.dots_comp)
        self.drawing_crosses(self.crosses_comp)

    def delete_target(self, target):
        self.target_selection.remove(target)

    def chec_ship(self, target):
        number_ship = self.territory_gamer.coords[target].collidelist(self.position_ship_gamer.ships)
        if number_ship >= 0:
            self.crosses_comp.append((self.territory_gamer.coords[target].x+2, self.territory_gamer.coords[target].y+2))
            return number_ship
        else:
            self.dots_comp.append((self.territory_gamer.coords[target].centerx, self.territory_gamer.coords[target].centery))
            return None

    def new_target_count_1(self, target):
        possible_target = []
        if target >= 10 and target - 10 in self.target_selection:
            possible_target.append(target - 10)
        if target % 10 != 0 and target - 1 in self.target_selection:
            possible_target.append(target - 1)
        if target <= 89 and target + 10 in self.target_selection:
            possible_target.append(target + 10)
        if (target + 1) % 10 != 0 and target + 1 in self.target_selection:
            possible_target.append(target + 1)
        x = random.choice(possible_target)
        self.direction_determination(target, x)
        return x

    def direction_determination(self, a, b):
        if a - b == 10:
            self.shoot_direction = 'left'
        elif a - b == 1:
            self.shoot_direction = 'up'
        elif b - a == 10:
            self.shoot_direction = 'right'
        elif b - a == 1:
            self.shoot_direction = 'down'  

    def check_new_target(self, target, x):
        while(True):
            if not target in self.target_selection:
                target += x
            else: 
                break
        return target

    def new_target_count_2(self, x):
        target = x
        if self.shoot_direction == 'left':
            if target >= 10 and target - 10 in self.target_selection:
                return (target - 10)
            else:
                self.shoot_direction = 'right'
                target = self.check_new_target(target, 10)
                return self.new_target_count_2(target - 10)
        elif self.shoot_direction == 'up':
            if target % 10 != 0 and target - 1 in self.target_selection:
                return (target - 1)
            else:
                self.shoot_direction = 'down'
                target = self.check_new_target(target, 1)
                return self.new_target_count_2(target - 1)
        elif self.shoot_direction == 'right':
            if target <= 89 and target + 10 in self.target_selection:
                return (target + 10)
            else:
                self.shoot_direction = 'left'
                target = self.check_new_target(target, -10)
                return self.new_target_count_2(target + 10)

        elif self.shoot_direction == 'down':
            if (target + 1) % 10 != 0 and target + 1 in self.target_selection:
                return (target + 1)
            else:
                self.shoot_direction = 'up'
                target = self.check_new_target(target, -1)
                return self.new_target_count_2(target + 1)

    def killing_ship(self, number_ship):
        rc = pygame.Rect((self.position_ship_gamer.ships[number_ship].x - 18, self.position_ship_gamer.ships[number_ship].y - 18, self.position_ship_gamer.ships[number_ship].width + 36, self.position_ship_gamer.ships[number_ship].height + 36))
        for i in rc.collidelistall(self.territory_gamer.coords):
            if i in self.target_selection:
                self.dots_comp.append((self.territory_gamer.coords[i].centerx, self.territory_gamer.coords[i].centery))
                self.delete_target(i)

    def shot_comp(self):
        if self.shooter:
            if self.count == 0:
                target = random.choice(self.target_selection)
            elif self.count == 1:
                target = self.new_target_count_1(self.target)
            else: 
                target = self.new_target_count_2(self.target)
            self.delete_target(target)
            if self.chec_ship(target) == None:
                self.shooter = False
            else: 
                number_ship = self.chec_ship(target)                
                self.target = target
                self.hit_point_ship_gamer[number_ship] -= 1
                if self.hit_point_ship_gamer[number_ship] == 0:                    
                    self.killing_ship(number_ship)
                    self.count = 0
                else:             
                    self.count += 1
                time.sleep(0.3)

    def stop_game(self):
        self.hit_point_ship = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.hit_point_ship_gamer = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.shotted = []
        self.dots = []
        self.crosses = []
        self.shotted_comp = []
        self.dots_comp = []
        self.crosses_comp = []
        self.shoot_direction = ''
        self.target = False
        self.count = 0
        self.shooter = False
        self.target_selection = [i for i in range(0, 100)] 
        self.window_message.number_message = 0   
