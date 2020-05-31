from pygame import *
def menu():
    running = True
    play = Rect(550,425,400,150)
    
    while running:
        for e in event.get():
            if e.type == QUIT:
                return "exit"

            mpos = mouse.get_pos()
            mb = mouse.get_pressed()

            draw.rect(screen,(255,165,0),play)
            if play.collidepoint(mpos):
                draw.rect(screen,(255,255,51),play,2)
                #if mb[0] == 1:
                    #return "play"
            else:
                draw.rect(screen,(255,165,0),play,2)
            playtext = regfont.render("PLAY",True,(255,255,255))
            screen.blit(playtext,(650,450))
            titletext = boldfont.render("Freddie Fazbear's Fishing",True,(255,255,255))
            screen.blit(titletext,(400,100))

screen = display.set_mode((1500,1000))
init()
regfont=font.Font("fonts/MinecraftRegular-Bmg3.otf",60)
boldfont=font.Font("fonts/MinecraftBold-nMK1.otf",60)
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()
    #if page = "play":
        #page = game()

quit()
    
