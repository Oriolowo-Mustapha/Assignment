import math
class QuadraticEquation:
    def __init__(self, a:int, b:int, c:int):
        self .__a = a
        self .__b = b
        self .__c = c

    def getDiscriminant(self):
        d = self .__b**2 - 4*self .__a*self .__c
        return d

    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return None
        else:
            root1 = -self .__b + math.sqrt(self.getDiscriminant() / 2*self .__a)
            return root1

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return None
        else:
            root2 = -self .__b - math.sqrt(self.getDiscriminant() / 2*self .__a)
            return root2

    