import pygame
import components.GameState as GameState

keytranslator = {
	pygame.K_a : 7,
	pygame.K_q : 7,
	pygame.K_s : 0,
	pygame.K_e : 1,
	pygame.K_d : 2,
	pygame.K_KP_4 : 3,
	pygame.K_KP_0 : 4,
	pygame.K_KP_5 : 5,
	pygame.K_KP_3 : 6,
}

keybinds = [
	pygame.K_a,
	pygame.K_q,
	pygame.K_s,
	pygame.K_e,
	pygame.K_d,
	pygame.K_KP_4,
	pygame.K_KP_0,
	pygame.K_KP_5,
	pygame.K_KP_3,
]

# 0 : released
# 1 : pressed
# 2 : repeat/hold

def keyHandler():   
	# keys = pygame.key.get_pressed()
	# for key in keybinds:
	# 	if (keys[key]):
	# 		if (GameState.pressed[keytranslator[key]] == 0):
	# 			GameState.pressed[keytranslator[key]] = 1
	# 		else:
	# 			GameState.pressed[keytranslator[key]] = 2
	# 	else:
	# 		GameState.pressed[keytranslator[key]] = 0
			
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			try:
				# if (GameState.pressed[keytranslator[event.key]] == 0):
				GameState.pressed[keytranslator[event.key]] = 1
			except:
				continue
		if event.type == pygame.KEYUP:
			try:
				GameState.pressed[keytranslator[event.key]] = 0
			except:
				continue