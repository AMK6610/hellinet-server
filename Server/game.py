import Models.Map
import random

from Models.Army import Army


def run():
    print("salam")

def decide(player_map, id):
    attack_prob = random.random()
    if attack_prob < 0.1:
        my_nodes = player_map.get_my_nodes(id)
        enemy_nodes = player_map.get_enemy_nodes(id)
        source = random.randint(0, len(my_nodes) - 1)
        destination = random.randint(0, len(enemy_nodes) - 1)

        return (my_nodes[source].id, enemy_nodes[destination].id)

    else:
        return None