#!/usr/bin/Python3

import os
from gtts import gTTS

echo -n 'hello' | gtts-cli - --output hello.mp3
