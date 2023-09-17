
# I have done an online course and got a certificate "https://olympus.mygreatlearning.com/courses/64364/certificate"

import pygame
import sys
from pygame.locals import *

pygame.init()
display_window = pygame.display.set_mode((800, 500))

pygame.display.set_caption(
    "My Game").display.pygame.display.set_caption("Hello World!")

while True:
    for each_event in pygame.event.get():
        if each_event.type == QUIT:
            sys.exit()
            pygame.display.update()
