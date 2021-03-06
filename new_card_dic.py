#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from sys import argv

def get_card_dic(file):
    cardname = {}
    cardstat = {}
    for line in file:
        card_info = line.strip().split('\t')
        if len(card_info) < 2:
            continue
        if card_info[0] == 'Name': 
            cardname[card_info[1]] = {}
            cardstat = cardname[card_info[1]]
            cardstat['Name'] = card_info[1]
        elif card_info[0] == 'Cost:': #and len(card_info) == 2:
            cardstat['cost'] = card_info[1]
        elif card_info[0] == 'Type:':
            cardstat['type'] = card_info[1]
        elif card_info[0] == 'Pow/Tgh:': #and len(card_info) == 2:
            cardstat['P/T'] = card_info[1]
        elif card_info[0] == 'Rules Text:': #and len(card_info) == 2:
            cardstat['Efects'] = card_info[1]
        elif card_info[0] == 'Set/Rarity:':
            cardstat['Set/Rarity'] = card_info[1]
    return cardname
    
def validate_deck(deck, basic, legal):
    for line in deck:
        card = line.strip().split('\t')
        if card[0] in basic:
            continue
        if card[1] not in legal:
            return "!!!Deck not valid!!!"
            exit
    return "Deck valid! :)"
    
# (do not delete) game play functions begin here

def shufle_deck(my_deck):
    my_deck = random.shuffle(my_deck)
    return my_deck

def pull_deck_from_dic(deck):
    cards = []
    for line in deck:
        card = line.strip().split('\t')
        for i in range(int(card[1])):
            cards.append(card[0])
    return cards
    
def play_first(x):
    players = range(1, (x+1))
    play1 = random.choice(players)
    return play1
    
def draw_hand(my_deck): # line "Hand=" and "Deck =" used for trouble shooting.
    hand = my_deck[:7]
    del my_deck[:7]
    return hand, my_deck 
    
def scryx(my_deck, x):
    return my_deck[:x]

def gameplay(my_deck):
    shufle_deck(my_deck)
    handsim = draw_hand(my_deck)
    return handsim
    
def play_card(hand, b_field, turn='y'):
    while turn == 'y': 
        card = raw_input('Play Card ')
        if card not in hand:
            print "Error, try again!"
            return play_card(hand, b_field)
        b_field.append(card)
        hand.remove(card)
        turn = raw_input('Play again? (y, n)')
    return card, hand, b_field
    
    
 
    
    
#########Work on these functions################


    
def draw_card(deck, hand):
#    c1 = deck[:1]
#     print deck
#     print c1
    hand.append(deck[0])
    del deck[0]
    return deck, hand
    
def game_status(life, deck):
    if life < 1:
        return False
    if len(deck) < 1:
        return False
    return True
    
def attack_opponent(card, player_life, cardname):
    player_life = player_life - power
    #get the power/toughness for the given card and subtract it from the players life
    #raw input ("do you want to attack") 
    return player_life


############Start Main Function#################

def main():

    script_name, deck1, deck2, card_info = argv
    
#    class atacking_creature:
#    class blocking_creature:
    
    basic = ['Mountain', 'Island', 'Plains', 'Forest', 'Swamp']
    legal = ['1', '2', '3', '4']
    
    file = open(card_info, 'U')
    cardname = get_card_dic(file)
    
    deck1 = open(deck1, 'U')
    deck2 = open(deck2, 'U')
    my_deck = pull_deck_from_dic(deck1)
    op_deck = pull_deck_from_dic(deck2)
    
#     x = 2
#     player_one = play_first(x)
#     print "player %s goes first" % player_one
    shufle_deck(my_deck)
    shufle_deck(op_deck)
    player1_hand, my_deck = draw_hand(my_deck)
    player2_hand, op_dech = draw_hand(op_deck)
    print "--player 1 hand:", player1_hand
    print "--player 2 hand:", player2_hand
    b_field = []
    print "Player One Turn"
    card, hand1, b_field  = play_card(player1_hand, b_field)
    print "Player Two Turn"
    card, hand2, b_field  = play_card(player2_hand, b_field)
    print card
    print "--Player1 hand:", hand1
    print "--Player2 hand:", hand2
    print "--Battlefield:", b_field
    
    player_1_life = 20
    player_2_life = 20
    
    game_on = True
    while game_on == True:
        draw_card(my_deck, hand1)
        print hand1
        print "Player One Turn"
        card, hand1, b_field  = play_card(player1_hand, b_field)
        game_on = game_status(deck1, player_1_life)
        draw_card(op_deck, hand2)
#         player_2_life = 
#        (card, player_life)
        print hand2
        print "Player Two Turn"
        card, hand2, b_field  = play_card(player2_hand, b_field)
#        player_2_life = attack_opponent(card, player_life)
#        game_on = game_status(deck2, player_2_life)
#         place_card_on_field(play_card(player1_hand))
        #put a bunch of stuff here:
        game_on = False
    
    #say who wins
            
    play = gameplay(my_deck)
#     print gameplay(my_deck)

if __name__ == "__main__":
    main()