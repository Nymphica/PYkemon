import pygame as pg
def draw_lifebar(hpPercent, pokemon, screen, bars, player2_life_bar, player1_life_bar):
    #in test phase
    if hpPercent >= 60: bar = bars[0]
    elif hpPercent >=30: bar = bars[1]
    else: bar = bars[2]

    life = int(hpPercent)
    pg.transform.scale(bar, (life,15))

    print('pokemon: ', pokemon,'hp percent:', hpPercent,' bar: ', bar, ' hp: ', life)

    if pokemon == 'player2': player2_life_bar = bar
    if pokemon == 'player1': player1_life_bar = bar