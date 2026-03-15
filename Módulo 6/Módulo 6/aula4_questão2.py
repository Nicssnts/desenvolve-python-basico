frase = input("Digite uma frase: Em um ninho de mafagafos, há cinco mafagafinhos. ")

vogais_ref = "aeiouAEIOU"

vogais = sorted([char.lower() for char in frase if char in vogais_ref])

consoantes = [char for char in frase if char.isalpha() and char not in vogais_ref]
print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")