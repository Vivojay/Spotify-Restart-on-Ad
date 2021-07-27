#Sound and Spotify imports
import os, subprocess as sp
import psutil, subprocess, time
from pynput.keyboard import Key, Controller
from SwSpotify import spotify as Sp
import winsound as ws

def restartSpot():
    for proc in psutil.process_iter():
        # check whether the process name matches, i.e. Spotify is open?
        if proc.name() == 'Spotify.exe':
            try:
                proc.kill()
            except Exception:
                pass

    while not 'Spotify.exe' in [i.name() for i in psutil.process_iter()]:
        try:
            subprocess.Popen('spotify.exe', shell=True)
        except Exception:
            pass

    time.sleep(0.1)
    keyboard = Controller()
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)

restartSpot()