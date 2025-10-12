init python:
    citizen_name_ypos = 628


screen stat(name, current, max, color=colors.label):
    text "[name]: {color=[color]}[current]/[max]"
    bar value AnimatedValue(current, max):
        xsize (400 if renpy.variant("mobile") or renpy.variant("touch") else 300)


screen player_money():
    frame:
        background Solid((0, 0, 0, 100))
        text "Money: $[money]"
        xpos (40 if renpy.variant("web") else 0)


screen player_stats():
    vbox:
        yalign 1.0
        use player_deck
        frame:
            vbox:
                use stat("Moves", player.moves, player.moves_max)
                null height 15
                use stat("Turns", player.turns, player.turns_max, colors.caution if player.turns < 2 else colors.label)
                null height 15
                use stat("Consensus", level.consensus("current"), level.consensus("goal"))


screen player_end_turn():
    frame:
        if renpy.variant("mobile") or renpy.variant("touch"):
            padding (20, 20)
        else:
            padding (10, 10)
        textbutton "End Turn":
            action Function(player.end_turn)
        xalign 1.0
        yalign 1.0


screen player_deck(xalign_pos=0, yalign_pos=0):
    frame:
        padding (10, 10)
        textbutton ("View Draw Pile" if level.battle else "View Deck"):
            action Show("draw_pile")
        xalign xalign_pos yalign yalign_pos


screen tooltip():
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                background Solid((255, 255, 255, 225))
                text tooltip color "#000"
                xalign 0.5


screen citizen_stats(citizen, xalign_pos):
    frame:
        xalign xalign_pos
        vbox:
            use stat("Consensus", citizen.consensus, citizen.consensus_max)
            null height 10
            use stat("Energy", citizen.energy, citizen.energy_max)
    button:
        action NullAction()
        background Solid((0, 0, 0, 200))
        text "[citizen.name]" xalign 0.5
        tooltip citizen.say()
        xalign xalign_pos ypos citizen_name_ypos
        xsize 400
    use tooltip


screen citizen_stats0(citizen, xalign_pos):
    use citizen_stats(citizen, xalign_pos)


screen citizen_stats1(citizen, xalign_pos):
    use citizen_stats(citizen, xalign_pos)


screen citizen_stats2(citizen, xalign_pos):
    use citizen_stats(citizen, xalign_pos)


screen citizen_stats3(citizen, xalign_pos):
    use citizen_stats(citizen, xalign_pos)


screen citizen_stats4(citizen, xalign_pos):
    use citizen_stats(citizen, xalign_pos)


screen draw_pile():

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
                for card in deck.draw_pile if level.battle else deck.cards:
                    use card_frame(card)

        null height 50

        frame:
            xalign 0.5
            textbutton "Close":
                action Hide("draw_pile")


screen card_frame(card, draggable=None):
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

        if draggable:
            mousearea:
                area (0, 0, card.offset, card.height)
                hovered [
                    Queue("sound", "ui/mouserelease1.ogg"),
                    Function(onhovered, draggable),
                ]


screen card(card, xalign_pos=0.5, yalign_pos=0.5):
    vbox:
        xalign xalign_pos yalign yalign_pos
        use card_frame(card)
