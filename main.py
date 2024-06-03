import pygame
import components.game as game
from components.judgement import judgement
from components.GameDisplay import GameDisplay
import components.GameState as GameState
from components.variables import  HEIGHT, WIDTH, NOTE_WIDTH
from components.keyHandler import keyHandler
from components.textdisplay import textdisplay
from pygame.locals import *
flags = DOUBLEBUF
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
clock = pygame.time.Clock()
running = 1
bgpath = GameState.bmsfile['info']['back_image']
BG = pygame.image.load(f'test/{bgpath}').convert()
BG = pygame.transform.scale(BG, (screen.get_width(), screen.get_height()))
BG.set_alpha(200)
dt = 0
time = 0

while running:
	screen.fill('black')
	screen.blit(BG, (0, 0))
	rect = pygame.Rect(0, 0, NOTE_WIDTH*8, HEIGHT)
	pygame.draw.rect(screen, pygame.Color(0,0,0, 150), rect)
	keyHandler()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0
	
	if GameState.playing :
		time += dt
	# time = pygame.mixer.music.get_pos()
	game.rendergame(screen, time)
	judgement(screen, time)
	GameDisplay(screen)
	textdisplay(screen, clock)
	pygame.display.flip()
	dt = clock.tick(120)

pygame.quit()