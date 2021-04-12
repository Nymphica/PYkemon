from battle.movesList import *
from battle.Pokemon import pokemon
#pokemon(name, moves, maxHp, atk, defense, spDefense, spAtk, speed, pokeType)

blastoise = pokemon('BLASTOISE', (surf, bite, outrage, hyperbeam), 79, 83, 100, 105, 85, 78, ('water'))
charizard = pokemon('CHARIZARD', (dragonclaw, flamethrower, megapunch, aerialace), 78, 84, 78, 85, 109, 100, ('fire', 'fliyng'))
pikachu = pokemon('PIKACHU', (thundershock, brickbreak, thief, thunderbolt), 35, 55, 40, 50, 50, 90, ('electric'))
charmander = pokemon('CHARMANDER', (megakick, ember, rockslide, inferno), 39, 52, 43, 50, 60, 65, ('fire'))
squirtle = pokemon('SQUIRTLE', (), 44, 48, 65, 64, 50, 43, ('water'))
bulbasaur = pokemon('BULBASAUR', (), 45, 49, 49, 65, 65, 45, ('grass', 'poison'))

pokemonList = [blastoise, charizard, pikachu, charmander, squirtle, bulbasaur]