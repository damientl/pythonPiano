from piano_lib.audioPlayer import AudioPlayer
from piano_lib.intervals import sleep_int_secs

if __name__ == '__main__':
    print('How many minutes is this repeating interval timer for?')
    intevalMinutes = int(input())


    audios = ('toco.mp3','grave.mp3')

    audio_player = AudioPlayer(audios)

    while (True):
        sleep_int_secs(intevalMinutes * 60)
        audio_player.play_audio(0)
        audio_player.play_audio(1)
    
