label shop:

    show screen player_deck(0, 1.0)

    python:
        config.menu_include_disabled = True
        cost_base = max(level.current, 3)
        cost_card_buy = cost_base + player.cards_bought
        cost_card_upgrade = cost_base * 2 + player.cards_upgraded
        cost_card_remove = cost_base * 3 + player.cards_removed

    menu:
        "What do you want to do?"

        "Buy a card (-$[cost_card_buy])
        {tooltip}Add 1 card to your deck ([player.draw_cards] choices)" if money >= cost_card_buy:
            python:
                config.menu_include_disabled = False
                money -= cost_card_buy
                player.cards_bought += 1

            call screen add_card

        "Upgrade a card (-$[cost_card_upgrade])
        {tooltip}Upgrade 1 card in your deck (max [player.draw_cards] choices)" if money >= cost_card_upgrade:
            python:
                config.menu_include_disabled = False
                money -= cost_card_upgrade
                player.cards_upgraded += 1

                card_type = renpy.random.choice(
                    ["all"] * (1 if level.current > 3 else 0) +
                    ["consensus"] * 6 +
                    ["cost"] * (1 if level.current > 2 else 0) +
                    ["draw"] * 3 +
                    ["energy"] * 3 +
                    ["stun"] * (1 if level.current > 1 else 0) +
                    []
                )

                if card_type == "consensus":
                    card_value = renpy.random.randint(1, 3)
                elif card_type in ["draw", "energy"]:
                    card_value = renpy.random.randint(1, 2)
                else:
                    card_value = 1

            call screen upgrade_card(card_type, card_value)

        "Remove a card (-$[cost_card_remove])
        {tooltip}Remove 1 card from your deck" if money >= cost_card_remove:
            python:
                config.menu_include_disabled = False
                money -= cost_card_remove
                player.cards_removed += 1

            call screen remove_card

        "Run assembly":
            python:
                config.menu_include_disabled = False
                level.next()

            hide screen player_deck
            jump battle


screen add_card:

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        text "Add 1 card to your deck:"

        null height 25

        hbox:
            spacing 25
            for card in Card.generate(player.draw_cards):
                button:
                    action [Function(deck.cards.append, card), Jump("shop")]
                    use card_frame(card)

        null height 25

        frame:
            xalign 0.5
            textbutton "Pass":
                action Jump("shop")


screen upgrade_card(card_type, card_value):

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        text Card.label_upgrade(card_type, card_value)

        null height 25

        hbox:
            spacing 25

            for card in deck.get_cards(player.draw_cards, card_type):
                button:
                    action [Function(card.upgrade, card_type, card_value), Jump("shop")]
                    use card_frame(card)

        null height 25

        frame:
            xalign 0.5
            textbutton "Pass":
                action Jump("shop")


screen remove_card:

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        viewport:
            scrollbars "horizontal"
            ysize 450

            hbox:
                spacing 25

                for card in deck.cards:
                    button:
                        action [Function(deck.cards.remove, card), Jump("shop")]
                        use card_frame(card)

        null height 50

        frame:
            xalign 0.5
            textbutton "Pass":
                action Jump("shop")
