define battle = False

label battle:

    hide screen player_money

    $ battle = True
    $ level.start()

    show screen player_stats

    jump player_turn
