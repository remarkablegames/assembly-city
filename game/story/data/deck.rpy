init python:
    class Deck:
        def __init__(self) -> None:
            self.cards = [
                Card(image="talk", cost=1, action={"consensus": {"value": 3}, "energy": {"value": -2}, "draw": {"value": 0}}),
                Card(image="talk", cost=1, action={"consensus": {"value": 3}, "energy": {"value": -2}}),
                Card(image="soda", cost=1, action={"energy": {"value": 2}, "draw": {"value": 0}}),
                Card(image="soda", cost=1, action={"energy": {"value": 2}}),
                Card(image="tea", cost=1, action={"draw": {"value": 2}}),
            ]

            self.draw_pile = []
            self.discard_pile = []
            self.disabled_pile = []
            self.hand = []


        def get_card(self, card_id: str) -> Card:
            """
            Get card by id.
            """
            return find(self.cards, {"id": card_id})


        def get_cards(self, count: int, upgrade="") -> Card:
            """
            Get cards.
            """
            cards = self.cards.copy()
            renpy.random.shuffle(cards)

            if upgrade in ["all", "stun"]:
                cards = list(filter(lambda card: card.action.get("consensus") and not card.action["consensus"].get(upgrade), cards))
            elif upgrade == "cost":
                cards = list(filter(lambda card: card.cost > 0, cards))
            else:
                cards = list(filter(lambda card: card.action.get(upgrade), cards))

            choices = []

            for _ in range(count):
                if not len(cards):
                    return choices
                choices.append(cards.pop())

            return choices


        def draw_cards(self, count: int) -> None:
            """
            Add card(s) to hand.
            """
            if not count:
                return

            for _ in range(count):
                if not len(self.draw_pile):
                    self.draw_pile = self.discard_pile.copy()
                    self.discard_pile = []
                    renpy.random.shuffle(self.draw_pile)

                    if not len(self.draw_pile):
                        return

                renpy.sound.queue("sound/draw.ogg")
                self.hand.append(self.draw_pile.pop(0))


        def discard_card(self, card: Card) -> None:
            """
            Discard card.
            """
            self.hand.remove(card)
            if card.name.lower() == "delay":
                self.disabled_pile.append(card)
            else:
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
            self.disabled_pile = []
            self.hand = []


default deck = Deck()
