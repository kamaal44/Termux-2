#!/usr/bin/Python3

import os
from gtts import gTTS

echo -n 'hello' | gtts-cli --file - --output hello.mp3
