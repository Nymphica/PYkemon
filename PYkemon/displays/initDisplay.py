import pygame as pg
from time import sleep
def draw_init():
    bg_color = (55, 55, 55) #background color
    res = (800, 600) #resolution
    screen = pg.display.set_mode(res)
    pg.display.set_caption("Initial Display")
    icon = pg.image.load('icon.png')# window icon
    pg.display.set_icon(icon)
    width = screen.get_width()
    height = screen.get_height()

    font = pg.font.Font('displays/font.ttf', height // 20)
    tiny_font = pg.font.Font('displays/font.ttf', height // 40)

    init_bg_img = pg.image.load('sprites/init_bg.png')
    init_bg_img = pg.transform.scale(init_bg_img, (800,600))

    press = font.render('Press any key',True, (140,140,140))

    trab_por = tiny_font.render('Made by:',True, (30,30,30))
    iza_jon = tiny_font.render('Izabel Lisboa and João Nascente',True, (30,30,30))

    screen.fill(bg_color)

    is_init=True
    press_pos = (0,0)
    cycle = 2

    while is_init :

        screen.blit(init_bg_img, (0,0))
        
        if cycle == 1:#make the press text desappear
            sleep(1)
            press_pos = (800, 600)
            screen.blit(press, press_pos)
            cycle=0

        elif cycle == 0: #make the press text appeare
            sleep(1)
            press_pos = (230, 400)
            screen.blit(press, press_pos)
            cycle=1

        else: #this just happens in the first loop, it's to avoid the sleep
            press_pos = (230, 400)
            screen.blit(press, press_pos)
            cycle=1
        
        screen.blit(trab_por, (330,550))
        screen.blit(iza_jon, (215,570))
        pg.display.flip()

        # capturing events: 
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                break
            if ev.type == pg.KEYDOWN:
                return "MENU"
                is_init = False
        