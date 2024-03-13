import pygame as p
import math as m
import random
WIDTH = random.randint(1200,1200)
HEIGHT = random.randint(600,600)
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (20, 180, 20)
BLUE = (0, 0, 255)
PINK = (251,82,255)

p.init()
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("ball")
clock = p.time.Clock()
run = True

class ball:
  def __init__(self,c):
    self.c=c
    self.x=random.randint(2,WIDTH-2)
    self.y=random.randint(2,HEIGHT-2)
    self.velo = 2
    self.angle = random.randint(1,360)
    self.xv = self.velo * m.cos(m.radians(self.angle)) 
    self.yv = self.velo * m.sin(m.radians(self.angle))
    self.r=1

  def update(self):
    if self.x+self.xv > WIDTH-self.r or self.x+self.xv < self.r:
      self.angle = 180 - self.angle
      self.velo+=1
      self.r+=1
    if self.y+self.yv > HEIGHT-self.r or self.y+self.yv < self.r:
      self.angle = 360 - self.angle
      self.velo+=1
      self.r+=1
    self.xv = self.velo * m.cos(m.radians(self.angle)) 
    self.yv = self.velo * m.sin(m.radians(self.angle))
    self.x+=self.xv
    self.y+=self.yv
    p.draw.circle(surface=screen,radius=self.r,color=(self.c),center=(self.x,self.y))

bals=[]
for i in range(100):
  bals.append(ball((random.randint(0,255),random.randint(0,255),random.randint(0,255))))
while run:
  clock.tick(FPS)
  for event in p.event.get():
    if event.type == p.QUIT:
      p.quit()
      quit()
  screen.fill(BLACK)
  for i in bals:
    if i.r>100:
      bals.pop(bals.index(i))
    i.update()
  if len(bals)==0:
    run=False
  p.display.update()


