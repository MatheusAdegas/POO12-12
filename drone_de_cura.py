from drone import Drone

class DroneDeCura(Drone):
    def __init__(self):
        self.cura = 12

    def curar(self, objeto):
        if objeto is None or not hasattr(objeto, "vida"):
            return 0
        objeto.vida = objeto.vida + self.cura
        if hasattr(objeto, "vivo") and objeto.vida > 0:
            objeto.vivo = True
        print("Drone de cura curou:", self.cura)
        return self.cura