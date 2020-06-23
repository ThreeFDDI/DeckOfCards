#!/usr/local/bin/python3
""" 
Let's play cards! 

Example script using deckofcardsapi.com
"""

import requests


# function to create a new deck and return the deck_id
def new_deck(numdecks):
    # URL to generat a new deck
    url = (
        "https://deckofcardsapi.com/api/deck/new/shuffle/"  
    )

    querystring = {"deck_count": numdecks}  # added numdecks variable

    response = requests.request(
        "GET", url, params=querystring
    )

    deck = response.json()
    deck_id = deck["deck_id"]

    
    # Print deck id
    print("\nYou've shuffled a new deck! Deck id: " + deck_id + "\n")  

    return deck_id


def draw_cards(numcards, deck_id, pnum):

    pnumcards = []

    url2 = (
        "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/"
    )  # URL to draw cards

    querystring2 = {"count": numcards}  # added numcards variable

    draw = requests.request(
        "GET", url2, params=querystring2
    ).json()

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
    print(
        f"\nThere are {str(draw['remaining'])} cards remaining in the deck.\n"
    )  

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

    # run the new_deck function to start
    deck_id = new_deck(numdecks)  

    for i in range(int(numplayers)):
        pnum += 1
        game[pnum] = draw_cards(numcards, deck_id, pnum)

    print("The following cards are in play:")

    for k, v in game.items():
        hand = ""
        for i in v:
            hand = hand + i + " "
        print("Player #" + str(k), "=>", hand)


if __name__ == "__main__":
    play_game()

