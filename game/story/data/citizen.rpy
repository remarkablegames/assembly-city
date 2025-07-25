init python:
    from math import ceil
    from uuid import uuid4

    class Citizen():
        ypos = 170

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

        def action(self, key: str):
            """
            Get first action.
            """
            return self.actions[0].get(key, 0)

        def image(self, state="") -> str:
            """
            Get image name.
            """
            if state:
                pass
            elif not player.turns:
                state = "idle"
            elif self.action("consensus") < 0:
                state = "lose consensus"
            elif self.action("energy") < 0:
                state = "lose energy"
            else:
                state = "idle"
            return f"{self.id} {state}"

        def say(self) -> str:
            """
            Get say.
            """
            if self.stunned:
                return f"{self.name} is stunned!"
            return self.action("say").format(name=self.name)

        def consense(self, value: int) -> None:
            """
            Update consensus.
            """
            if not value:
                return

            renpy.sound.queue("sound/punch.ogg", relative_volume=0.5)

            self.consensus += value

            if self.consensus > self.consensus_max:
                self.consensus = self.consensus_max
            elif self.consensus < 0:
                self.consensus = 0

            renpy.show(self.image(), at_list=[shake])

        def energize(self, value: int, sound="powerup") -> None:
            """
            Update energy.
            """
            if not value:
                return

            if sound == "soda":
                renpy.sound.queue(f"sound/{sound}.ogg", relative_volume=0.5)
            elif value > 0:
                renpy.sound.queue("sound/powerup.ogg", relative_volume=0.3)

            self.energy += value

            if self.energy > self.energy_max:
                self.energy = self.energy_max
            elif self.energy < 0:
                self.energy = 0

        def stun(self, stunned: bool) -> None:
            """
            Update stun.
            """
            self.stunned = bool(self.stunned or stunned)
