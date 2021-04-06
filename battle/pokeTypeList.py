from battle.PokeType import pokeType
#pokeType(name, strong, weak, ineffective)

psychic = pokeType('psychic', ['fight', 'poison'], ['steel', 'psychic'], ['dark'])
water = pokeType('water', ['ground', 'rock', 'fire'], ['water', 'grass', 'dragon'], [])
electric = pokeType('electric', ['flying', 'water'], ['grass', 'electric', 'dragon'], ['ground'])
dark = pokeType('dark', ['ghost', 'psychic'], ['fight', 'dark', 'fairy'], [])
dragon = pokeType('dragon', ['dragon'], ['steel'], ['fairy'])
normal = pokeType('normal', [], ['rock', 'steel'], ['ghost'])
fire = pokeType('fire', ['grass', 'ice', 'bug', 'steel'], ['fire', 'water', 'rock', 'dragon'], [])
flying = pokeType('flying', ['grass', 'fighting', 'bug'], ['electric', 'rock', 'steel'], [])