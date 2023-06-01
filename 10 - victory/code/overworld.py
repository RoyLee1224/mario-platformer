import pygame 
from game_data import levels
from support import import_folder
from decoration import Sky

class Node(pygame.sprite.Sprite):
	def __init__(self,pos,status,icon_speed,path):
		super().__init__()
		self.frames = import_folder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		if status == 'available':
			self.status = 'available'
		else:
			self.status = 'locked'
		self.rect = self.image.get_rect(center = pos)

		self.detection_zone = pygame.Rect(self.rect.centerx-(icon_speed/2),self.rect.centery-(icon_speed/2),icon_speed,icon_speed)

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self):
		if self.status == 'available':
			self.animate()
		else:
			tint_surf = self.image.copy()
			tint_surf.fill('black',None,pygame.BLEND_RGBA_MULT)
			self.image.blit(tint_surf,(0,0))

class Icon(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.pos = pos
		self.image = pygame.image.load('../graphics/overworld/hat.png').convert_alpha()
		self.rect = self.image.get_rect(center = pos)

	def update(self):
		self.rect.center = self.pos

class Overworld:
	def __init__(self,start_level,max_level,surface,create_level):

		# setup 
		self.display_surface = surface 
		self.max_level = max_level
		self.current_level = start_level
		self.create_level = create_level

		# movement logic
		self.moving = False
		self.move_direction = pygame.math.Vector2(0,0)
		self.speed = 8

		# sprites 
		self.setup_nodes()
		self.setup_icon()
		self.sky = Sky(8,'overworld')

		# time 
		self.start_time = pygame.time.get_ticks()
		self.allow_input = False
		self.timer_length = 300

		self.font = pygame.font.Font('../graphics/ui/ARCADEPI.ttf', 20)
		self.text_color = (255, 255, 255)
		self.text1 = 'Press left and right arrows to control'
		self.text2 = 'Press space to start'
		self.text1_pos = (self.display_surface.get_width() - 10, self.display_surface.get_height() - 40)  # Adjust Y position
		self.text2_pos = (self.display_surface.get_width() - 10, self.display_surface.get_height() - 10)  # Adjust Y position

		# add an opacity attribute for the breath effect
		self.opacity = 0
		self.opacity_change = 1


	def setup_nodes(self):
		self.nodes = pygame.sprite.Group()

		for index, node_data in enumerate(levels.values()):
			if index <= self.max_level:
				node_sprite = Node(node_data['node_pos'],'available',self.speed,node_data['node_graphics'])
			else:
				node_sprite = Node(node_data['node_pos'],'locked',self.speed,node_data['node_graphics'])
			self.nodes.add(node_sprite)

	def draw_paths(self):
		if self.max_level > 0:
			points = [node['node_pos'] for index,node in enumerate(levels.values()) if index <= self.max_level]
			pygame.draw.lines(self.display_surface,'#a04f45',False,points,6)

	def setup_icon(self):
		self.icon = pygame.sprite.GroupSingle()
		icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
		self.icon.add(icon_sprite)

	def input(self):
		keys = pygame.key.get_pressed()

		if not self.moving and self.allow_input:
			if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
				self.move_direction = self.get_movement_data('next')
				self.current_level += 1
				self.moving = True
			elif keys[pygame.K_LEFT] and self.current_level > 0:
				self.move_direction = self.get_movement_data('previous')
				self.current_level -= 1
				self.moving = True
			elif keys[pygame.K_SPACE]:
				self.create_level(self.current_level)

	def get_movement_data(self,target):
		start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
		
		if target == 'next': 
			end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
		else:
			end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

		return (end - start).normalize()

	def update_icon_pos(self):
		if self.moving and self.move_direction:
			self.icon.sprite.pos += self.move_direction * self.speed
			target_node = self.nodes.sprites()[self.current_level]
			if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
				self.moving = False
				self.move_direction = pygame.math.Vector2(0,0)

	def input_timer(self):
		if not self.allow_input:
			current_time = pygame.time.get_ticks()
			if current_time - self.start_time >= self.timer_length:
				self.allow_input = True

	import math

	def draw_text(self):
		self.opacity += 5 * self.opacity_change
		if self.opacity > 255 or self.opacity < 0:
			self.opacity_change *= -1

		text_color = (int(self.opacity), int(self.opacity), int(self.opacity), 255)

		text1_surface = self.font.render(self.text1, True, text_color)
		text1_rect = text1_surface.get_rect(bottomright=self.text1_pos)
		self.display_surface.blit(text1_surface, text1_rect)

		text2_surface = self.font.render(self.text2, True, text_color)
		text2_rect = text2_surface.get_rect(bottomright=self.text2_pos)
		self.display_surface.blit(text2_surface, text2_rect)

	def run(self):
		self.input_timer()
		self.input()
		self.update_icon_pos()
		self.icon.update()
		self.nodes.update()

		self.sky.draw(self.display_surface)
		self.draw_paths()
		self.nodes.draw(self.display_surface)
		self.icon.draw(self.display_surface)

		self.text1_pos = (self.display_surface.get_width() - 10, self.display_surface.get_height() - 40)
		self.text2_pos = (self.display_surface.get_width() - 10, self.display_surface.get_height() - 10)
		self.draw_text()