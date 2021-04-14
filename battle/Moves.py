class moves:
    def __init__(self, name, power, moveType, accuracy, pp, classe): #nome, poder, tipo, accuracy, pp, classe(fisico ou especial)
        self.__name = name
        self.__power = power
        self.__moveType = moveType
        self.__accuracy = accuracy
        self.__pp = pp
        self.__currentPP = self.__pp
        self.__classe = classe
    
    @property #getters to return variable valures
    def name(self):
        return self.__name

    @property
    def power(self):
        return self.__power

    @property
    def moveType(self):
        return self.__moveType

    @property
    def accuracy(self):
        return self.__accuracy

    @property
    def pp(self):
        return self.__pp

    @property
    def currentPP(self):
        return self.__currentPP

    @property
    def classe(self):
        return self.__classe

    @currentPP.setter #setting the current HP
    def currentPP(self, novoValor):
        self.__currentPP = novoValor