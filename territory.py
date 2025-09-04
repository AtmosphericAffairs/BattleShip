import pygame

class Territory():
    def __init__(self, screen):
        self.screen = screen
        self.number = [str(i) for i in range(1, 11)]
        self.bukvi = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']
                    
    def fill_battle(self):
        self.terrytory = pygame.draw.rect(self.screen, (230, 230, 230), (self.x, self.y, 201, 201))
        self.coords = []
        x = self.x
        y = self.y
        for i in range(10):
            for j in range(10):
                self.coords.append(pygame.draw.rect(self.screen, (50, 50, 50), (x, y, 22, 22), 2))
                y += 20
            y = self.y
            x += 20
        x = self.x

        for i in self.number:
            y += 20
            self.screen.blit(pygame.font.SysFont('serif', 18).render(i, True, (10, 10, 10)), (x-18, y-20))
        for i in self.bukvi:
            x += 20
            self.screen.blit(pygame.font.SysFont('serif', 18).render(i, True, (10, 10, 10)), (x-12, 0))
              