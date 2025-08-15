import os

from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = 'en'

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

# input_text = "Hello, how can I assist you today?"
# text_to_speech_with_gtts_old(input_text = input_text, output_filepath="gtts_testing.mp3")


import elevenlabs
from elevenlabs import ElevenLabs
from dotenv import load_dotenv
load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVEN_LABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "9BWtsMINqrJLrRacOk9x",
        output_format= "mp3_22050_32",
        model_id= "eleven_turbo_v2",
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

#new 

import subprocess
import platform 
from pydub import AudioSegment

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    sound = AudioSegment.from_mp3(output_filepath)
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    sound.export(wav_filepath, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")   


input_text = "Hello, how can I assist you today?, This is a test of the text to speech functionality."
# text_to_speech_with_gtts(input_text = input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "IKne3meq5aSn9XLyUdCD",
        output_format= "mp3_22050_32",
        model_id= "eleven_turbo_v2",
    )
    elevenlabs.save(audio, output_filepath)

    sound = AudioSegment.from_mp3(output_filepath)
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    sound.export(wav_filepath, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")