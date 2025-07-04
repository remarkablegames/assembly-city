init python:
    from json import load

    class Level:
        _data = load(renpy.file("story/data/levels.json"))

        @staticmethod
        def data() -> dict:
            """
            Get level data.
            """
            data = Level._data.get(str(wins))

            if data:
                return data
            else:
                renpy.jump("end")

        @staticmethod
        def consensus() -> dict:
            """
            Get consensus data.
            """
            return {
                "current": sum(list(map(lambda citizen: citizen.consensus, citizens.citizens))),
                "goal": Level.data()["consensus_goal"],
            }

        @staticmethod
        def start() -> None:
            """
            Start level.
            """
            data = Level.data()

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
