x = 0
y = 0
def setup():
    size(800,600)
    frameRate(6)
def draw():
    global x,y
    translate(400,300)
    rotate(radians(x))
    fill(160,11,11)
    ellipse(x,0,y,y)
    x = x + 10
    y = y + 5
    if y == 50:
        y = 0
    
    
    
