label reward:

    show commissioner smile 1

    if level.current == 1:
        commissioner "We make sure assembly participants are fairly compensated for their time."
        commissioner "I also included a bonus if you went beyond the consensus goal."
        commissioner "Managing the citizens’ energy levels can be tricky."

        show commissioner smile 1 at left
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
                show commissioner smile 1 at center
                with moveinright
                commissioner @ smile 3 "I hope it comes handy!"

            "No":
                commissioner "Alright."

        jump shop

    elif level.current == 2:
        commissioner "Experts provide context to help citizens make informed decisions."

        show commissioner smile 1 at left
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
                show commissioner smile 1 at center
                with moveinright
                commissioner @ smile 3 "Make good use of it!"

            "No":
                commissioner "Sounds good."

    elif level.current == 3:
        commissioner "Citizens vote on recommendations to decide if they should be included in the final report."

        show commissioner smile 1 at left
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
                show commissioner smile 1 at center
                with moveinright
                commissioner @ smile 3 "Good luck!"

            "No":
                commissioner "All good."

    else:
        jump shop

label reward_player:

    menu:
        "Select an upgrade:"

        "Moves +1
        {tooltip}Increase your moves from [player.moves_max] to [player.moves_max + 1]":
            $ player.moves_max += 1

        "Turns +1
        {tooltip}Increase the number of turns by 1":
            $ player.turns_max += 1

        "Draw cards +1
        {tooltip}Increase cards per hand and card choices in shop from [player.draw_cards] to [player.draw_cards + 1]":
            $ player.draw_cards += 1

        "Pass":
            pass

    jump shop
