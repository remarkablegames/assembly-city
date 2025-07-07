label reward:

    if not rewards:
        jump shop

    menu:
        "Claim a reward:"

        "Moves {color=[colors.moves]}+1
        {tooltip}Increase moves from [Player.moves_max] to [Player.moves_max + 1]":
            $ Player.moves_max += 1

        "Turns {color=[colors.moves]}+1
        {tooltip}Increase turns from [Player.turns_max] to [Player.turns_max + 1]":
            $ Player.turns_max += 1

        "Draw cards {color=[colors.moves]}+1
        {tooltip}Increase draw cards from [Player.draw_cards] to [Player.draw_cards + 1]":
            $ Player.draw_cards += 1

        "Buy/upgrade cards {color=[colors.moves]}+1
        {tooltip}Increase buy/upgrade card choices from [Player.shop_card_choices] to [Player.shop_card_choices + 1]":
            $ Player.shop_card_choices += 1

        "Pass":
            pass

    $ rewards -= 1

    jump reward
