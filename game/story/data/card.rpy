init python:
    from uuid import uuid4

    class Card:
        image = "cards/soda_card.png"
        width = 250
        height = 350
        offset = 80

        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())
            self.cost = kwargs.get("cost", 0)
            self.action = kwargs.get("action", {})
            self.value = kwargs.get("value", 0)

        def label_cost(self) -> str:
            """
            Cost label.
            """
            return emojis.get(self.cost)

        def label_description(self) -> str:
            """
            Description label.
            """
            label = "{color=[colors.white]}{size=*0.85}"
            for action, data in self.action.items():
                label += action.capitalize()
                label += f" {data['value']}"
                if data.get("times", 1) > 1:
                    label += f" ×{data.get('times')}"
                if data.get("stun"):
                    label += " Stun"
                if data.get("all"):
                    label += " All"
                label += "\n"
            return label.rstrip()

        @staticmethod
        def label_upgrade(action: str, value=1) -> str:
            """
            Upgrade label.
            """
            if action == "all":
                return f"Select a card to apply effects to {{b}}all{{/b}} citizens:"
            elif action == "cost":
                return f"Select a card to decrease {{b}}cost{{/b}} by {emojis.get(1)}:"
            elif action == "stun":
                return f"Select a card to {{b}}stun{{/b}} an citizen:"
            elif action == "times":
                return f"Select a card to increase action by 1 {{b}}time{{/b}}:"
            else:
                return f"Select a card to increase {{b}}{action}{{/b}} by {{b}}{value}{{/b}}:"

        def upgrade(self, action: str, value=1) -> None:
            """
            Upgrade card.
            """
            if action in ["all", "stun"]:
                self.action["consensus"][action] = 1
            elif action == "cost" and self.cost > 0:
                self.cost -= 1
            elif action == "times":
                action = self.action.get("consensus") if self.action.get("consensus") else self.action.get("energy")
                action["times"] = action.get("times", 1)
                action["times"] += 1
            else:
                if self.action.get(action):
                    self.action[action]["value"] += value
                else:
                    self.action[action] = {"value": value}

        def get_xpos(self) -> int:
            """
            Calculate x-position.
            """
            x = config.screen_width / 2
            x -= (self.width + self.offset * (len(deck.hand) - 1)) / 2
            x += deck.hand.index(self) * self.offset
            return int(x)

        def get_ypos(self) -> int:
            """
            Calculate y-position.
            """
            return config.screen_height - self.height

        def get_pos(self) -> int:
            """
            Calculate xy-position.
            """
            return self.get_xpos(), self.get_ypos()

        def use(self, citizen) -> None:
            """
            Use card.
            """
            if Player.moves < self.cost:
                return

            deck.discard_card(self)

            Player.moves -= self.cost

            draw = self.action.get("draw")
            if draw:
                for _ in range(draw.get("times", 1)):
                    deck.draw_cards(draw["value"])

            energy = self.action.get("energy")
            if energy:
                for _ in range(energy.get("times", 1)):
                    citizen.energize(energy["value"])

            moves = self.action.get("moves")
            if moves:
                for _ in range(moves.get("times", 1)):
                    renpy.sound.queue("sound/powerup.ogg")
                    Player.moves += moves["value"]

            consensus = self.action.get("consensus")
            if consensus:
                for _ in range(consensus.get("times", 1)):
                    for citizen in citizens.citizens if consensus.get("all") else [citizen]:
                        citizen.consense(consensus["value"])
                        if consensus.get("stun"):
                            citizen.stunned = True
                        renpy.show(f"battle {citizen.id}", at_list=[shake])

        @staticmethod
        def generate(count=1) -> list:
            """
            Generate card(s).
            """
            cards = []

            for _ in range(count):
                card = Card(
                    cost=renpy.random.randint(1, 3),
                    action={
                        renpy.random.choice(["consensus", "draw", "energy"]): {
                            "value": renpy.random.randint(1, 6)
                        },
                    },
                )
                cards.append(card)

            return cards
