x = 0
def setup():
    size(800,600)
    background
def draw():
    fill(206,8,8)
    rect(385,300,150,100)
    fill(255)
    line(mouseX, mouseY, pmouseX, pmouseY)
    if mousePressed == True:
        if mouseX >= 385 and mouseX <= 535 and mouseY >= 300 and mouseY <= 400:
            background(255)

