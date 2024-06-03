### my ass is not going to deal with input lags in pygame thanks for watching
# pybmson
![alt text]([image-1.png](https://bluestar.s-ul.eu/o8B0fnsQ))
lazy ass dev tryna making something cool in python

---

# pls contribute
- really wonky code, please take medicine before reading whatever the fuck is going on here
- config are like this
```
note height
note width
space between judgementline and bottom of the screen
window width
window height
note speed
```
- the way "keysound" works are like guitar hero where if u miss the stems only gets muted, and that's why its **bmson exclusive** for now
- i have no idea how the fuck is the input system in pygame works, sometimes the input just drops for no reason, so all the code for the judgement system is bypassed for now, before it gets even more broken, i tried to use the "increasing objindex each column" system like what i did in my previous game in js but in python but it skips for some reason when im sure it doesn't, so i gotta reinvent a new judgement system
- bg can be enabled by uncommenting, its just going to lag the shit out of your pc lel
- ONLY BMSON EXCLUSIVE
- i think ffmpeg ffplay ffprobe is needed idk
- put your bmson chart folder here and name it "test" and change the chart of the bms.bmson into something else u wanna play
- for requirements u need these i guess
```
import json
import re
import sounddevice as sd
import numpy as np
import pygame
from pydub import AudioSegment
```
- the keysound silcing system is implemented, and the raw data that got from the keysound can be played using the play_from_raw function i just wrote in GameState.py
    - this is the code that does the slicing, so just uncomment these i think
    - ```py 
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
        ```
