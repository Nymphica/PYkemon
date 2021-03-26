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

    @property
    def name(self):
        return self.__name
    @property
    def hp(self):
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
    
    def hitDamage(self, hitDamage):
        if self.__damage + hitDamage <= self.__maxHp:
            self.__damage += hitDamage
        else:
            self.__damage = self.__maxHp
    
    def isFainted(self):
        return self.__damage >= self.__maxHp
    
    def hitPokemon(self, moveName, enemy):
        for move in self.moves:
            if move.name == moveName:break
        iscritical = move.isCritical()
        extraDamage = 2 if iscritical else 1
        enemy.hitDamage(extraDamage * move.damage)