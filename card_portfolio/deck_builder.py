suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
bicycle_values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

tarokka_suits = ["Coins", "Glyphs", "Stars", "Swords"]
tarokka_lows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Master"]
tarokka_highs = ["Artifact", "Beast", "Broken One", "Darklord", "Donjon", "Seer", "Ghost", "Executioner", "Horseman", "Innocent", "Marionette", "Mists", "Raven", "Tempter"]

def deck_builder(suits, basic_values, jokers, single_values = []):
    separate_decks = [[], [], []]
    finished_deck = []
    joker = 0

    for suit in suits:
        for value in basic_values:
            separate_decks[0].append("{value} of {suit}".format(value=value, suit=suit))

    while joker < jokers:
        separate_decks[1].append("Joker")
        joker += 1

    if len(single_values) > 0:
        for value in single_values:
            separate_decks[2].append(value)

    return separate_decks


# bicycle = deck_builder(suit_list, bicycle_values, 2)

# for card in bicycle:
#     print(card)

# tarokka = deck_builder(tarokka_suits, tarokka_lows, 0, tarokka_highs)

# for clist in tarokka:
#     print(clist)

