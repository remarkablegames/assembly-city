init python:
    class Player:
        draw_cards = 3
        moves = 3
        moves_max = 3
        shop_card_choices = 3
        turns = 0
        turns_max = 0

        def end_turn(self) -> None:
            """
            End player turn.
            """
            self.turns -= 1
            deck.discard_hand()
            renpy.hide_screen("player_end_turn")
            renpy.jump("citizen_turn")

default player = Player()
