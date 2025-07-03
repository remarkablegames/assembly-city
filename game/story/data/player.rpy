init python:
    class Player():
        moves = 3
        moves_max = 3
        turns = 0
        turns_max = 0

        @staticmethod
        def end_turn() -> None:
            """
            End player turn.
            """
            Player.turns -= 1
            deck.discard_hand()
            renpy.hide_screen("player_end_turn")
            renpy.jump("citizen_turn")
