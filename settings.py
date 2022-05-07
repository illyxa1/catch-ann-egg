import pygame
pygame.init()

size = (500, 600)
clock = pygame.time.Clock()
FPS = 60
icon = pygame.image.load("sprites/icon.png")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
bg = pygame.image.load("sprites/bear/bg.png")

#player
leg_sprite = pygame.image.load("sprites/bear/leg.png")
hat_sprite = pygame.image.load("sprites/bear/hat.png")
body_sprite = pygame.image.load("sprites/bear/body.png")
player_bin_sprite = pygame.image.load("sprites/bear/bin.png")

# egg
egg_sprite = pygame.image.load("sprites/egg.png")
catch_egg = pygame.mixer.Sound('sounds/catch egg.wav')
broken_egg_sprite = pygame.image.load("sprites/broken egg.png")

# stone
stone_sprite = pygame.image.load("sprites/bear/stone.png")

# menu
menu_sprite = pygame.image.load("sprites/bear/menu.png")
play_button_sprites = [pygame.image.load("sprites/bear/playbutton.png"),
					   pygame.image.load("sprites/bear/playbutton2.png"),
					   pygame.image.load("sprites/bear/playbutton3.png")]

# lose window
lose_window_sprite = pygame.image.load("sprites/bear/micro window.png")
replay_button_sprites = [pygame.image.load("sprites/bear/replay button.png"),
						pygame.image.load("sprites/bear/replay button2.png")]