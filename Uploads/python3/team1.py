import random
import sys

MAP_DETAIL_LENGTH = 6

game_map = None


def read_map():
    global game_map
    nodes_count = int(input())
    # print(nodes_count)

    # if game_map is None:
    game_map = [[int(input()) for j in range(MAP_DETAIL_LENGTH)] for i in range(nodes_count)]


def main(client_id):
    inp = ''
    while inp != 'shutdown':
        inp = input()
        if inp == 'shutdown':
            break
        # print(inp)
        # print(1, 1)
        if inp == 'turn':
            # print(inp)
            read_map()

        source_id = -1
        dest_id = -1

        p = random.random()
        if p < 0.9:
            source_id = random.randint(0, len(game_map) - 1)
            while game_map[source_id][1] != client_id:
                source_id = random.randint(0, len(game_map) - 1)

            dest_id = random.randint(0, len(game_map) - 1)

        # print(len(game_map), len(game_map))
        print(source_id, dest_id)


# print(-10, -10)

if __name__ == "__main__":
    id = int(sys.argv[1])
    main(id)
