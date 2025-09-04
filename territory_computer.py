from territory import Territory
import pygame

class Territory_computer(Territory):
    def __init__(self, screen):
        super().__init__(screen)
        self.x = 332
        self.y = 20

    def fog_activation(self, level):
        if level == 2:
            pygame.draw.rect(self.screen, (230, 230, 230), (self.x, self.y, 201, 201))
            x = self.x
            y = self.y
            for i in range(10):
                for j in range(10):
                    self.coords.append(pygame.draw.rect(self.screen, (50, 50, 50), (x, y, 22, 22), 2))
                    y += 20
                y = self.y
                x += 20
            x = self.x

