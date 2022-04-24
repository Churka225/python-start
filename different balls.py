def setup():
    size(800,600)
def draw():
    for x in range(100):
        fill(random(0,255),random(0,255),random(0,255))
        ellipse(random(0,800),random(0,600),x,x)
    
