init python:
    from math import ceil

default money = 0
default bonus = 0

label win:

    hide screen player_end_turn
    hide screen player_stats

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2
    hide screen citizen_stats3
    hide screen citizen_stats4

    "You were able to reach a consensus!"

    if level.current == 0:
        hide commissioner idle
        show commissioner smile 1 with dissolve
        jump tutorial_questions

    scene bg hall day
    with fade

    show screen player_money

    show commissioner smile 1
    with dissolve

    $ bonus = level.consensus("current") - level.consensus("goal")
    $ money += max(level.current, 3) + bonus
    $ dialogue = renpy.random.choice(["Nice work!", "Great job!", "Good stuff!", "Amazing run!", "Excellent effort!"])

    commissioner "[dialogue]"
    commissioner "You earned $[max(level.current, 3)] + $[bonus] (bonus)."

    jump reward
