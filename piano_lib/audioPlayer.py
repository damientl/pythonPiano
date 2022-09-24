from playsound import playsound

class AudioPlayer:
    def __init__(self, audios):
        self.audios = audios
    
    def play_audio(self, index):
        playsound("assets/" + self.audios[index])