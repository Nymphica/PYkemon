import pygame as pg
from displays.button import Button, draw_button
from battle.pokemonList import *

def draw_menu():
    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res)
    pg.display.set_caption("Menu")
    icon = pg.image.load('icon.png')# window icon
    pg.display.set_icon(icon)
    width = screen.get_width()
    height = screen.get_height()

    font = pg.font.Font('displays/font.ttf', height // 20)
    tiny_font = pg.font.Font('displays/font.ttf', height // 43)

    # general button configuration:
    colors = ((55, 55, 55), (0,0,0))
    button_dim = (width // 2, height // 10)
    origin = (width //4, height //2)

    buttons = []
    positions = []
    movePositions=[(400, 520), (475, 550)]
    hpPosition= (475, 470)
    typePosition = (570, 430)
    typeTxt = font.render('Type:',True, (255,255,255))
    pokeSprites = []
    pokeMoves =[]
    pokemaxHp =[]
    pokeTypes = []
    labels = []
    #loop for button creation
    for i in range(len(pokemonList)):
        position = (origin[0] - button_dim[0]//2, origin[1] + button_dim[1] * (i - 3))
        positions.append(position)
        label = pokemonList[i].name
        labels.append(label)
        buttons.append(Button(label, button_dim, position, colors))
        pokemon = pg.image.load(pokemonList[i].pokeSprite[1])
        pokemon = pg.transform.scale(pokemon, (350, 350))
        pokeSprites.append(pokemon)

        moves = pokemonList[i].moves
        pokeMoves.append(moves)
        pokemaxHp.append(pokemonList[i].maxHp)
        #if it has 2 types, take the first
        if len(pokemonList[i].pokeType[0]) > 2 : pokeTypes.append(pokemonList[i].pokeType[0])
        else: pokeTypes.append(pokemonList[i].pokeType)

    cursor = 0

    choose_text = font.render('Choose your Pokemon:',True, (255,255,255))

    playerPokemon = "NONE"

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
                                playerPokemon = pokemonList[indButton]
                                print('choosed pokemon: ',playerPokemon.name)
                                return(playerPokemon, "NAMEIT")
                                running_menu = False
                                break
                                

        screen.fill(bg_color) #filling background

        screen.blit(choose_text, (10,50))

        for button in buttons:
            if cursor_position in button:
                indButton = labels.index(button.label)
                screen.blit(pokeSprites[indButton], (440, 70))

                hp = font.render(f'HP: {pokemaxHp[indButton]}',True, (255,255,255))
                screen.blit(hp, hpPosition)

                moves = tiny_font.render(f'moves: {pokeMoves[indButton][0].name}, {pokeMoves[indButton][1].name}',True, (255,255,255))
                screen.blit(moves, movePositions[0])
                moves1 = tiny_font.render(f'{pokeMoves[indButton][2].name}, {pokeMoves[indButton][3].name}',True, (255,255,255))
                screen.blit(moves1, movePositions[1])

                screen.blit(typeTxt, (420, 430))

                for poke in pokemonList:
                    if poke.name == button.label:
                        if 'fire' in poke.pokeType:
                            button.alternative_color = (255, 0, 0)
                            Type = (font.render(f'{pokeTypes[indButton]}',True, (255,0,0)))
                            screen.blit(Type, typePosition)
                        elif 'water' in poke.pokeType:
                            button.alternative_color = (0, 0, 255)
                            Type = (font.render(f'{pokeTypes[indButton]}',True, (0,0,255)))
                            screen.blit(Type, typePosition)
                        elif 'grass' in poke.pokeType:
                            button.alternative_color = (0, 255, 0)
                            Type = (font.render(f'{pokeTypes[indButton]}',True, (0,255,0)))
                            screen.blit(Type, typePosition)
                        elif 'electric' in poke.pokeType:
                            button.alternative_color = (255, 215, 0)
                            Type = (font.render(f'{pokeTypes[indButton]}',True, (255,215,0)))
                            screen.blit(Type, typePosition)
                    
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