from jogador import Jogador

class Commando(Jogador):
    def __init__(self):
        super().__init__()
        self.municao = 50

    def recarrega(self, n):
        self.municao = 50
        return self.municao