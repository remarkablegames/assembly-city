label start:

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
    "To help us answer this question, you’re invited to attend a Citizens’ Assembly."
    "The Citizens’ Assembly brings people from all walks of life to discuss and make recommendations on important issues."
    "There are no easy answers and this is an opportunity to tell us what you think needs to be done."
    "All we require from you are your views and ideas – you don't need to have any prior knowledge of the issues to take part."
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

    player "Fingers crosssed!"
