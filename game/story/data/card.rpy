init python:
    from uuid import uuid4

    class Card:
        label_description_ypos = 235
        label_name_ypos = 5
        width = 250
        height = 350
        offset = 80

        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())
            self.cost = kwargs.get("cost", 0)
            self.action = kwargs.get("action", {})
            self.value = kwargs.get("value", 0)
            image = kwargs.get('image')
            self.image = f"cards/{image}.png"
            self.name = image.capitalize()

        def label_name(self) -> str:
            """
            Name label.
            """
            return "{color=[colors.label]}{b}{k=-2}" + self.name.upper()

        def label_cost(self) -> str:
            """
            Cost label.
            """
            return emojis.get(self.cost)

        def label_description(self) -> str:
            """
            Description label.
            """
            label = ""
            color = "{color=[colors.label]}"

            for action, data in self.action.items():
                value = data["value"]

                if value:
                    label += action.capitalize()
                    label += f" +{value}" if value > 0 else f" {value}"

                if data.get("stun"):
                    label += " Stun"

                if data.get("all"):
                    label += " All"

                label += "\n"

            label = label.rstrip('\n')

            if len(label) < 15:
                size = "{size=*0.9}"
            elif len(label) < 25:
                size = "{size=*0.85}"
            else:
                size = "{size=*0.8}"

            return size + color + label

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
            Use card on citizen.
            """
            if player.moves < self.cost:
                return

            energy = self.action.get("energy")
            if energy and citizen.energy + energy["value"] < 0:
                return

            deck.discard_card(self)

            player.moves -= self.cost

            draw = self.action.get("draw")
            if draw:
                deck.draw_cards(draw["value"])

            if energy:
                for citizen in citizens.citizens if energy.get("all") else [citizen]:
                    citizen.energize(energy["value"])

            moves = self.action.get("moves")
            if moves:
                renpy.sound.queue("sound/powerup.ogg")
                player.moves += moves["value"]

            consensus = self.action.get("consensus")
            if consensus:
                for citizen in citizens.citizens if consensus.get("all") else [citizen]:
                    citizen.consense(consensus["value"], consensus.get("stun", False))

        @staticmethod
        def generate(count=1) -> list:
            """
            Generate card(s).
            """
            cards = []

            for _ in range(count):
                action = renpy.random.choice(["consensus", "draw", "energy"])

                if action == "draw":
                    image = "tea"
                elif action == "energy":
                    image = renpy.random.choice(["pizza", "soda"])
                else:
                    image = "talk"

                card = Card(
                    image=image,
                    cost=renpy.random.randint(1, 3),
                    action={
                        action: {
                            "value": renpy.random.randint(1, 6)
                        },
                    },
                )

                cards.append(card)

            return cards
