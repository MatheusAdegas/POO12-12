from jogador import Jogador
from operador import Operador
from inimigo import Inimigo
from drone import Drone
from drone_de_combate import DroneDeCombate
from drone_de_cura import DroneDeCura

if __name__ == "__main__":
    player = Operador()
    enemy = Inimigo()

    d1 = DroneDeCombate()
    d2 = DroneDeCura()

    print(f"vida do jogador: {player.vida}")
    print(f"vida do inimigo: {enemy.vida}")

    player.adicionaDrone(d1)
    player.adicionaDrone(d2) 

    player.ataca(enemy)
    d1.segue(enemy)
    d1.burst(enemy)
    enemy.ataca(player)
    d2.curar(player)

    print(f"vida do jogador: {player.vida}")
    print(f"vida do inimigo: {enemy.vida}")