import pygame

class Grownd:
	def __init__(self, surf, w, color, hitbox=0):
		self.w = w
		self.h = 100
		self.color = color
		self.screen = surf
		if hitbox:
			self.HITBOX = pygame.Rect(0, 500, w, 10)

	def draw(self, hitbox=0):
		pygame.draw.rect(self.screen, self.color, (0, 600 - self.h, self.w, self.h))
		if hitbox:
			pygame.draw.rect(self.screen, (0, 255, 0), (0, 500, self.w, 10), 1)
class Object:
	def __init__(self, sprite, pos, surf, screen_border):
		# sceen_border = (x_left, x_right, y_bottom, y_down)
		self.sprite = sprite
		self.pos_x, self.pos_y = pos[0], pos[1]
		self.screen = surf
		self.screen_border = screen_border
		self.sprite_rect = (sprite.get_width(), sprite.get_height())
		self.hitdox_created = False

	def create_hitbox(self, hitbox_pos, hitbox_size):		
		# положение относительно размера спрайта 
		if hitbox_pos == "center":
			self.hitbox_pos = (self.sprite.get_height() // 2, self.sprite.get_width() // 2)
		
		elif hitbox_pos[0] == "center":
			self.hitbox_pos = (self.sprite.get_width() // 2, hitbox_pos[1])
		
		elif hitbox_pos[1] == "center":
			self.hitbox_pos = (hitbox_pos[0], self.sprite.get_height() // 2)
		
		else:
			self.hitbox_pos = hitbox_pos

		# размер
		if hitbox_size == "end":
			self.hitbox_size = (self.sprite.get_height(), self.sprite.get_width())

		elif hitbox_size[0] == "end":
			self.hitbox_size = (self.sprite.get_width(), hitbox_size[1])

		elif hitbox_size[1] == "end":
			self.hitbox_size = (hitbox_size[0], self.sprite.get_height())

		else:
			self.hitbox_size = hitbox_size

		# создание аттрибута класса pygame.Rect()
		self.HITBOX = pygame.Rect(self.hitbox_pos[0] + self.pos_x, self.hitbox_pos[1] + self.pos_y, self.hitbox_size[0], self.hitbox_size[1]) 

	def draw(self, hitbox_created=False, draw_hitbox=False):
		self.screen.blit(self.sprite, (self.pos_x, self.pos_y))
		# просто для удобства рисование хит бокса
		if draw_hitbox:
			pygame.draw.rect(self.screen, (0, 255, 0), (self.hitbox_pos[0] + self.pos_x, self.hitbox_pos[1] + self.pos_y, self.hitbox_size[0], self.hitbox_size[1]), 3)
		# обновляем хитбокс
		if hitbox_created:
			self.HITBOX = pygame.Rect(self.hitbox_pos[0] + self.pos_x, self.hitbox_pos[1] + self.pos_y, self.hitbox_size[0], self.hitbox_size[1]) 

	def move(self,  pressed, key_right = None, key_left = None, key_up = None, key_down = None, iteration_x = None, iteration_y = None, direction = 1):
		if key_right and pressed[key_right] and self.pos_x + self.sprite_rect[0] < self.screen_border[1]:
			self.pos_x += iteration_x * direction


		if key_left and pressed[key_left] and self.pos_x > self.screen_border[0]:
			self.pos_x -= iteration_x * direction


		if key_down and pressed[key_down] and self.pos_y > self.screen_border[3]:
			self.pos_y += iteration_y * direction


		if key_up and pressed[key_up] and self.pos_y < self.screen_border[2]:
			self.pos_y -= iteration_y * direction

	def collide(self, 


		object):
		if self.HITBOX.colliderect(object.HITBOX):
			return True

		return 0


	def free_movement(self, x=0, y=0):
		self.pos_y += y
		self.pos_x += x