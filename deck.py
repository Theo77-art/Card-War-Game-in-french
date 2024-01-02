from card import Card
import random


class Deck:
    def __init__(self):
        self.__cards = []
        self.__init_deck()

    def __init_deck(self):
        values = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi"]
        colors = ["coeur", "carreau", "pique", "trèfle"]

        for color in colors:
            for value in values:
                self.__cards.append(Card(color, value))

    def __str__(self):
        print(self.__cards)

    ## DEBUG FUNCTION
    def get_length(self):
        return len(self.__cards)

    def get_cards(self):

        cards = ""

        for card in self.__cards:
            cards += f"{card.get_card()} ,"

        return cards

    ## UTILITY FUNCTION
    def shuffle(self):
        if len(self.__cards) > 2:
            random.shuffle(self.__cards)

    def deal_all_cards_equally(self):
        hands = [[], []]

        i = 0

        for card in self.__cards:
            if i % 2 == 0:
                hands[0].append(card)
            else:
                hands[1].append(card)

            i += 1

        self.__cards = []
        return hands

