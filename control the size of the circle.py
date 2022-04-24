x = 10
def setup():
    size(800,600)
def draw():
    global x
    background(255)
    ellipse(400,300,x,x)
    if key == CODED:
        if keyCode == UP:
            x = x+1
        if keyCode == DOWN:
            x = x-1
            
