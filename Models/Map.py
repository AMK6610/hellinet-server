from Models.Node import Node


class Map:
    def __init__(self):
        self.generate_default_map()

    def generate_default_map(self):
        self.nodes = [
            Node(1, 1, (0, 0), 2, 20, -1),
            Node(2, 2, (10, 10), 2, 20, -1),

            Node(3, 0, (4, 0), 2, 10),
            Node(4, 0, (6, 0), 2, 10),
            Node(5, 0, (5, 2), 2, 10),

            Node(6, 0, (4, 10), 2, 10),
            Node(7, 0, (6, 10), 2, 10),
            Node(8, 0, (5, 8), 2, 10),

            Node(9, 0, (6, 4), 2, 30),
            Node(10, 0, (5, 5), 2, 30),
            Node(11, 0, (4, 6), 2, 30),
            Node(12, 0, (4, 4), 2, 30),
            Node(13, 0, (6, 6), 2, 30),
        ]

    def populate(self):
        for node in self.nodes:
            node.populate()

    def do_events(self, events):
        # events is a list of Army's reached
        nodes_army_map = [[] for i in range(self.nodes)]
        for army in events:
            other_army_exist = False

            for other_army in nodes_army_map[army.destination_node.id - 1]:
                if other_army.ownerID == army.ownerID:
                    other_army.soldier_count += army.soldier_count
                    other_army_exist = True

            if not other_army_exist:
                nodes_army_map[army.destination_node.id - 1].append(army)

        for i in range(len(nodes_army_map)):
            if len(nodes_army_map[i]) == 0:
                continue
            elif len(nodes_army_map[i]) == 1:
                self.nodes[i].reach(nodes_army_map[i][0])
            elif len(nodes_army_map[i]) == 2:
                self.nodes[i].reach(nodes_army_map[i][0], nodes_army_map[i][1])
            else:
                raise Exception("more than two attackers")

    def check_finish(self):
        checkWin = True
        for node in self.nodes:
            if node.ownerID != self.nodes[0].ownerID:
                checkWin = False
                break

        return checkWin
