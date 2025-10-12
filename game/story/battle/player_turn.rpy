label player_turn:

    if player.turns <= 0:
        $ level.end()

    $ deck.draw_cards(player.draw_cards)

    show screen player_end_turn

    jump player_hand


label player_hand:

    call screen player_hand


screen player_hand():
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

                use card_frame(card, draggable)


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
