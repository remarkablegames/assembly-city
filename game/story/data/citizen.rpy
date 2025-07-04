init python:
    from uuid import uuid4

    class Citizen():
        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())

            self.name = kwargs.get("name", "")
            self.id = kwargs.get("id", self.name.lower())

            self.width = 550
            self.height = 650

            self.energy = kwargs.get("energy", 0)
            self.energy_max = kwargs.get("energy_max", 0)

            self.consensus = kwargs.get("consensus", 0)
            self.consensus_max = kwargs.get("consensus_max", 0)

            self.stunned = False

        def turn_rng(self) -> None:
            """
            Generate random numbers for turn.
            """
            pass

        def consense(self, value: int) -> None:
            """
            Update consensus.
            """
            renpy.sound.queue("sound/punch.ogg", relative_volume=0.5)
            self.consensus += value

        def energize(self, value: int, over_energize=False) -> None:
            """
            Update energy.
            """
            renpy.sound.queue("sound/potion.ogg", relative_volume=0.5)
            if not over_energize and self.energy + value >= self.energy_max:
                self.energy = self.energy_max
            else:
                self.energy += value
