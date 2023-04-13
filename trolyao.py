#!/usr/bin/env python
# coding: utf-8

# In[80]:


import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from datetime import datetime
import wikipedia 
from playsound import *
import pyaudio


# In[81]:


now = datetime.now()


# In[82]:


r = sr.Recognizer()


# In[ ]:



import playsound
def speak(text):
    tts= gTTS(text=text, lang='vi')
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
    with sr.Microphone() as source:
        audio_data= r.record(source, duration=5)
        #print("Recognizing...")
        try:
            text= r.recognize_google(audio_data, language='vi')
        except:
            text=""
        print(text)
        
        if text== "":
            root_brain=" Buổi tối vui vẻ, xin chào hôm nay bạn như thế nào? "
            print(root_brain)
            speak(root_brain)
        elif " Xin chào" in text:
            root_brain=" Xin chào bạn, bạn có khỏe không"
            print(root_brain)
            speak(root_brain)
        elif "ngày bao nhiêu" in text:
            root_brain=now.strftime("Hôm nay là ngày %d %m %Y")
            print(root_brain)
            speak(root_brain)
        elif "mấy giờ" in text:
            root_brain=now.strftime("%H:%M:%S")
            print(root_brain)
            speak(root_brain)
        elif text:
            wikipedia.set_lang("vi")
            root_brain.wikipedia.summary(text, sentences=1)
            print(root_brain)
            speak(root_brain)
        elif "Goodbye" in text:
            root_brain=" Tạm biệt"
            speak(root_brain)
            break
        else:
            root_brain= "Bạn muốn nói gì với tôi"
            print(root_brain)
            speak(root_brain)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[71]:


import speech_recognition as sr


# In[72]:


r = sr.Recognizer()


# In[77]:


with sr.Microphone() as source:
    audio_data= r.record(source, duration=5)
    print("Recognizing...")
    try:
        text= r.recognize_google(audio_data, language='vi')
    except:
        text=""
    print(text)


# In[ ]:




