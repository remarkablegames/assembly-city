# Should the user be allowed to rollback the game? If set to False, the user cannot interactively rollback.
define config.rollback_enabled = False

label start:

    scene bg gate day
    with fade

    player "It’s my first day as a facilitator for the Citizens’ Assembly."
    player "I’m excited and nervous at the same time."

    menu:
        "What should I do?"

        "Start with a tutorial":
            jump tutorial

        "Run the assembly":
            $ Level.next()
            jump battle
