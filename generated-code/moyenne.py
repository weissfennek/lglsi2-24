def calculer_moyenne(liste_notes):
    if not len(liste_notes):
        return 0
    if not all(isinstance(x, (int, float)) for x in liste_notes):
        return None
        
    return sum(liste_notes) / len(liste_notes)

# Must be a list of integer or float
notes = [85, 90, 78, 92]
resultat = calculer_moyenne(notes)
print("La moyenne est :", resultat)
