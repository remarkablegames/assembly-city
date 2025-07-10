init python:
    from math import ceil

default money = 0
default bonus = 0
default interest = 0
default rewards = 0
default wins = 0

label win:

    hide screen player_end_turn
    hide screen player_stats

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2
    hide screen citizen_stats3

    "You were able to reach a consensus!"

    if Level.level == 0:
        hide commissioner idle
        show commissioner smile 1 with dissolve
        jump tutorial_questions

    scene bg hall day
    with fade

    show screen player_money

    show commissioner smile 1
    with dissolve

    $ commissioner(renpy.random.choice(["Nice work!", "Great job!", "Good stuff!", "Amazing run!", "Excellent effort!"]))

    $ wins += 1
    $ interest = ceil(money * 0.4)
    $ bonus = renpy.random.randint(wins, round(wins * 1.5) + 1)
    $ money += bonus + interest

    commissioner "You earned $[bonus] + $[interest] (interest)."

    if wins % 5 == 0:
        $ rewards += 1
        jump reward

    jump shop
