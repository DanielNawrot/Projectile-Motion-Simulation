import pygame
from Particle import Particle
from Box import Box

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 60

p = Particle(400, 400, 100, 100, 0, -981, 10, 0.8)
box = Box(10, 790, 10, 790)

mouseDown = None
mouseUp = None

def start():
    pygame.draw.rect(screen, "white", (box.left, box.top, (box.right - box.left), (box.bottom - box.top)), 2)

def update(dt):
    p.vx = p.vx + p.ax * dt
    p.vy = p.vy + -p.ay * dt
    p.px = p.px + p.vx * dt
    p.py = p.py + p.vy * dt
    handleBoxCollisions()

def handleBoxCollisions():
    if p.px - p.radius <= box.left or p.px + p.radius >= box.right:
        p.vx = -p.vx * 0.9
    if p.py + p.radius >= box.bottom or p.py - p.radius <= box.top:
        p.vy = -p.vy * p.elasticity

    if p.py + p.radius >= box.bottom:
        p.py = box.bottom - p.radius
        p.vx *= 0.97 # drag
    if p.py - p.radius <= box.top:
        p.py = box.top + p.radius
    if p.px - p.radius <= box.left:
        p.px = box.left + p.radius
    if p.px + p.radius >= box.right:
        p.px = box.right - p.radius

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            mouseUp = pygame.mouse.get_pos()
            vecX = mouseUp[0] - mouseDown[0]
            vecY = mouseUp[1] - mouseDown[1]
            p.vx += vecX
            p.vy += vecY


    screen.fill("black")

    #Processing
    start()
    update(1 / FPS)
    pygame.draw.circle(screen, "white", (p.px, p.py), p.radius, 2)
    
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()