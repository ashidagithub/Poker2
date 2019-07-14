# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   模拟一个发牌机器和一个发牌员的场景
# ------------------------(max to 80 columns)-----------------------------------

from machine.std_mach import create_deck, \
    shuffled_deck, \
    record_deck

from dealer.mike import deal_to_a_player, deal_to_multi_players

# 场景一:
# 拿出一副新牌，记录； 洗牌，再记录
first_deck = []
create_deck(first_deck)
record_deck(first_deck, "deck-001.txt")

shuffled_deck(first_deck)
record_deck(first_deck, "deck-002.txt")

'''
# 场景二
Steven_deck =[]
deal_to_a_player(first_deck, 5, Steven_deck)
record_deck(Steven_deck, "Steven_deck.txt")

Vivian_deck =[]
deal_to_a_player(first_deck, 5, Vivian_deck)
record_deck(Vivian_deck, "Vivian_deck.txt")
'''

# 场景三
Steven_deck = []
Vivian_deck = []
Monica_deck = []
Jimmy_deck = []

deal_to_multi_players(first_deck, Steven_deck,
                      Vivian_deck, Monica_deck)
record_deck(Steven_deck, "Steven_deck.txt")
record_deck(Vivian_deck, "Vivian_deck.txt")
record_deck(Monica_deck, "Monica_deck.txt")
record_deck(Jimmy_deck, "Jimmy_deck.txt")
