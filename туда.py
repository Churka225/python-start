x = 0
mode = 0
def setup():
    size(800,600)
def draw():
    translate(400,300)
    global x,mode
    background(255)
    fill(160,11,11)
    ellipse(0,0,x,x)
    x = x + mode
    if x >= 400:
        mode = -10
    elif x <= 0: 
        mode = 10

    
    

        
