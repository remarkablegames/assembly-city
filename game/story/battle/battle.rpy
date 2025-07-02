define battle = False

label battle:

    $ battle = True

    scene bg teachers room day with dissolve

    show screen player_stats

    $ citizens.show()
    $ player.character.moves = player.character.moves_max
    $ deck.shuffle()

    jump player_turn
