init python:
    class Deck:
        def __init__(self) -> None:
            self.cards = [
                Card(image="talk", cost=1, action={"consensus": {"value": 3}, "energy": {"value": -2}}),
                Card(image="talk", cost=1, action={"consensus": {"value": 3}, "energy": {"value": -2}}),
                Card(image="tea", cost=1, action={"draw": {"value": 2}}),
                Card(image="soda", cost=1, action={"energy": {"value": 2}}),
                Card(image="soda", cost=1, action={"energy": {"value": 2}}),
                Card(image="pizza", cost=2, action={"energy": {"value": 2, "all": True}}),
                Card(image="expert", cost=2, action={"consensus": {"value": 3, "all": True}, "energy": {"value": -2, "all": True}}),
                Card(image="vote", cost=2, action={"consensus": {"value": 3, "stun": True}, "energy": {"value": -3}}),
            ]

            self.draw_pile = []
            self.discard_pile = []
            self.hand = []

        def get_card(self, card_id: str) -> Card:
            """
            Get card by id.
            """
            return find_by_id(self.cards, card_id)

        def get_cards(self, count: int, upgrade_card_type="") -> Card:
            """
            Get cards.
            """
            copy = self.cards.copy()
            renpy.random.shuffle(copy)

            if upgrade_card_type in ["all", "stun"]:
                copy = list(filter(lambda card: card.action.get("consensus") and not card.action["consensus"].get(upgrade_card_type), copy))
            elif upgrade_card_type == "cost":
                copy = list(filter(lambda card: card.cost > 0, copy))
            else:
                copy = list(filter(lambda card: card.action.get(upgrade_card_type), copy))

            cards = []
            for _ in range(count):
                if not len(copy):
                    return cards
                cards.append(copy.pop())
            return cards

        def draw_cards(self, count=Player.draw_cards) -> None:
            """
            Add card(s) to hand.
            """
            for _ in range(count):
                if not len(self.draw_pile):
                    self.draw_pile = self.discard_pile.copy()
                    self.discard_pile = []
                    renpy.random.shuffle(self.draw_pile)

                    if not len(self.draw_pile):
                        return narrator("No more cards to draw.")

                renpy.sound.queue("sound/draw.ogg")
                self.hand.append(self.draw_pile.pop(0))

        def discard_card(self, card: Card) -> None:
            """
            Discard card.
            """
            self.hand.remove(card)
            self.discard_pile.append(card)

        def discard_hand(self) -> None:
            """
            Discard hand at end of turn.
            """
            while len(self.hand):
                self.discard_pile.append(self.hand.pop(0))

        def shuffle(self) -> None:
            """
            Shuffle draw pile before battle.
            """
            self.draw_pile = self.cards.copy()
            renpy.random.shuffle(self.draw_pile)
            self.discard_pile = []
            self.hand = []

default deck = Deck()
