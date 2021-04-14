import pygame as pg
#from battle.PokeList import pokelistIMG
from battle.pokemonList import *
from displays.button import *
from random import randint #intreger random
from displays.img import image
from displays.fight_op import draw_moves
from time import sleep
from battle.lower_life import *

def draw_battle(player1, pokeName):
    pg.init()

    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res) #set screen
    pg.display.set_caption("Battle") #set caption
    width = screen.get_width() #screen width
    height = screen.get_height() #screen height

    font = pg.font.Font('displays/font.ttf', height // 30) 
    big_font = pg.font.Font('displays/font.ttf', height // 20) 
    
    #background
    bg = pg.image.load('sprites/battle_bg\FundoPokemon.png')
    bg = pg.transform.scale(bg, (800, 450))

    #pokemon status bar
    pp_bar = pg.image.load('sprites/battle_bg\pp_bar.png')
    pp_bar = pg.transform.scale(pp_bar, (800,150))

    #options FIGHT/RUN/ETC bar
    options = pg.image.load('sprites/battle_bg\Fgt_options.png')
    options = pg.transform.scale(options, (400,150))

    #text bar
    text_bar = pg.image.load('sprites/battle_bg\Text_bar.png')
    text_bar = pg.transform.scale(text_bar, (800,150))

    #Second pokemon bar
    bar_2 = pg.image.load('sprites/battle_bg\Bar_2.png')
    bar_2 = pg.transform.scale(bar_2, (360,160))

    #first pokemon bar
    bar_1 = pg.image.load('sprites/battle_bg\Bar_1.png')
    bar_1 = pg.transform.scale(bar_1, (360,140))

    #grey bar
    grey_bar = pg.image.load('sprites/battle_bg\gry_bar.png')
    grey_bar = pg.transform.scale(grey_bar, (1,13))#169, 13

    #yellow bar
    yellow_bar = pg.image.load('sprites/battle_bg\ylw_bar.png')
    yellow_bar = pg.transform.scale(yellow_bar, (170, 13))

    #red bar
    red_bar = pg.image.load('sprites/battle_bg\Red_bar.png')
    red_bar = pg.transform.scale(red_bar, (170,13))

    #enemy
    player2 = pokemonList[randint(0, len(pokemonList) - 1)]
    player2IMG = pg.image.load(player2.pokeSprite[1])
    pos, scale=(430, 0), (330,330)
    player2IMG = image("enemy",player2IMG, pos, scale, screen)

    #player
    player1IMG = pg.image.load(player1.pokeSprite[0])
    pos, scale= (0, 160), (290,290)
    player1IMG = image("player", player1IMG, pos, scale, screen)

    colors = ((55, 55, 55), (0, 0, 0))
    button_dim = (width // 5 + 15, height // 15)
    origin = (width-button_dim[0]*1.7, height-36)

    buttons = []
    positions = []
    labels = ['FIGHT', 'POKEMON', 'BAG', 'RUN']

    for i in range(len(labels)):
        if  i==0 :
            position = (origin[0] - button_dim[0]//2, origin[1] - button_dim[1] * 2)
        elif i==1:
            position = (origin[0] - button_dim[0]//2, origin[1] - button_dim[1] + 10)
        if  i==2 :
            position = (origin[0] + button_dim[0]//2, origin[1] - button_dim[1] * 2)
        elif i==3:
            position = (origin[0] + button_dim[0]//2, origin[1] - button_dim[1] + 10)

        positions.append(position)
        buttons.append(Button(labels[i], button_dim, position, colors))

    cursor = 0


    screen = pg.display.set_mode((800, 600)) #screen size
    screen.fill((255,255,255)) #Screen color background

    do_text1 = big_font.render('WHAT WILL',True, (255,255,255))
    do_text2 = big_font.render(f'{pokeName} DO?',True, (255,255,255))

    icon = pg.image.load('icon.png')# window icon
    pg.display.set_icon(icon)

    attacked = False
    player1_life_bar = [grey_bar, 1, (584 + 169, 358)]
    player2_life_bar = [grey_bar, 1, (156 + 169, 108)]
    you_win=False
    actual_damage = 0
    running=True
    life_bar_percent = 169
    while running:

        '''if you_win: sleep(2); pg.quit()

        if attacked:
            while damage[0] > 0:
                if actual_damage >= 166:
                    enemy_life_bar = red_bar
                    actual_damage=0
                    break
                damage[0] -= 1
                actual_damage += 1
                enemy_life_bar = pg.transform.scale(gry_bar, (actual_damage,15))

            while damage[0] > 0 and enemy_life_bar == red_bar:
                screen.blit( gry_bar, (153,108))
                if actual_damage >= 332:
                    do_text1 = big_font.render('YOU',True, (255,255,255))
                    do_text2 = big_font.render('WIN!',True, (255,255,255))
                    you_win = True
                    break
                damage[0] -= 1
                actual_damage += 1
                enemy_life_bar = pg.transform.scale(red_bar, (actual_damage-166,15))

            print(actual_damage, enemy_life_bar)
            attacked = False'''


        screen.blit( bg, (0,0) )
        screen.blit( player2IMG.img, player2IMG.pos )
        screen.blit( player1IMG.img, player1IMG.pos )
        screen.blit( bar_2, (420,280) )
        screen.blit( bar_1, (10,30) )
        screen.blit( text_bar, (0,450) )
        screen.blit( options, (400,450) )
        if player1.hpPercent < 33:
            screen.blit(red_bar, (584, 358))
        elif player1.hpPercent < 66:
            screen.blit(yellow_bar, (584, 358))
        if player2.hpPercent < 33:
            screen.blit(red_bar, (156, 108))
        elif player2.hpPercent < 66:
            screen.blit(yellow_bar, (156, 108))
        screen.blit( player2_life_bar[0], (156 + 169 - player2_life_bar[1],108) )#156, 108
        screen.blit( player1_life_bar[0], (584 + 169 - player1_life_bar[1], 358) )#584, 358

        screen.blit(do_text1, (40,480))
        screen.blit(do_text2, (40,530))



        # defining cursor position:
        cursor_position_shifted = positions[cursor] #from each button possition
        cursor_position = (
            cursor_position_shifted[0] + button_dim[0] // 10, # cursor position on X
            cursor_position_shifted[1] + button_dim[1] // 2#cursor position on Y
        )

        for button in buttons: # DRAW ALL BUTTONS
                draw_button(screen, button, bg_color, (255,255,255), font, False, True)

        # Printing cursor:
        sc = 16 #cursor size
        xcc, ycc = cursor_position
        x0c, y0c = xcc - sc // 2, ycc - sc // 2 # |‾
        x1c, y1c = xcc + sc // 2, ycc + sc // 2 #    _|
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
                        if cursor_position in button:
                            
                            choosed_action = button.label
                            print(choosed_action)

                            if choosed_action == "POKEMON":
                                return("MENU") # (temporario) return to menu to choose other pokemon

                            elif choosed_action == "RUN": #if run choose other enemy
                                player2 = pokemonList[randint(0, len(pokemonList) - 1)]
                                newEnemyIMG = pg.image.load(player2.pokeSprite[1])#(f'displays/imgs/front/{pokelistIMG[randint(0,3)]}.png')
                                player2IMG.img = newEnemyIMG

                            elif choosed_action == "FIGHT":
                                damage, modifier, used_move = draw_moves(screen, player1, player1IMG, player2, player2IMG, width, height, pp_bar, text_bar)
                                print("dano", damage)
                                player2.currentHp -= damage
                                if player2.isFainted():
                                    print("No céu tem pao?")
                                player2_life_bar[0], player2_life_bar[1] = lower_life(screen, player2.hpPercent, player2_life_bar, life_bar_percent)

                            running_menu = False
                            break
        pg.display.flip()
