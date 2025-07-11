label reward:

    if level.current == 1:
        commissioner "Managing the citizens’ energy levels can be hard."

        show commissioner at left
        with moveinleft

        $ card = Card(image="pizza", cost=2, action={"energy": {"value": 3, "all": True}, "draw": {"value": 1}})
        show screen card(card, 0.75)

        commissioner "Pizza can raise the energy of all participants."

        menu:
            "Would you like to add this card to your deck?"

            "Yes":
                $ deck.cards.append(card)
                queue sound "sound/draw.ogg"
                hide screen card
                show commissioner at center
                with moveinright
                commissioner @ smile 3 "I hope it comes handy!"

            "No":
                commissioner "Alright."

        jump shop

    elif level.current == 2:
        commissioner "Experts provide context to help citizens make informed decisions."

        show commissioner at left
        with moveinleft

        $ card = Card(image="expert", cost=2, action={"consensus": {"value": 4, "stun": True}, "energy": {"value": -2}})
        show screen card(card, 0.75)

        commissioner "An expert can stun a participant with facts and logic."

        menu:
            "Would you like to add this card to your deck?"

            "Yes":
                $ deck.cards.append(card)
                queue sound "sound/draw.ogg"
                hide screen card
                show commissioner at center
                with moveinright
                commissioner @ smile 3 "Make good use of it!"

            "No":
                commissioner "Sounds good."

    elif level.current == 3:
        commissioner "Citizens vote on recommendations to decide if they should be included in the final report."

        show commissioner at left
        with moveinleft

        $ card = Card(image="vote", cost=2, action={"consensus": {"value": 4, "all": True}, "energy": {"value": -2, "all": True}})
        show screen card(card, 0.75)

        commissioner "Voting can help the group come to a decision."

        menu:
            "Would you like to add this card to your deck?"

            "Yes":
                $ deck.cards.append(card)
                queue sound "sound/draw.ogg"
                hide screen card
                show commissioner at center
                with moveinright
                commissioner @ smile 3 "Good luck!"

            "No":
                commissioner "All good."

    else:
        jump shop

label reward_player:

    menu:
        "Select a reward:"

        "Moves {color=[colors.moves]}+1
        {tooltip}Increase your moves from [player.moves_max] to [player.moves_max + 1]":
            $ player.moves_max += 1

        "Turns {color=[colors.moves]}+1
        {tooltip}Increase your turns by 1":
            $ player.turns_max += 1

        "Draw cards {color=[colors.moves]}+1
        {tooltip}Increase drawn cards per hand from [player.draw_cards] to [player.draw_cards + 1]":
            $ player.draw_cards += 1

        "Buy/upgrade cards {color=[colors.moves]}+1
        {tooltip}Increase buy/upgrade card choices from [player.shop_card_choices] to [player.shop_card_choices + 1]":
            $ player.shop_card_choices += 1

        "Pass":
            pass

    jump shop
