define battle = False

label battle:

    $ battle = True

    scene bg teachers room day with dissolve

    show screen player_stats

    $ Level.start()
    $ citizens.show()
    $ Player.moves = Player.moves_max
    $ deck.shuffle()

    jump player_turn
