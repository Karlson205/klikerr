import pygame.image
from pygame.color import THECOLORS

class Musicc:
    def __init__(self):
        self.defo = pygame.image.load(r'img/defo.png')
        self.pos = (0, 550)
        self.klik = pygame.image.load(r"img/arcane.png")
        self.pos_klik = (125, 540)
        self.mech = pygame.image.load(r"img/jinx.png")
        self.pos_mech = (570, 500)
        self.image = pygame.image.load(r'img/DJ.png')
        self.defo_pos = (60, 0)
        self.plus = pygame.image.load(r'img/plus.png')
        self.plus_pos = (-23, 0)
        self.minus = pygame.image.load(r'img/minus.png')
        self.minus_pos = (-15, 150)

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        screen.blit(self.defo, self.defo_pos)
        screen.blit(self.klik, self.pos_klik)
        screen.blit(self.mech, self.pos_mech)
        screen.blit(self.plus, self.plus_pos)
        screen.blit(self.minus, self.minus_pos)