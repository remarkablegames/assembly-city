init python:
    from math import ceil

default money = 0
default bonus = 0

label win:

    hide screen tutorial_battle

    hide screen player_end_turn
    hide screen player_stats

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2
    hide screen citizen_stats3
    hide screen citizen_stats4

    "You were able to reach a consensus!"

    if level.current == 0:
        jump tutorial_battle_end

    stop music fadeout 4

    if level.current > 4:
        scene bg hall afternoon with fade
    else:
        scene bg hall day with fade

    show screen player_money

    play music "music/BGM8 Harukaze.ogg" volume 0.5 fadein 1

    show commissioner smile 1
    with dissolve

    $ bonus = level.consensus("current") - level.consensus("goal")
    $ base_reward = max(level.current, 3)
    $ money += base_reward + bonus
    $ dialogue = renpy.random.choice(["Nice work!", "Great job!", "Good stuff!", "Amazing run!", "Excellent effort!"])

    commissioner "[dialogue]"
    commissioner "You earned $[base_reward] + $[bonus] (bonus)."

    play audio "sound/cash.ogg" volume 0.5

    jump reward
