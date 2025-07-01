init python:
    from json import load

    class Levels:
        def __init__(self) -> None:
            self.levels = load(renpy.file("story/data/levels.json"))

        def get(self, level: int) -> dict:
            """
            Get level data.
            """
            try:
                return self.levels[str(level)]

            except KeyError:
                level = { "citizens": [] }
                names = Citizens.NAMES.copy()
                random = renpy.random.random()

                if wins > 6 and random < 0.3:
                    citizens_count = 3
                elif wins > 3 and random < 0.6:
                    citizens_count = 2
                else:
                    citizens_count = 1

                while citizens_count > 0:
                    name = renpy.random.choice(names)
                    names.remove(name)
                    attack_min = round(wins * (1 + renpy.random.random())) + 1
                    heal_min = round(wins * (1 + renpy.random.random())) + 1

                    level["citizens"].append({
                        "name": name,
                        "health": round(5 * (wins + 1) * (1 + renpy.random.random())),
                        "attack_min": attack_min,
                        "attack_max": attack_min + wins + 1,
                        "heal_min": heal_min,
                        "heal_max": heal_min + wins + 1,
                    })

                    citizens_count -= 1

                return level

default levels = Levels()
