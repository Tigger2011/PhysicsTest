
import pygame
import pymunk.pygame_util
import math
from sys import exit
import pymunk
import random


class ParticlesP:
    def __init__(self):
        self.particles = []
    def emit(self):
        if self.particles:
            self.deleteparticles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= +0.15
                pygame.draw.circle(screen,pygame.Color("Black"),particle[0], int(particle[1]))
    def addparticles(self):
        posx = pygame.mouse.get_pos()[0]
        posy = pygame.mouse.get_pos()[1]
        rad = 10
        directionx = random.randint(-3,3)
        directiony = random.randint(-3, 3)
        particle_circle = [[posx,posy], rad,[directionx, directiony]]
        self.particles.append(particle_circle)
    def deleteparticles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy
def create_ball(space,pos):
    body = pymunk.Body(1,100, body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,40)
    space.add(body,shape)
    return shape
def draw_ball(balls):
    for ball in balls:
        global posx
        posx = int(ball.body.position.x)
        global posy
        posy = int(ball.body.position.y)

        pygame.draw.circle(screen,(0,0,0),(posx,posy),40)


def static_ball(space):
    body = pymunk.Body(body_type= pymunk.Body.STATIC)
    body.position = (350,400)
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape
def draw_static_ball(static_balls):
    for static_ball in static_balls:
        posx= int(static_ball.body.position.x)
        posy=int(static_ball.body.position.y)


        pygame.draw.circle(screen,(0,0,0),(posx,posy),50)



pygame.init()
screen= pygame.display.set_mode((800,600))


pygame.display.set_caption("Ball game!")
clock = pygame.time.Clock()
gravx = 0
gravpower = 915
space = pymunk.Space()
space.gravity = (gravx,gravpower)


balls = []
balls.append(create_ball(space,pos=(0,410)))

static_balls = []
static_balls.append(static_ball(space))
particle1 = ParticlesP()
particleEvent = pygame.USEREVENT + 1
pygame.time.set_timer(particleEvent,150)
gameRunning = True

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == particleEvent:
            particle1.addparticles()
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(create_ball(space,event.pos))


    screen.fill((255, 255, 255))
    particle1.emit()
    draw_ball(balls)
    draw_static_ball(static_balls)
    space.step(1/50)

    pygame.display.update()

    clock.tick(120)


