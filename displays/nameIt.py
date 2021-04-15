# don´t forget that pg is pygame
import pygame as pg
from random import randint

def draw_nameIt(player1):

    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res) #set screen
    pg.display.set_caption("Name It") #set caption
    width = screen.get_width()
    height = screen.get_height()
    icon = pg.image.load('icon.png')# window icon

    input_box = pg.Rect(280, height//3.5, 200, 50) #rect for the input (x, y, width, height)

    font = pg.font.Font('displays/font.ttf', height // 20)
    big_font = pg.font.Font('displays/font.ttf', height // 20) 

    text= '' #string for the name input

    choose_text = font.render('Choose your Pokemon name:',True, (255,255,255)) #the choose text

    Mgender = big_font.render(f'♂',True, (0,0,255)) #set male gender
    Fgender = big_font.render(f'♀',True, (255,0,0)) # set female gender

    genders = [Mgender, Fgender] #list of gender

    pGender = genders[randint(0, 1)] #get an random gender

    running_name = True

    while running_name:
        screen.fill(bg_color) #filling background

        player = pg.image.load(player1.pokeSprite[1]) #the img of the choosed pokemon
        player = pg.transform.scale(player, (290,290))

        for event in pg.event.get(): #for all enevents made

            if event.type == pg.QUIT: #if it is the quit button, so quit
                running_name=False
                break

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN: #if ENTER
                    if text == '': #if it has a name
                        text = player1.name
                    running_name = False #done

                elif event.key == pg.K_BACKSPACE: #if BACKSPACE take off the last letter
                        text = text[:-1]
                else:
                        if len(text) < 5 : #else if the name length is less than 5 
                            text += event.unicode # add the letter

        txt_surface = font.render(text, True, (255,255,255)) #the txt surface
        screen.blit(txt_surface, (input_box.x+38, input_box.y+5)) #putting the txt on display
        
        # Blit the input_box rect.
        pg.draw.rect(screen, (255,255,255), input_box, 2)

        screen.blit(choose_text, (90,100))

        screen.blit( player, (240,250) )

        screen.blit( pGender, (250,height//3.5) )

        pg.display.flip()

        pg.display.set_icon(icon)
        
    return("BATTLE", text, pGender)