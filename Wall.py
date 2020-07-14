# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:08:53 2020

@author: soumitra
"""

import pygame
import numpy as np


class Bounds:
    def __init__(self, x1, y1, x2, y2):
        self.a = [x1, y1]
        self.b = [x2, y2]
        
        
    def drawWall(self, screen):
        pygame.draw.aaline(screen, (255, 255, 0), self.a, self.b, 5)
        
        
    
        
