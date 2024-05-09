import pygame
import components.game as game
from components.judgement import judgement
from components.GameDisplay import GameDisplay
import components.GameState as GameState
from components.variables import  HEIGHT, WIDTH
from components.keyHandler import keyHandler
from components.textdisplay import textdisplay


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
bgpath = GameState.bmsfile['info']['back_image']
BG = pygame.image.load(f'test/{bgpath}').convert()
BG = pygame.transform.scale(BG, (screen.get_width(), screen.get_height()))
BG.set_alpha(200)
dt = 0
time = 0
while running:
	# screen.fill('black')
	screen.blit(BG, (0, 0))
	keyHandler()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	if GameState.playing :
		time += dt
	# time = pygame.mixer.music.get_pos()
	GameDisplay(screen)
	game.rendergame(screen, time)
	judgement(screen, time)
	textdisplay(screen, clock)
	pygame.display.flip()
	dt = clock.tick(120)

pygame.quit()