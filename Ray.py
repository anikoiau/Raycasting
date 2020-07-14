# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:15:55 2020

@author: soumitra
"""


import pygame
import numpy as np

class Ray1:
    def __init__(self, x1, y1, rad):
        self.pos = [x1, y1]
        self.dir = [np.cos(rad), np.sin(rad)]
        
        
    # def drawRay(self, screen):
    #     self.end = [self.pos[0] + self.dir[0], self.pos[1] + self.dir[1]]
    #     #pygame.draw.line(screen, (255, 255, 255), self.pos, self.end, 1)
        
        
    def check(self, wall):
        # start point
        x1 = wall.a[0]
        y1 = wall.a[1]
        # end point
        x2 = wall.b[0]
        y2 = wall.b[1]
    
        #position of the ray
        x3 = self.pos[0]
        y3 = self.pos[1]
        x4 = self.pos[0] + self.dir[0]
        y4 = self.pos[1] + self.dir[1]
    
        #denominator
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        #numerator
        num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        if den == 0:
            return None
        
        #formulas
        t = num / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    
        if t > 0 and t < 1 and u > 0:
            #Px, Py
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            pot = np.array([x,y])
            return pot