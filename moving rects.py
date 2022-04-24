x = 0
def setup():
    size(800,600)
def draw():
    global x
    background(255)
    push()
    translate(x,0)
    for x in range(0,600,10):
        rect(0,x,10,10)
    pop()
    x = x+10
