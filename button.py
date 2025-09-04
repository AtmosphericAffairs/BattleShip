import pygame

class Button():
    def __init__(self, screen, level):
        self.screen = screen
        self.bt1 = pygame.draw.rect(self.screen, (230, 230, 230), (260, 227, 65, 20))
        self.text_btn1 = pygame.font.SysFont('serif', 16)
        if level == 1:
            self.screen.blit(self.text_btn1.render('Старт', True, (10, 10, 10)), (273, 227))
            self.bt2 = pygame.draw.rect(self.screen, (230, 230, 230), (60, 360, 120, 27))  
            self.screen.blit(self.text_btn1.render('Расставить', True, (10, 10, 10)), (67, 358))
            self.screen.blit(self.text_btn1.render('автоматически', True, (10, 10, 10)), (63, 370))  
        elif level > 1:
            self.screen.blit(self.text_btn1.render('Заново', True, (10, 10, 10)), (267, 227)) 
        

