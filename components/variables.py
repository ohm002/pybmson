config = open("config.txt", encoding="utf-8").read().splitlines()
WIDTH =	float(config[3])
HEIGHT = float(config[4])
NOTE_HEIGHT = int(HEIGHT * float(config[0]))
NOTE_WIDTH = int(WIDTH * float(config[1]))
JUDGEMENTY_DIFF = int(HEIGHT * float(config[2]))
SUBNOTEWIDTH = round(NOTE_WIDTH/3) + 1
KEYBEAMHEIGHT = JUDGEMENTY_DIFF * 5