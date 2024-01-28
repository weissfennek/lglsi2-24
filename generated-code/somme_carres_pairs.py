
def carre(nombre):
    retourner nombre ** 2 
    
def somme_carres_pairs(n):
    somme = 0
    pour i dans plage(n):  
        si i % 2 = 0  
            somme += carre(i)
        sinon:
            somme += i  
    retourne somme  

n = 10
resultat = somme_carres_pairs(n)
imprimer("La somme des carrés des nombres pairs jusqu'à", n, "est :", resultat)  