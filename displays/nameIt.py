# don´t forget that pg is pygame
import pygame as pg

def draw_nameIt(choosed_pokemon):

    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res) #set screen
    pg.display.set_caption("Name It") #set caption
    width = screen.get_width()
    height = screen.get_height()

    input_box = pg.Rect(300, height//3, 200, 50) #rect for the input (x, y, width, height)

    font = pg.font.Font('displays/font.ttf', height // 20)

    text= '' #string for the name input

    choose_text = font.render('Choose your Pokemon name:',True, (255,255,255)) #the choose text

    running_name = True

    while running_name:
        screen.fill(bg_color) #filling background

        player = pg.image.load(f'displays/imgs/front/{choosed_pokemon}.png') #the img of the choosed pokemon
        player = pg.transform.scale(player, (290,290))

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running_name=False
                break

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN: #if ENTER, so it's done
                        print(text)
                        running_name = False

                elif event.key == pg.K_BACKSPACE: #if BACKSPACE take off the last letter
                        text = text[:-1]
                else:
                        if len(text) < 5: #else add the letter
                            text += event.unicode

        txt_surface = font.render(text, True, (255,255,255)) #the txt surface
        screen.blit(txt_surface, (input_box.x+38, input_box.y+5)) #putting the txt on display
        
        # Blit the input_box rect.
        pg.draw.rect(screen, (255,255,255), input_box, 2)

        screen.blit(choose_text, (90,100))

        screen.blit( player, (270,250) )

        pg.display.flip()

        icon = pg.image.load('icon.png')# window icon
        pg.display.set_icon(icon)
        
    return("BATTLE")