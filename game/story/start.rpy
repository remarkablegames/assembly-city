label start:

    scene bg dining room day with fade

    "You receive a letter from the “Citizens’ Assembly”..."

    menu:
        "What should you do?"

        "Open it":
            jump open_letter

        "Discard it":
            "Eh... it’s probably junk mail or a scam."
            jump end

label open_letter:

    "Dear Householder,"
    "We need your help in solving a key issue facing our city."
    "We’re looking for a group of people to come together to make recommendations on:"
    "{i}How do we reduce congestion, improve air quality, and enhance public transportation?"
    "We thank you for your interest and look forward to hearing from you."

    menu:
        "What should you do?"

        "Register interest":
            "Hmm... I don’t have plans this weekend and I can meet new people."
            "Plus, they cover the meals and transportation costs."
            "I’ll apply and see if I get chosen – I've got nothing to lose."
            jump register_interest

        "Ignore the opportunity":
            "It’s probably not worth it..."
            jump end

label register_interest:

    "Register your name below..."

    $ player_name = renpy.input("My name is...", length=32).strip() or player_name

    player "Fingers crossed!"

    jump assembly_outside

label assembly_outside:

    scene bg gate day with fade

    player "I can’t believe I was chosen!"
    player "I’m feeling a bit nervous..."

    menu:
        "What should you do?"

        "Enter the assembly":
            "You take a deep breath and exhale."
            player "Alright, here I come!"
            jump assembly_hall

        "Go home":
            player "Maybe I sit this one out..."
            jump end

label assembly_hall:

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
            jump end

        "Nah":
            facilitator concerned "What are you here for?"
            player "Is this the game jam convention?"
            facilitator "I think you’re in the wrong place..."
            player "Ah, my bad. Let me check my location."
            jump end
