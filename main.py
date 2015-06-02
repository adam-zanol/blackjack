from kivy.core.window import Window


from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from menu import SplashScreen, MainMenu

import os,sys
from kivy.uix.widget import Widget
from kivy.uix.image import Image


# Set game colors
Window.clearcolor = [0, 0, 0, 1]
button_color = [.7, .8, 1, 1]

class MyApp(App):
    def build(self):
        self.title = "Blackjack"
        self.parent = Widget()  
        sm = ScreenManager()
        
        
        # set up the screens
        
        #splashcreen
        ss = Screen(name = 'splash_screen')
        splashmenu = SplashScreen()
        splashmenu.buildUp()
        ss.add_widget(splashmenu)
        
        #main menu
        mm = Screen(name = 'main_menu')
        mainmenu = MainMenu()
        mainmenu.buildUp()
        mm.add_widget(mainmenu)
        #add the logo to mainmenu and splashscreen
        logo = Image(source = 'images/logo.png')
        logo.width = Window.width/2
        logo.height = Window.height/2
        logo.x = Window.width/2 - (logo.width-logo.width*.05)
        logo.y = (Window.height/2 - logo.width/2)
        
        mm.add_widget(logo)
       
     
        #game screen
        
        
        #Add screens to screen manager
        sm.add_widget(ss)
        sm.add_widget(mm)
        
        sm.current = 'main_menu'
        
        return sm
        
if __name__ == '__main__':
   
    Config.set('graphics', 'height', '960');
    Config.set('graphics', 'width', '720');
    Config.write()
    MyApp().run()