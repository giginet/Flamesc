# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from core import *
import os

class Image(pygame.rect.Rect):
    def __init__(self, x=0 ,y=0, path=u""):
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        super(Image, self).__init__(x,y,self.rect.w,self.rect.h)
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = x
        self.y = y
        
    def render(self, x=None, y=None):
        if x:
            self.x = x
        if y:
            self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        Game.get_screen().blit(self.image, self.rect)
        
class Font(pygame.sprite.Sprite):
    pass