import random
class Tesouro:
    while True:
        posicao = [random.randint(0, 9), random.randint(0, 9)]
        if posicao != [0, 0]:
            break
