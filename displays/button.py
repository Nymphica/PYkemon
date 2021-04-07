import pygame
class Button:
    """
    Propriedades:
        label,
        size,
        offset,
        colors (main_color, alt_color)
    """
    def __init__(self, label, size, offset, colors):
        self.__label = label
        self.__size  = size
        self.__offset = offset
        self.__main_color = colors[0]
        self.__alt_color = colors[1]

    @property
    def label(self):
        return self.__label

    @property
    def size(self):
        return self.__size

    @property
    def offset(self):
        return self.__offset

    @property
    def main_color(self):
        return self.__main_color

    @property
    def alternative_color(self):
        return self.__alt_color

    @property
    def rect(self):
        x0, y0 = self.offset
        dx, dy = self.size
        return [x0, y0, dx, dy]

    @alternative_color.setter 
    def alternative_color(self, new_color): 
        self.__alt_color = new_color

    @label.setter
    def label(self, new_label):
        self.__label = new_label

    @offset.setter
    def offset(self, new_offset):
        self.__offset = new_offset

    def text_offset(self, text_size):
        x0, y0 = self.offset
        dx, dy = self.size
        dxt, dyt = text_size

        xt = x0 + dx // 2 - dxt // 2
        yt = y0 + dy // 2 - dyt // 2
        return xt, yt

    def __contains__(self, point):
        x0, y0 = self.offset
        dx, dy = self.size
        px, py = point

        contains_x = x0 <= px <= x0 + dx
        contains_y = y0 <= py <= y0 + dy

        return contains_x and contains_y
    
def draw_button(screen, button, bg_color, txt_color, font, highlighted=False, noColor=False):
    if highlighted:
        pygame.draw.rect(screen, button.alternative_color, button.rect)

    elif noColor:
        screen= pygame.Surface((50,50), pygame.SRCALPHA) #transparency
        pygame.draw.rect(screen, (0, 0, 0, 50), button.rect,1)
    
    else:
        pygame.draw.rect(screen, button.main_color, button.rect)
        pygame.draw.rect(screen, bg_color, button.rect, 2)
    
    if not noColor:
        text = font.render(button.label, True, txt_color) #font.render(text, antialias, (color), bg=none) - antialias smooth the edges of the pixels
        text_rect = text.get_rect()
        text_rect.center = (
        button.offset[0] + button.size[0] // 2, # text position on X
        # offset = first ponit on X line + size = distance from the first to the final point // 2
        button.offset[1] + button.size[1] // 2 # text position on Y
        )
        #text_size = (text.get_width(), text.get_height())
        screen.blit(text, text_rect)#button.text_offset(text_size))