from piano_lib.audioPlayer import AudioPlayer
from piano_lib.intervals import sleep_int_secs

if __name__ == '__main__':
    print('How many minutes is this repeating interval timer for?')
    intevalMinutes = int(input())

    audios = ['toco.mp3','grave.mp3','violin1.mp3','assobio-fim.mp3','piano.mp3','piano2.mp3']

    audio_player = AudioPlayer(audios)

    i=0
    while (True):
        sleep_int_secs(intevalMinutes * 60)
        audio_player.play_audio(i % len(audios))
        i+=1
    
