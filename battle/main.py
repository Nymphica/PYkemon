import pygame
import random
from Attack import attack
from Pokemon import pokemon
from PokeList import marco,marcoMoves, jorge,jorgeMoves


if __name__ == "__main__": #batalha
    while not(marco.isFainted() or jorge.isFainted()):

        print(f"É a vez do {marco.name}, qual golpe ele dará?")
        marcoAttack = marcoMoves[random.randint(0,2)] #aleatorio entre 0,2
        marco.hitPokemon(marcoAttack, jorge) #ataca inimigo com golpe
        print(marcoAttack.name)
        if not jorge.isFainted():
            print(f"É a vez do {jorge.name}, qual golpe ele dará?")
            jorgeAttack = jorgeMoves[random.randint(0,2)]
            jorge.hitPokemon(jorgeAttack, marco)
            print(jorgeAttack.name)

        print(f"{marco.name}|{marco.actualHp} HP / {jorge.name}|{jorge.actualHp} HP")

    winner = marco if jorge.isFainted() else jorge
    print(f"{winner.name} Ganhou!")

