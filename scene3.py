import pygame, scene2
from settings import *


def main(screen, points, broken_egg):
	running = True
	font = pygame.font.Font(None, 50)
	replay_button = pygame.Rect(160, 280, 180, 126)
	replay_button_sprite = replay_button_sprites[0]
	while running:
		mouse_pos = pygame.mouse.get_pos()
		not_clicked_place = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
		if not_clicked_place.colliderect(replay_button):
			replay_button_sprite = replay_button_sprites[1]
		else:
			replay_button_sprite = replay_button_sprites[0]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

			# (193, 197)
			# (209, 222)
			if event.type == pygame.MOUSEBUTTONDOWN:
				print(mouse_pos)
				clicked_place = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
				if clicked_place.colliderect(replay_button):
					return True
		Points = font.render(str(points), 1, WHITE)
		eggs = font.render(str(int((points / (points + len(broken_egg)) * 100))) + "%", 1, WHITE)

		screen.blit(lose_window_sprite, (260 - lose_window_sprite.get_width() // 2, 300 - lose_window_sprite.get_height() // 2))
		screen.blit(replay_button_sprite,(160, 280))
		screen.blit(Points, (231, 180))
		screen.blit(eggs, (209, 225))
		pygame.display.update()

