from battle.pokemonList import *
def attack(attacker, defender, move):
    modifier = 0
    for pkType in defender.pokeType:
        if pkType in move.moveType.strong:
            modifier += 1
        elif pkType in move.moveType.weak:
            modifier -=1
        elif pkType in move.moveType.ineffective:
            modifier = 0
            break
    if move.classe == 'physical':
        atk = attacker.atk
        defense = defender.defense
    elif move.classe == 'special':
        atk = attacker.spAtk
        defense = defender.spDefense
    damage = ((42*move.power*(atk/defense))/50 + 2) * modifier
    return(damage, modifier)