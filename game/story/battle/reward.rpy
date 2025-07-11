label reward:

    if not rewards:
        jump shop

    menu:
        "Select a reward:"

        "Moves {color=[colors.moves]}+1
        {tooltip}Increase your moves from [player.moves_max] to [player.moves_max + 1]":
            $ player.moves_max += 1

        "Turns {color=[colors.moves]}+1
        {tooltip}Increase your turns from [player.turns_max] to [player.turns_max + 1]":
            $ player.turns_max += 1

        "Draw cards {color=[colors.moves]}+1
        {tooltip}Increase drawn cards per hand from [player.draw_cards] to [player.draw_cards + 1]":
            $ player.draw_cards += 1

        "Buy/upgrade cards {color=[colors.moves]}+1
        {tooltip}Increase buy/upgrade card choices from [player.shop_card_choices] to [player.shop_card_choices + 1]":
            $ player.shop_card_choices += 1

        "Pass":
            pass

    $ rewards -= 1

    jump reward
