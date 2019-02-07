import math

class Node:
    def __init__(self, id, ownerID, position, factor, soldier_count, max_value=50):
        self.id = id
        self.max_value = max_value
        self.ownerID = ownerID
        self.soldier_count = soldier_count
        self.position = position
        self.factor = factor

    def reach_single(self, army):
        print("army from", army.source_node.id, "has reached", army.destination_node.id, "with", army.soldier_count, "soldiers")
        if self.ownerID == army.ownerID:
            self.soldier_count += army.soldier_count
            if self.soldier_count > self.max_value:
                self.soldier_count = self.max_value

            print("now", army.destination_node.id, "has", army.destination_node.soldier_count, "soldiers and is for", self.ownerID)
            return True
        elif self.soldier_count >= army.soldier_count:
            self.soldier_count -= army.soldier_count
            print("now", army.destination_node.id, "has", army.destination_node.soldier_count, "soldiers and is for", self.ownerID)
            return False
        else:
            self.soldier_count = army.soldier_count - self.soldier_count
            self.ownerID = army.ownerID
            print("now", army.destination_node.id, "has", army.destination_node.soldier_count, "soldiers and is for", self.ownerID)
            return True

    def reach_multiple(self, army1, army2):
        if army1.ownerID == self.ownerID:
            self.reach_single(army1)
            self.reach_single(army2)
        elif army2.ownerID == self.ownerID:
            self.reach_single(army2)
            self.reach_single(army1)
        else:
            defender_half = math.ceil(self.soldier_count / 2)
            if army1.soldier_count >= defender_half and army2.soldier_count >= defender_half:
                if army1.soldier_count > army2.soldier_count:
                    self.soldier_count = army1.soldier_count - army2.soldier_count
                    self.ownerID = army1.ownerID
                elif army2.soldier_count > army1.soldier_count:
                    self.soldier_count = army2.soldier_count - army1.soldier_count
                    self.ownerID = army2.ownerID
                else:
                    self.soldier_count = 0
            elif army1.soldier_count >= defender_half > army2.soldier_count:
                self.reach_single(army1)
                self.reach_single(army2)
            else:
                self.reach_single(army2)
                self.reach_single(army1)

    def populate(self):
        if self.ownerID != 0:
            self.soldier_count += self.factor
            if self.soldier_count > self.max_value != -1:
                self.soldier_count = self.max_value

    def march(self, army):
        self.soldier_count -= army.soldier_count