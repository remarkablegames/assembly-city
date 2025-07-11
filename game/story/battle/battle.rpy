define battle = False

label battle:

    hide screen player_money

    $ battle = True

    if level.current > 0:
        scene bg teachers room day with dissolve

    show screen player_stats

    $ level.start()

    jump player_turn
