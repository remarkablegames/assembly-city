screen stat(name, current, max):
    text "[name]: [current]/[max]"
    bar value AnimatedValue(current, max):
        xsize 300

screen player_money:
    frame:
        background Solid((0, 0, 0, 100))
        text "Money: $[money]"
        xpos (40 if renpy.variant("web") else 0)

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
                null height 15
                use stat("Turns", Player.turns, Player.turns_max)
                null height 15
                use stat("Consensus", Level.consensus("current"), Level.consensus("goal"))

screen player_end_turn:
    frame:
        padding (10, 10) xalign 1.0 yalign 1.0
        textbutton "End Turn":
            action Function(Player.end_turn)

screen tooltip:
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                background Solid((255, 255, 255, 225))
                text tooltip color "#000"
                xalign 0.5

init python:
    citizen_name_ypos = 628

screen citizen_stats0(citizen, xalign_position=0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Consensus", citizen.consensus, citizen.consensus_max)
            null height 10
            use stat("Energy", citizen.energy, citizen.energy_max)
    button:
        action NullAction()
        background Solid((0, 0, 0, 200))
        text "[citizen.name]" xalign 0.5
        tooltip citizen.say()
        xalign xalign_position ypos citizen_name_ypos
        xsize 400
    use tooltip

screen citizen_stats1(citizen, xalign_position=0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Consensus", citizen.consensus, citizen.consensus_max)
            null height 10
            use stat("Energy", citizen.energy, citizen.energy_max)
    button:
        action NullAction()
        background Solid((0, 0, 0, 200))
        text "[citizen.name]" xalign 0.5
        tooltip citizen.say()
        xalign xalign_position ypos citizen_name_ypos
        xsize 400
    use tooltip

screen citizen_stats2(citizen, xalign_position=0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Consensus", citizen.consensus, citizen.consensus_max)
            null height 10
            use stat("Energy", citizen.energy, citizen.energy_max)
    button:
        action NullAction()
        background Solid((0, 0, 0, 200))
        text "[citizen.name]" xalign 0.5
        tooltip citizen.say()
        xalign xalign_position ypos citizen_name_ypos
        xsize 400
    use tooltip

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
                    use card_frame(card)

        null height 50

        frame:
            xalign 0.5
            textbutton "Close":
                action Hide("draw_pile")

screen card_frame(card):
    frame:
        background Frame(card.image)
        label card.label_name():
            xalign 0.5
            ypos card.label_name_ypos
        label card.label_cost()
        label card.label_description():
            xalign 0.5
            ypos card.label_description_ypos
            padding (5, 0)
        xysize card.width, card.height
