define battle = False

label battle:

    $ battle = True

    scene bg teachers room day with dissolve

    show screen player_stats

    $ Level.start()

    jump player_turn
