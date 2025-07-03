label reward:

    if not rewards:
        jump shop

    menu:
        "Claim your reward (remaining: [rewards]):"

        "Reroll rewards (-$[wins // 2])" if money >= wins // 2 and wins > 1:
            $ money -= wins // 2
            jump reward

        "Increase max moves by {color=[colors.moves]}+1" if renpy.random.random() < 0.1:
            $ Player.moves_max += 1

        "Pass":
            pass

    $ rewards -= 1

    jump reward
