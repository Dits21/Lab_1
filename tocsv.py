import retro
import pygame
from pygame.locals import *
import cv2
import numpy as np
import imutils
import csv

import pandas as pd

video_size = 700, 500

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
csvfile = open('record.csv','w', newline='', encoding='utf8')
fieldnames = ['row', 'action', 'reward']
writer = csv.DictWriter(csvfile, fieldnames)
	
writer.writeheader()
cont=0
while not done:
    clock.tick(60)
    img = env.render(mode='rgb_array')
    img = np.flipud(np.rot90(img))# La rotamos
    image_np = imutils.resize(img, width=500)
    surf = pygame.surfarray.make_surface(image_np)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    action = key_action()
    ob, rew, done, info = env.step(action)
    pygame.event.pump()## Escucha los eventos
    print("Action ", action, "Reward ", rew)
    cont=cont+1
    writer.writerow({'row': cont, 'action': action, 'reward': rew})	

#    matriz = np.append(matriz, [action], rew)
	
#print(matriz)
#botones = pd.DataFrame(matriz)
#botones.to_csv('botones1.csv')