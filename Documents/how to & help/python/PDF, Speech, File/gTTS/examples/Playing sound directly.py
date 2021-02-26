#!/data/data/com.termux/files/usr/bin/python3

# Playing sound directly
# There’s quite a few libraries that do this.
# Write ‘hello’ to a file-like object to do further
# manipulation.

from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('hello', lang='en')
tts.write_to_fp(mp3_fp)

# Load `mp3_fp` as an mp3 file in
# the audio library of your choice
