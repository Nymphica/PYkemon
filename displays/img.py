import pygame as pg

class image:
    '''
    name : just to organize
    img :img
    origin : origin img
    pos : x and y position
    creen: screen for blit
    '''
    def __init__(self, name, img, pos, scale, screen):
        self.__scale = scale
        self.__img = pg.transform.scale(img, scale)
        self.__origin = pg.transform.scale(img, scale)
        self.__pos = pos
        self.w, self.h = self.__img.get_size()
        self.__screen = screen
        self.__is_red = False

        self.__name = name
    
    @property
    def scale(self):
        return self.__scale

    @property
    def img(self):
        return self.__img
    
    @property
    def origin(self):
        return self.__origin

    @property
    def pos(self):
        return self.__pos
    
    @property
    def screen(self):
        return self.__screen

    @property
    def is_red(self):
        return self.__is_red

    @img.setter
    def img(self, new_img):
        self.__img = pg.transform.scale(new_img, self.__scale)
        self.__origin = pg.transform.scale(new_img, self.__scale)
        self.w, self.h = self.__img.get_size()

    #turn img more red
    def turn_red(self):
        #it takes pixel per pixel and change the RBGA (red, green, blue, alpha (transparency)) values
        for x in range(self.w):
            for y in range(self.h):
                r = self.__img.get_at((x, y))[0]
                if r<200 and r>1:
                    while r != 254:
                        r+=1
                g = self.__img.get_at((x, y))[1]
                if g>150:
                    g=0
                b = self.__img.get_at((x, y))[2]
                if b>150:
                    b=0
                a = self.__img.get_at((x, y))[3]
                a = 1
                self.__img.set_at((x, y), pg.Color(r, g, b, a))

        self.__screen.blit( self.__img, self.__pos)
        self.__is_red = True
        print("red", self.__name) #just to debug

    #put img back to normal
    def back_img(self):
        #it takes pixel per pixel from a copy of the original img and replaceit in the actual img
        for x in range(self.w):
            for y in range(self.h):
                r = self.__origin.get_at((x, y))[0]
                r=r
                g = self.__origin.get_at((x, y))[1]
                b = self.__origin.get_at((x, y))[2]
                a = self.__origin.get_at((x, y))[3]
                self.__img.set_at((x, y), pg.Color(r, g, b, a))
        print("back", self.__name)

        self.__is_red = False

    #more img brightnes
    def more_bright(self):
        for x in range(self.w):
            for y in range(self.h):
                r = self.__img.get_at((x, y))[0]
                if r<205 and r>150:
                    r+=50
                g = self.__img.get_at((x, y))[1]
                if g<205 and g>150:
                    g+=50
                b = self.__img.get_at((x, y))[2]
                if b<205 and b>150:
                    b+=50
                a = self.__img.get_at((x, y))[3]
                self.__img.set_at((x, y), pg.Color(r, g, b, a))
        print("more bright", self.__name)

    #less img brightnes
    def drop_bright(self):

        for x in range(self.w):
            for y in range(self.h):
                r = self.__img.get_at((x, y))[0]
                if r>150:
                    r-=50
                g = self.__img.get_at((x, y))[1]
                if g>150:
                    g-=50
                b = self.__img.get_at((x, y))[2]
                if b>150:
                    b-=50
                a = self.__img.get_at((x, y))[3]
                self.__img.set_at((x, y), pg.Color(r, g, b, a))
        print("drop bright", self.__name)

    def shake(self):

        if self.__name=="enemy":

            for n in range(5):

                self.__pos = (460 , 0)
                self.__screen.blit(self.__img, self.__pos)
                self.__pos = (430 , 0)

        elif self.__name=="player":

            for n in range(5):

                self.__pos = (10 , 160)
                self.__screen.blit(self.__img, self.__pos)
                self.__pos= (0,160)
        
        print("shake ", self.__name)