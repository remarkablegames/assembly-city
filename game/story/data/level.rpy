init python:
    from json import load

    class Level:
        _data = load(renpy.file("story/data/levels.json"))
        level = 0

        @staticmethod
        def data() -> dict:
            """
            Get level data.
            """
            return Level._data.get(str(Level.level), {})

        @staticmethod
        def consensus(value: str) -> dict:
            """
            Get consensus value.
            """
            if value == "current":
                return sum(list(map(lambda citizen: citizen.consensus, citizens.citizens)))
            if value == "goal":
                return Level.data().get("consensus_goal", 0)

        @staticmethod
        def start() -> None:
            """
            Start level.
            """
            data = Level.data()

            if not data:
                renpy.jump("end")

            Player.turns = Player.turns_max = data["player_turns"]
            Player.moves = Player.moves_max

            citizens.generate(data["citizens"])
            citizens.show()

            deck.shuffle()

        @staticmethod
        def end() -> None:
            """
            End level.
            """
            if Level.consensus("current") < Level.consensus("goal"):
                renpy.jump("lose")
            else:
                renpy.jump("win")

        @staticmethod
        def next() -> None:
            """
            Increment level.
            """
            Level.level += 1

        @staticmethod
        def restart() -> None:
            """
            Restart level.
            """
            Level.level = 0
