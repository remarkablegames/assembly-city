init python:
    from math import ceil
    from uuid import uuid4

    class Citizen():
        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())

            self.name = kwargs.get("name", "")
            self.id = kwargs.get("id", self.name.lower())

            self.width = ceil(830 / oversample)
            self.height = ceil(916 / oversample)

            self.energy = kwargs.get("energy", 0)
            self.energy_max = kwargs.get("energy_max", 0)

            self.consensus = kwargs.get("consensus", 0)
            self.consensus_max = kwargs.get("consensus_max", 0)

            self.actions = kwargs.get("actions", [])

            self.stunned = False

        def image(self) -> str:
            """
            Get image.
            """
            return f"battle {self.id}"

        def say(self) -> str:
            """
            Get say.
            """
            if self.stunned:
                return f"{self.name} is stunned!"
            return self.actions[0]["say"]

        def consense(self, value: int) -> None:
            """
            Update consensus.
            """
            renpy.sound.queue("sound/punch.ogg", relative_volume=0.5)
            self.consensus += value
            if self.consensus > self.consensus_max:
                self.consensus = self.consensus_max
            elif self.consensus < 0:
                self.consensus = 0

        def energize(self, value: int) -> None:
            """
            Update energy.
            """
            renpy.sound.queue("sound/potion.ogg", relative_volume=0.5)
            self.energy += value
            if self.energy > self.energy_max:
                self.energy = self.energy_max
            elif self.energy < 0:
                self.energy = 0
