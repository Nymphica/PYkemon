from PokeType import pokeType
def main():
    psychic = pokeType('psychic', ['fight', 'poison'], ['steel', 'psychic'], ['dark'])
    water = pokeType('water', ['ground', 'rock', 'fire'], ['water', 'grass', 'dragon'], [])
    eletric = pokeType('eletric', ['flying', 'water'], ['grass', 'eletric', 'dragon'], ['ground'])
    dark = pokeType('dark', ['ghost', 'psychic'], ['fight', 'dark', 'fairy'], [])
    dragon = pokeType('dragon', ['dragon'], ['steel'], ['fairy'])
    normal = pokeType('normal', [], ['rock', 'steel'], ['ghost'])




if __name__ == '__main__':
    main()