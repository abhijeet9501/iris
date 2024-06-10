import os
import pygame

voice = 'gu-IN-DhwaniNeural'

def speak(message):
    # Define the command to generate speech using edge-tts
    # Adjust the rate by setting it to a negative value, e.g., -20% for a slower rate
    command = f'edge-tts --rate=-20% --voice {voice} --text "{message}" --write-media "data.mp3"'
    try:
        # Run the edge-tts command to generate speech
        os.system(command)

        # Initialize pygame
        pygame.init()
        pygame.mixer.init()

        # Check if the audio file exists and is not empty
        if os.path.exists("data.mp3") and os.path.getsize("data.mp3") > 0:
            # Load and play the audio file
            pygame.mixer.music.load("data.mp3")
            pygame.mixer.music.play()

            # Wait until the audio finishes playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        else:
            print("Error: The generated audio file is empty or does not exist.")

    except pygame.error as e:
        print(f"pygame.error: {e}")
    except Exception as e:
        print(f"Error in text_to_speech: {e}")
    finally:
        # Stop and quit the mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Remove the audio file
        if os.path.exists("data.mp3"):
            os.remove("data.mp3")


# Example usage
speak("Hello, this is a test of the Edge TTS and pygame integration.")
