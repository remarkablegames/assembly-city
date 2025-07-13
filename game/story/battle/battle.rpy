label battle:

    if level.current:
        play music "music/BGM10 Let's enjoy Camping!.ogg" volume 0.5 fadein 1

    hide screen player_money

    $ level.start()

    show screen player_stats

    jump player_turn
