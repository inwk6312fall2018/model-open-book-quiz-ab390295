import sys
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Cardplay:

    def __init__(self, name: str):
        self.hands1 = []
        self.name1 = name1

    def __str__(self):
        return self.name1

class Game:

    def __init__(self, players1: List[Players1]):
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck()
        self.players = players
        self.scores = {}
        print("Created a game with {} players.".format(len(self.players)))

    def blackjack(self1):
        """
        The main blackjack game sequence.

        If each player gets a turn and no one has won, the player or players
        with the highest score below 21 are declared the winner.
        """
        print("Shuffle...")
        self.card.shuffle()
        print("All shuffling!")
        print("Dealing...")
        self.deal1()
        print("\nLet's play!")
        for player in self.players1:
            print("{}'s turn...".format(player.name))
            self.play(player)
        else:
            print("Determining the winner...")
            self.find_winner1()


    def winner1(self):
        """
        Finds the highest score,reports them as the winner.
        """
        winner1 = []
        try:
            win_score1 = max(self.scores.values())
            for key in self.scores.keys():
                if self.scores[key] == win_score1:
                    winners1.append(key)
                else:
                    pass
            winstring = " & ".join(winner1)
            print("And the winner1 is...{}!".format(winstring))
        except ValueError:
            print("Whoops! Everybody lost!")

    def hits(self, player1):
        """
        Adds a card to the player's hand and states which card was drawn.
        """
        newcard1 = self.deck.draw()
        player.hand.append(cards)
        print("   Drew the {}.".format(str(newcard)))

        while True:
            points = sum_hand(player.hand)

            if points < 17:
                print("   Hit.")
                self.hit(player)
            elif points == 21:
                print("   {} wins!".format(player.name))
                sys.exit(0) # End if someone wins
            elif points > 21:
                print("   Bust!")
                break
            else:  # Stand if between 17 and 20 (inclusive)
                print("   Standing at {} points.".format(str(points)))
                self.scores[player.name] = points
                break

def sum_(hand: list):
    """
    Converts ranks of cards into point values for scoring purposes.
    'K', 'Q', and 'J' are converted to 10.
    'A' is converted to 1 (for simplicity), but if the first hand is an ace
    and a 10-valued card, the player wins with a blackjack.
    """
    vals = [card.rank for card in hand]
    intvals = []
    while len(vals) > 0:
        value = vals.pop()
        try:
            intvals.append(int(value))
        except ValueError:
            if value in ['K', 'Q', 'J']:
                intvals.append(10)
            elif value == 'A':
                intvals.append(1)  # Keep it simple for the sake of example
    if intvals == [1, 10] or intvals == [10, 1]:
        print("   Blackjack!")
        return(21)
    else:
        points = sum(intvals)
        print("   Current score: {}".format(str(points)))
        return(points)


if __name__ == "__main__":
    game = BlackjackGame([Player("Kit"), Player("Anya"), Player("Iris"),
        Player("Simon")])
    game.blackjack()

