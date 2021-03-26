from Attack import attack
from Pokemon import pokemon

#Marco
marcoMoves = [
        attack("feedback", 10, 0.3),
        attack("mutado", 25, 0.5),
        attack("aula4", 50, 0.3)
    ]
marco = pokemon("Marco", marcoMoves, 300)

#Jorge
jorgeMoves = [
        attack("armario", 10, 0.3),
        attack("jamboard", 25, 0.5),
        attack("desespero.py", 50, 0.3)
    ]

jorge = pokemon("Jorge", jorgeMoves, 300)