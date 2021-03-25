import pygame
def main():
    pygame.init()
    pygame.display.set_mode((800, 600))
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

if __name__ == '__main__':
    main()