def est_palindrome(mot): # Added :
    mot = mot.lower()
    return mot == mot[::-1]


mots = ["radar", "python", "stats", "level", "deified"]

# Vérifier si chaque mot est un palindrome
for mot in mots:
    if est_palindrome(mot): # Added :
        print(f"est un palindrome !")
    else:  # Added :
        print(f"n'est pas un palindrome.")
