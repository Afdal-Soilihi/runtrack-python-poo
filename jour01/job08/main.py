import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Informations du cercle - Rayon: {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

# Utiliser la classe Cercle
cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print(f"Circonférence du cercle1: {cercle1.circonference()}")
print(f"Aire du cercle1: {cercle1.aire()}")
print(f"Diamètre du cercle1: {cercle1.diametre()}")

cercle2.afficherInfos()
print(f"Circonférence du cercle2: {cercle2.circonference()}")
print(f"Aire du cercle2: {cercle2.aire()}")
print(f"Diamètre du cercle2: {cercle2.diametre()}")