#Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import kivy
"""
[INFO   ] [Logger      ] Record log in C:\Users\ASUS\.kivy\logs\kivy_21-12-30_4.txt
[INFO   ] [deps        ] Successfully imported "kivy_deps.gstreamer" 0.1.18
[INFO   ] [deps        ] Successfully imported "kivy_deps.angle" 0.3.0
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew" 0.3.0
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2" 0.3.1
[INFO   ] [Kivy        ] v2.0.0
[INFO   ] [Kivy        ] Installed at "C:\Users\ASUS\anaconda3\lib\site-packages\kivy\__init__.py"
[INFO   ] [Python      ] v3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
[INFO   ] [Python      ] Interpreter at "C:\Users\ASUS\anaconda3\python.exe"
>>> from kivy.app import App
[INFO   ] [Factory     ] 186 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_pil (img_ffpyplayer ignored)
"""
from kivy.uix.label import Label
#[INFO   ] [Text        ] Provider: sdl2
class MyApp(App):
        def build(self):
                return Label(text='Hello World')

if __name__=='__main__':
        MyApp().run()

"""	
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL" graphics system
[INFO   ] [GL          ] GLEW initialization succeeded
[INFO   ] [GL          ] Backend used <glew>
[INFO   ] [GL          ] OpenGL version <b'4.6.0 - Build 26.20.100.7372'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel(R) UHD Graphics 620'>
[INFO   ] [GL          ] OpenGL parsed version: 4, 6
[INFO   ] [GL          ] Shading version <b'4.60 - Build 26.20.100.7372'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <32>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
"""
