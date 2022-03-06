x = 250
mode = 0
def setup():
    size(1200,1000)
def draw():
    background(237,10,135)
    global x,mode 
    fill(160,11,11)
    ellipse(550,220,x,x)
    ellipse(660,220,x,x)
    rotate(radians(45))
    translate(0,0)
    push()
    fill(0)
    rect(1000,420,x,x)
    pop()
    #x = x + mode
    if x >= 300:
        mode = -10
    elif x <= 0:
        mode = 10
    
    
    
    
