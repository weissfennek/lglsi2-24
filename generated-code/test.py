def calcule_somme(n):
    somme = 0
    #En fait ton code manquait seulement les deux points(:) de la boucle for
    for i in range(1, n+1):
        somme += i
    return somme

nombre = 5
resultat = calcule_somme(nombre)
print(f"La somme des entiers de 1 à {nombre} est : {resultat}")
