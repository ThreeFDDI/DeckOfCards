#!/usr/local/bin/python3
""" 
Let's play cards! 

Example script using deckofcardsapi.com
"""

import requests


def new_deck(numdecks):
    """
    function to create a new deck and return the deck_id
    """
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
    print(f"\nYou've shuffled a new deck! Deck id: {deck_id}\n")

    return deck_id


def draw_cards(numcards, deck_id, pnum):
    """
    function to draw cards
    """
    # init list of player's cards
    pnumcards = []

    # URL to draw cards from deck
    url = (
        "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/"
    )  # URL to draw cards

    # parameter for number of cards
    querystring = {"count": numcards}

    # send GET request
    draw = requests.request("GET", url, params=querystring).json()

    # print the number and suit of each card drawn
    for i in draw["cards"]:  # parse HTTP response;
        print(
            "Player #"
            + str(pnum)
            + " drew the "
            + i["value"]
            + " of "
            + i["suit"]
            + "!"
        )
        # Add card code to list of all cards drawn
        pnumcards.append(i["code"])

    # print the number of remaining cards in the deck
    print(f"\nThere are {str(draw['remaining'])} cards remaining in the deck.\n")

    return pnumcards


def play_game():
    # Prompt user and set variable for number of players
    # numplayers = raw_input("\nHow many players will there be: ")
    numplayers = 3  # Lazy mode

    # Prompt user and set variable for number of decks to shuffle
    # numdecks = raw_input("\nHow many decks would you like to shuffle: ")
    numdecks = 1  # Lazy mode

    # Prompt user and set variable for number of cards to draw
    # numcards = raw_input("\nHow many cards would you like to draw: ")
    numcards = 5  # Lazy mode

    # set the total number of cards based on number of decks
    totalcards = int(numdecks) * 52

    # initialize dictionary to hold players and their cards
    game = {}

    # initialize player number variable
    pnum = 0

    # Repeat back the variable input by the user.
    print(
        "\nPreparing to shuffle "
        + str(numdecks)
        + " decks for a total of "
        + str(totalcards)
        + " cards. There will be "
        + str(numplayers)
        + " players drawing "
        + str(numcards)
        + " cards each."
    )

    # shuffle a new deck of cards
    deck_id = new_deck(numdecks)

    # draw cards for each player
    for i in range(int(numplayers)):
        pnum += 1
        game[pnum] = draw_cards(numcards, deck_id, pnum)

    # print out the cards in play for each player
    print("The following cards are in play:")
    for k, v in game.items():
        hand = ""
        for i in v:
            hand = hand + i + " "
        print("Player #" + str(k), "=>", hand)


if __name__ == "__main__":
    play_game()
