label tutorial:

    scene bg hall day
    with fade

    facilitator "Let me ask the Commissioner some questions."

    show commissioner smile 1
    with dissolve

    jump tutorial_questions


label tutorial_questions:

    show commissioner smile 1

    menu:
        "I’d like to ask..."

        "What is a Citizens’ Assembly?":
            commissioner @ smile 2 "It’s a form of deliberative democracy."
            commissioner "We invite a group of citizens to discuss policy issues."
            jump tutorial_assembly_questions

        "How do I run an assembly?":
            jump tutorial_how_to_run_assembly

        "Nevermind":
            commissioner smile 2 "Are you ready to run your first assembly?"

            menu:
                "Run assembly?"

                "Yes":
                    commissioner smile 3 "Alright, good luck!"
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

    commissioner @ smile 2 "The goal of an assembly is to learn, deliberate, and decide."
    commissioner "In the end, we want the citizens to reach a consensus."
    commissioner "Take a look at the screen to your left."

    show screen player_stats

    commissioner "You have a number of {color=[colors.note]}Turns{/color} to reach the {color=[colors.note]}Consensus{/color} goal."
    commissioner "Each turn, you draw [player.draw_cards] cards into your hand and spend {color=[colors.note]}Moves{/color} to play them."

    show commissioner smile 1 at right
    with moveinright

    $ card = find(deck.cards, {"name": "Talk"})
    show screen card(card, 0.35)
    play audio "sound/draw.ogg"

    commissioner @ smile 2 "{b}Talk{/b} increases a citizen’s {color=[colors.note]}Consensus{/color} by 3."
    commissioner "But the citizen must have enough {color=[colors.note]}Energy{/color} for you to use it."
    commissioner "It costs 1 {color=[colors.note]}Move{/color} to play."

    $ card = find(deck.cards, {"name": "Soda"})
    show screen card(card, 0.35)
    play audio "sound/draw.ogg"

    commissioner @ smile 2 "{b}Soda{/b} increases a citizen’s {color=[colors.note]}Energy{/color} by 2."
    commissioner "It costs 1 {color=[colors.note]}Move{/color} to play."

    $ card = find(deck.cards, {"name": "Tea"})
    show screen card(card, 0.35)
    play audio "sound/draw.ogg"

    commissioner @ smile 2 "{b}Tea{/b} draws 2 cards into your hand."
    commissioner "It costs 1 {color=[colors.note]}Move{/color} to play."

    hide screen card

    show commissioner smile 1 at center
    with moveinleft

    commissioner "Press {color=[colors.note]}View Deck{/color} to see your cards."
    commissioner smile 2 "Would you like to perform a trial run?"

    menu:
        "Perform a trial run?"

        "Yes":
            jump tutorial_battle

        "No":
            hide screen player_stats
            jump tutorial_questions


label tutorial_battle:

    commissioner smile 3 "Alright, let’s do it!"

    hide commissioner
    show screen tutorial_battle

    jump battle


label tutorial_battle_end:

    hide commissioner idle
    show commissioner smile 1 with dissolve

    commissioner "All assembly participants are fairly compensated for their time."
    commissioner @ smile 3 "I included a bonus if you go beyond the {color=[colors.note]}Consensus{/color} goal."

    jump tutorial_questions


screen tutorial_battle():
    frame:
        background Solid((0, 0, 0, 200))
        padding (10, 10)
        text """Drag the card to the citizen.

Press the name to see the citizen’s next action.

Press {color=[colors.note]}End Turn{/color} when out of {color=[colors.note]}Moves{/color}."""
        xsize 500
        xalign 1.0
