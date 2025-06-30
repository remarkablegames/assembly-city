transform left(value=0.2):
    xalign value
    yalign 1.0

transform right(value=0.8):
    xalign value
    yalign 1.0

transform opacity(value=1):
    alpha value

transform flip:
    xzoom -1.0

transform unflip:
    xzoom 1.0

transform resize(x=1, y=1):
    size (x, y)

transform rotate(degrees):
    rotate degrees

transform scale(ratio):
    zoom ratio

transform tint(color):
    matrixcolor TintMatrix(color)

transform ypos(position):
    ypos position