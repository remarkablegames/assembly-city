label reward:

    if level.current == 1:
        jump reward_pizza

    elif level.current == 2:
        jump reward_expert

    elif level.current == 3:
        jump reward_upgrade

    elif level.current == 4:
        jump reward_vote

    jump shop


label reward_upgrade:

    commissioner @ smile 2 "Select 1 of 3 upgrades that can help you facilitate an assembly."

    menu:
        "Choose an upgrade:"

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

    commissioner @ smile 3 "Great choice!"

    jump shop


label reward_pizza:

    commissioner "Managing the citizens’ energy levels can be tricky."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="pizza", cost=2, action={"energy": {"value": 3, "all": True}, "draw": {"value": 1}})
    show screen card(card, 0.75)

    commissioner "Pizza can raise the energy of all participants."

    menu:
        "Add this card to your deck?"

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


label reward_expert:

    commissioner "Experts provide context to help citizens make informed decisions."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="expert", cost=2, action={"consensus": {"value": 4, "stun": True}, "energy": {"value": -2}})
    show screen card(card, 0.75)

    commissioner "An expert can stun a participant with facts and logic."

    menu:
        "Add this card to your deck?"

        "Yes":
            $ deck.cards.append(card)
            queue sound "sound/draw.ogg"
            hide screen card
            show commissioner smile 1 at center
            with moveinright
            commissioner @ smile 3 "Make good use of it!"

        "No":
            commissioner "Sounds good."

    jump shop


label reward_vote:

    commissioner "Citizens vote on recommendations to decide if they should be included in the final report."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="vote", cost=2, action={"consensus": {"value": 4, "all": True}, "energy": {"value": -2, "all": True}})
    show screen card(card, 0.75)

    commissioner "Voting can help the group come to a decision."

    menu:
        "Add this card to your deck?"

        "Yes":
            $ deck.cards.append(card)
            queue sound "sound/draw.ogg"
            hide screen card
            show commissioner smile 1 at center
            with moveinright
            commissioner @ smile 3 "Good luck!"

        "No":
            commissioner "All good."

    jump shop
