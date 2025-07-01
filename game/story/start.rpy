label start:

    scene bg dining room day with fade

    "You receive a letter from the “Citizens’ Assembly”..."

label open_letter:

    "Dear Householder,"
    "We need your help in solving a pressing issue facing our city."
    "We look forward to hearing from you."

    menu:
        "What should you do?"

        "Register interest":
            "Interesting. I may actually have a say in what happens."
            jump register_interest

        "Ignore the opportunity":
            "It’s probably not worth it..."
            jump end

label register_interest:

    "Register your name below..."

    $ player_name = renpy.input("My name is...", length=32).strip() or player_name

    player "Fingers crossed!"

    jump assembly1
