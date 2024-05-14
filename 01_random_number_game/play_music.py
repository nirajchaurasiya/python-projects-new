from pydub import AudioSegment

from pydub.playback import play

# Fail sound
wrong_sound = AudioSegment.from_file("fail.mp3", format="mp3")

# Win sound
right_sound = AudioSegment.from_file("success.mp3", format="mp3")


def play_audio(audio):
    play(audio)
