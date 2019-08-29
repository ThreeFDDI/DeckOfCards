#!/usr/bin/python3
# """ Let's play cards! """

import requests
from pprint import pprint 

#numplayers = raw_input("\nHow many players will there be: ") # Prompt user and set variable for number of players
numplayers = 2 # Lazy mode 

#numdecks = raw_input("\nHow many decks would you like to shuffle: ") # Prompt user and set variable for number of decks to shuffle
numdecks = 5 # Lazy mode 

#numcards = raw_input("\nHow many cards would you like to draw: ") # Prompt user and set variable for number of cards to draw
numcards = 5 # Lazy mode 

totalcards = int(numdecks) * 52

game = {}

pnum = 0

def new_deck(numdecks): # function to create a new deck and return the deck_id
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/" # URL to generat a new deck

    querystring = {"deck_count":numdecks} # added numdecks variable

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "9f6207b2-5915-4e7a-a726-6d2a2b68751f"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    deck = response.json()
    deck_id = deck['deck_id']

    print("\nPreparing to shuffle " + str(numdecks) + " decks for a total of " + str(totalcards) \
            + " cards. There will be " + str(numplayers) + " players drawing " + str(numcards) + " cards each.") \
            # Repeat back the variable input by the user. If I were cool there would be a Y/N confirmation.

    print("\nYou've shuffled a new deck! Deck id: " + deck_id + "\n") # Print deck id

    return deck_id

def draw_cards(numcards, deck_id, pnum):

    pnumcards = []

    url2 = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/" # URL to draw cards

    querystring2 = {"count":numcards} # added numcards variable

    payload2 = ""
    headers2 = {
        'cache-control': "no-cache",
        'Postman-Token': "814ba960-bb73-4cbb-9e6d-263f77d820a0"
        }

    draw = requests.request("GET", url2, data=payload2, headers=headers2, params=querystring2).json()

    for i in draw['cards']: # parse HTTP response; 
        print("Player #" + str(pnum) + " drew the " + i['value'] + " of " + i['suit'] + "!") # print the number and suit of each card drawn
        pnumcards.append(i['code']) # Add card code to list of all cards drawn

    print("\nThere are " + str(draw['remaining']) + " cards remaining in the deck.\n") # print the number of remaining cards in the deck

    return pnumcards

if __name__ == '__main__':
    deck_id = new_deck(numdecks) # run the new_deck function to start

for i in range(int(numplayers)):
    pnum +=1
    game[pnum] = (draw_cards(numcards, deck_id, pnum)) 

print("The following cards are in play:")

for k,v in game.items():
    hand = ""
    for i in v:
        hand = hand + i +" "
    print("Player #" + str(k), "=>", hand)
