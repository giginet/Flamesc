# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *

class Paper(pygame.Sprite):
    u"""紙のベースクラス"""
    _filepath = u'/resources/image/kawaz.png'

    def __init__(self, x=0, y=0):
        self.image = Image(0,0,self._filepath)
        self.hitrect = Rect(x,y, self.image.width, self.image.height)
        
    def render(self):
        self.image.render()
        
    