from piano_lib.file_util import readlines
from piano_lib.intervals import IntervalPlayer
from piano_lib.audioPlayer import AudioPlayer


def play_intervals(filename):

    intervals = readlines(filename)
    audios = ('piano.mp3', 'piano2.mp3', 'in.mp3', 'out.mp3', 'hold.mp3', 'assobio-fim.mp3')

    audio_player = AudioPlayer(audios)
    interval_player = IntervalPlayer(intervals, audio_player)
    interval_player.play_intervals()

if __name__ == '__main__':
    #somdifpausa-0, som normal-1,in-2,out-3,hold-4

    programs = ['allSounds', '30s', 'default', '10s', 'wimhof', 'quadrada_wimhof', '20', 'pomodoro']
    i=0
    for o in programs:
        print(f"{i} - {programs[i]}")
        i+=1
    option = int(input())

    play_intervals(f"program/{programs[option]}.csv")
