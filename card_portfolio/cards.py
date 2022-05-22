suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
bicycle_values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

def deck_builder(suits, values, jokers):
    finished_deck = []
    joker = 0

    for suit in suits:
        for value in values:
            finished_deck.append("{value} of {suit}".format(value=value, suit=suit))

    while joker < jokers:
        finished_deck.append("Joker")
        joker += 1

    return finished_deck


bicycle = deck_builder(suit_list, bicycle_values, 2)

for card in bicycle:
    print(card)


