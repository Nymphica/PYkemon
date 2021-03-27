def main():

    class pokemon:
        '''
        name : str
        maxHp : int (maximo de vida)
        moves : list (todos os movimentos do pokemon, desde de cura até ataques)
        damage : int (ataque a ser sofrido)
        '''
        def __init__(self, name, moves, maxHp):
            self.__name = name
            self.__maxHp = maxHp
            self.__moves = moves
            self.__damage = 0
            self.__lifePercent = 100

        @property
        def name(self):
            return self.__name
        @property
        def maxHp(self):
            return self.__hp
        @property
        def moves(self):
            return self.__moves.copy()
        @property
        def damage(self):
            return self.__damage
        @property
        def actualHp(self):
            return self.__maxHp - self.__damage
        @property
        def lifePercent(self):
            return self.__lifePercent
        
        def hitDamage(self, hitDamage):#dano recebido por ataque
            if self.__damage + hitDamage < self.__maxHp:
                self.__damage += hitDamage
                self.__lifePercent = (self.__damage * 100)/self.__maxHp
            else:
                self.__damage = self.__maxHp
        
        def isFainted(self):#verifica se o pokemon morreu
            return self.__damage >= self.__maxHp
        
        def hitPokemon(self, moveName, enemy):
            for move in self.moves:
                if move.name == moveName:break
            iscritical = move.isCritical()
            extraDamage = 2 if iscritical else 1
            enemy.hitDamage(extraDamage * move.damage)
if __name__ == '__main__':
    main()