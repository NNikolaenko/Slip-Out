# -*- coding:utf-8 -*-

from pygame.sprite import Sprite
from pygame import Surface
from pygame import image
from pygame import display
from pygame import SRCALPHA
from pygame import font
from pygame import Color

colour = (30, 30, 30)


class TextObject(Sprite):
    def __init__(self, txt, pos=(0, 0)):
        Sprite.__init__(self)
        self.surface = Surface((1280, 720), SRCALPHA)
        self.txt = txt
        self.pos = pos
        self.font = font.SysFont('Comic Sans MS', 30)
        self.textSurface = self.font.render(self.txt, False, colour)
        self.surface.blit(self.textSurface, self.pos)

    def upload(self, text):
        self.surface = Surface((1280, 720), SRCALPHA)
        self.txt = text
        self.textSurface = self.font.render(self.txt, True, colour)
        self.surface.blit(self.textSurface, self.pos)

    def update(self):
        pass

    def draw(self, surface, typing=False):
        surface.blit(self.surface, (0, 0))
