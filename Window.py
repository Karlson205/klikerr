import pygame.image
from pygame.color import THECOLORS
from random import choice


class CodeWindow:
    def __init__(self):
        self.letters = ["D", "F", "G", "T", "O", "1", "2", "8", "3", "5", "6"]
        self.promo = [choice(self.letters) for x in range(8)]
        self.code_pos = (180, 300)

    def generate(self):
        self.promo = [choice(self.letters) for x in range(8)]

    def return_promo(self):
        return "".join(self.promo)

    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Вот ваш код:  {self.return_promo()} наслаждайтесь своим напитком", True, THECOLORS["red"])
        screen.fill((255, 255, 255))
        screen.blit(text, self.code_pos)
