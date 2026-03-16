frase = input("Digite uma frase: ")

vogais_referencia = "aeiouAEIOU"

indices = []

for i, caractere in enumerate(frase):
    if caractere in vogais_referencia:
        indices.append(i)

print(f"{len(indices)} vogais")
print(f"Índices {indices}")