def calculer_moyenne(liste_notes):
    length = 0
    for i in liste_notes:
        length += 1
    
    if length == 0:
        return 0
    else:
        somme = 0
        for i in liste_notes:
            somme += i
        return somme / length

# Must be a list of floats
notes = [85, 90, 78, 92]
moyenne = calculer_moyenne(notes)
print("La moyenne est :", moyenne)
