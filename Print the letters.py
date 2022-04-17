def setup():
    size(800,600)
def draw():
    if keyPressed == True:
        if key == 'h' or key == 'H' or key == 'р' or key == 'Р':
            fill(232,17,9)
            textAlign(CENTER,CENTER)
            textSize(30)
            text(u"hH",400,300)
