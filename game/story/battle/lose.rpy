label lose:

    if level.current:
        stop music fadeout 4

    hide screen tutorial_battle

    hide screen player_end_turn
    hide screen player_stats
    hide screen player_money

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2
    hide screen citizen_stats3
    hide screen citizen_stats4

    "You weren’t able to reach a consensus."

    if level.current:
        play music "music/BGM8 Harukaze.ogg" volume 0.5 fadein 1

    if level.current == 0:
        jump tutorial_battle_end

    jump end
