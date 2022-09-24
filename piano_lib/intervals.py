import time


def get_secs(intvs):
    for e in intvs:
        interv_list = e.split(',')
        yield float(interv_list[0])


def sleep_int_secs(sleep_secs):
    for i in range(0,sleep_secs):
        time.sleep(1)
        print(".", end="", flush=True)


def sleep_float(sleep_secs):
    sleep_fl = 0
    sleep_int = 0
    if sleep_secs > 1:
        sleep_int = int(sleep_secs)
        sleep_fl = sleep_secs - sleep_int

    sleep_int_secs(sleep_int)

    if sleep_fl > 0:
        time.sleep(sleep_fl)


class IntervalPlayer:
    def __init__(self, intervals, audioPlayer):
        self.intervals = intervals
        self.audioPlayer = audioPlayer

    def play_intervals(self):
        minutes = sum(get_secs(self.intervals)) / 60
        print(f"interval minutes: { minutes }")
        print()

        for interv in self.intervals:
            print(interv)
            interv_list = interv.split(',')
            sleep_float(float(interv_list[0]))
            print()
            self.audioPlayer.play_audio(int(interv_list[1]))

