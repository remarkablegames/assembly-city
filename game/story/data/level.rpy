init python:
    from json import load

    class Level:
        _data = load(renpy.file("story/data/levels.json"))
        _level = 0

        @staticmethod
        def data() -> dict:
            """
            Get level data.
            """
            return Level._data.get(str(Level._level), {})

        @staticmethod
        def consensus() -> dict:
            """
            Get consensus data.
            """
            return {
                "current": sum(list(map(lambda citizen: citizen.consensus, citizens.citizens))),
                "goal": Level.data().get("consensus_goal", 0),
            }

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
            consensus = Level.consensus()

            if consensus["current"] < consensus["goal"]:
                renpy.jump("lose")
            else:
                renpy.jump("win")

        @staticmethod
        def next() -> None:
            """
            Increment level.
            """
            Level._level += 1

        @staticmethod
        def restart() -> None:
            """
            Restart level.
            """
            Level._level = 0
