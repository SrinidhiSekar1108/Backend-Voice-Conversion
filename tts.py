from gtts import gTTS
import pygame
import os
import time

def text_to_speech(text):
    # Generate speech and save it as an MP3 file
    tts = gTTS(text=text, lang='en')
    mp3_file = "response.mp3"
    tts.save(mp3_file)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up pygame mixer and remove the file
    pygame.mixer.quit()
    os.remove(mp3_file)
