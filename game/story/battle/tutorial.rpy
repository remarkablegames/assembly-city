label tutorial:

    scene bg hall day
    with fade

    facilitator "Let me ask the Commissioner some questions."

    show commissioner smile 1
    with dissolve

    jump tutorial_questions


label tutorial_questions:

    menu:
        "I’d like to ask..."

        "What is a Citizens’ Assembly?":
            commissioner "It’s a form of deliberative democracy."
            commissioner "We invite a group of citizens to discuss policy issues."
            jump tutorial_assembly_questions

        "How do I run an assembly?":
            jump tutorial_how_to_run_assembly

        "Nevermind":
            commissioner @ smile 2 "Are you ready to run your first assembly?"

            menu:
                "Run assembly?"

                "Yes":
                    commissioner @ smile 3 "Alright, good luck!"
                    $ level.next()
                    jump battle

                "No":
                    jump tutorial_questions


label tutorial_assembly_questions:

    menu:
        "I’d like to know..."

        "How are the citizens selected?":
            commissioner @ smile 2 "We invite a broad group of people by lottery from an address database."
            commissioner "Then we select a representative sample in a fair and diverse manner."
            jump tutorial_assembly_questions

        "What kind of policy issues are discussed?":
            commissioner @ smile 2 "Policy issues that are complex, controversial, or lacks a clear consensus among decision-makers."
            commissioner "For example, climate change, social care, and constitutional matters."
            jump tutorial_assembly_questions

        "Where can I learn more about citizens assemblies?":
            commissioner @ smile 2 "You can learn more about citizens assemblies in this {a=https://oneworldornone.world/the-comic-book-explainer}comic book{/a}."
            commissioner "Alternatively, you can check out this helpful {a=https://assemblyexplainer.com/}explainer{/a}."
            jump tutorial_assembly_questions

        "Nevermind":
            jump tutorial_questions


label tutorial_how_to_run_assembly:

    commissioner "The goal of an assembly is to learn, deliberate, and decide."
    commissioner "In the end, we want the citizens to reach a consensus."
    commissioner "Take a look at the screen to your left."

    show screen player_stats

    commissioner "You have a number of {color=[colors.note]}Turns{/color} to reach the {color=[colors.note]}Consensus{/color} goal."
    commissioner "Each turn, you draw cards into your hand and spend {color=[colors.note]}Moves{/color} to play them."
    commissioner "Play your cards right and you can raise the citizens’ consensus."
    commissioner "Don’t forget to manage the citizens’ energy levels."
    commissioner "If it falls too low, it becomes hard to achieve consensus."
    commissioner "Press {color=[colors.note]}View Deck{/color} to see your cards."
    commissioner @ smile 2 "Would you like to perform a trial run?"

    menu:
        "Perform a trial run?"

        "Yes":
            jump tutorial_battle

        "No":
            hide screen player_stats
            jump tutorial_questions


label tutorial_battle:

    commissioner @ smile 3 "Alright, let’s do it!"

    hide commissioner
    show screen tutorial_battle

    jump battle


label tutorial_battle_end:

    hide commissioner idle
    show commissioner smile 1 with dissolve

    commissioner "All assembly participants are fairly compensated for their time."
    commissioner "I included a bonus if you go above the consensus goal."

    jump tutorial_questions


screen tutorial_battle:
    frame:
        background Solid((0, 0, 0, 200))
        padding (10, 10)
        text "Drag the card to the person.\n\nPress {color=[colors.note]}End Turn{/color} when out of {color=[colors.note]}Moves{/color}."
        xsize 500
        xalign 1.0
