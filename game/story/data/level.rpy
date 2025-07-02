init python:
    from json import load

    class Level:
        data = load(renpy.file("story/data/levels.json"))

        @staticmethod
        def start() -> None:
            """
            Start level.
            """
            data = Level.data.get(str(wins))
            if not data:
                renpy.jump("end")

            Player.turns = Player.turns_max = data["turns"]
            citizens.generate(data["citizens"])
