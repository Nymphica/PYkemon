import pygame
from musica import Musica
def main():

    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))#define a tela inicial
    pygame.display.set_caption("Pykemon")
    screen.fill((255, 0, 0))
    black = (0, 0, 0)
    selectionRect = pygame.draw.rect(screen, black, pygame.Rect(30, 30, 740, 540), 2)

    icon = pygame.image.load('icon.png')#icone da janela
    pygame.display.set_icon(icon)

    pygame.display.update()

    theme = 'sprites\AfireRedAbertura.wav'#coloca o tema de abertura para tocar
    Musica.musica(theme, 0.9)
    
    pygame.joystick.init()
    print(pygame.joystick.get_count())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()