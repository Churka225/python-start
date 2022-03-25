x = 0
mode = 0
def setup():
    size(800,600)
    background(0)
def draw():
    global x, mode
    noStroke()
    if mousePressed == False:
        fill(255)
        ellipse(random(0,800), random(0,600), random(1,5), random(1,5))
    if mousePressed == True:
        background(255)
        fill(236,237,14)
        ellipse(790,20,100,100)
        fill(200)
        ellipse(20,73,95,95)
        ellipse(88,65,100,100)
        ellipse(170,74,95,95)
        rect(20,50,170,68)
        x = x + mode 
        if x >= 800:
            mode = -10
        elif x <= 0:
            mode = 10
            
        
    
        
            
