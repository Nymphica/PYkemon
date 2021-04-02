import pygame

def main():

    pygame.init()
    pygame.display.set_caption("Background estatico")
    
    #background
    bg = pygame.image.load('battle\Battle_display\FundoPokemon.png')
    bg = pygame.transform.scale(bg, (800, 450))

    #pokemon status bar
    pp_bar = pygame.image.load('battle\Battle_display\pp_bar.png')
    pp_bar = pygame.transform.scale(pp_bar, (800,150))

    #options FIGHT/RUN/ETC bar
    options = pygame.image.load('battle\Battle_display\Fgt_options.png')
    options = pygame.transform.scale(options, (400,150))

    #text bar
    text_bar = pygame.image.load('battle\Battle_display\Text_bar.png')
    text_bar = pygame.transform.scale(text_bar, (800,150))

    #Second pokemon bar
    bar_2 = pygame.image.load('battle\Battle_display\Bar_2.png')
    bar_2 = pygame.transform.scale(bar_2, (360,160))

    #first pokemon bar
    bar_1 = pygame.image.load('battle\Battle_display\Bar_1.png')
    bar_1 = pygame.transform.scale(bar_1, (360,140))

    #grey bar
    gry_bar = pygame.image.load('battle\Battle_display\gry_bar.png')
    gry_bar = pygame.transform.scale(gry_bar, (172,15))

    #red bar
    red_bar = pygame.image.load('battle\Battle_display\Red_bar.png')
    red_bar = pygame.transform.scale(red_bar, (166,13))

    #meow
    meow = pygame.image.load('battle\Battle_display\meow.png')
    meow = pygame.transform.scale(meow, (350,350))

    #pikachu
    pikachu = pygame.image.load('battle\Battle_display\pikachu.png')
    pikachu = pygame.transform.scale(pikachu, (350,350))

    running=True
    while running:
        screen = pygame.display.set_mode((800, 600)) #screen size
        screen.fill((255,255,255)) #Screen color background

        screen.blit( bg, (0,0) )
        screen.blit( pp_bar, (0,450) )
        screen.blit( bar_2, (420,280) )
        screen.blit( bar_1, (10,30) )
        screen.blit( text_bar, (0,450) )
        screen.blit( options, (400,450) )
        screen.blit( gry_bar, (153,108) )
        screen.blit( red_bar, (587,358) )
        screen.blit( meow, (410,0) )
        screen.blit( pikachu, (0,138) )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
if __name__  == '__main__':
    main()