import pygame, time
from Valikot.paaValikko import paaValikko


#main-funktio
#sisältää vain turhaa testikoodia
def main():
    print("Toimii")
    sana:str = "tuloste"
    valikko = paaValikko(sana)
    while True:
        time.sleep(2)
        valikko.tulosta()
        



#Game-Active variaabeli
running = True
while running:
# Gameloop

    #Check For Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#    Button()


#Kutsutaan main-funktiota
if __name__ == "__main__":
    pygame.init()
    main()