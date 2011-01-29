# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.core import *
from pywaz.input import *
from pywaz.utils import *
from pywaz.graphic import *
from paper import *

import settings


class Player(Paper):
    _filepath = u"/resources/image/kawaz.png"
    INITIAL = {'x':0, 'y':0}
    
    def __init__(self):
        super(Paper, self).__init__(self.INITIAL.x, self.INITIAL.y)
        
    def act(self):
        pass
    
    def proceed(self):
        pass