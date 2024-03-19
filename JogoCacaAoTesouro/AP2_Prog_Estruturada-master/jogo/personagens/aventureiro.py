import random 
from jogo.ativos import item

class Aventureiro:
    def __init__(self, nome):
        self.nome = nome
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida_max = random.randint(100, 120)
        self.vida_atual = self.vida_max
        self.mochila = []
        self.posicao = [0, 0]
        self.uso_habilidade = 3

    def ver_atributos(self):
        print(f"{self.nome} atributos:")
        return (f"Vida: {self.vida_atual}, Forca: {self.forca}, Defesa: {self.defesa}, Habilidade: {self.uso_habilidade}")

    def atacar(self):
        return random.randint(1, 6) + self.forca

    def defender(self, dano):
        dano_recebido = dano - self.defesa
        if dano_recebido > 0:
            self.vida_atual -= dano_recebido
            return dano_recebido
        else: return "0"

    def dash(self):
        if self.uso_habilidade > 0:
            direcao = input("Escolha o lado para dar o dash: ").upper()
            if direcao in ["W", "A", "S", "D"]:
                if direcao == "W":
                    self.posicao[1] -= 2
                elif direcao == "S":
                    self.posicao[1] += 2
                elif direcao == "D":
                    self.posicao[0] += 2
                elif direcao == "A":
                    self.posicao[0] -= 2
                self.uso_habilidade -= 1
            else:
                print(f"{self.nome}, não conheço essa! Tente novamente!")
        else:
            print(f"{self.nome}, você não tem habilidade para usar")
        
    def mover(self, direcao):
        if direcao == "W":
            self.posicao[1] -= 1
        elif direcao == "S":
            self.posicao[1] += 1
        elif direcao == "D":
            self.posicao[0] += 1
        elif direcao == "A":
            self.posicao[0] -= 1

    def ad_mochila(self, item):
        self.mochila.append(item)

    def usar_item(self, item, index):
        self.mochila.pop(index)
        if item.tipo == "Vida":
            self.vida_atual = self.vida_atual * item.intensidade
            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max
        elif item.tipo == "Força":
            self.forca = self.forca + item.intensidade
        elif item.tipo == "Defesa":
            self.defesa = self.defesa + item.intensidade
    

    def ver_mochila(self):
        for i in range(len(self.mochila)):
            print(f"{i} - {self.mochila[i].nome}")


    def esta_vivo(self):
        return self.vida_atual > 0 
    
