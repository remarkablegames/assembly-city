label reward:

    if level.current == 1:
        call reward_deal

    elif level.current == 2:
        call reward_focus

    elif level.current == 3:
        call reward_upgrade

    elif level.current == 4:
        call reward_pizza

    elif level.current == 5:
        call reward_expert

    elif level.current == 6:
        call reward_upgrade

    elif level.current == 7:
        call reward_delay

    elif level.current == 8:
        call reward_vote

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
        {tooltip}Increase cards per hand to [player.draw_cards + 1] and shop cards from [player.draw_cards + 1]":
            $ player.draw_cards += 1
            $ player.shop_cards += 1

        "Skip":
            pass

    commissioner @ smile 3 "Great choice!"

    return


label reward_pizza:

    commissioner "Managing the citizens’ energy levels can be tricky."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="pizza", cost=2, action={"energy": {"value": 2, "all": True}, "draw": {"value": 2}})
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

        "No (+$5)
        {tooltip}Sell card and earn money":
            $ money += 5
            queue sound "sound/cash.ogg" volume 0.5
            hide screen card
            commissioner "Alright."

    return


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

        "No (+$5)
        {tooltip}Sell card and earn money":
            $ money += 5
            queue sound "sound/cash.ogg" volume 0.5
            hide screen card
            commissioner "Sounds good."

    return


label reward_vote:

    commissioner "Citizens vote on recommendations to decide if they should be included in the final report."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="vote", cost=2, action={"consensus": {"value": 3, "all": True}, "energy": {"value": -2, "all": True}})
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

        "No (+$5)
        {tooltip}Sell card and earn money":
            $ money += 5
            queue sound "sound/cash.ogg" volume 0.5
            hide screen card
            commissioner "All good."

    return


label reward_focus:

    commissioner "Sometimes you need to take a deep breath before moving forward."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="focus", cost=1, action={"moves": {"value": 2}, "energy": {"value": -1}})
    show screen card(card, 0.75)

    commissioner "Focus takes a bit of energy, but gives you an extra move."

    menu:
        "Add this card to your deck?"

        "Yes":
            $ deck.cards.append(card)
            queue sound "sound/draw.ogg"
            hide screen card
            show commissioner smile 1 at center
            with moveinright
            commissioner @ smile 3 "Take care!"

        "No (+$5)
        {tooltip}Sell card and earn money":
            $ money += 5
            queue sound "sound/cash.ogg" volume 0.5
            hide screen card
            commissioner "Makes sense."

    return


label reward_delay:

    commissioner "When deliberating, there are moments where you need more time."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="delay", cost=2, action={"turns": {"value": 1}, "energy": {"value": -2}})
    show screen card(card, 0.75)

    commissioner "Delay buys you extra turns, but you can only play it once per assembly."

    menu:
        "Add this card to your deck?"

        "Yes":
            $ deck.cards.append(card)
            queue sound "sound/draw.ogg"
            hide screen card
            show commissioner smile 1 at center
            with moveinright
            commissioner @ smile 3 "Use it wisely!"

        "No (+$5)
        {tooltip}Sell card and earn money":
            $ money += 5
            queue sound "sound/cash.ogg" volume 0.5
            hide screen card
            commissioner "Understood."

    return


label reward_deal:

    commissioner "There are times when compromise is necessary during a Citizens’ Assembly."

    show commissioner smile 1 at left
    with moveinleft

    $ card = Card(image="deal", cost=1, action={"consensus": {"value": -2}, "draw": {"value": 2}, "energy": {"value": 2}})
    show screen card(card, 0.75)

    commissioner "Deal lowers consensus, but energizes the participant and allows you to draw cards."

    menu:
        "Add this card to your deck?"

        "Yes":
            $ deck.cards.append(card)
            queue sound "sound/draw.ogg"
            hide screen card
            show commissioner smile 1 at center
            with moveinright
            commissioner @ smile 3 "You’re all set!"

        "No (+$5)
        {tooltip}Sell card and earn money":
            $ money += 5
            queue sound "sound/cash.ogg" volume 0.5
            hide screen card
            commissioner "Noted."

    return
