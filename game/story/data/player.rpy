init python:
    class Player:
        # battle
        draw_cards = 3
        moves = 3
        moves_max = 3
        turns = 0
        turns_max = 0

        # shop
        cards_bought = 0
        cards_upgraded =0
        cards_removed = 0

        def end_turn(self) -> None:
            """
            End player turn.
            """
            self.turns -= 1
            deck.discard_hand()
            renpy.hide_screen("player_end_turn")
            renpy.jump("citizen_turn")

default player = Player()
