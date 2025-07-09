label shop:

    $ config.menu_include_disabled = True
    $ reward_cost = max(wins, 3)

    menu:
        "What do you want to do?"

        "Buy a card (-$[reward_cost])
        {tooltip}Add 1 card to your deck ([Player.shop_card_choices] choices)" if money >= reward_cost:
            $ money -= reward_cost
            $ config.menu_include_disabled = False
            call screen add_card

        "Upgrade a card (-$[reward_cost * 2])
        {tooltip}Upgrade 1 card in your deck ([Player.shop_card_choices] choices)" if money >= reward_cost * 2:
            python:
                money -= reward_cost * 2
                config.menu_include_disabled = False
                upgrade_card_type = renpy.random.choice(
                    ["all"] * 1 +
                    ["consensus"] * 6 +
                    ["cost"] * 1 +
                    ["draw"] * 3 +
                    ["energy"] * 3 +
                    ["stun"] * 1 +
                    ["times"] * 1 +
                    []
                )
                upgrade_card_value = renpy.random.randint(1, 3)
            call screen upgrade_card

        "Remove a card (-$[reward_cost * 3])
        {tooltip}Remove 1 card from your deck" if money >= reward_cost * 3:
            $ money -= reward_cost * 3
            $ config.menu_include_disabled = False
            call screen remove_card

        "Battle":
            $ config.menu_include_disabled = False
            $ Level.next()
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
            for card in Card.generate(Player.shop_card_choices):
                button:
                    action [Function(deck.cards.append, card), Jump("shop")]
                    use card_frame(card)

        null height 25

        frame:
            xalign 0.5
            textbutton "Pass":
                action Jump("shop")

screen upgrade_card:

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        text Card.label_upgrade(upgrade_card_type, upgrade_card_value)

        null height 25

        hbox:
            spacing 25

            for card in deck.get_cards(Player.shop_card_choices, upgrade_card_type):
                button:
                    action [Function(card.upgrade, upgrade_card_type, upgrade_card_value), Jump("shop")]
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
