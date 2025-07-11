label assembly1:

    jump assembly1_signup

label assembly1_signup:

    scene bg hall day
    with fade

    facilitator "Hmm... where should I go next?"

    show commissioner
    with dissolve

    commissioner "Hi there! Are you here for the Citizens’ Assembly?"

    menu:
        "What should I say?"

        "Yes. Am I in the right place?":
            commissioner @ smile 1 "Yes, this is it. Let me get you signed up."
            facilitator "Much appreciated."

            show commissioner at left
            with moveinleft

            show badge at badge_size
            with dissolve

            commissioner @ smile 1 "Here’s your badge."

            hide badge
            with dissolve

            show commissioner at center
            with moveinright

            commissioner "Before we head in, let me quickly explain how the assembly works."

            commissioner "Your goal is to convince other participants to support your proposal."

            commissioner @ smile 1 "You’ll use cards — each one represents an argument, a resource, or a tactic."

            commissioner "Each card affects your performance in two ways..."
            commissioner "Agreement measures how much someone supports your idea."
            commissioner "Energy represents your mental stamina. Playing cards uses energy. If you run out, you can’t keep persuading."

            commissioner @ smile 1 "Each turn gives you 3 moves. Most cards cost 1 to 3 moves to play."

            commissioner "You’ll have a limited number of turns to build consensus."

            commissioner "If a majority of participants support your idea, you win the vote and earn money."

            commissioner @ smile 1 "You can spend money at the shop between assemblies to upgrade or buy new cards."

            commissioner @ smile 1 "Here are some example cards you'll come across..."

            show commissioner at left
            with moveinleft

            show discuss at card_size
            with dissolve

            commissioner "Discuss: +2 Agreement, -1 Energy"
            hide discuss
            with dissolve

            show tea at card_size
            with dissolve
            commissioner "Tea: +1 Energy, +1 Agreement"
            hide tea
            with dissolve

            show fatigue at card_size
            with dissolve
            commissioner "Fatigue: -1 to -3 Energy"
            hide fatigue
            with dissolve

            show soda at card_size
            with dissolve
            commissioner "Soda: +2 Energy"
            hide soda
            with dissolve

            show vote at card_size
            with dissolve
            commissioner "Vote: +3 Energy, -1 Agreement for everyone"
            hide vote
            with dissolve

            show doubt at card_size
            with dissolve
            commissioner "Doubt: -1 to -3 Agreement"
            hide doubt
            with dissolve

            show pizza at card_size
            with dissolve
            commissioner "Pizza: +1 Energy for everyone"
            hide pizza
            with dissolve

            show expert at card_size
            with dissolve
            commissioner "Expert: Both +3 Agreement and -2 Energy for everyone"
            hide expert
            with dissolve

            show commissioner at center
            with moveinright

            commissioner @ smile 1 "Alright, go ahead and grab a seat. We’ll get started soon!"

            jump assembly1_hall

        "No, I’m not here for that.":
            commissioner surprised "What are you here for?"
            facilitator "Is this the game jam convention?"
            commissioner "I think you’re in the wrong place..."
            facilitator "Ah, my bad. Let me check my location."
            jump end

label assembly1_hall:

    menu:
        "What should I do?"

        "Enter the room":
            jump assembly1_room

        "Talk to the commissioner":
            jump assembly1_commissioner

label assembly1_commissioner:

    menu:
        "What do I want to ask?"

        "What’s a Citizens’ Assembly?":
            commissioner @ smile 1 "Great question!"
            commissioner "A Citizens’ Assembly brings together people from all walks of life to hear evidence, discuss, and make recommendations on important issues."
            commissioner "Think of it as an innovative democratic tool!"
            jump assembly1_commissioner

        "What’s the issue?":
            commissioner "You’ll find out later today!"
            jump assembly1_commissioner

        "How was I selected?":
            commissioner "We randomly select from 1,000 addresses within the city who’s a permanent resident over 18 years old."
            commissioner "And you’re one of the lucky three people selected!"
            jump assembly1_commissioner

        "What happens after the event?":
            commissioner "Your ideas and recommendations will be presented to the local government."
            jump assembly1_commissioner

        "Nevermind":
            jump assembly1_hall

label assembly1_room:

    scene bg refectory day
    with fade

    show commissioner
    with dissolve

    commissioner @ smile 1 "Welcome to today’s Citizens’ Assembly."
    commissioner "You’re probably curious about today’s issue."
    commissioner @ sad "...the city is overrun by cats."
    commissioner "I’d like to introduce you to our cat expert."

    show commissioner at left
    with moveinleft
    show expert
    with moveinbottom

    expert "I’m smile 1 to answer any questions about cats."

    hide expert
    with moveoutbottom
    show commissioner at center
    with moveinright

    commissioner "By the end of this assembly, I’m looking to hear your solution on this problem."
    commissioner @ smile 1 "Now let’s learn, deliberate, and decide!"

    hide commissioner
    with dissolve

    jump assembly1_citizens

label assembly1_citizens:

    show student at left
    with moveinleft
    show trainer at right
    with moveinright

    show trainer at opacity(0.5)
    student "Hey there! I’m a fourth-year student at the nearby university."

    show student at opacity(0.5)
    show trainer at opacity

    trainer "I’m a personal trainer at a gym."

    hide student
    with dissolve
    hide trainer
    with dissolve

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

    show student at center
    with dissolve

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
                    facilitator "Not really..."
                    student "Then I’ll stick with my idea."

            jump assembly1_student

        "Nevermind":
            hide student
            with dissolve
            jump assembly1_talk

label assembly1_trainer:

    show trainer at center
    with dissolve

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
                    facilitator "Not really..."
                    trainer "Then I’ll stick with my idea."

            jump assembly1_trainer

        "Nevermind":
            hide trainer
            with dissolve
            jump assembly1_talk

label assembly1_expert:

    show expert at center
    with dissolve

    menu:
        "What would you like to ask?"

        "Nevermind":
            hide expert
            with dissolve
            jump assembly1_talk

label assembly1_vote:

    show commissioner
    with dissolve

    commissioner "Are you ready to vote on a proposal?"

    menu:
        "Am I ready to vote on a proposal?"

        "Yes":
            facilitator "Yes I am."
            jump end

        "No":
            hide commissioner
            with dissolve
            jump assembly1_talk
