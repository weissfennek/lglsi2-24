def calculer_moyenne(liste):
    if len(liste) == 0:
        return 0  # Retourne 0 si la liste est vide pour éviter une division par zéro
    somme = sum(liste)
    moyenne = somme / len(liste)
    return moyenne

# Exemple d'utilisation
liste_de_nombres = [5, 10, 15, 20, 25]
moyenne = calculer_moyenne(liste_de_nombres)
print("La moyenne est :", moyenne)
