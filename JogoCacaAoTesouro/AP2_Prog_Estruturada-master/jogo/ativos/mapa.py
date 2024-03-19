def desenhar(aventureiro, tesouro):
    for y in range(10):
        for x in range(10):
            if aventureiro.posicao == [x, y]:
                print("@", end=" ")
            elif tesouro.posicao == [x, y]:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

