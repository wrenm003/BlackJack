__author__ = 'Matt'
import random

Face_value = {
'Ace': 11,'King':10,'Queen':10,'Jack':10,
'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,
}








# ##################### class Deck_all_52 #####################

class Deck_all_52:
    def __init__(self): #Setting all 52 Display_cards first time

        self.cards_ = []
        for shape in [ 'Spade',  'Club','Heart','Diamond'  ]:
            for value in Face_value.keys():
                card = card_class(value, shape)
                self.cards_.append(card)



    def next_card(self): #getting the next card from the deck

        card_position = random.randint(0, len(self.cards_)-1)# take the next card randonmly from the deck


        card = self.cards_[card_position] #get the card of index card_position
        self.cards_.pop(card_position)
        return card     # return the card



## #####################class Cards_Cpu# ######################


    # #####################class card_class Start# #####################

class card_class:
    def __init__(self,value = 'Ace', shape = 'Diamond' ): #just setting the deafult values
        self.value_ = value
        self.shape_ = shape
    def __repr__(self):
        return '%s-%s' % (self.value_, self.shape_)
    def Check_ace(self):
        return self.value_ == 'Ace' #if card jack return true else false

    def __int__(self):
        return Face_value[self.value_]







class Cards_Cpu:
    def __init__(self, HandName = 'Cpu_play'): #constructor default setting the values


        self.Player_hands_ = HandName
        self.cards_ = []

    def Get_next_card(self, deck):

        self.cards_.append(deck.next_card()) #append the card to the player card



    def number_Exceeded(self): #if exceed game is over player busted

        return self.count_total_fun() >= 20



    def HandName(self): #Print the player hand name

        return self.Player_hands_


    def count_total_fun(self): #return the player's Player_Scoretl Display_cards value/number

        Player_Scoret = 0
        count_ace= 0;
        for card in self.cards_:
            Player_Scoret = Player_Scoret+int(card)  # count the value of the hand
            if card.Check_ace():   # counting ACE(s) as 11
                count_ace=count_ace+1;

        while Player_Scoret >=20 and count_ace > 0 :# check the number of ace

            Player_Scoret = Player_Scoret-10


        return Player_Scoret

    def Display_cards(self):

        text = ''
        for card in self.cards_:
            if text:
                text += ', '
            text += '%s' % card
        return text

    def Display_Allcards(self):#display fucntion
        return '%d: %s' % (self.count_total_fun(), self.Display_cards())

    def Display_FirstCard(self):

        return '%d: %s, ' % (self.count_total_fun(), self.cards_[0])

    def Winner_L00ser(self, Player_CPU):#show the final result win? lost?



        if Player_CPU.number_Exceeded():
            return 'Congrats!!you win'
        if self.number_Exceeded():
            return 'you Lost the game :('
        Player_Scoret_dealer = Player_CPU.count_total_fun()

        Player_Scoret_hand = self.count_total_fun()


        if Player_Scoret_dealer < Player_Scoret_hand:
             return 'Congrats!!you win'
        elif Player_Scoret_dealer > Player_Scoret_hand:
             return 'you Lost the game :('
        else:
            return 'No result it is tie'
    def Hit_or_not(self): #User might want the next one card

        return self.count_total_fun() < 18


#####################class Cpu_play#####################

class Cpu_play(Cards_Cpu): #Class for cpu


    def __init__(self):

        Cards_Cpu.__init__(self, 'Cpu_play')
    def hit_exit(self):

        return 'Cpu:  %s' % self.Display_Allcards()

    def Main_Message(self):

        return ' Cpu: %s' % self.Display_FirstCard()

    def Display_short(self):

        return 'Cpu:  %s' % self.Display_Allcards()



class Game_class: #For display the game progress


    def __init__(self, all_players = range(1, 1)):


        self.deck_ = Deck_all_52()

        self.players_ = {}
        for player in all_players: #To display all the player
            hand = Player('Player %s' % player)

            hand.Get_next_card(self.deck_)
            hand.Get_next_card(self.deck_)
            self.players_[player] = hand

        self.dealer_ = Cpu_play()

        self.dealer_.Get_next_card(self.deck_)
        self.dealer_.Get_next_card(self.deck_)

    def Print_Precise(self):

        Player_CPU = self.dealer_
        for player in self.all_players():
            hand = self.players_[player]
            print ('%s - %s!' % (hand.Display_short(), hand.Winner_L00ser(Player_CPU)))
        print (Player_CPU.Display_short())


    def Display_Main_message(self):

        Player_CPU = self.dealer_
        for player in self.all_players():
            hand = self.players_[player]
            print (hand.Main_Message())
        print (Player_CPU.Main_Message())

    def all_players(self):

        return self.players_.keys()



    def Game_Continue(self, player):


        hand = self.players_[player]
        while True:
            if hand.number_Exceeded():
                print ('%s - You lose :( ' % hand.hit_exit())
                break;

            question = '%s " Press S  For stand any key For hit" ' % hand.hit_exit()
            answer = input(question).lower()
            if 's' in answer:
                break

            hand.Get_next_card(self.deck_)




    def cpu_play_function(self):

        Player_CPU = self.dealer_
        while not (False): #untill the condition is true
            if Player_CPU.number_Exceeded():
                break
            elif Player_CPU.Hit_or_not():
                print ('%s - Cpu_play hits' % Player_CPU.hit_exit())
                Player_CPU.Get_next_card(self.deck_)
            else:
                break
        print ('%s - Cpu_play stands' % Player_CPU.hit_exit())

    def start_play(self):

        self.Display_Main_message()
        for player in self.all_players():
            self.Game_Continue(player)
        self.cpu_play_function()
        self.Print_Precise()




class Player(Cards_Cpu): #for Human player


    def __init__(self, HandName = 'Player'):

        Cards_Cpu.__init__(self, HandName)

    def hit_exit(self):
        return '%s, Scores %s' % (self.HandName(), self.Display_Allcards())



    def Display_short(self):#some precise

        return '    %s Scores %s' % (self.HandName(), self.Display_Allcards())

    def Main_Message(self):

        return '    %s Scores %s' % (self.HandName(), self.Display_Allcards())




##################### MAin starts here #####################

try:
 print ('BlackJack Developed by Matthew Wren at University of Brighton')
 number_of_players = int(input('Enter the number of players please'))
 all_players = range(1, number_of_players + 1)
 blackjack = Game_class(all_players)
 blackjack.start_play()
except ValueError:
    print ("Oops!  That was no valid number.  Try again...")


