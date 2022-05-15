a = 0
b = 0
c = 0
def setup():
    size(800, 600)
    global a, b, c
    a = loadImage("s dnem pobedi.jpg")
    b = loadImage("radiodenpobedi.jpg")
    c = loadImage("kartinka-9-maya-den-pobedy.jpg")
def draw():
    global a, b, c
    if mousePressed == True:
        if mouseButton == LEFT:
            image (a, 0, 0, 800, 600)
        if mouseButton == RIGHT:
            image (b, 0, 0, 800, 600)
        if mouseButton == CENTER:
            image (c, 0, 0, 800, 600)
    if keyPressed == True:
        if key == 'c' or key == 'C' or key == u'с' or key == u'С':
            fill(10,1,1)
            textAlign(CENTER,CENTER)
            textSize(30)
            text(u"С днём победы", 400, 300)
