import pygame
from components.variables import NOTE_WIDTH, HEIGHT, JUDGEMENTY_DIFF, NOTE_HEIGHT

def GameDisplay(screen):
	linepos = pygame.Vector2(0, screen.get_height())
	linepos2 = pygame.Vector2(NOTE_WIDTH*8, screen.get_height())
	pygame.draw.line(screen, 'gray', linepos, linepos2, JUDGEMENTY_DIFF*2)
	linepos = pygame.Vector2(0, screen.get_height() - JUDGEMENTY_DIFF - NOTE_HEIGHT /2)
	linepos2 = pygame.Vector2(NOTE_WIDTH*8, screen.get_height() - JUDGEMENTY_DIFF - NOTE_HEIGHT /2)
	pygame.draw.line(screen, 'red', linepos, linepos2, NOTE_HEIGHT)
