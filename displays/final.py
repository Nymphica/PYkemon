import pygame as pg
from musica import Musica
from displays.img import image

def draw_win(pokemon):
    pg.init()

    #general screen configuration
    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res) #set screen
    pg.display.set_caption("Battle") #set caption
    width = screen.get_width() #screen width
    height = screen.get_height() #screen height

    #fonts configuration
    font = pg.font.Font('displays/font.ttf', height // 30)
    med_font = pg.font.Font('displays/font.ttf', height // 25) 
    big_font = pg.font.Font('displays/font.ttf', height // 10)
    screen.fill(bg_color)

    #win text
    win = big_font.render(f'You win!',True, (255,255,255))
    screen.blit(win, (300,100))

    press = font.render(f'Press enter to leave or backspace to return',True, (200,200,200))
    screen.blit(press, (30,500))

    win_music = 'musica\win.wav'#play the win music
    Musica.musica(win_music, 0.7)

    pokeimg = pg.image.load(pokemon.pokeSprite[1])
    pokeimg =image('player', pokeimg, (250, 150), (350, 350), screen)
    screen.blit(pokeimg.img, pokeimg.pos)

    pg.display.flip()
    # capturing events:
    while True: 
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                break
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RETURN:
                    pg.quit(); break
                elif ev.key == pg.K_BACKSPACE:
                    return 'INIT'


def draw_lose(pokemon):
    pg.init()

    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res) #set screen
    pg.display.set_caption("Battle") #set caption
    width = screen.get_width() #screen width
    height = screen.get_height() #screen height

    font = pg.font.Font('displays/font.ttf', height // 30)
    med_font = pg.font.Font('displays/font.ttf', height // 25) 
    big_font = pg.font.Font('displays/font.ttf', height // 20)
    screen.fill(bg_color)

    lose = big_font.render(f'You Lose!',True, (255,255,255))
    screen.blit(lose, (300,100))

    press = font.render(f'Press enter to leave or backspace to return',True, (200,200,200))
    screen.blit(press, (30,500))

    lose_music = 'musica\lose.wav'#coloca o tema de perda para tocar
    Musica.musica(lose_music, 0.7)

    pokeimg = pg.image.load(pokemon.pokeSprite[1])
    pokeimg = image('player', pokeimg, (250, 150), (350, 350), screen)
    screen.blit(pokeimg.img, pokeimg.pos)

    rip = big_font.render(f'RIP',True, (255,255,255))
    screen.blit(rip, (350, 150))

    pg.display.flip()
    # capturing events: 
    while True: 
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                break
            if ev.type == pg.KEYDOWN:
                
                if ev.key == pg.K_RETURN:
                    pg.quit(); break
                elif ev.key == pg.K_BACKSPACE:
                    return 'INIT'

def draw_run():
    pg.init()

    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res) #set screen
    pg.display.set_caption("Battle") #set caption
    width = screen.get_width() #screen width
    height = screen.get_height() #screen height

    font = pg.font.Font('displays/font.ttf', height // 30)
    med_font = pg.font.Font('displays/font.ttf', height // 25) 
    big_font = pg.font.Font('displays/font.ttf', height // 20)
    screen.fill(bg_color)

    run = big_font.render(f'You escaped!',True, (255,255,255))
    screen.blit(run, (280,200))

    where = big_font.render(f'???',True, (255,255,255))
    screen.blit(where, (350,250))

    press = font.render(f'Press enter to leave or backspace to return',True, (200,200,200))
    screen.blit(press, (30,500))

    pg.display.flip()
    # capturing events:
    while True: 
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                break
            if ev.type == pg.KEYDOWN:
                
                if ev.key == pg.K_RETURN:
                    pg.quit(); break
                elif ev.key == pg.K_BACKSPACE:
                    return 'INIT'
