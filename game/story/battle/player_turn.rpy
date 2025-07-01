label player_turn:

    $ deck.draw_cards()

    show screen player_end_turn

    jump player_hand

label player_hand:

    python:
        for citizen in citizens.citizens:
            if renpy.showing(citizen.image) and citizen.health <= 0:
                citizens.hide(citizen)

    if citizens.dead():
        jump win

    elif player.character.health <= 0:
        jump lose

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
        if player.character.id == character_id:
            card.use(player.character)
        elif character_id:
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
        for citizen_index, citizen in enumerate(citizens.citizens):
            if citizen.health > 0:
                drag:
                    drag_name citizen.id
                    draggable False
                    droppable True
                    focus_mask True
                    idle_child f"citizens/{citizen.image}.png"
                    selected_idle_child f"citizens/{citizen.image} hover.png"
                    xalign citizens.xalign_position(citizen) yalign Citizens.YALIGN

        for card in deck.hand:
            drag:
                as draggable
                drag_name card.id
                dragged ondrag
                droppable False
                drag_raise False
                pos card.get_pos()

                frame:
                    background Frame(Card.IMAGE)
                    label card.label_cost()
                    label card.label_description() xalign 0.5 yalign 0.5
                    xysize Card.WIDTH, Card.HEIGHT

                    mousearea:
                        area (0, 0, Card.OFFSET, Card.HEIGHT)
                        hovered Function(onhovered, draggable)

        drag:
            drag_name player.character.id
            draggable False
            droppable True
            selected_idle_child Solid((255, 255, 255, 100), xsize=312, ysize=235)
            yalign 1.0

            frame:
                background Solid((0, 0, 0, 0))
                xysize 312, 235
