from playsound import playsound
from piano_lib.file_util import *
import time
import datetime


def get_secs(intvs):
    for e in intvs:
        interv_list = e.split(',')
        yield int(interv_list[0])

def sleep_print(sleep_secs):
    for i in range(0,sleep_secs):
        time.sleep(1)
        print(".", end="")

def getTimeToTrigger(int1Time):
    intHour = int(int1Time.split(':')[0])
    intMin = int(int1Time.split(':')[1])
    return datetime.datetime.now().replace(hour=intHour, minute=intMin, second=0, microsecond=0)

if __name__ == '__main__':
    intervals = readlines("program/alarms/int_alarms.txt")
    audios = ('piano.mp3', 'piano2.mp3')

    print(f"interval len: { len(intervals) }")
    print()
    while True:
        shouldTrigger = False
        for interv in intervals:
            now = datetime.datetime.now().replace(microsecond=0, second=0)
            timeToTrigger = getTimeToTrigger(interv)
            if now == timeToTrigger:
                print("alarm")
                shouldTrigger = True
        if shouldTrigger:
            playsound("assets/" + audios[1])
        else:
            print("not yet")

        sleep_print(59)
