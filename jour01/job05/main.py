class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées: ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée X: {self.x}")

    def afficherY(self):
        print(f"Coordonnée Y: {self.y}")

    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur

    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur

# Utiliser la classe Point
point_instance = Point(3, 5)
point_instance.afficherLesPoints()
point_instance.afficherX()
point_instance.afficherY()
point_instance.changerX(7)
point_instance.changerY(10)
point_instance.afficherLesPoints()