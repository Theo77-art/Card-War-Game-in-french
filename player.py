import random


class Player:
    def __init__(self, hand, name):
        self.__hand = hand
        self.__name = name

    def get_hand(self):

        cards = ""

        for card in self.__hand:
            cards += f" {card.get_card()} ,"

        return f"{self.__name} possède les cartes suivantes {cards}"

    def get_number_of_card_in_hand(self):
        return len(self.__hand)

    def get_name(self):
        return self.__name

    def draw_a_card(self):
        card = self.__hand[0]
        self.__hand.pop(0)

        return card

    def take_cards(self, cards):

        if isinstance(cards, list):
            for card in cards:
                self.__hand.append(card)

        else:
            self.__hand.append(cards)

    def shuffle_player_hand(self):
        if len(self.__hand) > 2:
            random.shuffle(self.__hand)
