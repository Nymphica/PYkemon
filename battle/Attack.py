import random
class attack:
    def __init__(self, name, damage, criticalP): #nome, dano do ataque, propabilidade de critico
        self.__name = name
        self.__damage = damage
        self.__criticalP = criticalP
    
    @property #getters para retornar valores das variaveis
    def name(self):
        return self.__name
    @property
    def damage(self):
        return self.__damage
    @property
    def criticalP(self):
        return self.__criticalP

    def isCritical(self):
        critical = random.random() #valor entre 0(0%) e 1 (100%)
        return critical <= self.__criticalP #se o valor aleatorio for igual ou maior que a chance de um critico retornara True