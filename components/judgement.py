import components.GameState as GameState
from components.judgementDisplayer import judgementDisplayer
import pygame
from components.variables import NOTE_WIDTH, KEYBEAMHEIGHT, JUDGEMENTY_DIFF

def getclosestnote(n, time, key):
	return key == n['lane'] and n['hit'] == -1 and time >= n['time'] - 200 and time <= n['time'] + 200

def sorta(n):
	return n['time']

KEYBEAM = pygame.image.load('hit.png')
KEYBEAM = pygame.transform.scale(KEYBEAM, (NOTE_WIDTH, KEYBEAMHEIGHT))
# currentobjindexList = [0,0,0,0,0,0,0,0]

def judgecol(screen, time, i):
	# currentobjindex = currentobjindexList[i]
	hitobjlist = list(filter(lambda note : getclosestnote(note, time, i+1), GameState.objlist))
	hitobjlist.sort(key=sorta)
	if (len(hitobjlist) > 0):
		hitobj = hitobjlist[0]
		if GameState.pressed[i] == 1:
			# if (hitobj['hit'] == -1):
			# print("obj skip alert at ", i+1, '!!!')
			# if GameState.pressed[i] == 1:
			GameState.pressed[i] = 0
			offset = abs(hitobj['time'] - time) 
			# if (offset <= 200):
			# if (offset <= 18):
			GameState.judge = 'perfect'
			GameState.combo += 1
			# elif (offset <= 40):
			# 	GameState.judge = 'great'
			# 	GameState.combo += 1
			# elif (offset <= 50):
			# 	GameState.judge = 'good'
			# 	GameState.combo += 1
			# elif (offset <= 100):
			# 	GameState.judge = 'bad'
			# 	GameState.combo = 0
			# else:
			# 	GameState.judge = 'poor'
			# 	GameState.combo = 0

			for segment in GameState.audio_segments:
				if (segment['name'] == hitobj['channel']):
					# if (offset > 100):
					# 	# if (segment['sound'].get_volume() != 0):
					# 	segment['sound'].set_volume(0)
					# else:
					# 	# if (segment['sound'].get_volume() != 1):
					segment['sound'].set_volume(1)
			GameState.objlist[hitobj['id']]['hit'] = time
			# GameState.objlist.remove(hitobj)
			GameState.score += 100
			# currentobjindexList[i] += 1
			# try:
			# GameState.play_from_raw(hitobj[0]['sprite'])
			# except:
			# 	continue
		if (i != 7):
			i+=1
		else:
			i = 0
			screen.blit(KEYBEAM, (0 + NOTE_WIDTH * i, screen.get_height() - JUDGEMENTY_DIFF - KEYBEAMHEIGHT))
		


def judgement(screen, time):
	for i in range(8):
		judgecol(screen, time, i)
	judgementDisplayer(screen)