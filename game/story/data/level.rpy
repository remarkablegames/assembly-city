init python:
    from json import load

    class Level:
        _data = load(renpy.file("story/data/levels.json"))
        battle = False
        current = 0

        def data(self) -> dict:
            """
            Get level data.
            """
            return self._data.get(str(self.current), {})

        def consensus(self, value: str) -> dict:
            """
            Get consensus value.
            """
            if value == "current":
                return sum(list(map(lambda citizen: citizen.consensus, citizens.citizens)))
            if value == "goal":
                return self.data().get("consensus_goal", 0)

        def start(self) -> None:
            """
            Start level.
            """
            self.battle = True
            data = self.data()

            if not data:
                renpy.jump("end")

            player.turns = player.turns_max = data["player_turns"]
            player.moves = player.moves_max

            if self.current > 0:
                renpy.scene()
                renpy.show(data["scene"])
                renpy.with_statement(dissolve)

            citizens.generate(data["citizens"])
            citizens.show()

            deck.shuffle()

        def end(self) -> None:
            """
            End level.
            """
            self.battle = False
            if self.consensus("current") < self.consensus("goal"):
                renpy.jump("lose")
            else:
                renpy.jump("win")

        def next(self, level=0) -> None:
            """
            Increment level.
            """
            if level:
                self.current = level
            else:
                self.current += 1

        def restart(self) -> None:
            """
            Restart level.
            """
            self.current = 0

default level = Level()
