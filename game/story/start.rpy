label start:

    scene bg dining room day with fade

    "You receive a letter from the “Citizens’ Assembly”..."

    menu:
        "What should you do?"

        "Open it":
            jump open_letter

        "Discard it":
            "Eh... it’s probably a junk mail or scam."
            jump end

label open_letter:

    "Dear Householder,"
    "We need your help in solving a pressing issue facing our city."
    "We look forward to hearing from you."

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

    jump assembly1
