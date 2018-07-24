import copy
import sys

from Models.Map import Map

player1 = __import__(sys.argv[1][: -3])
player2 = __import__(sys.argv[2][: -3])


def main():
    # print(sys.argv)
    game_map = Map()
    game_map.generate_default_map()
    player_map = copy.deepcopy(game_map)


if __name__ == "__main__":
    main()
