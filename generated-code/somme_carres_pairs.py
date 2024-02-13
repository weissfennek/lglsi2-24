def carre(nombre):
    return nombre ** 2

def somme_carres_pairs(n):
    somme = 0
    for i in range(n+1):  # change range(n) to range(n+1) to include n in the loop
        if i % 2 == 0:
            somme += carre(i)  # add the square of i to the sum if i is even
    return somme

n = 10
resultat = somme_carres_pairs(n)
print("La somme des carrés des nombres pairs jusqu'à", n, "est :", resultat)
