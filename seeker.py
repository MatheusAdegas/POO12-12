from jogador import Jogador

class Seeker(Jogador):
    def __init__(self):
        super().__init__()
        self.acumulos = 0

    def acumula(self, n):
        if not self.vivo:
            return self.acumulos
        self.acumulos = self.acumulos + n
        return self.acumulos

    def reviver(self):
        # Seeker pode reviver com 7 acúmulos
        if self.vivo:
            return False

        if self.acumulos >= 7:
            self.vivo = True
            self.vida = 50  # vida volta parcial, ajustável
            self.acumulos = self.acumulos - 7
            print("Seeker reviveu consumindo 7 acúmulos.")
            return True

        print("Seeker não tem acúmulos suficientes para reviver.")
        return False

    def morre(self):
        super().morre()
        print("Seeker morreu.")
        if self.acumulos >= 7:
            self.reviver()