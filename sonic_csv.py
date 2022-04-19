import retro
import pygame
from pygame.locals import *
import cv2
import numpy as np
import imutils
import imageio
import base64
import IPython
import csv 

import pandas as pd

video_size = 700, 500
video_filename = "SONIC.mp4"


def key_action():
    #["B", "A", "MODE", "START", "UP", "DOWN", "LEFT", "RIGHT", "C", "Y", "X", "Z"]
    buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        buttons[6] = 1
    if keys[K_UP]:
        buttons[0] = 1
    if keys[K_RIGHT]:
        buttons[7] = 1
    if keys[K_DOWN]:
        buttons[5] = 1
    return buttons

pygame.init()
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
screen = pygame.display.set_mode(video_size)
env.reset()

done = False
clock = pygame.time.Clock()
#archivo
csvfile = open('record.csv','a', newline='', encoding='utf8')
names = ['row', 'action', 'reward']
writer = csv.DictWriter(csvfile, fieldnames=names)
cont=0	


with imageio.get_writer(video_filename, fps=60) as video:
 while not done:
    clock.tick(60) 
    img = env.render(mode='rgb_array') 
    img = np.flipud(np.rot90(img))
    image_np = imutils.resize(img, width=500) 
    surf = pygame.surfarray.make_surface(image_np)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    video.append_data(env.render(mode='rgb_array'))
    action = key_action()
    ob, rew, done, info = env.step(action)
    pygame.event.pump()
    print("Action ", action, "Reward ", rew)
    cont=cont+1
    writer.writerow({'row': cont, 'action': action, 'reward': rew})



def embed_mp4(filename):
  """Embeds an mp4 file in the notebook."""
  video = open(filename,'rb').read()
  b64 = base64.b64encode(video)
  tag = '''
  <video width="640" height="480" controls>
    <source src="data:video/mp4;base64,{0}" type="video/mp4">
  Your browser does not support the video tag.
  </video>'''.format(b64.decode())

  return IPython.display.HTML(tag)


embed_mp4(video_filename)
