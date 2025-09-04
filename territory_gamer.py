from territory import Territory
import pygame

class Territory_gamer(Territory):
    def __init__(self, screen):
        super().__init__(screen)
        self.x = 60
        self.y = 20
