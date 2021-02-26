import pdftotext
from gtts import gTTS
from sys import argv
with open(argv[1], "rb") as f:
    pdf = pdftotext.PDF(f)
    document= "\n\n".join(pdf)
    tts = gTTS(document)
    print("Saving Audio file")
    tts.save(argv[1]+".mp3")