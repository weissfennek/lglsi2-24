class CarteEtudiant:
    def __init__(self, prenom, nom, numero_etudiant):
        self.prenom = prenom
        self.nom = nom
        self.numero_etudiant = numero_etudiant

    def afficher_informations(self):
        print("Nom:", self.nom)
        print("Prénom:", self.prenom)
        print("Numéro étudiant:", self.numero_etudiant)

# Exemple d'utilisation
etudiant1 = CarteEtudiant("John", "Doe", "123456")
etudiant2 = CarteEtudiant("Jane", "Smith", "789012")

# Affichage des informations des cartes étudiants
etudiant1.afficher_informations()
print("\n")
etudiant2.afficher_informations()
