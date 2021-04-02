class pokeType:
    '''
    type: str(nome do tipo)
    strong: list(lista de tipos contra os quais ele é forte)
    weak: list(lista de tipos contra os quais ele é fraco)
    ineffective: list(lista de tipos contra os quais ele é inefetivo)
    '''
    def __init__(self, typeName, strong, weak, ineffective):
        self.__typeName = typeName
        self.__strong = strong
        self.__weak = weak
        self.__ineffective = ineffective

    @property
    def typeName(self):
        return self.__typeName

    @property
    def strong(self):
        return self.__strong

    @property
    def weak(self):
        return self.__weak

    @property
    def ineffective(self):
        return self.__ineffective