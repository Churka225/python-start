x = 0
mode = 0
def setup():
    size(800,600)
def draw():
    global x, mode
    background(255)
    fill(160,11,11)
    ellipse(200,x,50,50)
    x = x + mode
    if x >= 600:
        mode = -10
    elif x <= 0:
        mode = 10
    if mousePressed == False:
        background(0)
