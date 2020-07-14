# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:26:41 2020

@author: soumitra
"""


import numpy as np
import pygame
import Ray


class Point:
    def __init__(self):
        self.pos = [200, 200]
        
        
    def draw(self, screen):
        for ray in self.rays:
            ray.drawRay(screen)
            
        
    def lookAt(self, screen, walls):
        self.rays = []
        
        for i in range(0, 360, 1):
            self.rays.append(Ray.Ray1(self.pos[0], self.pos[1], np.deg2rad(i)))
        # self.rays.append(Ray.Ray1(self.pos[0], self.pos[1], np.pi/3))
        # self.rays.append(Ray.Ray1(self.pos[0], self.pos[1], i))
        # self.rays.append(Ray.Ray1(self.pos[0], self.pos[1], i))
        
        for ray in self.rays:
            closest = 1000000000
            closestpt = None
            
            for wall in walls:
                pt = ray.check(wall)
                
                if pt is not None:
                    dist = np.linalg.norm(pt - self.pos)
                    
                    if dist < closest:
                        closest = dist
                        closestpt = pt
            
        
            if closestpt is not None:
                pygame.draw.line(screen, (255, 255, 255), self.pos, np.array(closestpt, int), 1)
