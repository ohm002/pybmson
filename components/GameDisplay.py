import pygame
from components.variables import NOTE_WIDTH, HEIGHT, JUDGEMENTY_DIFF, NOTE_HEIGHT

def GameDisplay(screen):
	rect = pygame.Rect(0, 0, NOTE_WIDTH*8, HEIGHT)
	pygame.draw.rect(screen, pygame.Color(0,0,0), rect)
	linepos = pygame.Vector2(0, screen.get_height() - JUDGEMENTY_DIFF - NOTE_HEIGHT /2)
	linepos2 = pygame.Vector2(NOTE_WIDTH*8, screen.get_height() - JUDGEMENTY_DIFF - NOTE_HEIGHT /2)
	pygame.draw.line(screen, 'green', linepos, linepos2, NOTE_HEIGHT)