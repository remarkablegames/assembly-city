label end:

    stop music fadeout 4

    hide screen player_end_turn
    hide screen player_stats
    hide screen player_money

    hide screen citizen_stats0
    hide screen citizen_stats1
    hide screen citizen_stats2
    hide screen citizen_stats3
    hide screen citizen_stats4

    if level.data():
        jump bad_ending
    else:
        jump good_ending


label good_ending:

    play music "music/BGM6 Graduation.ogg" volume 0.5 fadein 1

    scene bg courtyard2 day
    with fade

    show commissioner smile 1
    with dissolve

    commissioner "With the assembly over, we’ll publish a formal public response to the members’ recommendations."
    commissioner "We encourage everyone to stay in touch and remain engaged."
    commissioner "Helping a group of people contribute meaningfully to public discourse is a once-in-a-lifetime experience."
    commissioner smile 3 "Be proud of your impact!"

    jump the_end


label bad_ending:

    play music "music/BGM8 Harukaze.ogg" volume 0.5 fadein 1

    scene bg courtyard1 day
    with fade

    show commissioner
    with dissolve

    commissioner "Although a consensus wasn’t achieved, it doesn't render the process moot."
    commissioner "We will transparently report the lack of consensus and explain the reasons for disagreement."
    commissioner "This can provide valuable insights to decision-makers."
    commissioner smile 1 "Thanks for facilitating!"

    jump the_end


label the_end:

    scene black
    with fade

    $ level.restart()

    "{b}End{/b}."

    return
