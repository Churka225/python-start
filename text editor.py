def setup():
    size(800,600)
def draw():
    if keyPressed == True:
        if key == 'm' or key == 'M' or key == 'ь' or key == 'Ь':
            fill(232,17,9)
            textAlign(CENTER,CENTER)
            textSize(30)
            text(u"M",400,300)
    if keyPressed == True:
        if key == 'y' or key == 'Y' or key == 'н' or key == 'Н':
            fill(232,17,9)
            textAlign(CENTER,CENTER)
            textSize(30)
            text(u"y",420,300)
