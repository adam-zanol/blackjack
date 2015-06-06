"""
This module contains the different menu screen widgets
"""

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class MyButton(Button):
    """
    My Button class inherits a kivy button and creates uniform buttons
    to use on any menu when needed
    """
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.05
        self.color = [0,0,0,1]
        self.background_down = "buttons/white_button.png"
        self.background_normal = "buttons/red_button.png"
        
class SmartMenu(Widget):
    """"
    SmartMenu class is used as a base class for each other menu screen
    """
    buttonList = []
    
    def __init__(self, **kwargs):
    #create custom events first
        self.register_event_type('on_button_release')
        super(SmartMenu, self).__init__(**kwargs)
    def on_button_release(self, *args):
        pass
    def callback(self,instance):
        print('The button %s is being pressed' % instance.text)
        self.buttonText = instance.text
        self.dispatch('on_button_release') 
 
    def addButtons(self):
        for k in self.buttonList:
            tmpBtn = MyButton(text = k)
            tmpBtn.bind(on_release = self.callback)
            self.layout.add_widget(tmpBtn)
     
    def buildUp(self):
    #self.colorWindow()
        self.addButtons()
class MainMenu(SmartMenu):
    buttonList = [ 'Play', 'Settings']
    def __init__(self,**kwargs):
        super(MainMenu, self).__init__(**kwargs)
        #Create the layout
        self.layout = BoxLayout(orientation = 'vertical',spacing = Window.height*.01)
        self.layout.width = Window.width/2
        self.layout.height = Window.height/4
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = (Window.height/2 - self.layout.height/2)-Window.height/10
        print(Window.width)
        print(Window.height)
        #Create the buttons
        
        self.add_widget(self.layout)


class SplashScreen(SmartMenu):
    """
    Represents the intro screen
    """
    layout = GridLayout(orientation = 'vertical')
    def __init__(self,**kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        play_btn = Button(text = 'Play')
        