from playsound import playsound
from piano_lib.file_util import *
import time


def get_secs(intvs):
    for e in intvs:
        interv_list = e.split(',')
        yield float(interv_list[0])

def sleep_print(sleep_secs):
    for i in range(0,sleep_secs):
        time.sleep(1)
        print(".", end="")

def sleep_float(sleep_secs):
    sleep_fl = 0
    sleep_int = 0
    if sleep_secs > 1:
        sleep_int = int(sleep_secs)
        sleep_fl = sleep_secs - sleep_int

    for i in range(0,sleep_int):
        time.sleep(1)
        print(".", end="")

    if sleep_fl > 0:
        time.sleep(sleep_fl)

def play_intervals(filename):
    intervals = readlines(filename)

    audios = ('piano.mp3', 'piano2.mp3', 'in.mp3', 'out.mp3', 'hold.mp3')

    minutes = sum(get_secs(intervals)) / 60
    print(f"interval mins: { minutes }")
    print()
    for interv in intervals:

        print(interv)
        interv_list = interv.split(',')
        sleep_float(float(interv_list[0]))
        print()
        playsound("assets/" + audios[int(interv_list[1])])
