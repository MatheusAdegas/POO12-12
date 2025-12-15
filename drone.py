class Drone:
    def __init__(self):
        self.altura = 10
        self.seguindo = None

    def segue(self, objeto):
        self.seguindo = objeto
        print("Drone seguindo:", getattr(objeto, "nome", objeto))
        return self.seguindo