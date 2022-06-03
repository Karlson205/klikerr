import pygame.image
from pygame.color import THECOLORS


class Level:
    def __init__(self):
        self.value = 1
        self.image = pygame.image.load(r'img/new_level2.png')
        self.pos = (50, 0)

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        self.write(screen)

    def write(self,screen):
        font = pygame.font.SysFont('arial', 20)
        text = font.render(f"{self.value}", True, [255,255,255])
        screen.blit(text, (65, 35))