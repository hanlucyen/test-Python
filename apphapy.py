import kivy 
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
import time
import playsound as playsound
alarm=False

class MyApp(App):
    def build(self):
        return Builder.load_string(
'''
BoxLayout:
    textInput:
        id: hour
        font_size: 32
    TextInput:
        id: min
        font_size: 32
'''
)
    def on_star(self):
        Clock.schedule_interval(
            self.update, 1
        )
    def update(self,*args):
        global alarm
        h=time.strftime('%H')
        m=time.strftime('%M')
        hour=self.root.ids.hour.text
        min=self.root.ids.min.text
        if h==hour and m==min and not alarm:
            playsound.playsound("alarm.wav")
            alarm=True
MyApp().run()
