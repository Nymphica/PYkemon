import pygame as pg
from displays.button import Button, draw_button
from battle.pokemonList import *

def draw_menu():
    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res)
    pg.display.set_caption("Menu")
    width = screen.get_width()
    height = screen.get_height()

    font = pg.font.Font('displays/font.ttf', height // 20)

    # general button configuration:
    colors = ((55, 55, 55), (0,0,0))
    button_dim = (width // 2, height // 10)
    origin = (width //4, height //2)

    buttons = []
    positions = []
    pokeSprites = []
    labels = []
    for i in range(len(pokemonList)):
        position = (origin[0] - button_dim[0]//2, origin[1] + button_dim[1] * (i - 3))
        positions.append(position)
        label = pokemonList[i].name
        labels.append(label)
        buttons.append(Button(label, button_dim, position, colors))
        pokemon = pg.image.load(pokemonList[i].pokeSprite[1])
        pokemon = pg.transform.scale(pokemon, (350, 350))
        pokeSprites.append(pokemon)

    cursor = 0

    choose_text = font.render('Choose your Pokemon:',True, (255,255,255))

    player1 = "NONE"

    icon = pg.image.load('icon.png')# window icon
    pg.display.set_icon(icon)

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
                                indButton = labels.index(button.label)
                                player1 = pokemonList[indButton]
                                print(player1)
                                return(player1, "NAMEIT")
                                running_menu = False
                                break
                                

        screen.fill(bg_color) #filling background

        screen.blit(choose_text, (10,50))

        for button in buttons:
            if cursor_position in button:
                indButton = labels.index(button.label)
                screen.blit(pokeSprites[indButton], (440, 70))
                for poke in pokemonList:
                    if button.label == poke.name:
                        if 'fire' in poke.pokeType:
                            button.alternative_color = (255, 0, 0)
                        elif 'water' in poke.pokeType:
                            button.alternative_color = (0, 0, 255)
                        elif 'grass' in poke.pokeType:
                            button.alternative_color = (0, 255, 0)
                        elif 'electric' in poke.pokeType:
                            button.alternative_color = (255, 215, 0)
                
                draw_button(screen, button, bg_color,(255,255,255), font, True)
            else:
                draw_button(screen, button, bg_color,(255,255,255), font)

        # Printing cursor:
        sc = 16 #cursor size
        xcc, ycc = cursor_position
        x0c, y0c = xcc - sc // 2, ycc - sc // 2 # |‾
        x1c, y1c = xcc + sc // 2, ycc + sc // 2 #    _|
        pg.draw.polygon(
            screen, (255, 255, 255),
            [(x0c, y0c), (x1c, (y0c + y1c) // 2), (x0c, y1c)]
        )