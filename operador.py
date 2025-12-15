from jogador import Jogador

class Operador(Jogador):
    def __init__(self):
        super().__init__()
        self.custoVida = 0
        self.sacrificeBonus = 0.0
        self.drones = []  # operador pode controlar drones

    def adicionaDrone(self, drone):
        if drone is None:
            return False
        self.drones.append(drone)
        print("Operador adicionou drone:", drone.__class__.__name__)
        return True

    def controlaDrones(self, alvo):
        # manda todos seguirem o alvo
        for d in self.drones:
            if hasattr(d, "segue"):
                d.segue(alvo)

    def ataca(self, alvo):
        if not self.vivo:
            return

        # Se tiver custo/bonus, aplica (mesma ideia do REX)
        if self.custoVida > 0:
            self.receberDano(self.custoVida)
            if not self.vivo:
                return

        dano_final = self.dano
        dano_final = int(dano_final * (1.0 + self.sacrificeBonus))

        # hasattr 
        if alvo is not None and hasattr(alvo, "receberDano"):
            alvo.receberDano(dano_final)

        print("Operador atacou. Dano:", dano_final)

    def cura(self, alvo):
        # Cura simples
        if alvo is None or not hasattr(alvo, "vida"):
            return 0
        cura_valor = 10
        alvo.vida = alvo.vida + cura_valor
        if hasattr(alvo, "vivo") and alvo.vida > 0:
            alvo.vivo = True
        return cura_valor