init python:
    def character_callback(event, interact=True, **kwargs) -> None:
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("ui/rollover2.ogg", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()


define facilitator = Character("Facilitator", callback=character_callback)
define commissioner = Character("Commissioner", image="commissioner", callback=character_callback)
