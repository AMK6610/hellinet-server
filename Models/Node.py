import math

from Models.Army import Army
class Node:
    def __init__(self, id, ownerID, position, factor, soldier_count, max_value=50):
        self.id = id
        self.max_value = max_value
        self.ownerID = ownerID
        self.soldier_count = soldier_count
        self.position = position
        self.factor = factor

    def reach(self, army):
        if self.ownerID == army.ownerID:
            self.soldier_count += army.soldier_count
            if self.soldier_count > self.max_value:
                self.soldier_count = self.max_value
            return True
        elif self.soldier_count >= army.soldier_count:
            self.soldier_count -= army.soldier_count
            return False
        else:
            self.soldier_count = army.soldier_count - self.soldier_count
            self.ownerID = army.ownerID
            return True

    def reach(self, army1, army2):
        if army1.ownerID == self.ownerID:
            self.reach(army1)
            self.reach(army2)
        elif army2.ownerID == self.ownerID:
            self.reach(army2)
            self.reach(army1)
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
                self.reach(army1)
                self.reach(army2)
            else:
                self.reach(army2)
                self.reach(army1)

    def populate(self):
        if self.ownerID != 0:
            self.soldier_count += self.factor
            if self.soldier_count > self.max_value != -1:
                self.soldier_count = self.max_value
