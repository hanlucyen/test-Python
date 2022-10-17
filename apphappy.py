"""
import kivy
from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text='Happy brithday')
if __name__=='__main__':
    MyApp().run()
        

from kivy.app import App
from kivy.uix.button import Button
class SimpleApp(App):
    def build(self):
        def a(instance,value):
            print("Happy brithday")
        btn=Button(text="Kivy-Clicked!",font_size=150)
        btn.bin(state=a)
        return btn

from kivy.app import App
from kivy.uix.slider import Slider
class SimpleApp(App):
    def build(self):
        slide=Slider(orientation='vertical',value_track=True,value_track_color=(1,0,0,1))
        return slide
if __name__=="__main__":
    SimpleApp().run()
"""
import tkinter as tk
import requests


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="PyMi.vn checker")
        self.label.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind("<Key-Return>", self.check_site)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Check web site up/down. Enter URL:"
        self.hi_there["command"] = self.check_site
        self.hi_there.pack()

        self.quit = tk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

    def check_site(self, event=None):
        url = self.contents.get().strip() or "https://pymi.vn"
        if not url.startswith("http"):
            url = "http://{}".format(url)

        resp = requests.head(url, timeout=3)
        print("{} response: {}".format(url, resp.status_code))


root = tk.Tk()
app = Application(master=root)
app.master.title("My checker app")
app.master.minsize(300, 200)
app.mainloop()
