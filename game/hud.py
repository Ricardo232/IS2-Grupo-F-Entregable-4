import pygame as pg
from os import *
from settings import *
from spritesheet import *

class HUD(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.folder = "HUD"
        self.image = self.load_life()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = ((0, HEIGHT))

    def load_life(self):
        self.width = 87
        self.height = 76
        backlife_sprite = SpriteSheet(self.folder, "Empty Life Orb.png")
        self.backlife = backlife_sprite.image
        frontlife_sprite = SpriteSheet(self.folder, "Life Orb.png")
        self.frontlife = frontlife_sprite.image
        self.frontlife.set_colorkey((0, 1, 0))
        image = pg.Surface((self.width, self.height))
        image.blit(self.backlife, (0, 0))
        image.blit(self.frontlife, (0, 0))
        image.set_colorkey((BLACK))
        return image

    def get_life(self, n):
        self.image.fill((WHITE))
        self.image.blit(self.backlife, (0, 0))
        self.image.blit(self.frontlife, (0, self.height * n), (0, self.height * n, self.width, self.height))
