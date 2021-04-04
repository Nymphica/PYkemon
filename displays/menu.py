import pygame as pg
from displays.button import Button, draw_button

def draw_menu():
    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res)
    pg.display.set_caption("Menu")
    width = screen.get_width()
    height = screen.get_height()

    font = pg.font.Font('displays/font.ttf', height // 20)

    # general button configuration:
    high_color= (0, 0, 0)
    colors = ((55, 55, 55), high_color)
    button_dim = (width // 2, height // 10)
    origin = (width //4, height //2)

    # creating first button:
    position1 = (origin[0] - button_dim[0] // 2, origin[1] - button_dim[1] * 2)
    label1 = "PIKACHU"
    button1 = Button(label1, button_dim, position1, colors)

    # creating second button:
    position2 = (origin[0] - button_dim[0] // 2, origin[1] - button_dim[1])
    label2 = "CHARMANDER"
    button2 = Button(label2, button_dim, position2, colors)

    # creating third button:
    position3 = (origin[0] - button_dim[0] // 2, origin[1])
    label3 = "BULBASAUR"
    button3 = Button(label3, button_dim, position3, colors)

    # creating fourth button:
    position4 = (origin[0] - button_dim[0] // 2, origin[1] + button_dim[1])
    label4 = "SQUIRTLE"
    button4 = Button(label4, button_dim, position4, colors)

    # creating fifth button:
    position5 = (origin[0] - button_dim[0] // 2, origin[1] + button_dim[1]*2)
    label5 = "GASTLY"
    button5 = Button(label5, button_dim, position5, colors)

    buttons = [button1, button2, button3, button4, button5] #buttons list
    positions = [position1, position2, position3, position4, position5] #buttons positions list
    cursor = 0

    pikachu = pg.image.load('displays/imgs/front/PIKACHU.png')
    pikachu = pg.transform.scale(pikachu, (350,350))
    charmander = pg.image.load('displays/imgs/front/CHARMANDER.png')
    charmander = pg.transform.scale(charmander, (350,350))
    bulbasaur = pg.image.load('displays/imgs/front/BULBASAUR.png')
    bulbasaur = pg.transform.scale(bulbasaur, (350,350))
    squirtle = pg.image.load('displays/imgs/front/SQUIRTLE.png')
    squirtle = pg.transform.scale(squirtle, (350,350))
    gastly = pg.image.load('displays/imgs/front/GASTLY.png')
    gastly = pg.transform.scale(gastly, (350,350))

    choose_text = font.render('Choose your Pokemon:',True, (255,255,255))

    choosed_pokemon = "NONE"

    running_menu=True

    while running_menu:
        pg.display.update()
        # defining cursor position:
        cursor_position_shifted = positions[cursor] #from each button possition
        cursor_position = (
            cursor_position_shifted[0] + button_dim[0] // 20, # cursor position on X
            cursor_position_shifted[1] + button_dim[1] // 2 #cursor position on Y
        )

        # capturing events: 
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                break
            if ev.type == pg.KEYDOWN:

                # Moving cursor:
                if ev.key == pg.K_UP:
                    cursor -= 1
                elif ev.key == pg.K_DOWN:
                    cursor += 1

                #Verifyng cursor limits:
                if cursor >= len(positions):
                    cursor -= len(positions)
                elif cursor < 0:
                    cursor += len(positions)
                
                #choose pokemon
                if ev.key == pg.K_RETURN:
                    for button in buttons:
                        if cursor_position in button:
                                choosed_pokemon = button.label
                                print(choosed_pokemon)
                                return(choosed_pokemon, "NAMEIT")
                                running_menu = False
                                break
                                

        screen.fill(bg_color) #filling background

        screen.blit(choose_text, (10,100))

        for button in buttons:
            if cursor_position in button:
                if button.label == "PIKACHU":
                    button.alternative_color = (255, 215, 0)
                    screen.blit( pikachu, (450,125) )
                
                elif button.label == "CHARMANDER":
                    button.alternative_color = (255, 0, 0)
                    screen.blit( charmander, (450,125) )

                elif button.label == "BULBASAUR":
                    button.alternative_color = (0, 255, 0)
                    screen.blit( bulbasaur, (450,125) )

                elif button.label == "SQUIRTLE":
                    button.alternative_color = (0, 0, 255)
                    screen.blit( squirtle, (450,125) )
                    
                else: #gastly
                    button.alternative_color = (255, 0, 255)
                    screen.blit(gastly, (450,125) )
                
                draw_button(screen, button, bg_color, font, True)
            else:
                draw_button(screen, button, bg_color, font)

        # Printing cursor:
        sc = 16 #cursor size
        xcc, ycc = cursor_position
        x0c, y0c = xcc - sc // 2, ycc - sc // 2 # |‾
        x1c, y1c = xcc + sc // 2, ycc + sc // 2 #    _|
        pg.draw.polygon(
            screen, (255, 255, 255),
            [(x0c, y0c), (x1c, (y0c + y1c) // 2), (x0c, y1c)]
        )
        icon = pg.image.load('icon.png')# window icon
        pg.display.set_icon(icon)