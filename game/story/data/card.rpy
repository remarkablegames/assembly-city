init python:
    from uuid import uuid4


    class Card:
        label_description_ypos = 230
        label_name_ypos = 5
        width = 268
        height = 365
        offset = 80


        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())
            self.cost = kwargs.get("cost", 0)
            self.action = kwargs.get("action", {})

            image = kwargs.get('image')
            self.image = f"cards/{image}.png"
            self.name = image.capitalize()

            if renpy.variant("mobile") or renpy.variant("touch"):
                self.label_description_ypos = 220


        def label_size(self, label: str) -> str:
            """
            Get label size.
            """
            size = 1.0
            length = len(label)

            if length < 5:
                size = 0.95
            elif length < 15:
                size = 0.9
            elif length < 25:
                size = 0.85
            elif length < 35:
                size = 0.8
            else:
                size = 0.75

            if renpy.variant("mobile") or renpy.variant("touch"):
                size -= 0.15

            return f"{{size=*{size}}}" if not size == 1.0 else ""


        def label_name(self) -> str:
            """
            Name label.
            """
            return self.label_size(self.name) + "{color=[colors.label]}{b}{k=-2}" + self.name.upper()


        def label_cost(self) -> str:
            """
            Cost label.
            """
            return self.label_size(str(self.cost)) + emojis.get(self.cost)


        def label_description(self) -> str:
            """
            Description label.
            """
            label = ""
            color = "{color=[colors.label]}"

            for action, data in self.action.items():
                value = data["value"]

                if not value:
                    continue

                label += action.capitalize()
                label += f" +{value}" if value > 0 else f" {value}"

                if data.get("stun"):
                    label += " Stun"

                if data.get("all"):
                    label += " All"

                if action == "turns":
                    label += " once per assembly"

                label += "\n"

            label = label.strip()

            return self.label_size(label) + color + label


        @staticmethod
        def label_upgrade(action: str, value=1) -> str:
            """
            Upgrade label.
            """
            if action == "all":
                return f"Select a card to apply effects to {{b}}{{color=[colors.note]}}all{{/color}}{{/b}} citizens:"
            elif action == "cost":
                return f"Select a card to decrease {{b}}{{color=[colors.note]}}cost{{/color}}{{/b}} by {{b}}{emojis.get(1)}{{/b}}:"
            elif action == "stun":
                return f"Select a card to {{b}}{{color=[colors.note]}}stun{{/color}}{{/b}} an citizen:"
            else:
                return f"Select a card to increase {{b}}{{color=[colors.note]}}{action}{{/color}}{{/b}} by {{b}}{value}{{/b}}:"

        def upgrade(self, action: str, value=1) -> None:
            """
            Upgrade card.
            """
            if action == "all":
                self.action["consensus"]["all"] = True
                self.action["energy"]["all"] = True
            elif action == "stun":
                self.action["consensus"]["stun"] = True
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

            energy = self.action.get("energy", {})
            if energy and citizen.energy + energy["value"] < 0:
                return

            player.moves -= self.cost

            draw = self.action.get("draw")
            if draw:
                deck.draw_cards(draw["value"])

            moves = self.action.get("moves")
            if moves:
                renpy.sound.queue("sound/level.ogg", relative_volume=0.5)
                player.moves += moves["value"]

            turns = self.action.get("turns")
            if turns:
                renpy.sound.queue("sound/heartbeat.ogg", relative_volume=0.5)
                player.turns += turns["value"]

            consensus = self.action.get("consensus", {})

            if consensus.get("all") and energy.get("all"):
                for citizen in citizens.citizens:
                    if citizen.energy + energy["value"] >= 0:
                        citizen.consense(consensus["value"])
                        citizen.energize(energy["value"], self.name.lower())
                        citizen.stun(consensus.get("stun"))
            else:
                if consensus:
                    for citizen in citizens.citizens if consensus.get("all") else [citizen]:
                        citizen.consense(consensus["value"])
                        citizen.stun(consensus.get("stun"))

                if energy:
                    for citizen in citizens.citizens if energy.get("all") else [citizen]:
                        citizen.energize(energy["value"], self.name.lower())

            deck.discard_card(self)


        @staticmethod
        def generate(count=1) -> list:
            """
            Generate card(s).
            """
            cards = []

            for _ in range(count):
                cost = renpy.random.randint(1, 1 if level.current < 5 else 2)

                card_type = renpy.random.choice(
                    ["moves"] * (1 if level.current > 1 else 0) +
                    ["consensus"] +
                    ["draw"] +
                    ["energy"] +
                    []
                )

                action = {
                    card_type: {
                        "value": renpy.random.randint(level.current, max(3, level.current)),
                    },
                }

                if action.get("consensus"):
                    image = "talk"
                    action["energy"] = {"value": -renpy.random.randint(0, 2)}
                elif action.get("draw"):
                    image = "tea"
                    action["draw"]["value"] = renpy.random.randint(2, 3) if level.current < 5 else renpy.random.randint(3, 6)
                elif action.get("energy"):
                    image = "soda"
                elif action.get("moves"):
                    image = "focus"
                    action["moves"] = {"value": renpy.random.randint(2, 3)}
                    cost = renpy.random.randint(1, action["moves"]["value"] - 1)
                    action["energy"] = {"value": -renpy.random.randint(0, 2)}

                if not action.get("draw") and renpy.random.randint(0, 1):
                    action["draw"] = {"value": renpy.random.randint(0, 2)}

                card = Card(image=image, cost=cost, action=action)
                cards.append(card)

            return cards
