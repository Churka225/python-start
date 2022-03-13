def setup():
    size(600,400)
    background(0)
def draw():
    noStroke()
    fill(random(200, 255))
    ellipse(random(0, 600), random(0, 400), random(1, 5),random(1, 5))
    if mousePressed == True:
        background(0)
