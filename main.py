from time import sleep
from kivy.core.audio import SoundLoader

MUSIC = "/sdcard/Music/bg.mp3"

sound = SoundLoader.load(MUSIC)
if sound:
    sound.loop = True
    sound.play()

while True:
    sleep(1)
