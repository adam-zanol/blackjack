"""
This module controls the main game graphics and game play

"""
from kivy.uix.scatterlayout import ScatterLayout
from deck import Deck
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from random import shuffle
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.layout import Layout

from kivy.graphics import Rectangle
from kivy.graphics import Color
class MyButton(Button):
    """
    My Button class inherits a kivy button and creates uniform buttons
    to use on any menu when needed
    """
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.03
        self.color = [0,0,0,1]
        self.background_down = "buttons/white_button.png"
        self.background_normal = "buttons/red_button.png"
        
class GameView(FloatLayout):
    player = 0
    dealer = 0
    def __init__(self, **kwargs):
        super(GameView, self).__init__(**kwargs)
   
        #player portion of game screen
        self.player = PlayerView()
        self.add_widget(self.player)
        #dealer portion of game screen
        self.dealer = DealerView()
        self.add_widget(self.dealer)
        
class HandView(FloatLayout):
    
    cards = []
    grid = 0
    cards_value = 0
    def __init__(self, **kwargs):
        super(HandView, self).__init__(**kwargs)  
        self.grid = FloatLayout(width = Window.width, spacing = -Window.width/2)
        self.value_lbl = Label(text = '0',font_size = Window.width*0.03)
       
    def add_card(self, card):
        pass
    def calculate_value(self):
        self.value = 0
        for card in self.cards:
            self.value+= card.value()
        self.value_lbl.text = str(self.value)
        print(self.value)
class PlayerView(HandView):
    cards = []
    money = 0
    hit_btn = 0
    stay_btn = 0
    double_down_btn = 0
    surrender_btn = 0 
    def __init__(self, **kwargs):
        super(PlayerView, self).__init__(**kwargs)
        
        #Create and add the buttons to a horizontal grid
        self.player_btns = GridLayout(cols = 4,height = Window.height/16, y = Window.height/2, size_hint_y = None)
        self.hit_btn = MyButton(text = 'Hit')
        self.stay_btn = MyButton(text = 'Stay')
        self.double_down_btn = MyButton(text = 'Double Down')
        self.surrender_btn = MyButton(text = 'Surrender')
        self.player_btns.add_widget(self.hit_btn)
        self.player_btns.add_widget(self.stay_btn)
        self.player_btns.add_widget(self.double_down_btn)
        self.player_btns.add_widget(self.surrender_btn)
        self.add_widget(self.player_btns)
        self.add_widget(self.grid)
        #place the card grid
        self.grid.x = Window.width/2 - self.grid.width/2
        self.grid.y = -(Window.height*(.2))
        
        #Bind the buttons
        self.hit_btn.bind(on_release = self.hit)
        
        self.value_lbl.pos_hint = {'x':0 ,'y': -0.05}
        
        self.add_widget(self.value_lbl)
    def hit(self,instance):
        Clock.schedule_once(self.parent.parent.add_to_player)
        
    def add_card(self,card = 0):
        self.cards.append(card)
        print(card)
        tmp_image = CardImage(source = 'images/card.png',y = -Window.height*(.2))
        tmp_image.x += 1000
        self.grid.add_widget(tmp_image)
        anim = Animation(x = Window.width/4*len(self.cards)-Window.width/2,duration = 0.2)
        anim.start(tmp_image)
        
        if (len(self.cards) > 1):
            self.hit_btn.disabled = False
            self.stay_btn.disabled = False
            self.double_down_btn.disabled = False
        self.calculate_value()
    
        
class DealerView(HandView):
    cards = []
    def __init__(self,**kwargs):
        super(DealerView, self).__init__(**kwargs)
        
        self.add_widget(self.grid)
        #place the card grid
        self.grid.x = Window.width/2 - self.grid.width/2
        self.grid.y = (Window.height)
        
        self.value_lbl.pos_hint = {'x':0 ,'y': 0.1}
        
        self.add_widget(self.value_lbl)
    def add_card(self,card):
        self.cards.append(card)
        print(card)
        if(len(self.cards) == 1):
            tmp_image = CardImage(source = 'images/blank.png',y = Window.height/4)
        else:
            tmp_image = CardImage(source = 'images/2spades.png',y = Window.height/4)
        tmp_image.x += 1000
        self.grid.add_widget(tmp_image)
        anim = Animation(x = Window.width/4*len(self.cards)-Window.width/2,duration = 0.2)
        anim.start(tmp_image)
        
class CardImage(Image):
    def __init__(self,s=0,r=0, **kwargs):
        super(CardImage, self).__init__(**kwargs)
        
class Game(Screen):
    complete_deck = []
    game_layout = 0
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        #Create 4 decks
        self.toucher = Touch_handler()
        self.add_widget(self.toucher)
        for _ in range(4):
            tmp_deck = Deck()
            for card in tmp_deck.cards:
                self.complete_deck.append(card)
                print(card)
            
        
        # Shuffle the deck
        shuffle(self.complete_deck)
        
        self.game_layout = GameView()
        self.add_widget(self.game_layout)
    def start_round(self):
        #deal two cards to player and 2 cards to dealer
        for btn in self.game_layout.player.player_btns.children:
            btn.disabled = True
        Clock.schedule_once(self.add_to_dealer,1)
        Clock.schedule_once(self.add_to_player,2)
        Clock.schedule_once(self.add_to_dealer,3)
        Clock.schedule_once(self.add_to_player,4)
        
     
        
    def add_to_dealer(self,delay):
        self.game_layout.dealer.add_card(self.complete_deck.pop())
    def add_to_player(self,delay):
        self.game_layout.player.add_card(self.complete_deck.pop())
 
    def end_round(self):
        pass
    
    
class Touch_handler(Layout):
    def __init__(self, **kwargs):
        super(Touch_handler, self).__init__(**kwargs)
        size = (Window.width, Window.height)
    def on_touch_down(self,touch):
        if touch.is_double_tap:
            self.parent.game_layout.player.hit(0)
    def on_touch_move(self, touch):
        print('The touch is at position', touch.pos)
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(size=(1, 1),pos = touch.pos)