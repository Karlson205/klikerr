import pygame.image

class Music:
    def __init__(self):
        self.image = pygame.image.load(r'img/DJ.png')
        self.pos = (0, 550)

    def draw(self, screen):
        screen.blit(self.image, self.pos)