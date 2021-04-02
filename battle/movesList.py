from Moves import moves
from pokeTypeList import *
def main():
    bite = moves('bite', 60, dark, 100, 25, 'physical')
    surf = moves('surf', 90, water, 100, 15, 'special')
    outrage = moves('outrage', 120, dragon, 100, 10, 'physical')
    hyperbeam = moves('hyper beam', 150, normal, 90, 5, 'special')

if __name__ == '__main__':
    main()