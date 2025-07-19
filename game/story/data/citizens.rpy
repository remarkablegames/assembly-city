init python:
    class Citizens:
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
                renpy.show(citizen.image(), at_list=[position(xalign_position)])

            renpy.with_statement(dissolve)

        def hide(self, citizen: Citizen) -> None:
            """
            Hide citizen.
            """
            renpy.hide(citizen.image())
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

            if count == 1:
                xalign_position = 0.5

            elif count == 2:
                if index == 0:
                    xalign_position = 0.25
                elif index == 1:
                    xalign_position = 0.75

            elif count == 3:
                if index == 0:
                    xalign_position = 0.1
                elif index == 1:
                    xalign_position = 0.5
                elif index == 2:
                    xalign_position = 0.9

            elif count == 4:
                if index == 0:
                    xalign_position = 0.05
                elif index == 1:
                    xalign_position = 0.35
                elif index == 2:
                    xalign_position = 0.65
                elif index == 3:
                    xalign_position = 0.95

            elif count == 5:
                if index == 0:
                    xalign_position = 0
                elif index == 1:
                    xalign_position = 0.25
                elif index == 2:
                    xalign_position = 0.5
                elif index == 3:
                    xalign_position = 0.75
                elif index == 4:
                    xalign_position = 1.0

            return xalign_position

        def turn(self) -> None:
            """
            Citizen turn.
            """
            for citizen in self.citizens:
                narrator(citizen.say())
                action = citizen.actions.pop(0)

                if citizen.stunned:
                    citizen.actions.append(action)
                    renpy.show(citizen.image())
                    continue

                energy = action.get("energy")
                if energy:
                    for citizen in citizens.citizens if action.get("all", False) else [citizen]:
                        citizen.energize(energy)

                consensus = action.get("consensus")
                if consensus:
                    for citizen in citizens.citizens if action.get("all", False) else [citizen]:
                        citizen.consense(consensus)

                renpy.show(citizen.image())
                citizen.actions.append(action)

            self.end_turn()

        def end_turn(self) -> None:
            """
            Citizen end turn.
            """
            for citizen in self.citizens:
                citizen.stunned = False

default citizens = Citizens()
