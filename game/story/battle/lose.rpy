label lose:

    hide screen player_end_turn
    hide screen player_stats
    hide screen player_money

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2
    hide screen citizen_stats3

    "You weren’t able to reach a consensus."

    if level.current == 0:
        hide commissioner idle
        show commissioner smile 1 with dissolve
        jump tutorial_questions

    scene black with fade

    jump end
