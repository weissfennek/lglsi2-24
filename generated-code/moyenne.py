def calculer_moyenne(liste_notes):
    total = 0
    for note in liste_notes:
        total += note
    moyenne = total / len(liste_notes)
    return moyenne


notes = [85, 90, 78, 92, "a"]
resultat = calculer_moyenne(notes)
print("La moyenne est :", resultat)
