from battle.pokemonList import *
def attack(attacker, defender, move):
    print('ATTACK', '-'*20)
    print('attacker:', attacker.name, 'defender:', defender.name)
    modifier = 1
    atk=0
    defense=0
    for pkType in defender.pokeType:
        if pkType in move.moveType.strong:
            modifier += 1
            print('strong')
        elif pkType in move.moveType.weak:
            modifier -=1
            print('weak')
        else:
            print('ineffective')

    if move.classe == 'physical':
        atk = attacker.atk
        defense = defender.defense
    elif move.classe == 'special':
        atk = attacker.spAtk
        defense = defender.spDefense
    damage = ((42*move.power*(atk/defense))/50 + 2) * modifier
    print('attack damage:', damage)
    
    #take ho from the defender(enemy)
    print('defender hp:', defender.maxHp, 'hp percent:', defender.hpPercent)
    defender.currentHp -= damage
    print('defender current HP: ', defender.currentHp)
    print('defender  current HP percent: ',defender.hpPercent)

    #take pp from the attacker(player)
    for this_move in attacker.moves:
        if this_move == move:
            this_move.currentPP = 1 
            print(f'move: {this_move.name} pp: ', this_move.currentPP)