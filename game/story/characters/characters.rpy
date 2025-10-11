init python:
    MUSIC_CHANNEL_DIALOGUE = "dialogue"

    renpy.music.register_channel(MUSIC_CHANNEL_DIALOGUE, "voice", loop=True)

    def character_callback(event, interact=True, **kwargs) -> None:
        if event == "show_done":
            renpy.music.play("ui/rollover2.ogg", channel=MUSIC_CHANNEL_DIALOGUE)
        elif event == "slow_done":
            renpy.music.stop(channel=MUSIC_CHANNEL_DIALOGUE, fadeout=0.2)

    def dismiss_callback() -> bool:
        renpy.play("ui/click_003.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback


define narrator = Character(None, callback=character_callback)
define facilitator = Character("Facilitator", callback=character_callback)
define commissioner = Character("Commissioner", image="commissioner", callback=character_callback)
