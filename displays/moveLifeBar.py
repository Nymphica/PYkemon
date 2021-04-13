import pygame as pg
def draw_lifebar(hpPercent, pokemon, screen, bars, enemy_life_bar, player_life_bar):
    #in test fase
    if hpPercent >= 60: bar = bars[0]
    elif hpPercent >=30: bar = bars[1]
    else: bar = bars[2]

    life = int(hpPercent)
    pg.transform.scale(bar, (life,15))

    print('pokemon: ', pokemon,'hp percent:', hpPercent,' bar: ', bar, ' hp: ', life)

    if pokemon == 'enemy': enemy_life_bar = bar
    if pokemon == 'player': player_life_bar = bar