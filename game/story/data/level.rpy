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
        def start() -> None:
            """
            Start level.
            """
            data = Level.data()

            Player.turns = Player.turns_max = data["turns"]
            Player.moves = Player.moves_max

            citizens.generate(data["citizens"])
            citizens.show()

            deck.shuffle()

        @staticmethod
        def end() -> None:
            """
            End level.
            """
            data = Level.data()

            consensus = sum(list(map(lambda citizen: citizen.consensus, citizens.citizens)))
            if consensus >= data["consensus"]:
                renpy.jump("win")
            else:
                renpy.jump("lose")
