label end:

    stop music fadeout 4

    hide screen player_end_turn
    hide screen player_stats
    hide screen player_money

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2
    hide screen citizen_stats3
    hide screen citizen_stats4

    if level.data():
        call end_bad
    else:
        call end_good

    $ level.restart()

    scene black

    "{b}End{/b}."

    return


label end_good:

    return


label end_bad:

    return
