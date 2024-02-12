def carre(nombre):
    return nombre ** 2

def somme_carres_pairs(n):
    somme = 0
    for i in range(n+1):
        if i % 2 == 0:
            somme += carre(i)
    return somme

n = 10
resultat = somme_carres_pairs(n)
print("La somme des carrés des nombres pairs jusqu'à", n, "est :", resultat)
