from deck import Deck
from player import Player


class Game:
    def __init__(self):
        hands = self.__prepare_cards()
        self.__player1 = Player(hands[0], "Joueur 1")
        self.__player2 = Player(hands[1], "Joueur 2")
        self.__turn_count = 0
        self.__in_game_cards = []
        self.__cards_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi", "As"]

    def __prepare_cards(self):
        deck = Deck()
        deck.shuffle()
        hands = deck.deal_all_cards_equally()

        return hands

    def __compare_cards(self, card1, card2):
        index_card1 = self.__cards_values.index(card1)
        index_card2 = self.__cards_values.index(card2)

        if index_card1 > index_card2:
            return 1

        elif index_card1 < index_card2:
            return 2

        else:
            return 0

    def __is_a_player_won(self):

        if self.__player1.get_number_of_card_in_hand() == 0 or self.__player2.get_number_of_card_in_hand() == 0:
            return True

        else:
            return False

    def __get_number_card_in_game(self):

        return len(self.__in_game_cards)

    def __get_turn_count(self):
        return self.__turn_count

    def __start(self):
        input("Appuyez sur n'importe quel touche pour commencer la partie")

    def run(self):

        self.__start()

        while not self.__is_a_player_won():

            if self.__get_turn_count() % 100 != 0:
                self.__player1.shuffle_player_hand()
                self.__player2.shuffle_player_hand()
                print("mélange des main des joueurs")

            self.turn()
            print(f"Le joueur 1 possède {self.__player1.get_number_of_card_in_hand()}")
            print(f"Le joueur 2 possède {self.__player2.get_number_of_card_in_hand()}")
            print(f"Tour n°{self.__get_turn_count()} , il y a {self.__get_number_card_in_game()} en jeu")
            input("Appuyez sur n'importe quel touche pour continuez")

        self.stop()

    def turn(self):
        card1 = self.__player1.draw_a_card()
        card2 = self.__player2.draw_a_card()
        self.__in_game_cards.append(card1)
        self.__in_game_cards.append(card2)

        print(f" {card1.get_card()} vs {card2.get_card()}")

        if self.__compare_cards(card1.get_value(), card2.get_value()) == 1:
            self.__player2.take_cards(self.__in_game_cards)
            self.__in_game_cards.clear()

            print("le joueur 1 gagne cette bataille")

        elif self.__compare_cards(card1.get_value(), card2.get_value()) == 2:
            self.__player1.take_cards(self.__in_game_cards)
            self.__in_game_cards.clear()

            print("le joueur 2 gagne cette bataille")

        else:
            print("égalité")

        self.__turn_count += 1

    def stop(self):
        if self.__player1.get_number_of_card_in_hand() == 0:
            print(f"Le joueur 1 a gagné en {self.__turn_count} tours")

        if self.__player2.get_number_of_card_in_hand() == 0:
            print(f"Le joueur 2 a gagné en {self.__turn_count} tours")

        print("partie terminée")