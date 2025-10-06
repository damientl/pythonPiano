import pygame
import time

class AudioPlayer:
    def __init__(self, audios):
        pygame.mixer.init()
        self.audios = audios
        self.loaded_sounds = []
        for audio_file in self.audios:
            print("Loading audio: " + "assets/" + audio_file)
            sound = pygame.mixer.Sound("assets/" + audio_file)
            self.loaded_sounds.append(sound)
    
    def play_audio(self, index):
        print("Playing audio: " + "assets/" + self.audios[index])
        sound = self.loaded_sounds[index]
        sound.play()
        # Wait for the sound to finish playing
        while pygame.mixer.get_busy():
            time.sleep(0.1)
