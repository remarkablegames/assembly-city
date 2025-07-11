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
            commissioner @ smile 2 "It’s a form of deliberative democracy, where a diverse group of citizens engage in informed discussion and deliberation to address complex policy questions."
            jump tutorial_questions

        "How do I run an assembly?":
            commissioner "The goal of an assembly is to learn, deliberate, and decide."
            commissioner "In other words, we want the participating citizens to reach a consensus."
            commissioner "Take a look at the screen to your left."
            show screen player_stats
            commissioner "You have a set number of turns to achieve the consensus goal."
            commissioner "Each turn, you draw cards into your hand and spend moves to play them."
            commissioner "Play your cards right and you can raise the citizens’ consensus."
            commissioner "Don’t forget to manage the citizens’ energy levels."
            commissioner "If a citizen’s energy falls too low, it becomes hard to increase consensus."
            commissioner @ smile 2 "Would you like to do a trial run?"
            menu:
                "Yes":
                    commissioner @ smile 3 "Alright, let’s do it!"
                    hide commissioner
                    jump battle
                "No":
                    jump tutorial_questions

        "Nevermind":
            commissioner @ smile 2 "Are you ready to run your first assembly?"
            menu:
                "Yes":
                    commissioner @ smile 3 "Alright, good luck!"
                    $ Level.next()
                    jump battle
                "No":
                    jump tutorial_questions
