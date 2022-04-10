x = 0
def setup():
    size(800,600)
    background(255)
def draw():
    fill(206,8,8)
    rect(385,300,150,100)
    fill(255)
    line(mouseX, mouseY, pmouseX, pmouseY)
    if mousePressed == True:
        if mouseX >= 385 and mouseX <= 535 and mouseY >= 300 and mouseY <= 400:
            background(255)
    fill(255,3,3)
    rect(10,10,160,100)
    def mouseClicked():
        if mouseX >= 10 and mouseX <= 170 and mouseY >= 10 and mouseY <= 110:
            stroke(255,3,3)
    fill(83,14,203)
    rect(180,10,160,100)
    if mousePressed == True: 
        if mouseX >= 180 and mouseX <= 340 and mouseY >= 10 and mouseY <= 110:
            strokeWeight(3)
    fill(6,152,22)
    rect(350,10,160,100)
    if mouseButton == LEFT:
        stroke(19,155,2)
