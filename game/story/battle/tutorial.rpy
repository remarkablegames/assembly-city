label tutorial:

    scene bg hall day
    with fade

    facilitator "Let me ask the Commissioner some questions."

    show commissioner smile 1
    with dissolve

    jump tutorial_questions


label tutorial_questions:

    menu:
        "I’d like to ask you..."

        "What’s a Citizens’ Assembly?":
            jump tutorial_what_is_assembly

        "How do I run an assembly?":
            jump tutorial_how_to_run_assembly

        "Nevermind":
            commissioner @ smile 2 "Are you ready to run your first assembly?"

            menu:
                "Yes":
                    commissioner @ smile 3 "Alright, good luck!"
                    $ level.next()
                    jump battle

                "No":
                    jump tutorial_questions


label tutorial_what_is_assembly:

    commissioner @ smile 2 "It’s a form of deliberative democracy, where a diverse group of citizens engage in informed discussion and deliberation to address complex policy questions."

    jump tutorial_questions


label tutorial_how_to_run_assembly:

    commissioner "The goal of an assembly is to learn, deliberate, and decide."
    commissioner "In the end, we want the participating citizens to reach a consensus."
    commissioner "Take a look at the screen to your left."

    show screen player_stats

    commissioner "You have a set number of turns to reach the consensus goal."
    commissioner "Each turn, you draw [player.draw_cards] cards into your hand and spend [player.moves] moves to play them."
    commissioner "Play your cards right and you can raise the citizens’ consensus."
    commissioner "Don’t forget to manage the citizens’ energy levels."
    commissioner "If it falls too low, it becomes hard to achieve consensus."
    commissioner "Press {b}View Deck{/b} to see your cards."
    commissioner @ smile 2 "Would you like to do a trial run?"

    menu:
        "Do a trial run?"

        "Yes":
            commissioner @ smile 3 "Alright, let’s do it!"
            hide commissioner
            jump battle

        "No":
            hide screen player_stats
            jump tutorial_questions
