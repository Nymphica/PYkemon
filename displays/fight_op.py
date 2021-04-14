#all battle potions
from displays.button import *
from displays.img import *
import pygame as pg
from time import sleep
from random import randint
from battle.attack import attack
#draw_moves(screen to blit, )
def draw_moves(player, pokeName, player1, player1IMG, player2, player2IMG, text_bars, screen, player1Info, player2Info):

    width = screen.get_width() #screen width
    height = screen.get_height() #screen height

    pp_bar, text_bar = text_bars

    #recathing player and enemy info for after re-blit
    pName, pLevel, pPp, pokeGender = player1Info
    eName, eGender, eLevel = player2Info

    #background
    bg = pg.image.load('sprites/battle_bg\FundoPokemon.png')
    bg = pg.transform.scale(bg, (800, 450))

    #Second pokemon bar
    bar_2 = pg.image.load('sprites/battle_bg\Bar_2.png')
    bar_2 = pg.transform.scale(bar_2, (360,160))

    #first pokemon bar
    bar_1 = pg.image.load('sprites/battle_bg\Bar_1.png')
    bar_1 = pg.transform.scale(bar_1, (360,140))

    bg_color = (255, 255, 255) #background color
    font = pg.font.Font('displays/font.ttf', height // 30)
    tiny_font = pg.font.Font('displays/font.ttf', height // 35)
    big_font = pg.font.Font('displays/font.ttf', height // 20)

    if player == 'player2':

        player1IMG = pg.image.load(player1.pokeSprite[1])
        pos, scale= (430, 0), (330,330)
        player1IMG = image("player2", player1IMG, pos, scale, screen)

        player2IMG = pg.image.load(player2.pokeSprite[0])
        pos, scale= (0, 160), (290,290)
        player2IMG = image("player1",player2IMG, pos, scale, screen)

        used_text = big_font.render(f'{player2.name} used',True, (255,255,255))
        used_text1 = big_font.render('',True, (255,255,255))

        on = True

        damage = 0

        cycle = 0

        while on:
            #separated by cycles to avoid the sleep of stop the hole thread

            #cycle = 0 choose a random move, hit the enemy and turn it red
            #cycle = 1 turnning the enemy img back to normal and blit the used move text
            #cycle = 2 blit the efecctivenes text

            if cycle == 2: 
                sleep(2) #wait for the used move text to blit
                move = choosed_move

                if randint(0, 100) > move.accuracy: #if accuracy
                    damage, modifier = 0, 1 #set damage and modifier
                    #rendering and blit the  effectiveness text
                    text = "Attack missed"
                    efecctivenes = big_font.render(text,True, (255,255,255))
                    screen.blit( text_bar, (0,450) )
                    screen.blit(efecctivenes, (40,480))
                
                else:
                    damage, modifier = attack(player2, player1, move) #make the attack and set the damage and modifier of it

                    if modifier != 1: #see the effectiveness of the attack
                        if modifier == 2:
                            text = "THAT WAS SUPER EFECCTIVE!"
                        elif modifier == 0:
                            text = "THAT WAS INEFFECTIVE!"
                        elif modifier == 0.5:
                            text = "THAT WASN'T VERY EFFECTIVE"
                        #rendering and blit the effectiveness text
                        effectiveness = big_font.render(text,True, (255,255,255))
                        screen.blit( text_bar, (0,450) )
                        screen.blit(effectiveness, (40,480))

                    pg.display.flip() #flip display
                return(damage, move)
                on = False #stop whyle loop

            elif cycle == 1: 
                sleep(1) #wait for the attack animation
                player1IMG.back_img() #turn the player 1 image back to normal
                #blit everything
                screen.blit( player1IMG.origin, player1IMG.pos )
                screen.blit( text_bar, (0,450) )
                screen.blit(used_text, (40,480))
                screen.blit(used_text1, (40,530))
                #change the cycle
                cycle=2
                pg.display.flip()#flip the display

            elif cycle==0:

                #choose a random move
                choosed_move = player2.moves[randint(0,3)]
                if choosed_move.currentPP<0: #checking if it has pp
                    continue

                #setting the move used text with the choosed move
                used_text1 = big_font.render(f'{choosed_move.name}!',True, (255,255,255))

                #blit the background to make an new animation
                screen.blit( bg, (0,0) )
                #turn player 1 red and shake player 2
                player1IMG.turn_red()
                player2IMG.shake()
                #blit the other display components
                screen.blit( bar_2, (420,280) )
                screen.blit( bar_1, (10,30) )
                screen.blit( text_bar, (0,450) )
                #enemy info
                screen.blit(eName, (27,55))
                screen.blit(eLevel, (310,55))
                screen.blit(eGender, (245,50))
                #player info
                screen.blit(pName, (470,310))
                screen.blit(pokeGender, (675,305))
                screen.blit(pLevel, (735,310))
                screen.blit(pPp, (630,377))
                #change the cycle
                cycle=1

    if player == 'player1':
        # loop for cathing the move names
        labels=[]
        for move in player1.moves:
            labels.append(move.name)

        # setting the displays cofiguration
        bg_color = (255, 255, 255) #background color
        font = pg.font.Font('displays/font.ttf', height // 30)
        big_font = pg.font.Font('displays/font.ttf', height // 20) 

        # general button configuration:
        colors = ((255, 255, 255), (255, 255, 255))
        button_dim = (width // 5 + 60, height // 15) #button dimension
        origin = (width-button_dim[0]*3.8, height-36) #button origin in display

        buttons = [] #list for all the buttons, for future loop to blit them
        positions = [] #list for all the buttons positions, for future loop to blit them

        # loop for creating buttons
        for i in range(len(labels)):
            if  i==0 : #first button
                position = (origin[0] + 150 - button_dim[0]//3, origin[1] - button_dim[1] * 2)
            elif i==1: #second button
                position = (origin[0] + 150 - button_dim[0]//3, origin[1] - button_dim[1] + 10)
            if  i==2 : #third button
                position = (origin[0] + 230 + button_dim[0]//3, origin[1] - button_dim[1] * 2)
            elif i==3: #four button
                position = (origin[0] + 230 + button_dim[0]//3, origin[1] - button_dim[1] + 10)

            positions.append(position) #adding the position
            buttons.append(Button(labels[i], button_dim, position, colors)) #adding the button

        
        cursor = 0 #cursor index

        #separeded because of the paragraph
        used_text = big_font.render(f'{pokeName} used',True, (255,255,255)) # Pokemon used
        used_text1 = big_font.render('',True, (255,255,255)) # Move!

        on = True # variable to stop the while loop
        player_attacked = False 
        damage = 0 # variable to stock the damage od the attack
        is_text = False

        cycle = 0
        while on :


            #cycle = 0 blit the attack options, catch the choosed move and animate the battle (enemy turn red and player shake) 
            #cycle = 1 turnning the enemy img back to normal and blit the used move text
            #cycle = 2 blit the efecctivenes text

            if cycle == 2:

                sleep(1)
                if randint(0, 100) > move.accuracy:

                    damage, modifier = 0, 1
                    text = "Attack missed"
                    efecctivenes = big_font.render(text,True, (255,255,255))
                    screen.blit( text_bar, (0,450) )
                    screen.blit(efecctivenes, (40,480))

                else:

                    damage, modifier = attack(player1, player2, move)

                    if modifier != 1:
                        
                        if modifier == 2:
                            text = "THAT WAS SUPER EFECCTIVE!"

                        elif modifier == 0:
                            text = "THAT WAS INEFFECTIVE!"

                        elif modifier == 0.5:
                            text = "THAT WASN'T VERY EFFECTIVE"

                        efecctivenes = big_font.render(text,True, (255,255,255))
                        screen.blit( text_bar, (0,450) )
                        screen.blit(efecctivenes, (40,480))
                    pg.display.flip()
                    sleep(1)
                return(damage, move)
                on = False

            if cycle == 1:
                sleep(0.001) #quait for the previous animation
                #turn the player 2 image back to normal
                player2IMG.back_img()
                #blit the hole pokemons information again and the used move text
                screen.blit( player2IMG.origin, player2IMG.pos )
                screen.blit( text_bar, (0,450) )
                screen.blit(used_text, (40,480))
                screen.blit(used_text1, (40,530))
                screen.blit( bar_2, (420,280) )
                screen.blit( bar_1, (10,30) )
                #player2 info
                screen.blit(eName, (27,55))
                screen.blit(eLevel, (310,55))
                screen.blit(eGender, (245,50))
                #player1 info
                screen.blit(pName, (470,310))
                screen.blit(pokeGender, (675,305))
                screen.blit(pLevel, (735,310))
                screen.blit(pPp, (630,377))
                #change the cycle
                cycle=2

            if cycle == 0:

                screen.blit( pp_bar, (0,450) )

                for button in buttons: # DRAW ALL BUTTONS
                    draw_button(screen, button, bg_color, (49,47,48), tiny_font)

                # defining cursor position:
                cursor_position_shifted = positions[cursor] #from each button possition
                cursor_position = (
                    cursor_position_shifted[0] - 10 + button_dim[0] - 197, # cursor position on X
                    cursor_position_shifted[1] + button_dim[1] // 2#cursor position on Y
                )

                # Printing cursor:
                sc = 16 #cursor size
                xcc, ycc = cursor_position
                x0c, y0c = xcc - sc // 2, ycc - sc // 2 # |‾
                x1c, y1c = xcc + sc // 2, ycc + sc // 2 #    _|

                #draw cursor
                pg.draw.polygon(
                screen, (55, 55, 55),# cursor color
                [(x0c, y0c), (x1c, (y0c + y1c) // 2), (x0c, y1c)]
                    )

                #setting the attack informations
                for button in buttons:
                    if cursor_position in button:
                        for move in player1.moves:
                            if move.name == button.label:
                                pp_text = font.render(f'{move.pp}',True, (55,55,55))
                                curpp_text= font.render(f'{move.currentPP}',True, (55,55,55))
                                type_text = font.render(f'{move.moveType.typeName}',True, (55,55,55))
                                #blit the attack information
                                screen.blit(pp_text, (735, 484))
                                screen.blit(curpp_text, (680, 484))
                                screen.blit(type_text, (635, 542))

                #capturing events
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
                                    #cathing the move object with the move name
                                    for move in player1.moves:
                                        if move.name == button.label: 
                                            if move.currentPP > 0: #if the move isn't out of pp
                                            
                                                #set the used move text with the used move
                                                used_text1 = big_font.render(f'{button.label}!',True, (255,255,255))
                                                #animate the battle (turn the enemy red and the player shakes)
                                                player2IMG.turn_red()
                                                player1IMG.shake()
                                                #blit the pokemon informations again
                                                screen.blit( bar_2, (420,280) )
                                                screen.blit( bar_1, (10,30) )
                                                screen.blit( text_bar, (0,450) )
                                                #player2 info
                                                screen.blit(eName, (27,55))
                                                screen.blit(eLevel, (310,55))
                                                screen.blit(eGender, (245,50))
                                                #player info
                                                screen.blit(pName, (470,310))
                                                screen.blit(pokeGender, (675,305))
                                                screen.blit(pLevel, (735,310))
                                                screen.blit(pPp, (630,377))
                                                #change the cycle
                                                cycle = 1

            pg.display.flip()