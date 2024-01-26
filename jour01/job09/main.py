class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Informations du produit - Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

# Utiliser la classe Produit
produit1 = Produit("Livre", 10, 5)
produit2 = Produit("Ordinateur", 800, 10)

produit1.afficher()
print(f"Prix TTC du produit1: {produit1.calculerPrixTTC()}")

produit2.afficher()
print(f"Prix TTC du produit2: {produit2.calculerPrixTTC()}")

produit1.modifierNom("Cahier")
produit2.modifierPrix(900)

produit1.afficher()
print(f"Nouveau prix TTC du produit1: {produit1.calculerPrixTTC()}")

produit2.afficher()
print(f"Nouveau prix TTC du produit2: {produit2.calculerPrixTTC()}")