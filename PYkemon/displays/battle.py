import pygame as pg
#from battle.PokeList import pokelistIMG
from battle.pokemonList import *
from displays.button import *
from random import randint #intreger random
from displays.img import image
from displays.fight_op import draw_moves
from displays.moveLifeBar import draw_lifebar
from time import sleep
from battle.lower_life import *

def draw_battle(player1, pokeName, pokeGender):
    pg.init()

    #general display configuration
    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res) #set screen
    pg.display.set_caption("Battle") #set caption
    width = screen.get_width() #screen width
    height = screen.get_height() #screen height

    #fonts configuration
    font = pg.font.Font('displays/font.ttf', height // 30)
    med_font = pg.font.Font('displays/font.ttf', height // 25) 
    big_font = pg.font.Font('displays/font.ttf', height // 20) 
    
    #LOADING ALL THE IMAGES
    #background
    bg = pg.image.load('sprites/battle_bg\FundoPokemon.png')
    bg = pg.transform.scale(bg, (800, 450))

    #pokemon status bar
    pp_bar = pg.image.load('sprites/battle_bg\pp_bar.png')
    pp_bar = pg.transform.scale(pp_bar, (800,150))

    #text bar
    text_bar = pg.image.load('sprites/battle_bg\Text_bar.png')
    text_bar = pg.transform.scale(text_bar, (800,150))

    text_bars = [pp_bar, text_bar]

    #options FIGHT/RUN/ETC bar
    options = pg.image.load('sprites/battle_bg\Fgt_options.png')
    options = pg.transform.scale(options, (400,150))

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

    #yellow bar

    ylw_bar =pg.image.load('sprites/battle_bg\ylw_bar.png')
    ylw_bar = pg.transform.scale(ylw_bar, (1,15))

    #red bar
    red_bar = pg.image.load('sprites/battle_bg\Red_bar.png')
    red_bar = pg.transform.scale(red_bar, (170,13))

    life_bars = [grey_bar, ylw_bar, red_bar]

    #player2
    player2 = pokemonList2[randint(0, len(pokemonList2) - 1)]
    player2IMG = pg.image.load(player2.pokeSprite[1])
    pos, scale=(430, 0), (330,330) #position and scale of the image
    player2IMG = image("player2",player2IMG, pos, scale, screen) #class for battle animation

    #player
    player1IMG = pg.image.load(player1.pokeSprite[0])
    pos, scale= (0, 160), (290,290) #position and scale of the image
    player1IMG = image("player1", player1IMG, pos, scale, screen)#class for battle animation

    #some button configuration
    colors = ((55, 55, 55), (0, 0, 0))
    button_dim = (width // 5 + 15, height // 15)
    origin = (width-button_dim[0]*1.7, height-36)

    buttons = [] #list of all buttons, for future blit
    positions = []  #list of all buttons positions, for future blit
    labels = ['FIGHT', 'POKEMON', 'BAG', 'RUN'] #button labels

    #loop for creating buttons
    for i in range(len(labels)):
        #position (x,y)
        if  i==0 : #first buttons
            position = (origin[0] - button_dim[0]//2, origin[1] - button_dim[1] * 2)
        elif i==1: #second button
            position = (origin[0] - button_dim[0]//2, origin[1] - button_dim[1] + 10)
        if  i==2 : #tirdh button
            position = (origin[0] + button_dim[0]//1.7, origin[1] - button_dim[1] * 2)
        elif i==3: #fourth button
            position = (origin[0] + button_dim[0]//1.7, origin[1] - button_dim[1] + 10)

        positions.append(position) #add the position

        buttons.append(Button(labels[i], button_dim, position, colors)) #add the button

    cursor = 0 #cursor index

    #setting the screen
    screen = pg.display.set_mode((800, 600)) #screen size
    screen.fill((255,255,255)) #Screen color background

    #setting the "what wil pokemon do?" text
    do_text1 = big_font.render('WHAT WILL',True, (255,255,255))
    do_text2 = big_font.render(f'{pokeName} DO?',True, (255,255,255))

    #POKEMONS ESPECIFICATION
    Mgender = big_font.render(f'♂',True, (0,0,255)) # pokemon male gender
    Fgender = big_font.render(f'♀',True, (255,0,0)) # pokemon female gender

    genders = [Mgender, Fgender] #gender list
    #ENEMY info
    eName = med_font.render(f'{player2.name}',True, (55,55,55)) #enemy name
    eGender = genders[randint(0, 1)] #enemy gender
    eLevel = med_font.render('1',True, (55,55,55)) #enemy level
    eInfo = [eName, eGender, eLevel]
    #PLAYER info
    pName = med_font.render(f'{pokeName}',True, (55,55,55)) #player name
    pLevel = med_font.render('1',True, (55,55,55)) #player level
    currHp = player1.currentHp
    maxHp = player1.maxHp
    pHp = med_font.render(f'{currHp}/{maxHp}',True, (55,55,55)) #player hp
    pInfo = [pName, pLevel, pHp, pokeGender]

    # window icon
    icon = pg.image.load('icon.png')
    pg.display.set_icon(icon)

    #setting the initial life bars for player and enemy
    player1_life_bar = [grey_bar, 1, (584 + 169, 358)]
    player2_life_bar = [grey_bar, 1, (156 + 169, 108)]
    #variable to stop the while loop
    running=True
    #setting the life bar percent
    life_bar_percent = 169

    if player1.speed > player2.speed:#decide quem inicia o jogo com base na velocidade dos dois pokemons
        turn = 0
    else:
        turn = 1

    while running:

        #blit the background images
        screen.blit( bg, (0,0) )
        screen.blit( player2IMG.img, player2IMG.pos )
        screen.blit( player1IMG.img, player1IMG.pos )
        screen.blit( bar_2, (420,280) )
        screen.blit( bar_1, (10,30) )
        screen.blit( text_bar, (0,450) )
        screen.blit( options, (400,450) )

        #setting the actual life bar
        #player
        if player1.hpPercent < 33:
            screen.blit(red_bar, (584, 358))
        elif player1.hpPercent < 66:
            screen.blit(yellow_bar, (584, 358))
        #enemy
        if player2.hpPercent < 33:
            screen.blit(red_bar, (156, 108))
        elif player2.hpPercent < 66:
            screen.blit(yellow_bar, (156, 108))
        
        #blit the background life bar
        screen.blit( player2_life_bar[0], (156 + 169 - player2_life_bar[1], 108) )#156, 108
        screen.blit( player1_life_bar[0], (584 + 169 - player1_life_bar[1], 358) )#584, 358

        #blit the "what wil pokemon do?" text
        screen.blit(do_text1, (40,480))
        screen.blit(do_text2, (40,530))
        #blit the pokemons information
        screen.blit(eName, (27,55))
        screen.blit(eLevel, (310,55))
        screen.blit(eGender, (245,50))
        screen.blit(pName, (470,310))
        screen.blit(pokeGender, (675,305))
        screen.blit(pLevel, (735,310))
        screen.blit(pHp, (630,377))

        if turn == 0:
    # defining cursor position:
            cursor_position_shifted = positions[cursor] #from each button possition
            cursor_position = (
                cursor_position_shifted[0] + button_dim[0] // 10, # cursor position on X
                cursor_position_shifted[1] + button_dim[1] // 2#cursor position on Y
            )

            # DRAW ALL BUTTONS
            for button in buttons: 
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

            #cathing events
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running = False
                    pg.quit()

                if ev.type == pg.KEYDOWN: #if a eky is pressed

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

                                if choosed_action == "POKEMON":
                                    return("MENU") #return menu to choose other pokemon

                                elif choosed_action == "RUN": #if run choose other enemy
                                    if randint(0, 100) >= 50:
                                        return 'RUN'
                                    else:
                                        turn = 1
                                        cantRun = big_font.render("Can't escape!",True, (255,255,255))
                                        screen.blit( text_bar, (0,450) )
                                        screen.blit(cantRun, (40,480))
                                        pg.display.flip()
                                        sleep(1)

                                elif choosed_action == "FIGHT":
                                    #display the attck options and animate the batlte
                                    damage, used_move = draw_moves('player1', pokeName, player1, player1IMG, player2, player2IMG, text_bars, screen, pInfo, eInfo)
                                    #lower the enemy hp
                                    player2.currentHp -= damage
                                    #redraw the new enemy hp bar
                                    player2_life_bar[0], player2_life_bar[1] = lower_life(screen, player2.hpPercent, player2_life_bar, life_bar_percent)
                                    #lower the player move pp
                                    used_move.currentPP -= 1
                                    turn = 1

                                    #in case the player1 or player2 is dead - WIN or LOSE
                                    if player2.isFainted(): return('WIN'); pygame.quit() ; running = False
                                    if player1.isFainted(): return('LOSE') ; pygame.quit() ; running = False
                                    running_menu = False
                                    break
                                
        else:
            pg.display.flip()
            #take an random move for the enemy and animate the batlte
            damage, used_move = draw_moves('player2', pokeName, player1, player1IMG, player2, player2IMG, text_bars, screen, pInfo, eInfo)
            #lower the player hp
            player1.currentHp -= damage
            #set the new pp text
            pHp = med_font.render(f'{int(player1.currentHp)}/{maxHp}',True, (55,55,55))
            #lower the enemy move pp
            used_move.currentPP -= 1
            #redraw the new player hp bar
            player1_life_bar[0], player1_life_bar[1] = lower_life(screen, player1.hpPercent, player1_life_bar, life_bar_percent)
            turn = 0

            #in case the player1 or player2 is dead - WIN or LOSE
            if player2.isFainted(): return('WIN'); pygame.quit() ; running = False
            if player1.isFainted(): return('LOSE') ; pygame.quit() ; running = False


        pg.display.flip()
