from battle.movesList import *
from battle.Pokemon import pokemon
#pokemon(name, moves, maxHp, atk, defense, spDefense, spAtk, speed, pokeType)

blastoise = pokemon('BLASTOISE', (surf, bite, outrage, hyperbeam), 79, 83, 100, 105, 85, 78, ('water'))
charizard = pokemon('CHARIZARD', (dragonclaw, flamethrower, megapunch, aerialace), 78, 84, 78, 85, 109, 100, ('fire'))

pokemonList = [blastoise, charizard]