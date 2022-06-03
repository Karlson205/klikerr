import pygame.image

pygame.init()


class Boss:
    def __init__(self, level):
        self.level = level
        self.hp = 50 * level
        self.img = pygame.image.load(r"img/boss.png")
        self.pos = (100, 200)

    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def bite(self, damage):
        """
        Эта функция добавляет валюту №2
        """
        self.hp -= damage
        if self.hp <= 0:
            self.level += 1
            self.hp = 50 * self.level
            return 13 * self.level
        return 0