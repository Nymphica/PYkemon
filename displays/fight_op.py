#all battle potions
from displays.button import *
from displays.img import *
import pygame as pg
from time import sleep

def draw_moves(screen, pokemon, pokeName, player, enemy, width, height, pp_bar, text_bar):

    labels=[]
    for move in pokemon.moves:
        labels.append(move.name)

    bg_color = (255, 255, 255) #background color
    font = pg.font.Font('displays/font.ttf', height // 30)
    big_font = pg.font.Font('displays/font.ttf', height // 20) 

# general button configuration:
    colors = ((255, 255, 255), (255, 255, 255))
    button_dim = (width // 5 + 15, height // 15)
    origin = (width-button_dim[0]*3.8, height-36)

    buttons = []
    positions = []

    for i in range(len(labels)):
        if  i==0 :
            position = (origin[0] - button_dim[0]//3, origin[1] - button_dim[1] * 2)
        elif i==1:
            position = (origin[0] - button_dim[0]//3, origin[1] - button_dim[1] + 10)
        if  i==2 :
            position = (origin[0] + 110 + button_dim[0]//3, origin[1] - button_dim[1] * 2)
        elif i==3:
            position = (origin[0] + 110 + button_dim[0]//3, origin[1] - button_dim[1] + 10)

        positions.append(position)
        buttons.append(Button(labels[i], button_dim, position, colors))

    used_text = big_font.render(f'{pokeName} used',True, (255,255,255))
    used_text1 = big_font.render('',True, (255,255,255))

    on = True
    player_attacked = False
    is_text=False
    cursor = 0
    cycle = 0
    while on :

        if enemy.is_red:
            print('is red')
            sleep(0.001)
            enemy.back_img()
            screen.blit( enemy.origin, enemy.pos )
            screen.blit( text_bar, (0,450) )
            screen.blit(used_text, (40,480))
            screen.blit(used_text1, (40,530))
            cycle=1

        if is_text:
            sleep(1)
            for move in pokemon.moves:
                if move.name == choosed_move :
                    print(move.name)
                    print(move.power)
                    return(move.power)
            on = False

        # defining cursor position:
        cursor_position_shifted = positions[cursor] #from each button possition
        cursor_position = (
            cursor_position_shifted[0] - 40 + button_dim[0] // 10, # cursor position on X
            cursor_position_shifted[1] + button_dim[1] // 2#cursor position on Y
        )

        # Printing cursor:
        sc = 16 #cursor size
        xcc, ycc = cursor_position
        x0c, y0c = xcc - sc // 2, ycc - sc // 2 # |‾
        x1c, y1c = xcc + sc // 2, ycc + sc // 2 #    _|

        if not player_attacked:
            screen.blit( pp_bar, (0,450) )
            for button in buttons: # DRAW ALL BUTTONS
                draw_button(screen, button, bg_color, (0,0,0), font)
            pg.draw.polygon(
            screen, (55, 55, 55),# cursor color
            [(x0c, y0c), (x1c, (y0c + y1c) // 2), (x0c, y1c)]
        )

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
                pg.quit()

            if ev.type == pg.KEYDOWN:

                # Moving cursor:
                if ev.key == pg.K_UP:
                    cursor -= 1
                elif ev.key == pg.K_DOWN:
                    cursor += 1
                elif ev.key == pg.K_LEFT:
                    cursor -= 2
                elif ev.key == pg.K_RIGHT:
                    cursor += 2

                #Verifyng cursor limits:
                if cursor >= len(positions):
                    cursor -= len(positions)
                elif cursor < 0:
                    cursor += len(positions)
                
                #choose action
                if ev.key == pg.K_RETURN:

                    for button in buttons:

                        if buttons[cursor] is button:

                            move_name = f'{button.label}!'
                            choosed_move = button.label
                            print(move_name)
                            used_text1 = big_font.render(move_name,True, (255,255,255))
                            enemy.turn_red()
                            player.shake()
                            player_attacked = True
        
        if cycle == 1: cycle = 0; is_text= True; print('change cycle')

        pg.display.flip()

'''
                        elif choosed_action in [move.name for move in player1.moves]:
                            screen.blit( pp_bar, (0,450) )
                            enemyIMG.turn_red() #turn enemy red
                            screen.blit( bar_2, (420,280) ) #temporario
                            screen.blit( red_bar, (587,358) )#temporario
                            player.shake() #shake player img'''