import pygame
from musica import Musica
from displays.allDisplays import *
pygame.init()

theme = 'musica\AfireRedAbertura.wav'#coloca o tema de abertura para tocar
Musica.musica(theme, 0.7)
def main():
    pygame.joystick.init()
    print(pygame.joystick.get_count())

    display = "INIT" # actual display

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if display == "INIT":
            display = draw_init()

        if display == "MENU":
            choosed_pokemon, display = draw_menu()

        elif display == "NAMEIT":
            display, pokeName, pokeGender = draw_nameIt(choosed_pokemon)
            
        elif display == "BATTLE":
            bg_music = 'musica/battle.wav'
            Musica.musica(bg_music, 0.7)
            display = draw_battle(choosed_pokemon, pokeGender)
        
        elif display == 'WIN':
            draw_win(choosed_pokemon)
        
        elif display == 'LOSE':
            draw_lose(choosed_pokemon)

if __name__ == '__main__':
    main()