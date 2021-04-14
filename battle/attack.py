from battle.pokemonList import *
def attack(attacker, defender, move):
    strong = 0
    weak = 0
    ineffective = 0
    if defender.pokeType == 'tuple':
        for pkType in defender.pokeType:
            if pkType in move.moveType.strong:
                strong += 1
            elif pkType in move.moveType.weak:
                weak += 1
            elif pkType in move.moveType.ineffective:
                ineffective += 1
                break
    else:
        if defender.pokeType in move.moveType.strong:
            strong += 1
        elif defender.pokeType in move.moveType.weak:
            weak += 1
        elif defender.pokeType in move.moveType.ineffective:
            ineffective += 1
        
    print(strong, weak)
    if ineffective >= 1:
        modifier = 0
    elif strong > weak:
        modifier = 2
    elif weak > strong:
        modifier = 0.5
    elif weak == strong:
        modifier = 1
    if move.classe == 'physical':
        atk = attacker.atk
        defense = defender.defense
    elif move.classe == 'special':
        atk = attacker.spAtk
        defense = defender.spDefense
    damage = 0.25*(((42*move.power*(atk/defense))/50 + 2) * modifier)

    '''#take pp from the attacker(player)
    for this_move in attacker.moves:
        if this_move == move:
            this_move.currentPP = 1 
            print(f'move: {this_move.name} pp: ', this_move.currentPP)'''
    return damage, modifier