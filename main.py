from kivy.core.window import Window

 # KIVY STUFF
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Canvas
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior, DragBehavior

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.modalview import ModalView

from kivy.graphics.vertex_instructions import *
from kivy.uix.filechooser import FileChooserListView, FileChooserIconView

import os,sys
from kivy.uix.screenmanager import ScreenManager

Config.set('graphics','resizable',0)

# Set game colors
Window.clearcolor = [.2, .2, .2, 1]
button_color = [.7, .8, 1, 1]

class MyApp(App):
    def build(self):
        self.title = "Blackjack"
        sm = ScreenManager()
  
        return sm
        
if __name__ == '__main__':
    Config.set('graphics','resizable',0);
    Config.set('graphics', 'height', '960');
    Config.set('graphics', 'width', '720');
    Config.write()
    MyApp().run()