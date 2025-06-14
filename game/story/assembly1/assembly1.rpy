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

    facilitator @ happy "Welcome everybody to today’s Citizens’ Assembly."
    facilitator "You’re probably curious about today’s issue."
    facilitator "So without further ado, the problem we’ll be talking about is..."
    facilitator @ concerned "...the city is overrun by cats."
    facilitator "I’d like to introduce you to our cat expert."

    show facilitator at left
    with moveinleft

    show expert
    with moveinbottom

    expert "I’m happy to answer any questions you may have about cats."

    hide expert
    with moveoutbottom

    show facilitator at center
    with moveinright

    facilitator "By the end of the day, I’ll be looking forward to hear your recommendation on how to solve this problem!"
