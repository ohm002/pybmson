import pygame
from components.variables import WIDTH
import components.GameState as GameState

judges = {
	"perfect": "GREAT",
	"great": "GREAT",
	"good": 'GOOD',
	"bad": 'BAD',
	"poor": 'POOR',
	"miss": 'MISS',
}

judgesColors = {
	"perfect": 'pink',
	"great": 'yellow',
	"good": 'green',
	"bad": 'purple',
	"poor": 'red',
	"miss": 'red',
}

font2 = pygame.font.SysFont(None, 60)
def judgementDisplayer(screen):
    # pass
	# img2 = font2.render(str(GameState.score), True, judgesColors[GameState.judge])
	img1 = font2.render(f"{judges[GameState.judge]} {GameState.combo}", True, judgesColors[GameState.judge])
	screen.blit(img1, (100, 50))
	# screen.blit(img2, (WIDTH/2, 50))