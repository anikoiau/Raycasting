# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:22:17 2020

@author: soumitra
"""


import pygame
import numpy as np
import Wall
import Ray
import Particle
import time

np.random.seed(int(time.time()))
WIDTH = 800
HEIGHT = 700

SCREEN = (WIDTH, HEIGHT)

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN)
        
        self.stop = False
        self.clock = pygame.time.Clock()
        self.raypos = [None, None]
        self.pointpos = [None, None]
        self.particle = Particle.Point()
        
        self.walls = []
        
        for i in range(3):
            x1 = np.random.randint(0,WIDTH)
            y1  = np.random.randint(0, HEIGHT)
            x2 = np.random.randint(0, WIDTH)
            y2 = np.random.randint(0, HEIGHT)
           
            self.walls.append(Wall.Bounds(x1,y1,x2,y2))

        self.walls.append(Wall.Bounds(0,0,WIDTH,0))
        self.walls.append(Wall.Bounds(0, 0, 0, HEIGHT))
        self.walls.append(Wall.Bounds(0, HEIGHT, WIDTH, HEIGHT))
        self.walls.append(Wall.Bounds(WIDTH, 0, WIDTH, HEIGHT))
        
        
        
    def draw(self):
        #wall = Wall.Bounds(400, 100, 400, 500)
        #ray = Ray.Ray1(100, 300, 0)
        
        for wall in self.walls:
            wall.drawWall(self.screen)
        #ray.drawRay(self.screen)
        #self.particle.draw(self.screen)
        
        
    def run(self):
        
        while not self.stop:
            self.screen.fill((10, 10, 10))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopgame = True
                    pygame.quit()
                    
                if event.type == pygame.MOUSEMOTION:

                    pos = event.pos
                    self.particle.pos[0] = pos[0]
                    self.particle.pos[1] = pos[1]
                    
                    # try:
                    #      pos = event.pos
                         
                    #      self.raypos[0] = pos[0]
                    #      self.raypos[1] = pos[1]
                         
                    #      self.m = (pos[1] - 300)/(pos[0] - 100)
                    #      self.radians = np.arctan(self.m)
                    # except ZeroDivisionError:
                    #     if self.m < 0: 
                    #         self.radians = -np.pi/2
                    #     else:
                    #         self.radians = np.pi/2
                        
                    # print(self.m, '  ', self.radians)
                    
            s1 = self.screen        
            pygame.draw.circle(s1, (255, 255, 255), np.array(pos), 20, 20)
            self.particle.lookAt(self.screen, self.walls)
            #self.ray = Ray.Ray1(100, 300, self.radians)        
            self.draw()
            self.clock.tick()
            pygame.display.update()
            
            
            
D = Display()
D.run()
        
        