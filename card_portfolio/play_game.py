from tarokka_data import tarokka_low_deck, tarokka_high_deck
from images import opening_title, clean_table, one_card_down, two_cards_down, three_cards_down, four_cards_down, five_cards_down, one_card_up, two_cards_up, three_cards_up, four_cards_up, five_cards_up, full_tri_table_down, clean_tri_table, pick_1, pick_2, pick_3
import random





def play_game():
    
    pulled_card_library = []
    round_1l = []
    round_2l = []
    round_3l = []
    round_4l = []
    round_5l = []






    input("To begin, press Enter/Return key")
    print(opening_title)
    input("Press Enter to continue")
    print("The mystical woman stares into your eyes as she splits the deck in two.\nShe shuffles each deck separately in front of her.")
    random.shuffle(tarokka_low_deck)
    random.shuffle(tarokka_high_deck)
    print("From the first deck, she begins to deal the cards and explains...\n")
    input("Press Enter to continue")
    print(clean_table)
    print("\"I will deal cards into five stacks. Each stack represents three potential futures that you will decipher here today.\"")
    input("Press Enter to continue")
    print(one_card_down)
    print("\"For you who will choose from these, this card will tell of history.\"")
    input("Press Enter to continue")
    print(two_cards_down)
    print("\"Let they who choose this card reveal holy protection.\"")
    input("Press Enter to continue")
    print(three_cards_down)
    print("\"The hero who chooses this card may find vengeance.\"")
    input("Press Enter to continue")
    print(four_cards_down)
    print("She sets down the larger deck and picks up the smaller. She places another card. \"The brightest light...,\"")
    input("Press Enter to continue")
    print(five_cards_down)
    print("\"... and the blackest night.\" She sets down the smaller deck, and stares at you intensely. \"Who will choose first?\"")
    input("Press Enter to continue")
    print(clean_tri_table)
    print("\"Pay attention now, I will be placing three cards in front of you. I can only present possibilities, it is you who will determine your fate. Are you ready?\"")
    input("Press Enter to continue")


    def round1():
        for x in range(3):
            round_1l.append(tarokka_low_deck.pop(0))

        print(full_tri_table_down + "\n")
        
        while True:
            r1input = input("\"Choose from the three cards in front of you\": ")
            if r1input not in ('1', '2', '3'):
                print("Try again.")
            else:
                break


        if r1input == "1":
            pulled_card_library.append(round_1l[0])
            print(pick_1)
        elif r1input == "2":
            pulled_card_library.append(round_1l[1])
            print(pick_2)
        elif r1input == "3":
            pulled_card_library.append(round_1l[2])
            print(pick_3)

        card = pulled_card_library[0]
        return "\"You have revealed the {name} card, hero. This is the {namealt} card. This card tells of history. Knowledge of the ancient will help you better understand your enemy. {description}\"".format(name=card.name, namealt=card.namealt, description=card.description)
      
    print(round1())
    # print(round_1l)
    input("Press Enter to continue")
    print(one_card_up)
    print("She turns and faces you before taking the next stack of cards in her hand.")
    input("Press Enter to continue")

    def round2():
        for x in range(3):
            round_2l.append(tarokka_low_deck.pop(0))

        print(full_tri_table_down + "\n")
        
        while True:
            r1input = input("\"Choose from the three cards in front of you\": ")
            if r1input not in ('1', '2', '3'):
                print("Try again.")
            else:
                break


        if r1input == "1":
            pulled_card_library.append(round_2l[0])
            print(pick_1)
        elif r1input == "2":
            pulled_card_library.append(round_2l[1])
            print(pick_2)
        elif r1input == "3":
            pulled_card_library.append(round_2l[2])
            print(pick_3)

        card = pulled_card_library[1]
        return "\"A bit of luck brings you the {name}. This one is also known as the {namealt} card. This card tells of a powerful force for good and protection, a holy symbol of great hope. {description}\"".format(name=card.name, namealt=card.namealt, description=card.description)

    print(round2())
    # print(round_2l)
    input("Press Enter to continue")
    print(two_cards_up)
    print("With two cards chosen, she turns to her next player...")
    input("Press Enter to continue")

    def round3():
        for x in range(3):
            round_3l.append(tarokka_low_deck.pop(0))

        print(full_tri_table_down + "\n")
        
        while True:
            r1input = input("\"Choose from the three cards in front of you\": ")
            if r1input not in ('1', '2', '3'):
                print("Try again.")
            else:
                break


        if r1input == "1":
            pulled_card_library.append(round_3l[0])
            print(pick_1)
        elif r1input == "2":
            pulled_card_library.append(round_3l[1])
            print(pick_2)
        elif r1input == "3":
            pulled_card_library.append(round_3l[2])
            print(pick_3)

        card = pulled_card_library[2]
        return "\"I'm not surprised to see you've chosen the {namealt}, that's what they call the {name}. It's hardly the first time the {namealt} has revealed itself. This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight. {description}\"".format(name=card.name, namealt=card.namealt, description=card.description)   

    print(round3())
    # print(round_3l)
    input("Press Enter to continue")
    print(three_cards_up)
    print("Her expression becomes dour, as she prepares the next stack. There is a reverence she has to cards from the smaller deck, as if the secrets they hold are more valuable.")
    input("Press Enter to continue")

    def round4():
        for x in range(3):
            round_4l.append(tarokka_high_deck.pop(0))

        print(full_tri_table_down + "\n")
        
        while True:
            r1input = input("\"Choose from the three cards in front of you\": ")
            if r1input not in ('1', '2', '3'):
                print("Try again.")
            else:
                break


        if r1input == "1":
            pulled_card_library.append(round_4l[0])
            print(pick_1)
        elif r1input == "2":
            pulled_card_library.append(round_4l[1])
            print(pick_2)
        elif r1input == "3":
            pulled_card_library.append(round_4l[2])
            print(pick_3)

        card = pulled_card_library[3]

        pulled_card_options = [card.edesca, card.edescb]
    
        if len(card.edescb) > 1:
            choice = random.choice(pulled_card_options)
            card.description = choice
        else:
            card.description = card.edesca

        return "\"This card, yes. The {name} is a great boon for you. If you can find them, this card sheds light on one who will help you greatly in the battle against darkness. {description}\"".format(name=card.name, description=card.description)
        
    print(round4())
    input("Press Enter to continue")
    print(four_cards_up)
    print("You notice a nearly imperceptible shudder as she prepares and arranges the final three cards.")
    input("Press Enter to continue")


    def round5():
        for x in range(3):
            round_5l.append(tarokka_high_deck.pop(0))

        print(full_tri_table_down + "\n")
        
        while True:
            r1input = input("\"Choose from the three cards in front of you\": ")
            if r1input not in ('1', '2', '3'):
                print("Try again.")
            else:
                break


        if r1input == "1":
            pulled_card_library.append(round_5l[0])
            print(pick_1)
        elif r1input == "2":
            pulled_card_library.append(round_5l[1])
            print(pick_2)
        elif r1input == "3":
            pulled_card_library.append(round_5l[2])
            print(pick_3)

        card = pulled_card_library[4]
        card.description = card.location
        return "\"Take heed and be careful with the information I share with you now. You have selected the {name}. Your enemy is a creature of darkness, whose powers are beyond mortality. This card will lead you to him! {description}\"".format(name=card.name, description=card.description)
        
    print(round5())
    input("Press Enter to continue")
    print(five_cards_up)

    for card in pulled_card_library:
        print("You pulled the " + card.name)

    print("Thanks for playing!")
    


play_game()








