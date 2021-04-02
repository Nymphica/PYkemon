def main():

    class moves:
        def __init__(self, name, power, moveType, accuracy, pp, classe): #nome, poder, tipo, accuracy, pp, classe(fisico, especial ou status)
            self.__name = name
            self.__power = power
            self.__moveType = moveType
            self.__accuracy = accuracy
            self.__pp = pp
            self.__currentPP = self.__pp
            self.__classe = classe
        
        @property #getters para retornar valores das variaveis
        def name(self):
            return self.__name

        @property
        def power(self):
            return self.__power

        @property
        def moveType(self):
            return self.power

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

        @currentPP.setter
        def currentPP(self, novoValor):
            self.currentPP = novoValor
            
if __name__ == '__main__':
    main()