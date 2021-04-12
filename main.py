import pygame
from musica import Musica
from displays.allDisplays import *
pygame.init()

#theme = 'musica\AfireRedAbertura.wav'#coloca o tema de abertura para tocar
#Musica.musica(theme, 0.9)
def main():
    pygame.joystick.init()
    print(pygame.joystick.get_count())

    display = "MENU" # actual display

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if display == "MENU":
            choosed_pokemon, display = draw_menu()

        elif display == "NAMEIT":
            display, pokeName = draw_nameIt(choosed_pokemon)
            
        elif display == "BATTLE":
            display = draw_battle(choosed_pokemon, pokeName)

if __name__ == '__main__':
    main()