init python:
    def say_allow_dismiss() -> bool:
        renpy.sound.play("ui/drop_004.ogg")
        return True

    config.say_allow_dismiss = say_allow_dismiss


label start:

    play music "music/BGM8 Harukaze.ogg" volume 0.5 fadein 1

    scene bg gate day
    with fade

    facilitator "It’s my first day as the facilitator for the Citizens’ Assembly."
    facilitator "I’m excited and nervous at the same time."

    menu:
        "What should I do?"

        "Start with a tutorial":
            jump tutorial

        "Run assembly":
            $ level.next()
            jump battle
