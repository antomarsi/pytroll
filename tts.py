from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os.path, time

mp3_file = 'files/tts.mp3'
if (not os.path.exists(mp3_file)):
    mp3_fp = BytesIO()
    tts = gTTS('Power Off', 'en')
    tts.save(mp3_file)

while (True):
    playsound(mp3_file)
    time.sleep(30)
