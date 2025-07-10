define battle = False

label battle:

    hide screen player_money

    $ battle = True

    if Level.level > 0:
        scene bg teachers room day with dissolve

    show screen player_stats

    $ Level.start()

    jump player_turn
