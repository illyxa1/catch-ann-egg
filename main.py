import pygame
from settings import *
import scene1, scene2, scene3

screen = pygame.display.set_mode(size)
pygame.display.set_icon(icon)
pygame.display.set_caption("catch an egg")
replay = False

while True:
	if not replay:
		scene1.main(screen)
	fact = scene2.main(screen)
	replay = scene3.main(screen, fact[0], fact[1])