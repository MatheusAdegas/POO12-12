class Inimigo:
    def __init__(self):
        self.dano = 8
        self.vida = 60
        self.velocidade = 8
        self.vivo = True

    def persegue(self, alvo):
        if not self.vivo:
            return
        print("Inimigo está perseguindo:", getattr(alvo, "nome", alvo))

    def ataca(self, alvo):
        if not self.vivo:
            return
        if alvo is None:
            return
        if hasattr(alvo, "receberDano"):
            alvo.receberDano(self.dano)
        print("Inimigo atacou causando:", self.dano)

    def pula(self):
        if not self.vivo:
            return
        print("Inimigo pulou.")

    def receberDano(self, dano_recebido):
        if not self.vivo:
            return 0
        self.vida = self.vida - dano_recebido
        if self.vida <= 0:
            self.morre()
        return self.vida

    def morre(self):
        self.vida = 0
        self.vivo = False
        print("Inimigo morreu.")