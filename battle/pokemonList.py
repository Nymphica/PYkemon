from battle.movesList import *
from battle.Pokemon import pokemon

#a list of all pokemons in game
#pokemon(name, moves, maxHp, atk, defense, spDefense, spAtk, speed, pokeType)

blastoise1 = pokemon('BLASTOISE', (surf, bite, outrage, hyperbeam), 79, 83, 100, 105, 85, 78, ('water'))
charizard1 = pokemon('CHARIZARD', (dragonclaw, flamethrower, megapunch, aerialace), 78, 84, 78, 85, 109, 100, ('fire', 'fliyng'))
pikachu1 = pokemon('PIKACHU', (thundershock, brickbreak, thief, thunderbolt), 35, 55, 40, 50, 50, 90, ('electric'))
charmander1 = pokemon('CHARMANDER', (megakick, ember, rockslide, inferno), 39, 52, 43, 50, 60, 65, ('fire'))
squirtle1 = pokemon('SQUIRTLE', (skullbash, hydropump, bite, watergun), 44, 48, 65, 64, 50, 43, ('water'))
bulbasaur1 = pokemon('BULBASAUR', (tackle, bodyslam, vinewhip, solarbeam), 45, 49, 49, 65, 65, 45, ('grass', 'poison'))
introbot = pokemon('INTROBOT', (armario, aula04, beberagua, feedback), 250, 100, 100, 100, 100, 150, ('introcomp'))

blastoise2 = pokemon('BLASTOISE', (surf, bite, outrage, hyperbeam), 79, 83, 100, 105, 85, 78, ('water'))
charizard2 = pokemon('CHARIZARD', (dragonclaw, flamethrower, megapunch, aerialace), 78, 84, 78, 85, 109, 100, ('fire', 'fliyng'))
pikachu2 = pokemon('PIKACHU', (thundershock, brickbreak, thief, thunderbolt), 35, 55, 40, 50, 50, 90, ('electric'))
charmander2 = pokemon('CHARMANDER', (megakick, ember, rockslide, inferno), 39, 52, 43, 50, 60, 65, ('fire'))
squirtle2 = pokemon('SQUIRTLE', (skullbash, hydropump, bite, watergun), 44, 48, 65, 64, 50, 43, ('water'))
bulbasaur2 = pokemon('BULBASAUR', (tackle, bodyslam, vinewhip, solarbeam), 45, 49, 49, 65, 65, 45, ('grass', 'poison'))

#two lists to avoid the same pokemon object for player and enemy
pokemonList1 = [pikachu1, charmander1, squirtle1, bulbasaur1, blastoise1, charizard1]
pokemonList2 = [pikachu2, charmander2, squirtle2, bulbasaur2, blastoise2, charizard2]