from pygame import*
from math import*

init()

GREEN=(0,255,0)
BLACK=(0,0,10)
display.set_caption("Oribit")
screen = display.set_mode((1000, 1000))
myClock =time.Clock()
coords = [490, 320]
angle = 0
rect = Rect(coords[0],coords[1],20,20)
speed = -1000000
next_tick = 1

rod=[500,500]
pond=image.load("images/pond.png")
X=0
Y=1
mov=False

rs=3

v=[0,0]
def drawscene(pond,rod):
    screen.blit(pond,(200,250))
    draw.line(screen,GREEN,(rod[X],rod[Y]),(coords[0],coords[1]))
    
    
def move_coords(angle, radius, coords):
    theta = radians(angle)
    return coords[0] + radius * cos(theta), coords[1] + radius * sin(theta)
def moverod(rod):
    global rs
    global mov
    keys = key.get_pressed()
    
    if keys[K_w]:    
        v[Y] = -rs
        mov=True
    if keys[K_s]:
        v[Y]=rs
        mov=True
    if keys[K_d]:
        v[X] = rs
        mov=True
    if keys[K_a]:
        v[X] = -rs
        mov=True
    if mov==True:
        rod[X]+=v[X]
        rod[Y]+=v[Y]
        mov=False
    if keys[K_UP]:
            rs+=0.5
    if keys[K_DOWN] and rs>1:
            rs-=0.5


        
 
def main():
    global event
    global next_tick
    global angle
    global coords

    running = True
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False

        mx,my=mouse.get_pos()
         
        ticks = time.get_ticks() 
        if ticks > next_tick:
            next_tick += speed
            angle += 0.5
            coords = move_coords(angle, 2, coords)
            rect.topleft = coords

             

        moverod(rod)
        screen.fill(BLACK)
        drawscene(pond,rod)
        
        screen.fill((0,150,0), rect)
        
        display.flip()
        myClock.tick(30)
     
    quit()

main()


      
