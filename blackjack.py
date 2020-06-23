#!/usr/local/bin/python3
""" 
Let's play Blackjack! 

Blackjack game using deckofcardsapi.com
"""

import requests
from pprint import pprint


# TODO (Done) Start new game

# TODO (Done) Reshuffle

# TODO The Deal

# TODO Betting

# TODO Dealer turn

# TODO NPC turn

# TODO Player turn


def new_game():
    """
    function to create a new deck and return the deck_id
    """
    # Prompt user and set variable for number of players
    # numplayers = raw_input("\nHow many players will there be: ")
    numplayers = 3  # Lazy mode

    # Prompt user and set variable for number of decks to shuffle
    # numdecks = raw_input("\nHow many decks would you like to shuffle: ")
    numdecks = 6  # Lazy mode
    
    # URL to generate a new deck
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

    # parameter for number of decks
    querystring = {"deck_count": numdecks}  

    # send GET request
    response = requests.request("GET", url, params=querystring)

    # parse json response
    deck = response.json()
    
    # extract deck ID
    deck_id = deck["deck_id"]

    # Print deck id
    print(f"\nYou've started a new game of Blackjack!\n\nDeck id: {deck_id}\n")

    return deck_id, numplayers


def draw_cards(numcards, deck_id, pnum):
    """
    function to draw cards
    """
    # init list of player's cards
    pnumcards = []

    # URL to draw cards from deck
    url = (
        "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/"
    )

    # parameter for number of cards
    querystring = {"count": numcards}

    # send GET request
    draw = requests.request("GET", url, params=querystring).json()

    # print the number and suit of each card drawn
    for card in draw["cards"]:  # parse HTTP response;
        print(
            "Player #"
            + str(pnum)
            + " drew the "
            + card["value"]
            + " of "
            + card["suit"]
            + "!"
        )
        # Add card code to list of all cards drawn
        pnumcards.append(card["code"])

    # print the number of remaining cards in the deck
    print(f"\nThere are {str(draw['remaining'])} cards remaining in the deck.\n")

    return pnumcards


def shuffle_deck(deck_id):
    """
    Function to reshuffle an existing deck
    """
    print(f"Reshuffling deck id: {deck_id}\n")
    # URL to shuffle existing deck
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"

    # send GET request
    requests.request("GET", url)


def play_game():
    # initialize dictionary to hold players and their cards
    game = {}

    # initialize player number variable
    pnum = 0


    # shuffle a new deck of cards
    deck_id, numplayers = new_game()

    numcards = 5 

    game[1] = draw_cards(numcards, deck_id, pnum)

    shuffle_deck(deck_id)

    game[1] = draw_cards(numcards, deck_id, pnum)

#    # draw cards for each player
#    for i in range(int(numplayers)):
#        pnum += 1
#        game[pnum] = draw_cards(numcards, deck_id, pnum)
#
#    # print out the cards in play for each player
#    print("The following cards are in play:")
#    for k, v in game.items():
#        hand = ""
#        for i in v:
#            hand = hand + i + " "
#        print("Player #" + str(k), "=>", hand)


if __name__ == "__main__":
    play_game()
