def setup():
    size(800,600)
def draw():
    if keyPressed == True:
        if key == 'b' or key == 'B' or key == 'и' or key == 'И':
            fill(232,17,9)
            textAlign(CENTER,CENTER)
            textSize(30)
            text(u"B",400,300)
        if key == 'e' or key == 'E' or key == 'у' or key == 'У':
            fill(232,17,9)
            textAlign(CENTER,CENTER)
            textSize(30)
            text(u"e",420,300)
        if key == 'a' or key == 'A' or key == 'ф' or key == 'Ф':
            fill(232,17,9)
            textAlign(CENTER,CENTER)
            textSize(30)
            text(u"a",444,300)
