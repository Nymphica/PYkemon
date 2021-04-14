import pygame
from math import floor
def lower_life(screen, lifePercent, defender_bar, life_bar_percent):
    if lifePercent <= 0:
        current_bar_percent = life_bar_percent
    else:
        current_bar_percent = life_bar_percent - floor((lifePercent*life_bar_percent)/100)
    print("percent", current_bar_percent)
    print(lifePercent)
    for i in range(current_bar_percent):
        defender_bar[0] = pygame.transform.scale(defender_bar[0], (defender_bar[1]+i, 13))
        screen.blit(defender_bar[0], (defender_bar[2][0]- i, defender_bar[2][1]))
        pygame.display.flip()
    return defender_bar[0], current_bar_percent