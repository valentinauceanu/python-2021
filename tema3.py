class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return str(self.numarator) + "/" + str(self.numitor)

    def __add__(self, other):
        if self.numitor == other.numitor:
            return Fractie(self.numarator + other.numarator, self.numitor)
        if self.numitor != other.numitor:
            numitor_nou = self.numitor * other.numitor
            numarator_nou = self.numarator*other.numitor + self.numitor*other.numarator
            return Fractie(numarator_nou, numitor_nou)

    def __sub__(self,other):
        if self.numitor == other.numitor:
            return Fractie(self.numarator - other.numarator, self.numitor)
        if self.numitor != other.numitor:
            numitor_nou = self.numitor * other.numitor
            numarator_nou = self.numarator * other.numitor - self.numitor * other.numarator
            return Fractie(numarator_nou, numitor_nou)

    def inverse(self):
        auxiliar = self.numarator
        self.numarator = self.numitor
        self.numitor = auxiliar
        return Fractie(self.numarator, self.numitor)


fractie1 = Fractie(5, 7)
print(fractie1.__str__())
fractie2 = Fractie(3, 2)
suma = fractie1.__add__(fractie2)
print(suma.__str__())
diferenta = fractie1.__sub__(fractie2)
print(diferenta.__str__())
print(fractie1.inverse())