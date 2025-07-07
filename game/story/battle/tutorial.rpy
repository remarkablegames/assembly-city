label tutorial:

    scene bg hall day
    with fade

    player "Let me ask the Commissioner some questions."

    show commissioner smile 1
    with dissolve

    jump tutorial_questions

label tutorial_questions:

    menu:
        "I’d like to ask you..."

        "What is a Citizens’ Assembly?":
            commissioner @ smile 2 "It’s a form of deliberative democracy, where a diverse group of citizens engage in informed discussion and deliberation to address complex policy questions."
            jump tutorial_questions

        "How do I run an assembly?":
            commissioner "The goal of an assembly is to have the citizens {b}learn{/b}, {b}deliberate{/b}, and {b}decide{/b}."
            commissioner "In other words, we want them to achieve a consensus."
            commissioner "Take a look at the screen to your left."
            show screen player_stats
            commissioner "You have a set number of turns to achieve the consensus goal."
            commissioner "For each turn, you will draw a hand and you have a set number of moves to play your cards."
            commissioner "If you play your cards right, you can increase the consensus of the citizens."
            commissioner "Remember, you need to manage the citizens’ energy levels."
            commissioner "If it drops too low, it gets hard to increase consensus."
            commissioner "Let’s do a trial run."
            hide commissioner
            jump battle

        "Nevermind":
            commissioner @ smile 2 "Are you ready to run your first assembly?"
            menu:
                "Yes":
                    commissioner @ smile 3 "Alright, good luck!"
                    $ Level.next()
                    jump battle
                "No":
                    jump tutorial_questions
