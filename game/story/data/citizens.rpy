init python:
    class Citizens:
        # Names that are mapped to their respective images.
        # E.g., name "Student 1" -> image "student_1".
        NAMES = ["Lawyer"]
        YALIGN = 0.2

        def __init__(self) -> None:
            self.citizens = []
            self.count = 0

        def generate(self, citizens: list) -> None:
            """
            Generate citizens.
            """
            self.citizens = []
            self.count = len(citizens)

            for citizen in citizens:
                self.citizens.append(Citizen(**citizen))

        def show(self) -> None:
            """
            Show citizens.
            """
            for index, citizen in enumerate(self.citizens):
                xalign_position = self.xalign_position(citizen)
                renpy.show_screen(f"citizen_stats{index}", citizen, xalign_position)
                renpy.show(f"battle {citizen.image}", at_list=[position(xalign_position)])

            renpy.with_statement(dissolve)

        def hide(self, citizen: Citizen) -> None:
            """
            Hide citizen.
            """
            renpy.hide(citizen.image)
            renpy.with_statement(dissolve)
            renpy.hide_screen(f"citizen_stats{citizens.index(citizen)}")

        def get(self, citizen_id: str) -> Citizen:
            """
            Get citizen by id.
            """
            return find_by_id(self.citizens, citizen_id)

        def index(self, citizen: Citizen) -> int:
            """
            Get citizen index.
            """
            return self.citizens.index(citizen)

        def xalign_position(self, citizen: Citizen) -> float:
            """
            Get citizen xalign position.
            """
            count = self.count
            index = self.citizens.index(citizen)

            xalign_position = 0.5

            if count == 2:
                if index == 0:
                    xalign_position = 0.25
                elif index == 1:
                    xalign_position = 0.75
            elif count == 3:
                if index == 0:
                    xalign_position = 0.1
                elif index == 2:
                    xalign_position = 0.9

            return xalign_position

        def turn(self) -> None:
            """
            Citizen turn.
            """
            for citizen in self.citizens:
                if citizen.stunned:
                    narrator(f"{citizen.name} is stunned!")
                    continue

                citizen.turn_rng()

                if citizen.heal_value and citizen.energy < citizen.energy_max and renpy.random.random() < 0.5:
                    narrator(f"{citizen.name} healed {citizen.heal_value} energy.")
                    citizen.heal(citizen.heal_value)

            self.end_turn()

        def end_turn(self) -> None:
            """
            Citizen end turn.
            """
            for citizen in self.citizens:
                citizen.stunned = False

default citizens = Citizens()
