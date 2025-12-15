from drone import Drone

class DroneDeCombate(Drone):
    def __init__(self):
        super().__init__()
        self.tiros = 3

    def burst(self, alvo):
        if alvo is None or not hasattr(alvo, "receberDano"):
            return 0

        total = 0
        i = 0
        while i < self.tiros:
            alvo.receberDano(4)
            total = total + 4
            i = i + 1

        print("Drone de combate disparou burst. Total dano:", total)
        return total