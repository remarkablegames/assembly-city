label assembly1:

    jump assembly1_outside

label assembly1_outside:

    scene bg gate day with fade

    player "I can’t believe I was chosen!"
    player "I’m feeling a bit nervous..."

    menu:
        "What should you do?"

        "Enter the assembly":
            "You take a deep breath and exhale."
            player "Alright, here I come!"
            jump assembly1_signup

        "Go home":
            player "Maybe I sit this one out..."
            jump end

label assembly1_signup:

    scene bg hall day with fade

    player "Hmm... where should I go next?"

    show facilitator with dissolve

    facilitator "Hi there! Are you here for the Citizens’ Assembly?"

    menu:
        "What should I say?"

        "Yep":
            facilitator @ happy "Awesome, let me get you signed up."
            player "Much appreciated."
            facilitator "Here’s your badge. Feel free to grab a seat, we’ll get started soon."
            jump assembly1_hall

        "Nah":
            facilitator concerned "What are you here for?"
            player "Is this the game jam convention?"
            facilitator "I think you’re in the wrong place..."
            player "Ah, my bad. Let me check my location."
            jump end

label assembly1_hall:

    menu:
        "What should I do?"

        "Enter the room":
            jump assembly1_room

        "Talk to the facilitator":
            jump assembly1_facilitator

label assembly1_facilitator:

    menu:
        "What do I want to ask?"

        "What’s a Citizens’ Assembly?":
            facilitator @ happy "Great question!"
            facilitator "A Citizens’ Assembly brings together people from all walks of life to hear evidence, discuss, and make recommendations on important issues."
            facilitator "Think of it as an innovative democratic tool!"
            jump assembly1_facilitator

        "What’s the issue?":
            facilitator "You’ll find out later today!"
            jump assembly1_facilitator

        "How was I selected?":
            facilitator "We randomly select from 1,000 addresses within the city who’s a permanent resident over 18 years old."
            facilitator "And you’re one of the lucky three people selected!"
            jump assembly1_facilitator

        "What happens after the event?":
            facilitator "Your ideas and recommendations will be presented to the local government."
            jump assembly1_facilitator

        "Nevermind":
            jump assembly1_hall

label assembly1_room:

    scene bg refectory day with fade

    show facilitator with dissolve

    facilitator @ happy "Welcome to today’s Citizens’ Assembly."
    facilitator "You’re probably curious about today’s issue."
    facilitator "So without further ado, the problem we’ll be discussing is..."
    facilitator @ concerned "...the city is overrun by cats."
    facilitator "I’d like to introduce you to our cat expert."

    show facilitator at left with moveinleft
    show expert with moveinbottom

    expert "I’m happy to answer any questions about cats."

    hide expert with moveoutbottom
    show facilitator at center with moveinright

    facilitator "By the end of this assembly, I’m looking to hear your solution on this problem."
    facilitator @ happy "Now let’s learn, deliberate, and decide!"

    hide facilitator with dissolve

    jump assembly1_citizens

label assembly1_citizens:

    show student at left with moveinleft
    show trainer at right with moveinright

    show trainer at opacity(0.5)
    student "Hey there! I’m a fourth-year student at the nearby university."

    show student at opacity(0.5)
    show trainer at opacity

    trainer "I’m a personal trainer at a gym."

    # player talks to citizens + expert to gather info
    # player selects an idea
    # each citizen has a bar that shows how convinced they are
    # each dialogue option can +/- citizen influence
    # if player reaches a certain persuasion score, citizen will vote for that idea
    # player wins if idea wins majority vote and player wins $$
    # player can buy items to improve persuasion
    # player has hp/mp (mental power?) where bad arguments will hurt player
    # deckbuilding?

    hide student with dissolve
    hide trainer with dissolve

    jump assembly1_talk

label assembly1_talk:

    menu:
        "What do you want to do?"

        "Talk to Student":
            jump assembly1_student

        "Talk to Trainer":
            jump assembly1_trainer

        "Talk to Expert":
            jump assembly1_expert

        "Vote on a proposal":
            jump assembly1_vote

label assembly1_student:

    show student at center with dissolve

    menu:
        "What would you like to talk about?"

        "What’s your idea?":
            student "We should study cats to learn their language."
            student "Then we can communicate with their leader and ask them to migrate elsewhere."
            student "What do you think?"

            menu:
                "I think..."

                "It’s a good idea":
                    student "Great!"

                "It’s a bad idea":
                    student "Do you have any evidence why it’s a bad idea?"
                    player "Not really..."
                    student "Then I’ll stick with my idea."

            jump assembly1_student

        "Nevermind":
            hide student with dissolve
            jump assembly1_talk

label assembly1_trainer:

    show trainer at center with dissolve

    menu:
        "What would you like to talk about?"

        "What’s your idea?":
            trainer "I believe we can train cats into helpful workers of society."
            trainer "Then we can leverage their strength to produce electricity, agriculture, and other goods."
            trainer "What do you think?"

            menu:
                "I think..."

                "It’s a good idea":
                    trainer "Excellent!"

                "It’s a bad idea":
                    trainer "Do you have any proof why it’s a bad idea?"
                    player "Not really..."
                    trainer "Then I’ll stick with my idea."

            jump assembly1_trainer

        "Nevermind":
            hide trainer with dissolve
            jump assembly1_talk

label assembly1_expert:

    show expert at center with dissolve

    menu:
        "What would you like to ask?"

        "Nevermind":
            hide expert with dissolve
            jump assembly1_talk

label assembly1_vote:

    show facilitator with dissolve

    facilitator "Are you ready to vote on a proposal?"

    menu:
        "Am I ready to vote on a proposal?"

        "Yes":
            player "Yes I am."
            jump end

        "No":
            hide facilitator with dissolve
            jump assembly1_talk
