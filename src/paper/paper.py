# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *

import settings

class Paper(pygame.sprite.Sprite):
    u"""紙のベースクラス"""
    _filepath = u'../resources/image/kawaz.png'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.image = Image(0,0,self._filepath)
        self.hitrect = Rect(x,y, self.image.width, self.image.height)
        self.accele = Vector()
        self.gravity = Vector()
        
    def render(self):
        self.image.render(self.x, self.y)
        
    def act(self):
        self._gravity()
        self.accele = self.accele + self.gravity
        self.x += self.accele.x
        self.y += self.accele.y
        
    def _gravity(self):
        self.gravity.y += settings.GRAVITY