import random

class Insect:

    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.flight = 0

    def set_flight(self):
        self.flight = random.randint(1,10)

    def get_wings(self):
        return self.wings

    def get_legs(self):
        return self.legs
    
    def get_flight(self):
        return self.flight
        