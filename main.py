from kivy.core.window import Window

from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

from menu import SplashScreen, MainMenu


from kivy.uix.widget import Widget
from kivy.uix.image import Image

import os,sys
from game import GameView, Game

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
        self.ss = Screen(name = 'splash_screen')
        splashmenu = SplashScreen()
        splashmenu.buildUp()
        self.ss.add_widget(splashmenu)
        
        #main menu
        self.mm = Screen(name = 'main_menu')
        self.mainmenu = MainMenu()
        self.mainmenu.buildUp()
        self.mm.add_widget(self.mainmenu)
        
        #add the logo to mainmenu and splashscreen
        logo = Image(source = 'images/logo.png')
        logo.width = Window.width/2
        logo.height = Window.height/2
        logo.x = Window.width/2 - (logo.width-logo.width*.05)
        logo.y = (Window.height/2 - logo.width/2)
        self.mm.add_widget(logo)
       
     
        #game screen
        
        self.gs = Game(name = 'game')
        
      
        
        #Add screens to screen manager
        sm.add_widget(self.ss)
        sm.add_widget(self.mm)
        sm.add_widget(self.gs)
        
        sm.current = 'main_menu'
        
        def check_screen_change(obj):
            if(self.mainmenu.buttonText == 'Play'):
                sm.current = 'game'
                self.gs.start_round()
                
                
        self.mainmenu.bind(on_button_release = check_screen_change)
        
        return sm
        
if __name__ == '__main__':
   
    Config.set('graphics', 'height', '960');
    Config.set('graphics', 'width', '720');
    Config.write()
    MyApp().run()