init python:
    from math import ceil

default money = 0
default loot = 0
default interest = 0
default rewards = 0
default wins = 0

label win:

    hide screen player_end_turn
    hide screen player_stats

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2

    "You were able to reach a consensus!"

    if Level.level == 0:
        hide commissioner idle
        show commissioner smile 1 with dissolve
        jump tutorial_questions

    show screen player_money

    $ wins += 1
    $ interest = ceil(money * 0.4)
    $ loot = renpy.random.randint(wins, round(wins * 1.5) + 1)
    $ money += loot + interest

    "You earned $[loot] + $[interest] (interest)."

    if wins % 3 == 1:
        $ rewards += 1
        jump reward

    else:
        jump shop
