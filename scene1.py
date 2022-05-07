import pygame
from settings import *


def main(screen):
	running = True
	play_button_sprite = play_button_sprites[0]
	play_button = pygame.Rect(320, 430, 150, 70)
	while running:
		mouse_pos = pygame.mouse.get_pos()
		not_clicked_place = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
		if not_clicked_place.colliderect(play_button):
			play_button_sprite = play_button_sprites[1]

		else:
			play_button_sprite = play_button_sprites[0]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				print(mouse_pos)
				clicked_place = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
				if clicked_place.colliderect(play_button):
					play_button_sprite = play_button_sprites[2]
					running = False

		screen.blit(menu_sprite, (0, 0))
		screen.blit(play_button_sprite, (320, 430))
		pygame.display.update()