from jogo.personagens import aventureiro, monstro
def combate(aventureiro, monstro):
    print("Voce entrou em COMBATE!")
    print(monstro.ver_atributos())
    while aventureiro.esta_vivo() and monstro.esta_vivo():
        # Fase do aventureiro
        dano_aventureiro = aventureiro.atacar()
        dano_recebido_m = monstro.defender(dano_aventureiro)
        print(f"{aventureiro.nome} atacou o monstro, causando {dano_recebido_m} de dano!")

        if not monstro.esta_vivo():
            print(f"O monstro foi derrotado por {aventureiro.nome}!")
            print(aventureiro.ver_atributos())
            break

        # Fase do monstro
        if monstro.esta_vivo():
            dano_monstro = monstro.atacar()
            dano_recebido_a = aventureiro.defender(dano_monstro)
            print(f"O monstro atacou {aventureiro.nome}, causando {dano_recebido_a} de dano!")

        if not aventureiro.esta_vivo():
            print(f"{aventureiro.nome} foi derrotado pelo monstro!")
            break
