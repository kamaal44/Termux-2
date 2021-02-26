#!@TERMUX_PREFIX@/bin/python3

import pdftotext
from gtts import gTTS
from sys import argv
with open("/data/data/com.termux/files/home/python/pdf/Blue-Moon.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
    document= "\n\n".join(pdf)
    tts = gTTS(document)
    print("Saving Audio file")
    tts.save(Blue-Moon.pdf+".mp3")