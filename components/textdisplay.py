import components.GameState as GameState
import pygame

def textdisplay(screen, clock):
	font = pygame.font.SysFont(None, 30)
	img = font.render(str(clock.get_fps()), True, "white")
	screen.blit(img, (10, 10))