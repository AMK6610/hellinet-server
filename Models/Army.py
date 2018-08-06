class Army:
    def __init__(self, ownerID, source_node, destination_node):
        self.soldier_count = source_node.soldier_count // 2
        self.ownerID = ownerID
        self.destination_node = destination_node
        self.source_node = source_node

    def distance(self):
        return (20 * (abs(self.source_node.position[0] - self.destination_node.position[0]) +
                      abs(self.source_node.position[1] - self.destination_node.position[1])))
