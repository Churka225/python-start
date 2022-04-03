x = 0
def setup():
    size(800,600)
    background(0)
def draw():
    frameRate(9)
    global x
    fill(206,8,8)
    rect(385,300,150,100)
    fill(255)
    textSize(20)
    textAlign(CENTER,CENTER)
    text(x, 385 + 75, 300 + 50)
    if mousePressed == True:
        if mouseX >= 385 and mouseX <= 535 and mouseY >= 300 and mouseY <= 400:
            x = x + 1
