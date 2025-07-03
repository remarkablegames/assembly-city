screen stat(name, current, max):
    text "[name]: [current]/[max]"
    bar value AnimatedValue(current, max):
        xalign 0.5
        xsize 300

screen player_stats:
    vbox:
        yalign 1.0

        frame:
            padding (10, 10)
            textbutton f"{'View Draw Pile' if battle else 'View Deck'}":
                action Show("draw_pile")

        frame:
            vbox:
                use stat("Moves", Player.moves, Player.moves_max)
                null height 10
                use stat("Turns", Player.turns, Player.turns_max)
                null height 10
                text "Money: $[money]"

screen player_end_turn:
    frame:
        padding (10, 10) xalign 1.0 yalign 1.0
        textbutton "End Turn":
            action Function(Player.end_turn)

screen citizen_stats0(citizen, xalign_position=0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Consensus", citizen.consensus, citizen.consensus_max)
            null height 10
            use stat("Energy", citizen.energy, citizen.energy_max)

screen citizen_stats1(citizen, xalign_position=0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Consensus", citizen.consensus, citizen.consensus_max)
            null height 10
            use stat("Energy", citizen.energy, citizen.energy_max)

screen citizen_stats2(citizen, xalign_position=0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Consensus", citizen.consensus, citizen.consensus_max)
            null height 10
            use stat("Energy", citizen.energy, citizen.energy_max)

screen draw_pile:

    dismiss action Hide("draw_pile")

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

                for card in deck.draw_pile if battle else deck.cards:
                    frame:
                        background Frame(Card.IMAGE)
                        label card.label_cost()
                        label card.label_description() xalign 0.5 yalign 0.5
                        xysize Card.WIDTH, Card.HEIGHT

        null height 50

        frame:
            xalign 0.5
            textbutton "Close":
                action Hide("draw_pile")
