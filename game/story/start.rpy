label start:

    $ level.restart()

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
