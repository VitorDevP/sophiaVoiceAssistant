import playsound
import os

sound = None

def play(sound):
    playsound.playsound(sound)

def beep():
    play('beep.mp3')

def beep2():
    play('beep2.mp3')
