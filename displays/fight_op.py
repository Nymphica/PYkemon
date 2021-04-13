#all battle potions
from displays.button import *
from displays.img import *
import pygame as pg
from time import sleep
from random import randint
from battle.attack import attack
#draw_moves(screen to blit, )
def draw_moves(pokemon, pokeName, player, playerIMG, enemy, enemyIMG, text_bars, screen, playerInfo, enemyInfo):

    width = screen.get_width() #screen width
    height = screen.get_height() #screen height

    pp_bar, text_bar = text_bars

    #recathing player and enemy info for after re-blit
    pName, pLevel, pPp, pokeGender = playerInfo
    eName, eGender, eLevel = enemyInfo

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

    if pokemon == 'enemy':

        #invert the enemy img for the player img
        enemyIMG = pg.image.load(player.pokeSprite[1])
        pos, scale=(430, 0), (290,290)
        enemyIMG = image("enemy",enemyIMG, pos, scale, screen)
        #invert the player img for the enemy img
        playerIMG = pg.image.load(enemy.pokeSprite[0])
        pos, scale= (0, 160), (330,330)
        playerIMG = image("player", playerIMG, pos, scale, screen)

        #invert the enemy for the player and the player for he enemy
        print('INVERT','-'*20, '\nplayer:',player.name, 'enemy:', enemy.name)
        invert = player
        player = enemy
        enemy = invert

        print('player:',player.name, 'enemy:', enemy.name)

        used_text = big_font.render(f'{player.name} used',True, (255,255,255))
        used_text1 = big_font.render('',True, (255,255,255))

        on = True
        player_attacked = False
        damage = 0
        is_text=False

        cursor = 0

        cycle = 0
        while on :

            if enemyIMG.is_red:
                print('is red')
                sleep(0.01)
                enemyIMG.back_img()
                screen.blit( enemyIMG.origin, enemyIMG.pos )
                screen.blit( text_bar, (0,450) )
                screen.blit(used_text, (40,480))
                screen.blit(used_text1, (40,530))
                cycle=1

            if is_text:
                sleep(1)
                for move in player.moves:
                    if move == choosed_move :
                        print(move.name)
                        print(move.power)
                        damage = attack(player, enemy, move)
                on = False

            if not player_attacked:

                choosed_move = player.moves[randint(0,3)]
                print(choosed_move.name)
                used_text1 = big_font.render(f'{choosed_move.name}!',True, (255,255,255))

                screen.blit( bg, (0,0) )
                enemyIMG.turn_red()
                playerIMG.shake()
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

                player_attacked = True
        
            #this cylce is used to avoid the sleep() of stopping the same loop that blits the text so it wait AFTER the text is blit
            if cycle == 1: cycle = 0; is_text= True; print('cycle changed')

            pg.display.flip()

    if pokemon == 'player':
        # loop for cathing the move names
        labels=[]
        for move in player.moves:
            labels.append(move.name)

        bg_color = (255, 255, 255) #background color
        font = pg.font.Font('displays/font.ttf', height // 30)
        big_font = pg.font.Font('displays/font.ttf', height // 20) 

        # general button configuration:
        colors = ((255, 255, 255), (255, 255, 255))
        button_dim = (width // 5 + 60, height // 15)
        origin = (width-button_dim[0]*3.8, height-36)

        buttons = []
        positions = []

        # loop for creating buttons
        for i in range(len(labels)):
            if  i==0 :
                position = (origin[0] + 150 - button_dim[0]//3, origin[1] - button_dim[1] * 2)
            elif i==1:
                position = (origin[0] + 150 - button_dim[0]//3, origin[1] - button_dim[1] + 10)
            if  i==2 :
                position = (origin[0] + 230 + button_dim[0]//3, origin[1] - button_dim[1] * 2)
            elif i==3:
                position = (origin[0] + 230 + button_dim[0]//3, origin[1] - button_dim[1] + 10)

            positions.append(position)
            buttons.append(Button(labels[i], button_dim, position, colors))

        used_text = big_font.render(f'{pokeName} used',True, (255,255,255))
        used_text1 = big_font.render('',True, (255,255,255))

        on = True
        player_attacked = False
        damage = 0
        is_text=False

        cursor = 0

        cycle = 0
        while on :

            if enemyIMG.is_red:
                print(' enemy is red')
                sleep(0.001)
                enemyIMG.back_img()
                screen.blit( enemyIMG.origin, enemyIMG.pos )
                screen.blit( text_bar, (0,450) )
                screen.blit(used_text, (40,480))
                screen.blit(used_text1, (40,530))
                screen.blit( bar_2, (420,280) )
                screen.blit( bar_1, (10,30) )

                #enemy info
                screen.blit(eName, (27,55))
                screen.blit(eLevel, (310,55))
                screen.blit(eGender, (245,50))
                #player info
                screen.blit(pName, (470,310))
                screen.blit(pokeGender, (675,305))
                screen.blit(pLevel, (735,310))
                screen.blit(pPp, (630,377))
                cycle=1

            if is_text:
                sleep(1)
                for move in player.moves:
                    if move.name == choosed_move :
                        print('choosed move name: ', move.name)
                        print('choosed move power: ', move.power)
                        damage = attack(player, enemy, move)
                    return(damage)
                on = False

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

            if not player_attacked:

                screen.blit( pp_bar, (0,450) )

                for button in buttons: # DRAW ALL BUTTONS
                    draw_button(screen, button, bg_color, (49,47,48), tiny_font)

                #draw cursor
                pg.draw.polygon(
                screen, (55, 55, 55),# cursor color
                [(x0c, y0c), (x1c, (y0c + y1c) // 2), (x0c, y1c)]
            )

                for button in buttons:
                    if cursor_position in button:
                        for move in player.moves:
                            if move.name == button.label:
                                pp_text = font.render(f'{move.pp}',True, (55,55,55))
                                curpp_text= font.render(f'{move.currentPP}',True, (55,55,55))
                                type_text = font.render(f'{move.moveType.typeName}',True, (55,55,55))
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

                                choosed_move = button.label
                                print(f'{button.label}!')
                                used_text1 = big_font.render(f'{button.label}!',True, (255,255,255))
                                enemyIMG.turn_red()
                                playerIMG.shake()

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

                                player_attacked = True
        
            #this cylce is used to avoid the sleep() of stopping the same loop that blits the text so it wait AFTER the text is blit
            if cycle == 1: cycle = 0; is_text= True; print('change cycle:', cycle)

            pg.display.flip()