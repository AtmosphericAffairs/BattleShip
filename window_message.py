import pygame

class Window_message():
    def __init__(self, screen):
        self.screen = screen
        self.number_message = 0
        self.message_font = pygame.font.SysFont('serif', 20)
    
    def message_output(self, level):
        if level > 1:
            
            surf = pygame.Surface((360, 100))
            surf.fill((100, 100, 100))
            if self.number_message == 0:
                surf.blit(self.message_font.render('СТРЕЛЯЙ!', True, (0, 0, 0)), (130, 40))
            elif self.number_message == 1:
                surf.blit(self.message_font.render('Мимо...', True, (0, 0, 0)), (130, 40))
            elif self.number_message == 2:
                surf.blit(self.message_font.render('Ранил!', True, (240, 10, 10)), (130, 40))
                surf.blit(self.message_font.render('Стреляй снова', True, (0, 0, 0)), (100, 60))
            elif self.number_message == 3:
                surf.blit(self.message_font.render('УБИЛ!', True, (240, 10, 10)), (130, 40))
                surf.blit(self.message_font.render('Стреляй снова', True, (0, 0, 0)), (100, 60))
            elif self.number_message == 4:
                surf.blit(self.message_font.render('Попробуй еще раз', True, (0, 0, 0)), (100, 40))
            elif self.number_message == 5:
                surf.blit(self.message_font.render('Увы, но тебя отодрали,', True, (240, 10, 10)), (65, 40))
                surf.blit(self.message_font.render('словно русских при Цусиме', True, (240, 10, 10)), (45, 60))
            elif self.number_message == 6:
                surf.blit(self.message_font.render('Вот это битва, словно Ютландский бой!', True, (240, 10, 10)), (0, 40))
                surf.blit(self.message_font.render('Поздравляю!', True, (240, 10, 10)), (110, 60))
            self.screen.blit(surf, (120, 290))