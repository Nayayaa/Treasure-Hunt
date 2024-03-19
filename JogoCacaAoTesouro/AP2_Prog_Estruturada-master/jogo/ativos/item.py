
class Item:
    def __init__(self, nome, tipo, intensidade):
        self.nome = nome
        self.tipo = tipo
        self.intensidade = intensidade

    def cria_item(tipo_item):
        if tipo_item == "vida1":
            item_aleatorio = Item("poção de vida", "Vida", 20)
        elif tipo_item == "vida2":
            item_aleatorio = Item("poção de vida 2", "Vida", 40)
        elif tipo_item == "forca1":
            item_aleatorio = Item("poção de força", "Força", 1)
        elif tipo_item== "forca2":
            item_aleatorio = Item("poção de força 2", "Força", 2)
        elif tipo_item == "defesa":
            item_aleatorio = Item("poção de defesa", "Defesa", 1)
        return item_aleatorio
    