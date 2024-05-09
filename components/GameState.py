import json
import re
import sounddevice as sd
import numpy as np
import pygame
from pydub import AudioSegment
pygame.init()
config = open("config.txt", encoding="utf-8").read().splitlines()
WIDTH =	float(config[3])
HEIGHT = float(config[4])
NOTE_WIDTH = int(WIDTH * float(config[1]))
NOTE_HEIGHT = int(HEIGHT * float(config[0]))
JUDGEMENTY_DIFF = int(HEIGHT * float(config[2]))
OFFSET = int(float(config[6]))
bmsfile = json.loads(open("bms.bmson", encoding="utf-8").read())
playing = False
objlist = []
i = 0

def play_from_raw(w):
	audio_array = np.array(w.get_array_of_samples())
	w.export('test.wav', format="wav")
	sd.play(audio_array, samplerate=w.frame_rate)
	sd.wait()

# def trim_audio(input_file_path, time, end):
# 	# load the audio file
# 	audio = AudioSegment.from_ogg(input_file_path)
# 	# audio.
# 	# return audio
# 	if (end != None):
# 		return audio[time:end]
# 	else:
# 		return audio[time:]
	
def trim_audio(input_file_path):
	# load the audio file
	audio = AudioSegment.from_ogg(input_file_path)
	# audio.
	return audio
	# if (end != None):
	# 	return audio[time:end]
	# else:
	# 	return audio[time:]

def trim_audio2(audio_segment, start_ms, end_ms):
	"""
	Trim an audio segment.

	Args:
		audio_segment (AudioSegment): The input audio segment.
		start_ms (int): Start time of the trim (in milliseconds).
		end_ms (int): End time of the trim (in milliseconds).

	Returns:
		AudioSegment: Trimmed audio segment.
	"""
	if (end_ms != None):
		return audio_segment[start_ms:end_ms]
	else:
		return audio_segment[start_ms:]


sound = bmsfile['sound_channels'][0]['name']
# sound = sound['name']
sound = re.sub("wav", "ogg", sound)
file = f'test/{sound}'
print(f'loading {sound}')
combined = trim_audio(file)
# play(combined)
w = 0
audio_segments = []
import threading

def loadsoundchannel(soundd):
	sound = re.sub("wav", "ogg", soundd)
	file = f'test/{sound}'
	print(f"loading {sound}")
	audio_segments.append({
		"name" : soundd ,
		"sound" : pygame.mixer.Sound(file)})

for soundd in bmsfile['sound_channels']:
	thread = threading.Thread(target=loadsoundchannel, args=(soundd['name'],))
	thread.start()
			# thread = threading.Thread(target=trim_and_append, args=(sound, time, nexttime, channel['name'], note['x'],))

playing = True

pygame.mixer.set_num_channels(len(bmsfile['sound_channels']))
# pygame.mixer.init()
# pygame.mixer.music.load((f'out.mp3'))
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.pause()
# import concurrent.futures

def trim_and_append(sound, time, nexttime, name, x):
	# print(f"rendering {sound} | {time} to {nexttime}")
	# spriteaudio = trim_audio2(AudioSegment.from_ogg(f'test/{sound}'), (time), (nexttime))
	objlist.append({
		'channel': name,
		'lane': x,
		'time': time,
		'hit' : -1,
		# 'sprite': spriteaudio
	})
	# print('loaded : ', len(objlist), ' out of ', targetobjlength)
def renderspritenotes(channel):
	# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
	i = 0
	for note in channel['notes']:
		time = (((note['y'] / bmsfile['info']['resolution'])) - 4) * ((60000 / bmsfile['info']['init_bpm']))
		try:
			nexttime = (((channel['notes'][i+1]['y'] / bmsfile['info']['resolution'])) - 4) * ((60000 / bmsfile['info']['init_bpm']))
			# print(channel['notes'][i2+1]['y'])
		except:
			nexttime = None
		# if (i3 == 5):
		sound = channel['name']
		sound = re.sub("wav", "ogg", channel['name'])
		# trim_and_append(sound, time, nexttime)
		trim_and_append(sound, time, nexttime, channel['name'], note['x'])
		# thread = threading.Thread(target=trim_and_append, args=(sound, time, nexttime, channel['name'], note['x'],))
		# thread.start()
		i += 1

			

targetobjlength = 0
worklist = []

for channel in bmsfile['sound_channels']:
	targetobjlength += len(channel['notes'])
for channel in bmsfile['sound_channels']:
	sorted = channel['notes'].sort(key=lambda a : a['y'])
	worklist.append(threading.Thread(target=renderspritenotes, args=(channel,)))

for work in worklist:
	work.start()


print(targetobjlength)

i2 = 0
linelist = []
for note in bmsfile['lines']:
	time = (((note['y'] / bmsfile['info']['resolution'])) - 4) * ((60000 / bmsfile['info']['init_bpm']))
	try:
		nexttime = (channel['notes'][i2+1]['y'] / bmsfile['info']['resolution']) * (60000 / bmsfile['info']['init_bpm'])
	except:
		nexttime = None
	sound = channel['name']
	sound = re.sub("wav", "ogg", channel['name'])
	linelist.append({
		'time': time,
		'hit' : -1,
	})
	i+=1
	i2+=1
	

renderedaudio = 0
# while not playing:
# 	# print(len(objlist))
# 	if (renderedaudio != len(objlist)):
# 		renderedaudio = len(objlist)
# 		print('loaded : ', len(objlist), ' out of ', targetobjlength)
# 	playing = targetobjlength == renderedaudio

while not playing:
	# print(len(objlist))
	if (renderedaudio != len(audio_segments)):
		renderedaudio = len(audio_segments)
		print('loaded : ', len(objlist), ' out of ', len(bmsfile['sound_channels']))
	playing = bmsfile['sound_channels'] == renderedaudio

pygame.time.wait(1000)
for segment in audio_segments:
	segment['sound'].play()
# playing = True

i = 0
for obj in objlist:
	obj['id'] = i
	i += 1

def chart():
	return objlist

pressed = [0,0,0,0,0,0,0,0]
pressed2 = [0,0,0,0,0,0,0,0]
score = 0
combo = 0
judge = 'poor'