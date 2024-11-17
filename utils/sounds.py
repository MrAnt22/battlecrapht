import pygame
import random

def initialize_sounds():
    pygame.mixer.init()

def play_music(music):
    music1 = pygame.mixer.Sound(music)
    music1.set_volume(0.1)
    music1.play()

def stop_music(sound=None):
    if sound:
        sound.stop()
    else:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.quit()
        pygame.mixer.init()

def play_random_sound():
    arthas_replics = [
        "assets/sounds/arthasreplics/1.mp3",
        "assets/sounds/arthasreplics/2.mp3",
        "assets/sounds/arthasreplics/3.mp3",
        "assets/sounds/arthasreplics/4.mp3",
        "assets/sounds/arthasreplics/5.mp3",
        "assets/sounds/arthasreplics/6.mp3",
        "assets/sounds/arthasreplics/7.mp3",
        "assets/sounds/arthasreplics/8.mp3",
        "assets/sounds/arthasreplics/9.mp3",
        "assets/sounds/arthasreplics/10.mp3",
        "assets/sounds/arthasreplics/11.mp3",
        "assets/sounds/arthasreplics/12.mp3",
        
    ]
    sound_file = random.choice(arthas_replics)
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
