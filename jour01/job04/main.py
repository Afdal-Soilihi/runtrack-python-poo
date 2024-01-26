class Personne:
    def __init__(self, nom="", prenom=""):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        return f"{self.nom} {self.prenom}"

# Instancier plusieurs personnes et utiliser la méthode SePresenter
personne1 = Personne("Dupont", "Jean")
personne2 = Personne("Martin", "Alice")

print(personne1.sePresenter())
print(personne2.sePresenter())