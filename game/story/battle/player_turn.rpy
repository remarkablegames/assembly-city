label player_turn:

    if Player.turns <= 0:
        $ battle = False
        $ Level.end()

    $ deck.draw_cards()

    show screen player_end_turn

    jump player_hand

label player_hand:

    call screen player_hand

init python:
    def ondrag(drags, drop) -> None:
        drag = drags[0]
        card_id = drag.drag_name
        card = deck.get_card(card_id)

        if not drop:
            drag.snap(card.get_xpos(), card.get_ypos(), 0.2)
            return

        character_id = drop.drag_name
        if character_id:
            citizen = citizens.get(character_id)
            card.use(citizen)

        # snap unused card back
        if card in deck.hand:
            drag.snap(card.get_xpos(), card.get_ypos(), 0.2)

        renpy.jump("player_hand")

    def onhovered(draggable) -> None:
        draggable.top()

screen player_hand:
    draggroup:
        for citizen in citizens.citizens:
            drag:
                drag_name citizen.id
                draggable False
                droppable True
                focus_mask True
                idle_child Solid((0, 0, 0, 0), xsize=citizen.width, ysize=citizen.height)
                selected_idle_child citizen.image("hover")
                xalign citizens.xalign_position(citizen)
                ypos citizen.ypos

        for card in deck.hand:
            drag:
                as draggable
                drag_name card.id
                dragged ondrag
                droppable False
                drag_raise False
                pos card.get_pos()

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

                    mousearea:
                        area (0, 0, card.offset, card.height)
                        hovered [Play("sound", "ui/mouserelease1.ogg"), Function(onhovered, draggable)]
