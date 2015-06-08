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
        self.background_color = [1,0,0,1]
        #self.background_down = "buttons/white_button.png"
        #self.background_normal = "buttons/red_button.png"
        
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
        self.grid = FloatLayout(width = Window.width,height = Window.height)
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
    """
    The player view class controls the players cards and interactions
    It also displays the players cards
    """
    cards = []
    money = 0
    money_label = 0
    current_bet_lbl = 0
    placed_bet = 100
    placed_bet_lbl = 0
    hit_btn = 0
    stay_btn = 0
    double_down_btn = 0
    surrender_btn = 0
    place_bet_btn = 0
    
    def __init__(self, **kwargs):
        super(PlayerView, self).__init__(**kwargs)
        
        #Create and add the buttons to a horizontal grid
        self.player_btns = GridLayout(cols = 4,height = Window.height/16, y = Window.height/2, size_hint_y = None)
        self.hit_btn = MyButton(text = 'Hit')
        self.stay_btn = MyButton(text = 'Stay')
        self.double_down_btn = MyButton(text = 'Double Down')
        self.surrender_btn = MyButton(text = 'Surrender')
        self.place_bet_btn = MyButton(text = 'Place Bet',pos_hint = {'x': .1 ,'y': .1}, size_hint = (.80,.05))
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
        self.stay_btn.bind(on_release = self.stay)
        self.value_lbl.pos_hint = {'x':0 ,'y': -0.05}
        self.place_bet_btn.bind(on_release = self.place_bet)
        #Betting buttons
        self.up_bet_btn = MyButton(text = '>',pos_hint = {'x': .7 ,'y': 0}, size_hint = (.2,.1))
        self.down_bet_btn = MyButton(text = '<',pos_hint = {'x':.1 ,'y': 0}, size_hint = (.2,.1))
        self.up_bet_btn.bind(on_release = self.update_bet)
        self.down_bet_btn.bind(on_release = self.update_bet)
        self.current_bet_lbl = Label(text = '$100',pos_hint = {'x':0 ,'y': -.45})
        self.current_bet = 100
        self.add_widget(self.up_bet_btn)
        self.add_widget(self.down_bet_btn)
        self.add_widget(self.current_bet_lbl)
        self.add_widget(self.place_bet_btn)
        #money and current bet labels
        self.money = 10000
        self.money_label = Label(text = '$' + str(self.money),pos_hint = {'x':0 ,'y': .45})
        self.placed_bet_lbl = Label(text = '$' + str(self.placed_bet),pos_hint = {'x':-.3 ,'y': -.05})
        self.add_widget(self.money_label)
        self.add_widget(self.value_lbl)
        self.add_widget(self.placed_bet_lbl)
        
    def update_bet(self,instance):
        print(instance.text)
        if(instance.text == '<' and self.current_bet > 100):
            self.current_bet -= 100
            self.current_bet_lbl.text = '$' + str(self.current_bet)
        elif (instance.text == '>'):
            self.current_bet += 100
            self.current_bet_lbl.text = '$' + str(self.current_bet)
            
   
    def hit(self,instance):
        Clock.schedule_once(self.parent.parent.add_to_player)
    def stay(self,instance):
        # Disable the users buttons
        for btn in self.player_btns.children:
            btn.disabled = True
        
        #Begin dealer draw
        Clock.schedule_once(self.parent.parent.begin_dealer)
    def place_bet(self,instance):
        self.placed_bet = self.current_bet
        self.placed_bet_lbl.text = self.current_bet_lbl.text
        self.parent.parent.start_round()
    def add_card(self,card = 0):
        self.cards.append(card)
        print(card)
        tmp_image = CardImage(source = 'images/'+card.rank+card.suit+'.png',y = Window.height*(.15),size_hint = (0.25,0.25))
        tmp_image.x += 1000
        self.grid.add_widget(tmp_image)
        anim = Animation(x = (Window.width/2-Window.width/2)+ tmp_image.width*len(self.cards) *Window.width/900,duration = 0.2)
        anim.start(tmp_image)
        
        if (len(self.cards) > 1):
            self.hit_btn.disabled = False
            self.stay_btn.disabled = False
            self.double_down_btn.disabled = False
        self.calculate_value()
        if self.value >21:
            for btn in self.player_btns.children:
                btn.disabled = True
            
        
class DealerView(HandView):
    cards = []
    dealer_card = 0
    def __init__(self,**kwargs):
        super(DealerView, self).__init__(**kwargs)
        
        self.add_widget(self.grid)
        #place the card grid
        self.grid.x = Window.width/2 - self.grid.width/2
        self.grid.y = (Window.height)
        
        self.value_lbl.pos_hint = {'x':0 ,'y': 0.1}
        
        self.add_widget(self.value_lbl)
        
    def add_card(self,card = 0):
        self.cards.append(card)
        print(card)
        if(len(self.cards) == 1):
            tmp_image = CardImage(source = 'images/blank.png',y = Window.height*(.65),size_hint = (0.25,0.25))
            self.dealer_card = tmp_image
        else:
            tmp_image = CardImage(source = 'images/'+card.rank+card.suit+'.png',y = Window.height*(.65),size_hint = (0.25,0.25))
            
        tmp_image.x += 1000
        self.grid.add_widget(tmp_image)
        anim = Animation(x = (Window.width/2-Window.width/2)+ (tmp_image.width*len(self.cards))*Window.width/900,duration = 0.2)
        anim.start(tmp_image)

    def dealer_draw(self,card):
        pass
class CardImage(Image):
    def __init__(self,s=0,r=0, **kwargs):
        super(CardImage, self).__init__(**kwargs)
        
class Game(Screen):
    complete_deck = []
    game_layout = 0
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        #Create 4 decks
        self.toucher = Touch_Handler()
        self.add_widget(self.toucher)
        # playing with 4 decks
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
       
        Clock.schedule_once(self.add_to_player,1)
        Clock.schedule_once(self.add_to_dealer,2)
        Clock.schedule_once(self.add_to_player,3)     
        Clock.schedule_once(self.add_to_dealer,4) 
    def add_to_dealer(self,delay):
        self.game_layout.dealer.add_card(self.complete_deck.pop())
    def add_to_player(self,delay):
        self.game_layout.player.add_card(self.complete_deck.pop())
    def begin_dealer(self,delay):
        
        card = self.complete_deck.pop()
        
        #show the dealers first card
        self.game_layout.dealer.dealer_card.source = 'images/'+self.game_layout.dealer.cards[0].rank+self.game_layout.dealer.cards[0].suit+'.png'
        #show the dealers numerical value
        self.game_layout.dealer.calculate_value()
        
        # dealer deals to self until their hand is greater than 16
        while(self.game_layout.dealer.value < 17):
            self.game_layout.dealer.add_card(card)
            self.game_layout.dealer.calculate_value()
            card = self.complete_deck.pop()
        
        Clock.schedule_once(self.end_round,3)
    def end_round(self,instance):
        # See who won and update players value
        self.game_layout.player.cards.clear()
        self.game_layout.dealer.cards.clear()
        self.remove_widget(self.game_layout)
        self.game_layout = GameView()
        self.add_widget(self.game_layout)
        self.start_round()
class Touch_Handler(Layout):
    """
    The touch handler class allows the user to use gestures
    instead of the buttons to hit, stay, and surrender
    """
    def __init__(self, **kwargs):
        super(Touch_Handler, self).__init__(**kwargs)
        size = (Window.width, Window.height)
    def on_touch_down(self,touch):
        if touch.is_double_tap and self.parent.game_layout.player.hit_btn.disabled == False:
            self.parent.game_layout.player.hit(0)
    def on_touch_move(self, touch):
        print('The touch is at position', touch.pos)
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(size=(1, 1),pos = touch.pos)