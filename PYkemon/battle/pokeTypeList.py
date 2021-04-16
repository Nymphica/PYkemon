from battle.PokeType import pokeType
#pokeType(name, strong, weak, ineffective)

psychic = pokeType('psychic', ['fight', 'poison'], ['steel', 'psychic'], ['dark', 'introcomp'])
water = pokeType('water', ['ground', 'rock', 'fire'], ['water', 'grass', 'dragon'], ['introcomp'])
electric = pokeType('electric', ['flying', 'water'], ['grass', 'electric', 'dragon'], ['ground', 'introcomp'])
dark = pokeType('dark', ['ghost', 'psychic'], ['fight', 'dark', 'fairy'], ['introcomp'])
dragon = pokeType('dragon', ['dragon'], ['steel'], ['fairy', 'introcomp'])
normal = pokeType('normal', [], ['rock', 'steel'], ['ghost', 'introcomp'])
fire = pokeType('fire', ['grass', 'ice', 'bug', 'steel'], ['fire', 'water', 'rock', 'dragon'], ['introcomp'])
flying = pokeType('flying', ['grass', 'fighting', 'bug'], ['electric', 'rock', 'steel'], ['introcomp'])
poison = pokeType('poison', ['grass', 'fairy'], ['poison', 'ground', 'rock', 'ghost'], ['steel', 'introcomp'])
rock = pokeType('rock', ['fire', 'ice', 'flying', 'bug'], ['fighting', 'ground', 'steel'], ['introcomp'])
fighting = pokeType('fighting', ['normal', 'ice', 'rock', 'dark', 'steel'], ['poison', 'flying', 'psychic', 'bug', 'fairy'], ['ghost', 'introcomp'])
grass = pokeType('grass', ['water','ground','rock'], ['fire','grass','poison','fluing', 'bug', 'dragon', 'steel'], ['introcomp'])

#easter egg
introcomp = pokeType('introcomp', ['psychic', 'water', 'electric', 'dark', 'dragon', 'normal', 'fire', 'flying', 'poison', 'rock', 'fighting', 'grass'], [], [])