class Jogador:
    def __init__(self):
        self.dano = 10
        self.vida = 100
        self.velocidade = 10
        self.chanceCritico = 0  # 0 a 100
        self.vivo = True

    def move(self, direcao):
        if not self.vivo:
            return
        # direcao pode ser "frente", "tras", "esquerda", "direita"...
        print("Jogador se move para:", direcao, "| velocidade:", self.velocidade)

    def pula(self):
        if not self.vivo:
            return
        print("Jogador pulou.")

    def ataca(self, alvo):
        if not self.vivo:
            return

        if alvo is None:
            return

        dano_final = self.dano

        # (se a vida do alvo for múltipla de 10 e chanceCritico > 0, crita)
        if self.chanceCritico > 0 and (getattr(alvo, "vida", 0) % 10 == 0):
            dano_final = dano_final + (dano_final * self.chanceCritico) // 100

        if hasattr(alvo, "receberDano"):
            alvo.receberDano(dano_final)
        print("Jogador atacou causando:", dano_final)

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
        print("Jogador morreu.")