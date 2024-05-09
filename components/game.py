import pygame
import components.GameState as GameState
config = open("config.txt", encoding="utf-8").read().splitlines()
def interpolate(input, inputMin, inputMax, outputMin, outputMax):
	return ((input - inputMin) / (inputMax - inputMin)) * (outputMax - outputMin) + outputMin

def visiblefunc(a, time):
	return int(a['time'])-SPEED <= time and int(a['time']) + 1000 >= time and a['hit'] == -1


WIDTH =	float(config[3])
HEIGHT = float(config[4])
NOTE_WIDTH = int(WIDTH * float(config[1]))
NOTE_HEIGHT = int(HEIGHT * float(config[0]))
JUDGEMENTY_DIFF = int(HEIGHT * float(config[2]))
SPEED = int(float(config[5]))
switch = {
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0,
	'6': 0,
	'7': 0,
	'8': 0,
}
switch2 = {
	1: 'white',
	2: 'blue',
	3: 'white',
	4: 'blue',
	5: 'white',
	6: 'blue',
	7: 'white',
	8: 'red',
}



def rendergame(screen, time):
	visibleobjects = filter(lambda obj: visiblefunc(obj, time), GameState.objlist)
	visiblelines = filter(lambda obj: visiblefunc(obj, time), GameState.linelist)
	for line in visiblelines:
		starttime = line['time']
		y = interpolate(time, starttime-SPEED, starttime, 0, (HEIGHT-JUDGEMENTY_DIFF))- NOTE_HEIGHT
		rect = pygame.Rect(0, y, NOTE_WIDTH*8, 2)
		pygame.draw.rect(screen, 'white', rect)
	for note in visibleobjects:
		if (note['lane'] != 0):
			column = note['lane']
			if (note['lane'] != 8):
				column+=1
			else:
				column = 1
			starttime = note['time']
			y = interpolate(time, starttime-SPEED, starttime, 0, (HEIGHT-JUDGEMENTY_DIFF))- NOTE_HEIGHT*2
			# print(y, time)
			if (time > note['time'] + 400):
				GameState.judge = 'miss'
				note['hit'] == time
				GameState.combo = 0
			# currentobjindexList[i] += 1
				for segment in GameState.audio_segments:
					if (segment['name'] == note['channel']):
						segment['sound'].set_volume(0)
			x = 0 + (column - 1) * NOTE_WIDTH
			rect = pygame.Rect(x, y, NOTE_WIDTH, NOTE_HEIGHT)
			
			pygame.draw.rect(screen, switch2[note['lane']], rect)