import pygame
class Particle:
    px = 0 
    py = 0
    vx = 0
    vy = 0
    ax = 0 
    ay = 0 
    radius = None
    elasticity = 1 # Coefficient of Restitution
    def __init__(self, px=400, py=400, vx=0, vy=0, ax=0, ay=9, radius=0, elasticity=1):
        self.px = px 
        self.py = py
        self.vx = vx
        self.vy = vy
        self.ax = ax 
        self.ay = ay
        self.radius = radius
        self.elasticity = elasticity

        