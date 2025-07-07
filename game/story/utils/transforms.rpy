transform position(xalign_position=0.5):
    xalign xalign_position
    ypos Citizen.ypos

transform shake:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0

transform left(value=0.2):
    xalign value
    yalign 1.0

transform right(value=0.8):
    xalign value
    yalign 1.0

transform opacity(value=1):
    alpha value

transform card_size:
    zoom 0.65
    xalign 0.5
    yalign 0.5

transform badge_size:
    zoom 0.50
    xalign 0.5
    yalign 0.5
