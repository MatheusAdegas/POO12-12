from jogador import Jogador

class REX(Jogador):
    def __init__(self):
        super().__init__()
        self.custoVida = 5
        self.sacrificeBonus = 1.0  # multiplicador

    def ataca(self, alvo):
        if not self.vivo:
            return
        # REX perde vida para causar dano
        self.receberDano(self.custoVida)

        if not self.vivo:
            return

        dano_final = self.dano
        dano_final = int(dano_final * (1.0 + self.sacrificeBonus))

        if alvo is not None and hasattr(alvo, "receberDano"):
            alvo.receberDano(dano_final)

        print("REX atacou e perdeu", self.custoVida, "de vida. Dano:", dano_final)

    def cura(self, alvo):
        if alvo is None:
            return 0
        if not hasattr(alvo, "vida"):
            return 0

        cura_valor = 15
        alvo.vida = alvo.vida + cura_valor
        if hasattr(alvo, "vivo") and alvo.vida > 0:
            alvo.vivo = True
        return cura_valor