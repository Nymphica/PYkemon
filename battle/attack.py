from battle.pokemonList import *
def attack(attacker, defender, move):
    #setting the attack especifications variables
    strong = 0
    weak = 0
    ineffective = 0

    #seeing if the attacker move is storng, weak or ineffective for the enemy
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
        
    #setting the move power modifier
    if ineffective >= 1:
        modifier = 0
    elif strong > weak:
        modifier = 2
    elif weak > strong:
        modifier = 0.5
    elif weak == strong:
        modifier = 1
    
    #setting the attack and defense attributes according if the move was physical or special
    if move.classe == 'physical':
        atk = attacker.atk
        defense = defender.defense
    elif move.classe == 'special':
        atk = attacker.spAtk
        defense = defender.spDefense

    #setting the damage
    damage = 0.25*(((42*move.power*(atk/defense))/50 + 2) * modifier)

    return damage, modifier