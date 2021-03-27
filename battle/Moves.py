def main():

    class moves:
        def __init__(self, name, power, moveType, accuracy, pp): #nome, poder, tipo, accuracy, pp
            self.__name = name
            self.__power = power
            self.__moveType = moveType
            self.__accuracy = accuracy
            self.__pp = pp
            self.__currentPP = self.__pp
        
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

        @currentPP.setter
        def currentPP(self, novoValor):
            self.currentPP = novoValor
            
if __name__ == '__main__':
    main()