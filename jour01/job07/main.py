class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Utiliser la classe Personnage
perso_instance = Personnage()
perso_instance.droite()
perso_instance.haut()
print(f"Position du personnage: {perso_instance.position()}")
