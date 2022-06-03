import pygame.image

class Name:
    def __init__(self):
        self.image = pygame.image.load(r"img/pavel.png")
        self.pos = (50,0)


    def draw(self, screen):
        screen.blit(self.image, self.pos)