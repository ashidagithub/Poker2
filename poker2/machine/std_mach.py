# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   定义标准发牌机的动作函数
# ------------------------(max to 80 columns)-----------------------------------

# import some external moduls
import random
import codecs
import os

def create_deck(new_deck):
    '推出一副新牌'
    print('\n -- debug: I made a new deck.')

    # initialize var
    cardJokers = ('♞', '♘')
    cardMarks = ('♠', '♥', '♣', '♦')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n -- debug: I shuffled a deck')

    random.shuffle(deck_to_be_shuffled)
    return


def record_deck(deck_to_be_record, filename):
    '记录一副牌'
    print('\n -- debug: I record a deck')

    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close

    return
