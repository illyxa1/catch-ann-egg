import  pygame
from settings import *
from modules import *
from random import randint, choice

pygame.init()

def main(screen):
	grownd = Grownd(screen, 500, WHITE, 1)
	end_game = False
	max_count = randint(100, 500)
	# player = Object(player_sprite, (100, 340), screen, (0, size[0], 0, size[1]))
	# player.create_hitbox((0, 150), (10, 120))
	# player's body parts
	points = 0
	all_points = 0
	player_x = 200
	player_y = 270
	
	hat = Object(hat_sprite, (player_x, player_y), screen, (0, size[0], 0, size[1]))
	body = Object(body_sprite, (player_x + 10, player_y + 68), screen, (0, size[0], 0, size[1]))
	left_leg = Object(leg_sprite, (player_x + 30, player_y + 156), screen, (0, size[0], 0, size[1]))
	right_leg = Object(leg_sprite, (player_x + 65, player_y + 168), screen, (0, size[0], 0, size[1]))
	player_bin = Object(player_bin_sprite, (player_x, player_y + 137), screen, (0, size[0], 0, size[1]))
	player_bin.create_hitbox((0, 0), (100, 30))
	player_legs_move = 0
	iterator = 1

	egg = Object(egg_sprite, (100, 0), screen, (0, size[0], 0, size[1]))
	egg.create_hitbox((0, 0), "end")
	egg.type = "egg"
	egg.deat_body = broken_egg_sprite
	broken_eggs = []
	a=0

	stone = Object(stone_sprite, (100, 0), screen, (0, size[0], 0, size[1]))
	stone.create_hitbox((0, 0), "end")
	stone.type = "stone"
	stone.deat_body = stone_sprite

	falling_objects = [egg, stone]
	falling_object = choice(falling_objects)

	font = pygame.font.Font("fonts/Phenomena-Black.ttf", 50)
	# pygame.mixer.music.load("music/music.mp3")
	# pygame.mixer.music.play(-1)

	while not end_game: 
		last_hat_x = hat.pos_x
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		keys = pygame.key.get_pressed()
		hat.move(pressed=keys, key_right = pygame.K_RIGHT, key_left = pygame.K_LEFT, iteration_x=10)
		
		player_bin.pos_x = hat.pos_x + 10
		body.pos_x = hat.pos_x + 10
		left_leg.pos_x = hat.pos_x + 30
		right_leg.pos_x = hat.pos_x + 65
		if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
			left_leg.pos_y += player_legs_move
			right_leg.pos_y -= player_legs_move
			player_bin.pos_y += player_legs_move


			if player_legs_move == 6 or player_legs_move == -6:
				iterator *= -1
			player_legs_move += iterator * 2

		falling_object.free_movement(y=a)
		a += 1
		if falling_object.HITBOX.colliderect(player_bin.HITBOX):
			if falling_object.type == "stone":
				all_points += points
				points = 0
			else:
				points += 1
				catch_egg.play()

		if falling_object.HITBOX.colliderect(grownd.HITBOX):
			broken_eggs.append((falling_object.pos_x, falling_object.pos_y, falling_object.type, falling_object.deat_body))

		if all_points + len(broken_eggs) + points== max_count:
			end_game = True
			return (points, broken_eggs)

		if falling_object.HITBOX.colliderect(player_bin.HITBOX) or falling_object.HITBOX.colliderect(grownd.HITBOX):
			a = 1
			falling_object.free_movement(y=-500)
			falling_object.pos_x = randint(0, 450)
			falling_object = choice(falling_objects)

		Points = font.render(str(points), 1, WHITE)



		#screen.fill(BLACK)
		screen.blit(bg, (0, 0))
		for i in broken_eggs:
			screen.blit(i[3], (i[0], i[1]))
		# player.draw(1)
		left_leg.draw()
		right_leg.draw()
		body.draw()
		hat.draw()
		player_bin.draw(1)
		falling_object.draw(1)
		screen.blit(Points, (250, 10))

		
		clock.tick(FPS)
		pygame.display.update()

