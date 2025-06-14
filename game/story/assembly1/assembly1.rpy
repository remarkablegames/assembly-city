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
            jump assembly1_hall

        "Go home":
            player "Maybe I sit this one out..."
            jump end

label assembly1_hall:

    scene bg hall day with fade

    player "Hmm... which room is it?"

    show facilitator with dissolve

    facilitator "Hi there! Are you here for the Citizens’ Assembly?"

    menu:
        "What should I say?"

        "Yep":
            facilitator @ happy "Awesome, let me get you signed up."
            player "Much appreciated."
            facilitator "Here’s your badge. Feel free to grab a seat, we’ll get started soon."
            jump assembly1_room

        "Nah":
            facilitator concerned "What are you here for?"
            player "Is this the game jam convention?"
            facilitator "I think you’re in the wrong place..."
            player "Ah, my bad. Let me check my location."
            jump end

label assembly1_room:

    scene bg refectory day with fade

    player "Which table was I assigned to again?"
