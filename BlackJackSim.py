# Evgeni Koevski
# BlackJack Simulator

import random

from tkinter import*
# For images and tkinter
from PIL import Image, ImageTk
# DeckSim

# THis is how this works. Main loop launches main menu(). Main menu() launches game. Game launches round and once round is done it shoots back to game where the screen is cleareed. The process is iterated until all cards are out.



                                            ##############################################
                                            ## ###        CLASSES     ############
                                            ##############################################


# THe following class manipulates the SHOE
class deck():                                           #### IN USE  #######

    def __init__(self, deck_num):
        self.decks = int(deck_num)
        self.cards = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]*int(deck_num)
        self.disposed = []
        self.start = len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self): # returns a card and removes from deck
        temp = self.cards[0]
        self.cards.pop(0)
        self.disposed.append(temp)
        return temp


    def cards_left(self):
        return len(self.cards)

    def cards_start(self):
        return self.start

    def show_cards(self):
        print(self.cards)



## The following class is the TABLE                # IT is one of the main classes, keeps track of cards on table and dealer hand value
class table():                                           ###### IN USE  ######
    def __init__(self, set_min, set_max, BJ_payout):
        self.minimum = set_min
        self.maximum = set_max
        self.BJpayout = BJ_payout
        self.total_cards = 0
        self.dealerhand = 0
        self.playerhand = 0
        self.dealer_card_record = []
        self.player_card_record = []
        self.player_ace = 0
        self.dealer_ace = 0
        self.table_bet = 0
        self.the_bet_on_the_table = 0


    def placing_bet(self, bett):
        self.the_bet_on_the_table = bett


    def get_the_bet(self):
        return self.the_bet_on_the_table



    def place_bet(self, beta):      #The bet on the table
        self.table_bet = int(beta)


    def get_bet(self):
        return self.table_bet




    def draw_card(self, deck_object) :         #The dealer cards on the table
        self.player_first_card = deck_object.draw()
        return self.player_first_card

    def add_cards(self):
        self.total_cards += 1

    def get_total_cards(self):
        return self.total_cards




    def dealer_hand(self, value):
        self.dealerhand += value[0]
        self.dealer_card_record.append(value[0])
        print(self.dealer_card_record)

    def get_dealer_hand(self):
        if self.dealerhand > 21 and 11 in self.dealer_card_record and self.dealer_ace == 0:
            self.dealerhand -= 10
            self.dealer_ace = 1
        return self.dealerhand

    def clear_dealer_hand(self):
        self.dealerhand = 0
        self.dealer_card_record = []
        self.dealer_ace = 0


    def get_dealer_card_record(self):
        return self.dealer_card_record




    def player_hand(self, value):
        self.playerhand += value[0]
        self.player_card_record.append(value[0])
        print(self.player_card_record)

    def get_player_hand(self):
        if self.playerhand > 21 and 11 in self.player_card_record and self.player_ace == 0:
            self.playerhand -= 10
            self.player_ace = 1

        return self.playerhand

    def clear_player_hand(self):
        self.playerhand = 0
        self.player_card_record = []
        self.player_ace = 0

    def get_player_card_record(self):
        return self.player_card_record


## The following class is the BANKROLL
class player_bank():
    def __init__(self, start_money):
        self.balance = start_money


    def add(self, bet):
        self.balance += bet

    def subtract(self, bet):
        self.balance -= bet

    def get(self):
        return self.balance


## THe following class is the CASINO TRAY
class casino_bank():
    def __init__(self, start_money):
        self.balance = start_money

    def add(self, bet):
        self.balance += int(bet)

    def subtract(self, bet):
        self.balance -= bet

    def get(self):
        return self.balance


class cards_display():                                              # IN USE
    def __init__(self, card):
        self.card = card
        translator = {"1C":[11,"C"], "2C":[2,"C"], "3C":[3,"C"], "4C":[4,"C"], "5C":[5,"C"], "6C":[6,"C"], "7C":[7,"C"], "8C":[8,"C"], "9C":[9,"C"], "10C":[10,"C"], "JC":[10,"C"], "QC":[10,"C"], "KC":[10,"C"], "1D":[11,"D"], "2D":[2,"D"], "3D":[3,"D"], "4D":[4,"D"], "5D":[5,"D"], "6D":[6,"D"], "7D":[7,"D"], "8D":[8,"D"], "9D":[9,"D"], "10D":[10,"D"], "JD":[10,"D"], "QD":[10,"D"], "KD":[10,"D"], "1H":[11,"H"], "2H":[2,"H"], "3H":[3,"H"], "4H":[4,"H"], "5H":[5,"H"], "6H":[6,"H"], "7H":[7,"H"], "8H":[8,"H"], "9H":[9,"H"], "10H":[10,"H"], "JH":[10,"H"], "QH":[10,"H"], "KH":[10,"H"], "1S":[11,"S"], "2S":[2,"S"], "3S":[3,"S"], "4S":[4,"S"], "5S":[5,"S"], "6S":[6,"S"], "7S":[7,"S"], "8S":[8,"S"], "9S":[9,"S"], "10S":[10,"S"], "JS":[10,"S"], "QS":[10,"S"], "KS":[10,"S"]}
        self.value = translator[card]

    def get_value(self):
        return self.value

    def print_card(self, row, column):
        card_image = Image.open("pictures/" + self.card + ".png")
        Img = ImageTk.PhotoImage(card_image)
        logo = Label(root ,image = Img)
        logo.image = Img


        logo.grid(row = row, column = column)















                                            ##############################################
                                            ###########        FUNCTIONS      ############
                                            ##############################################
## AI function dealer
def dealer_decision():
    if BJ1.get_player_hand() > 21:       # BASICALLY DEACKER CHECKS ON PLAYER HAND TO MAKE SURE NO BUSTS. IF SO, SEIZE CONTROL and END ROUND

        bust_label = Label(root, text = "BUST", font = ("Arial", 40))
        bust_label.grid(row = 4, column = 0)
        back_card.destroy()
        Button_Hit.destroy()
        Button_Double.destroy()
        Button_Stay.destroy()

        Button_Continue = Button(root, text = "Continue", width = 15, height = 1, command = main_game, font = ('Arial' ,20), bg = "red")
        Button_Continue.grid(row = 5, column = 1, columnspan = 2)
        casino_money.add(BJ1.get_the_bet())
        lost_sign = Label(root, text = "You've lost: $" + str(BJ1.get_the_bet()), font = ("Arial", 20), bg = "red")
        lost_sign.grid(row = 5, column = 3, columnspan = 5)


def reshuffle():
    global shoe
    shoe = deck(num_decks_global)
    shoe.shuffle()

    DoSomething = Label(root, text = "RESHUFFLED", bg = "YELLOW", font = ("Arial", 30))
    DoSomething.grid(row = 7, column = 1)
    shoe.show_cards()





def create_deck(num_decks):
    global num_decks_global
    num_decks_global = num_decks
    global shoe
    shoe = deck(num_decks)
    shoe.shuffle()
    shoe.show_cards()
    DoSomething = Label(root, text = "You've created a {0} deck shoe.".format(num_decks))
    DoSomething.grid(row = 7, column = 1)



def place_card(row, column):
    card = BJ1.draw_card(shoe)
    card_object = cards_display(card)
    card_object.print_card(row,column)
    BJ1.add_cards()
    return card_object.get_value()


def hit(player_accumulator, butt_double):
    card = BJ1.draw_card(shoe)
    card_object = cards_display(card)
    card_object.print_card(4,2 + len(BJ1.get_player_card_record()))
    BJ1.player_hand(card_object.get_value())
    BJ1.add_cards()
    butt_double.destroy()


    spacer4 = Label(root, text = BJ1.get_player_hand(), font = ("Arial", 40))
    spacer4.grid(row = 4, column = 0)
    dealer_decision()                              # TANGLING, DEALER DECISION IS ACCESSED AT END FUNCTION TO DETERMINE IF BUST


def dealer_play(dealer_accumulator):
    back_card.destroy()
    dealer_accumulator.destroy()
    spacer3 = Label(root, text = BJ1.get_dealer_hand(), font = ("Arial", 40))
    spacer3.grid(row = 1, column = 0)
    while BJ1.get_dealer_hand() < 17:
        card = BJ1.draw_card(shoe)
        card_object = cards_display(card)
        card_object.print_card(1,2 + len(BJ1.get_dealer_card_record()))
        BJ1.dealer_hand(card_object.get_value())
        BJ1.add_cards()


        spacer4 = Label(root, text = BJ1.get_dealer_hand(), font = ("Arial", 40))
        spacer4.grid(row = 1, column = 0)
    payout()


def place_bet2(bets):

    if player_money.get() - int(bets) >= 0:

        BJ1.placing_bet(int(bets))
        player_money.subtract(int(bets))
    main_game()

def payout():

    Button_Hit.destroy()
    Button_Stay.destroy()
    Button_Double.destroy()


    if BJ1.get_dealer_hand() < BJ1.get_player_hand() or BJ1.get_dealer_hand() > 21:     #Player Win
        player_money.add(BJ1.get_the_bet())
        player_money.add(BJ1.get_the_bet())
        casino_money.subtract(BJ1.get_the_bet())
        lost_sign = Label(root, text = "You've won: $" + str(BJ1.get_the_bet()), font = ("Arial", 20), bg = "red")
        lost_sign.grid(row = 5, column = 3, columnspan = 5)
        BJ1.placing_bet(0)
        Button_Continue = Button(root, text = "Continue", width = 15, height = 1, command = main_game, font = ('Arial' ,20), bg = "red")
        Button_Continue.grid(row = 5, column = 1, columnspan = 2)


    elif BJ1.get_dealer_hand() > BJ1.get_player_hand() and BJ1.get_dealer_hand() < 22:     # Player Loss
        casino_money.add(BJ1.get_the_bet())

        lost_sign = Label(root, text = "You've lost: $" + str(BJ1.get_the_bet()), font = ("Arial", 20), bg = "red")
        lost_sign.grid(row = 5, column = 3, columnspan = 5)
        BJ1.placing_bet(0)
        Button_Continue = Button(root, text = "Continue", width = 15, height = 1, command = main_game, font = ('Arial' ,20), bg = "red")
        Button_Continue.grid(row = 5, column = 1, columnspan = 2)
    else:#Push
        lost_sign = Label(root, text = "PUSH: Bet was:$" + str(BJ1.get_the_bet()), font = ("Arial", 20), bg = "red")
        lost_sign.grid(row = 5, column = 3, columnspan = 5)
        player_money.add(BJ1.get_the_bet())
        BJ1.placing_bet(0)
          #returns money to player
        Button_Continue = Button(root, text = "Continue", width = 15, height = 1, command = main_game, font = ('Arial' ,20), bg = "red")
        Button_Continue.grid(row = 5, column = 1, columnspan = 2)



def dealer_blackjack():
    casino_money.add(BJ1.get_the_bet())
    BJ1.placing_bet(0)



def player_blackjack():
    player_money.add(BJ1.get_the_bet()*1.5 + BJ1.get_the_bet())
    casino_money.subtract(BJ1.get_the_bet()*1.5)
    BJ1.placing_bet(0)




def double(player_accumulator, dealer_accumulator):
    dealer_accumulator.destroy()
    spacer3 = Label(root, text = BJ1.get_dealer_hand(), font = ("Arial", 40))
    spacer3.grid(row = 1, column = 0)

    if player_money.get() - int(BJ1.get_the_bet()) >= 0:
        BJ1.placing_bet(BJ1.get_the_bet()*2)
        player_money.subtract(BJ1.get_the_bet())
    else:
        return
    hit(player_accumulator, Button_Double)
    dealer_play(dealer_accumulator)


def end_game():
    for stuff in root.winfo_children():
        stuff.destroy()
    dealer_text = Label(root, text = "Game Over \n Have a good day sir.", font = ("Arial", 60))
    dealer_text.grid(row = 0, column = 1, columnspan=2)

    end = 1
    root.mainloop()




                                            ##############################################
                                            ######        Main Game      #################
                                            ##############################################
################################ MAIN_GAME IS THE MAIN FUNCTION DURING GAME PLAY #######################
def play_round():


    for stuff in root.winfo_children():
        stuff.destroy()



    dealer_text = Label(root, text = "Dealer Cards", font = ("Arial", 40))
    dealer_text.grid(row = 0, column = 1, columnspan=2)

    dealer_decision()  # AI before proceding


    # First Cards
    BJ1.dealer_hand(place_card(1,1))
    BJ1.player_hand(place_card(4,1))

    BJ1.dealer_hand(place_card(1,2))
    BJ1.player_hand(place_card(4,2))


    global back_card
    card_image = Image.open("pictures/" + "Back.png")
    Img = ImageTk.PhotoImage(card_image)
    back_card = Label(root ,image = Img)
    back_card.image = Img
    back_card.grid(row = 1, column = 2)


    spacer3 = Label(root, text = "xx", font = ("Arial", 40))
    spacer3.grid(row = 1, column = 0)
    spacer4 = Label(root, text = BJ1.get_player_hand(), font = ("Arial", 40))
    spacer4.grid(row = 4, column = 0)
    player_text = Label(root, text = "Player Cards", font = ("Arial",40))
    player_text.grid(row = 3, column = 1, columnspan = 2)

    global Button_Hit
    global Button_Stay
    global Button_Double


    Button_Double = Button(root, text = "Double", width = 15, height = 1, command = lambda: double(spacer4, spacer3), font = ('Arial' ,20))
    Button_Double.grid(row = 7, column = 1, columnspan = 2)
    Button_Hit = Button(root, text = "Hit", width = 15, height = 1, command = lambda: hit(spacer4, Button_Double), font = ('Arial' ,20))
    Button_Hit.grid(row = 5, column = 1, columnspan = 2)
    Button_Stay = Button(root, text = "Stay", width = 15, height = 1, command = lambda: dealer_play(spacer3), font = ('Arial' ,20))
    Button_Stay.grid(row = 6, column = 1, columnspan = 2)



    if BJ1.get_dealer_hand() == 21 and BJ1.get_player_hand() == 21:
        text_bj_push = Label(root, text = "PUSH", font = ('Arial',20))
        text_bj_push.grid(row = 5, column = 3)
        Button_Continue = Button(root, text = "Continue", width = 15, height = 1, command = main_game, font = ('Arial' ,20), bg = "red")
        Button_Continue.grid(row = 5, column = 1, columnspan = 2)
        back_card.destroy()


    elif BJ1.get_dealer_hand() == 21:
        dealer_blackjack()
        Button_Hit.destroy()

        BJ = Label(root, text = "DEALER HAS A BLACKJACK!!!", font = ("Arial", 30), bg = "red")
        BJ.grid(row = 5, column = 3)

        Button_Double.destroy()
        Button_Stay.destroy()
        Button_Continue = Button(root, text = "Continue", width = 15, height = 1, command = main_game, font = ('Arial' ,20), bg = "red")
        Button_Continue.grid(row = 5, column = 1, columnspan = 2)
        back_card.destroy()

    if BJ1.get_player_hand() == 21:
        player_blackjack()
        Button_Hit.destroy()

        BJ = Label(root, text = "YOU GOT BLACKJACK!!!", font = ("Arial", 30), bg = "green")
        BJ.grid(row = 5, column = 3)



        Button_Double.destroy()
        Button_Stay.destroy()
        Button_Continue = Button(root, text = "Continue", width = 15, height = 1, command = main_game, font = ('Arial' ,20), bg = "red")
        back_card.destroy()
        Button_Continue.grid(row = 5, column = 1, columnspan = 2)






    root.mainloop()




################################ MAIN_GAME                   THIS RESETS ALL ATTRIBUTES FROM TABLE BJ1, HOWEVER BANKROLL IS SAME
def main_game():

    for stuff in root.winfo_children():
        stuff.destroy()

    BJ1.clear_player_hand()   # Reset table cards
    BJ1.clear_dealer_hand()

    if player_money.get() <= 0 and BJ1.get_the_bet() == 0:
        end_game()







    ######### PLACE BETS using casino_bank player_bank and BJ1.place_bet() ##################





    spacer = Label(root, text = "   ", font = ("Arial", 50))
    spacer.grid(row = 0, column = 0)



    player_bank_info = Label(root, text = "Player Bankroll: ", font = ("Arial" , 20))
    player_bank_info.grid(row = 1, column = 1)
    casino_bank_info = Label(root, text = "Casino Bankroll: ", font = ("Arial" , 20))
    casino_bank_info.grid(row = 2, column = 1)
    your_bet_info = Label(root, text = "Your last bet: ", font = ("Arial" , 20))
    your_bet_info.grid(row = 3, column = 1)

    player_bankroll = Label(root, text = player_money.get(), font = ("Arial" , 20))
    player_bankroll.grid(row = 1, column = 2)
    casino_bankroll = Label(root, text = casino_money.get(), font = ("Arial" , 20))
    casino_bankroll.grid(row = 2, column = 2)
    your_bet = Label(root, text = BJ1.get_the_bet(), font = ("Arial" , 20))
    your_bet.grid(row = 3, column = 2)

    how_much_bet = Label(root, text = "Place your bet: ", font = ("Arial" , 20))
    how_much_bet.grid(row = 4, column = 1)


    bet_entry = Entry(root, text = "", width = 5 , font = ('Arial' ,20))
    bet_entry.grid(row = 4, column = 2)

    Button_Bet = Button(root, text = "BET", width = 15, height = 1, command = lambda: place_bet2(bet_entry.get()), font = ('Arial' ,20))
    Button_Bet.grid(row = 5, column = 1, columnspan = 2)
    Button_Play = Button(root, text = "Play", width = 15, height = 1, command = play_round, font = ('Arial' ,20))
    Button_Play.grid(row = 6, column = 1, columnspan = 2)

#############################################################################################################################################################!!!!!!
        #################################### RESHUFFELEEE
    if shoe.cards_left()/shoe.cards_start() < 1/5:
        reshuffle()

    root.mainloop()




# Main Menu Window
def main_menu():
    for stuff in root.winfo_children():
        stuff.destroy()


    #Title + Main Menu Label

    spacer = Label(root, text = "                     ", font = ('Arial' ,100))
    spacer.grid(row = 0, column = 0)

    title = Label(root, text = " Count Master ", font = ('Arial' ,40) )
    title.grid(row = 1, column = 1, columnspan = 10)

    main_menu_label = Label(root, text = " MAIN MENU ", font = ('Arial' ,20) )
    main_menu_label.grid(row = 2, column = 1, columnspan = 10)

    Button_Start_Game = Button(root, text = "Start Game", width = 30, height = 1, command = main_game, font = ('Arial' ,20))
    Button_Start_Game.grid(row = 4, column = 1, columnspan = 2)

    Text = Label(root, text = "Number of decks:", font = ('Arial' ,20))
    Text.grid(row = 6, column = 1)

    spacer2 = Label(root, text = "                     ", font = ('Arial' ,15))
    spacer2.grid(row = 5, column = 1)

    Enter_Decks = Entry(root, text = "6", width = 5 , font = ('Arial' ,20))
    Enter_Decks.grid(row = 6, column = 2)

    Button_Ok = Button(root, text = "OK", font = ('Arial' ,20), command = lambda: create_deck(Enter_Decks.get()))     # Passes number of decks to function above and creates decks.
    Button_Ok.grid(row = 6,  column = 3)




    #### HOW TO ADD IMAGES ONTO SCREEN USING PILLOW ####
    Img = ImageTk.PhotoImage(Image.open("pictures/" + "BJLogo.png"))
    logo = Label(root ,image = Img)
    logo.image = Img
    logo.grid(row = 3, column = 1)







### MAIN ##

# Variables/Widgets

root = Tk("Count Master")
root.geometry("1920x1080")
root.title("Count Master")






#### MAIN FUNCTION   ################################
def main():
    global casino_money
    global player_money
    global BJ1
    casino_money = casino_bank(30000)
    player_money = player_bank(200)
    BJ1 = table(5, 100, 1.5)            #INITIATE TABLE
    main_menu()


    root.mainloop()

main()
