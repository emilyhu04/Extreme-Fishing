from pygame import *
from math import *
from random import *
init()

size = width, height = 1000,1000
screen = display.set_mode(size)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

angler=("images/angler.png")
banana=image.load("images/banana.png")
#bluefish=image.load("images/bluefish.png")
pufferfish=image.load("images/pufferfish.png")
goldfish=image.load("images/goldfish.png")
greenfish=image.load("images/green fish.png")
shark=image.load("images/shark.png")
pond=image.load("images/pond.png")

mov=False
rs=3

ticks=time.get_ticks()

pondx,pondy=500,550
pondrad=300

display.set_caption("Oribit")
myClock =time.Clock()
coords = [500, 300]
angle = 0
rect = Rect(coords[0],coords[1],20,20)
speed = 50
next_tick = 500

X=0
Y=1
mov=False

v=[0,0]

rod=[500,650]

bigenemy = [500,550,1,500,550,True,0,16712970,0,0,1,0]
SHOTSELECTION = 2
SHOTX = 3
SHOTY = 4
NEWSHOT = 5
SHOTPOINT = 6   
SHOTCOLOR = 7
SHOTTRACKX = 8
SHORTTRACKY = 9
TIMER = 10
selectedquadrent = 11
player = [500,250,0,505,255,0,0]
PLAYERSCORE = 2
RODX = 3
RODY = 4
RODA = 5
RODB = 6

powerup = [0,0,1,0]
POWERUPVAL = 2
PUTIMER = 3


fish = []
fish1 = [600,600,1,False]
fish2 = [300,400,1,False]
fish3 = [270,280,4,False]
fish.append(fish1)
fish.append(fish2)
fish.append(fish3)
FISHX = 0
FISHY = 1
FISHVALUE = 2
FISHCAUGHT = 3

BLACK=(0,0,130)


regfont=font.Font("fonts/MinecraftRegular-Bmg3.otf",60)
boldfont=font.Font("fonts/MinecraftBold-nMK1.otf",60)
italicfont=font.Font("fonts/MinecraftItalic-R8Mo.otf",60)

def drawscene(enemy,fish):
  screen.fill(BLACK)
  screen.blit(pond,(100,250))
  draw.line(screen,GREEN,(rod[X],rod[Y]),(coords[X],coords[Y]))
  if enemy[TIMER] ==10 and enemy[SHOTSELECTION] == 3:
    shotRect = Rect(enemy[SHOTTRACKX],enemy[SHOTTRCKY],10,10)
    draw.rect(screen,BLUE,shotRect)
  elif enemy[TIMER] >20 and enemy[SHOTSELECTION] == 3:
    shotRect = Rect(enemy[SHOTTRACKX],enemy[SHOTTRCKY],10,10)
    draw.rect(screen,BLUE,shotRect)
  if enemy[SHOTSELECTION] == 4 and enemy[TIMER] < 100:
    if enemy[selectedquadrent] == 1:
      blockingRect = Rect(enemy[X],enemy[Y],300,300)
      draw.rect(screen,BLUE,blockingRect)
      if enemy[TIMER] > 100:
        draw.rect(screen,RED,blockingRect)
        if blockingRect.collidepint(player[X],player[Y]):
          player[PLAYERSCORE] -= enemy[SHOTPOINT]
    elif enemy[selectedquadrent] == 2:
      blockingRect = Rect(enemy[X],enemy[Y],-300,300)
      draw.rect(screen,BLUE,blockingRect)
      if enemy[TIMER] > 100:
        draw.rect(screen,RED,blockingRect)
        if blockingRect.collidepint(player[X],player[Y]):
          player[PLAYERSCORE] -= enemy[SHOTPOINT]
    elif enemy[selectedquadrent] == 3:
      blockingRect = Rect(enemy[X],enemy[Y],300,-300)
      draw.rect(screen,BLUE,blockingRect)
      if enemy[TIMER] > 100:
        draw.rect(screen,RED,blockingRect)
        if blockingRect.collidepint(player[X],player[Y]):
          player[PLAYERSCORE] -= enemy[SHOTPOINT]
    elif enemy[selectedquadrent] == 4:
      blockingRect = Rect(enemy[X],enemy[Y],-300,-300)
      draw.rect(screen,BLUE,blockingRect)
      if enemy[TIMER] > 100:
        draw.rect(screen,RED,blockingRect)
        if blockingRect.collidepint(player[X],player[Y]):
          player[PLAYERSCORE] -= enemy[SHOTPOINT]
  for x in range(0,len(fish)):
    if fish[x][FISHCAUGHT] != true:
      fishRect = Rect(fish[x][FISHX],fish[x][FISHY],10,10)
      draw.rect(screen,(100,100,100),fishRect)

  
    #if fish[x][FISHVALUE] == 1 and fish[x][FISHCAUGHT] == True :
    #elif fish[x][FISHVALUE] == 2 and fish[x][FISHCAUGHT] == True :
    #elif fish[x][FISHVALUE] == 3 and fish[x][FISHCAUGHT] == True :
    #elif fish[x][FISHVALUE] == 4 and fish[x][FISHCAUGHT] == True :
    #This will momentarily 
    
    



def bigEnemy(enemy,player,powerup):
  if enemy[NEWSHOT] == True:
    enemy[SHOTSELECTION] = randint(1,4)
    enemy[SHOTTRACKX] = player[X]
    enemy[SHOTTRACKY] = player[Y]
    enemy[NEWSHOT] == False
    enemy[selectedquadrent] = randint(1,4)
  if powerup[PWTIMER] != 2:
    if enemy[SHOTSELECTION] == 1:
      enemy[SHOTPOINT] = 100
      enemy[SHOTCOLOR] = 16713707
      if enemy[SHOTX] != player[X]:
        if enemy[SHOTX] < player[X]:
          enemy[SHOTX] += 2
        elif enemy[SHOTX] > player[X]:
          enemy[SHOTX] -=2
      if enemy[SHOTY] != player[Y] :
        if enemy[SHOTY] < player[Y]:
          enemy[SHOTY] += 2
        elif enemy[SHOTY] > player[Y]:
          enemy[SHOTY] -= 2
      shotRect = Rect(enemy[SHOTX],enemy[SHOTY],10,10)
      if shotRect.colldepoint(player[X],player[Y]):
        player[PLAYERSCORE] -= enemy[SHOTPOINT]
        enemy[NEWSHOT] = True
      if shotrect.collidepoint(player[RODX],player[RODY]):
        enemy[NEWSHOT] = True
    if enemy[SHOTSELECTION] == 2:
      enemy[SHOTPOINT] = 200
      enemy[SHOTCOLOR] = 16760923
      if enemy[SHOTX] != enemy[SHOTTRACKX]:
        if enemy[SHOTX] < enemy[SHOTTRACKX]:
          enemy[SHOTX] += 20
        elif enemy[SHOTX] > enemy[SHOTTRACKX]:
          enemy[SHOTX] -= 20
      if enemy[SHOTY] != enemy[SHORTTRACKY] :
        if enemy[SHOTY] < enemy[SHOTTRACKY]:
          enemy[SHOTY] += 20
        elif enemy[SHOTY] > enemy[SHORTTRACKY]:
          enemy[SHOTY] -= 20
      shotRect = Rect(enemy[SHOTX],enemy[SHOTY],20,20)
      if shotRect.colldepoint(player[X],player[Y]):
        player[PLAYERSCORE] -= enemy[SHOTPOINT]
        enemy[NEWSHOT] = True
      if shotrect.collidepoint(player[RODX],player[RODY]):
        enemy[NEWSHOT] = True
    if enemy[SHOTSELECTION] == 3:
      enemy[SHOTPOINT] = 10000
      enemy[SHOTCOLOR] = 7192764
      enemy[TIMER] += 1
      shotRect = Rect(enemy[SHOTTRACKX],enemy[SHOTTRCKY],10,10)
      if enemy[TIMER] >= 20:
        if shotRect.colldepoint(player[X],player[Y]):
          player[PLAYERSCORE] -= enemy[SHOTPOINT]
          enemy[NEWSHOT] = True
      if enemy[TIMER] == 30:
        enemy[TIMER] = 0
      if shotrect.collidepoint(player[RODX],player[RODY]):
        enemy[NEWSHOT] = True
    if enemy[SHOTSELECTION] == 4:
      enemy[TIMER] += 1
      enemy[SHOTPOINT] = 10
      enemy[SHOTCOLOR] = 7192764
      if enemy[TIMER] >= 400:
        enemy[TIMER] = 0
        enemy[NEWSHOT] = True
    elif enemy[SHOTY] >= 1000 or enemy[SHOTY] <= 0 or enemy[SHOTX] >= 1000 or enemy[SHOTX] <= 0:
      enemy[NEWSHOT] = True
  else:
    powerup[PWTIMER] += 1
    if powerup[PWTIMER] >= 500:
      powerup[POWERUPVAL] = 0

def highscore(lohighscores):
  namesandscores = []
  for i in range(0,10):
    openedfile = open(lohighscores)
    score = lohighscores+1
    scores = (lohighscores,int(score))
    namesandscores.append(scores)
  namesandscores.sort()
  del namesandscores[0]
  out = open(lohighscores, "w")
  for i in range(0,10):
    out.write(str(namesandscores[i] + "\n"))
  out.close
      

    


def fishCatch(player,fish,powerup):
  for x in range(0,len(fish)):
    fishRect = Rect(fish[x][FISHX],fish[x][FISHY],10,10)
    if fishrect.collidepoint(player[RODX],player[RODY]):
      fish[x][FISHCAUGHT] = True
    if fish[x][FISHCAUGHT]:
      if fish[x][FISHVALUE] == 1:
        player[PLAYERSCORE] += 100
        if powerup[POWERUPVAL] == 1:
          player[PLAYERSCORE] += 100
          powerup[POWERUPVAL] = 0
      elif fish[x][FISHVALUE] == 2:
        player[PLAYERSCORE] += 200
        if powerup[POWERUPVAL] == 1:
          player[PLAYERSCORE] += 200
          powerup[POWERUPVAL] = 0
      elif fish[x][FISHVALUE] == 3:
        player[PLAYERSCORE] += 300
        if powerup[POWERUPVAL] == 1:
          player[PLAYERSCORE] += 300
      elif fish[x][FISHVALUE] == 4:
        player[PLAYERSCORE] += 400
        if powerup[POWERUPVAL] == 1:
          player[PLAYERSCORE] += 400
      elif fish[x][FISHVALUE] == 5:
        player[PLAYERSCORE] += 500
        if powerup[POWERUPVAL] == 1:
          player[PLAYERSCORE] += 500
      elif fish[x][FISHVALUE] == 6:
        player[PLAYERSCORE] += 600
        if powerup[POWERUPVAL] == 1:
          player[PLAYERSCORE] += 600
      elif fish[x][FISHVALUE] == 7:
        player[PLAYERSCORE] += 0
      fish[x][FISHVALUE] = randint(1,7)
      fish[x][FISHX] = randint(201,799)
      fish[x][FISHY] = randint(251,849)

def move_coords(angle, radius, coords):
    theta = radians(angle)
    return coords[0] + radius * cos(theta), coords[1] + radius * sin(theta)

#def moverod(rod,powerup):
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
    
    rod[X]+=v[X]
    rod[Y]+=v[Y]
    if mov==True:
        mov=False
    if keys[K_UP]:
       rs+=0.5
    if keys[K_DOWN]:
      rs-=0.5
##    if keys[K_UP]:
##      if powerup[POWERUPVAL] != 3:
##        rs+=0.5
##      else:
##        rs+=1
##        powerup[PWTIMER] +=1
##        if power[PWTIMER] >= 600:
##          powerup[POWERUPVAL] = 0
##    if keys[K_DOWN] and rs>1:
##      if powerup[POWERUPVAL] != 3:
##        rs-=0.5
##      else:
##        rs-=1
##        powerup[PWTIMER] +=1
##        if power[PWTIMER] >= 600:
##          powerup[POWERUPVAL] = 0   

##def powerups(powerup,player):
##  if powerup[CAUGHT] == False:
##    powerupRect = Rect(powerup[X],powerup[Y],10,10)
##  if powerupRect.collidepoint(player[X],player[Y]):
##    powerup[POWERUPVAL] = randint(1,4)
##    powerup[CAUGHT] = True
##    powerup[X] = randint(200,800)
##    powerup[Y] = randint(250,850)
##  #One doubles your next score
##                                        



circlestuff = [500,550,90]
ANGLE = 2

def menu(action):
    running = True
    play = Rect(300,425,400,150)

    menuback = image.load("images/title screen resized.jpg")
    
    while action=="menu":
        for e in event.get():
            if e.type == QUIT:
                quit()

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        screen.blit(menuback,(0,0))

        draw.rect(screen,(255,165,0),play)
        if play.collidepoint(mpos):
            draw.rect(screen,(255,255,51),play,5)
            if mb[0] == 1:
                main("game")
        else:
            draw.rect(screen,(255,165,0),play,2)
        playtext = regfont.render("PLAY",True,(255,255,255))
        screen.blit(playtext,(425,460))
        titletext = boldfont.render("Frederick Foombotto's",True,(255,165,0))
        titletext2= boldfont.render("Fishing",True,(255,165,0))
        screen.blit(titletext,(125,75))
        screen.blit(titletext2,(400,150))
        display.flip()
        

def main(action):
    global event
    global next_tick
    global angle
    global coords
    running = True
    while action=="game":
        for e in event.get():
            if e.type == QUIT:
                action= "menu"

              
        ticks=time.get_ticks()
        if ticks > next_tick:
            next_tick += speed
            angle += 0.333
            coords = move_coords(angle, 2, coords)
            rect.topleft = coords

        moverod(rod)
##        bigenemy(bigenemy,coords,powerup)
##        screen.fill((0,0,30))
        drawscene(bigenemy,fish1)
        display.flip()
        myClock.tick(30)
menu("menu")


 


