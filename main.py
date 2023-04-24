from gtts import gTTS
import os
import time

#text='this mail is from infoysis about the enterance exam'
lang='en'
def speak(text):
    text=text.replace('*','')
    text=text.replace('=','')
    obj=gTTS(text=text,lang=lang)

    obj.save('Hi.mp3')

    os.system('mpg123 Hi.mp3')
    time.sleep(10)
    os.system('rm -rf Hi.mp3')
    return
