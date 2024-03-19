import random
from jogo.ativos import tesouro
class Monstro:
    def __init__(self):
        self.forca = random.randint(5, 25)
        self.defesa = random.randint(5, 10)
        self.vida = random.randint(10, 100)

    def ver_atributos(self):
        print("Monstro atributos")
        return (f"Vida: {self.vida}, Forca: {self.forca}, Defesa: {self.defesa}")

    def atacar(self):
        return self.forca

    def defender(self, dano):
        dano_recebido = dano - self.defesa
        self.vida -= dano_recebido
        return dano_recebido

    def esta_vivo(self):
        return self.vida > 0
    
