init python:
    class Player:
        def __init__(self) -> None:
            # battle
            self.draw_cards = 3
            self.moves = 3
            self.moves_max = 3
            self.turns = 0
            self.turns_max = 0

            # shop
            self.cards_bought = 0
            self.cards_removed = 0
            self.cards_upgraded = 0
            self.shop_cards = 2


        def end_turn(self) -> None:
            """
            End player turn.
            """
            self.turns -= 1
            deck.discard_hand()
            renpy.hide_screen("player_end_turn")
            renpy.jump("citizen_turn")


default player = Player()
