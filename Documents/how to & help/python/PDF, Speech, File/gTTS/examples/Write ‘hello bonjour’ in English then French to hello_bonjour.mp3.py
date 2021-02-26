#!/data/data/com.termux/files/usr/bin/python3

# Write ‘hello bonjour’ in English then French to hello_bonjour.mp3

from gtts import gTTS
tts_en = gTTS('hello', lang='en')
tts_fr = gTTS('bonjour', lang='fr')

with open('hello_bonjour.mp3', 'wb') as f:
    tts_en.write_to_fp(f)
    tts_fr.write_to_fp(f)
