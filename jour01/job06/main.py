class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Utiliser la classe Animal
animal_instance = Animal()
print(f"Âge de l'animal: {animal_instance.age}")
animal_instance.vieillir()
print(f"Âge de l'animal après vieillissement: {animal_instance.age}")
animal_instance.nommer("Fido")
print(f"Nom de l'animal: {animal_instance.prenom}")