class pokemon:
    '''
    name : str
    maxHp : int (maximo de vida)
    moves : list (todos os movimentos do pokemon, desde de cura até ataques)
    atk : int (atributo de ataque)
    defense : int (atributo de defesa)
    spDefense : int (atributo de defesa especial)
    spAtk : int (atributo de ataque especial)
    speed : int (atributo de velocidade)
    pokeSprite : tupla de 2 str (caminho para o sprite do pokemon) (costas, frente)
    pokeType : tupla de no maximo 2 str com o tipo/s do pokemon
    '''
    def __init__(self, name, moves, maxHp, atk, defense, spDefense, spAtk, speed, pokeType):
        self.__name = name
        self.__moves = moves
        self.__maxHp = maxHp
        self.__atk = atk
        self.__defense = defense
        self.__spDefense = spDefense
        self.__spAtk = spAtk
        self.__speed = speed
        self.__pokeSprite = ("sprites\pokemon\Costas\{}.png".format(self.__name), "sprites\pokemon\Frente\{}.png".format(self.__name))
        self.__currentHp = maxHp
        self.__hpPercent = 100
        self.__pokeType = pokeType

    @property
    def name(self):
        return self.__name
    
    @property
    def maxHp(self):
        return self.__maxHp
    
    @property
    def moves(self):
        return self.__moves
    
    @property
    def atk(self):
        return self.__atk
    
    @property
    def defense(self):
        return self.__defense

    @property
    def spDefense(self):
        return self.__spDefense

    @property
    def spAtk(self):
        return self.__spAtk

    @property
    def speed(self):
        return self.__speed

    @property
    def pokeSprite(self):
        return self.__pokeSprite
    
    @property
    def currentHp(self):
        return self.__currentHp
    
    @property
    def hpPercent(self):
        return self.__hpPercent

    @property
    def pokeType(self):
        return self.__pokeType

    @currentHp.setter
    def currentHp(self, novoValor):
        self.__currentHp = novoValor
        self.__hpPercent = (100 * self.__currentHp)/self.__maxHp
    
    @hpPercent.setter
    def hpPercent(self, novoValor):
        self.__lifePercent = novoValor
        self.__currentHp = (self.__hpPercent * self.__maxHp)/100
    
    def isFainted(self):#verifica se o pokemon morreu
        return self.__hpPercent <= 0