from corrida import Corrida
class Motorista:
    def __init__(self):
        self.corridas = []

    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)

    def remover_corrida(self, corrida):
        self.corridas.remove(corrida)