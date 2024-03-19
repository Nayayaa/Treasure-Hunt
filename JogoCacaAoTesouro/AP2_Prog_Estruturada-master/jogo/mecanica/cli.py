import random

from jogo.ativos import item, mapa, tesouro
from jogo.mecanica import combate
from jogo.personagens import aventureiro, monstro, arte


def escolher_acao(dic_probabilidades):
    acao_escolhida = random.choices(list(dic_probabilidades.keys()), weights= dic_probabilidades.values())[0]
    return acao_escolhida

def jogo():
    p1 = aventureiro.Aventureiro(input("Deseja buscar um tesouro? Primeiro, informe seu nome: "))
    tes = tesouro.Tesouro()
    dist_acoes = {
        "nada" : 0.4,
        "Item" : 0.2,
        "Monstro" : 0.4
    }
    dist_item = {
        "vida1" : 0.5,
        "vida2" : 0.3,
        "forca1" : 0.1,
        "forca2" : 0.5,
        "defesa" : 0.5
    }
    print(f"Saudações, {p1.nome}! Boa sorte!")
    if p1.posicao != tes.posicao:
        mapa.desenhar(p1, tes)

    while True:
        if not p1.esta_vivo():
            arte.game_over()
            break
        op = input("Insira o seu comando(Q = sair, T = ver atributos, I = inventario, E = usar habilidade, WASD = mover): ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            print(p1.ver_atributos())

        elif op == "I":
            p1.ver_mochila()
            while True:
                try:
                    numero_item_input = input("Digite o numero do item(Q = Fechar): ")
                    if numero_item_input.upper() == "Q":
                        print("Mochila Fechada")
                        break
                    numero_item = int(numero_item_input)
                    if numero_item <= len(p1.mochila) - 1:
                        print(f"Voce usou um item do tipo {p1.mochila[numero_item].tipo}")
                        p1.usar_item(p1.mochila[numero_item], numero_item)
                        break
                    else:
                        print("Número de item fora do intervalo válido. Tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            continue

        elif op in ["W", "A", "S", "D", "E"]:
            if op == "E":
                p1.dash()
            p1.mover(op)  # Atualize a posição do jogador

            if (p1.posicao[0] < 0 or p1.posicao[0] >= 10 or
                p1.posicao[1] < 0 or p1.posicao[1] >= 10):
                arte.game_over()
                break
            mapa.desenhar(p1, tes)
            acao = escolher_acao(dist_acoes)

            if tes.posicao == p1.posicao:
                print(f"PARABENS, {p1.nome}! Você encontrou o tesouro!")
                arte.win()
                arte.treasure()
                break
            elif acao == "Monstro":
                print("Um monstro apareceu!")
                arte.bixo()
                m = monstro.Monstro()
                combate.combate(p1, m)

            elif acao == "Item":
                tipo = escolher_acao(dist_item)
                i = item.Item.cria_item(tipo)
                print("Você encontrou um item")
                p1.ad_mochila(i)

        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")



