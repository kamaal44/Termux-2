#!/data/data/com.termux/files/usr/bin/python3

# hello’ in English to hello.mp3

from gtts import gTTS
tts = gTTS('hello', lang='en')
tts.save('hello.mp3')
