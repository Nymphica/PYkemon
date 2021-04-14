import pygame as pg
from displays.img import image

def draw_win(pokemon):
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

    win = big_font.render(f'You win!',True, (0,0,255))
    screen.blit(win, (250,200))

    pokeimg = pg.image.load(pokemon.pokeSprite[1])
    pokeimg =image('player', pokeimg, (200, 300), (350, 350), screen)
    screen.blit(pokeimg.img, pokeimg.pos)

    pg.display.flip()
    # capturing events: 
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            break
        if ev.type == pg.KEYDOWN: pg.quit(); break


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

    lose = big_font.render(f'You Lose!',True, (0,0,255))
    screen.blit(lose, (250,200))

    pokeimg = pg.image.load(pokemon.pokeSprite[1])
    image('player', pokeimg, (200, 300), (350, 350), screen)
    pokeimg.drop_bright()
    screen.blit(pokeimg.img, pokeimg.pos)

    pg.display.flip()
    # capturing events: 
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            break
        if ev.type == pg.KEYDOWN: pg.quit(); break

def draw_run(pokemon):
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

    run = big_font.render(f'You runned!',True, (0,0,255))
    screen.blit(run, (250,200))

    pg.display.flip()
    # capturing events: 
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            break
        if ev.type == pg.KEYDOWN: pg.quit(); break
