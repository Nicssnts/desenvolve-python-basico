def encontrar_anagramas():
    frase = input("Digite uma frase: ")
    objetivo = input("Digite a palavra objetivo: ").lower()

    objetivo_ordenado = sorted(objetivo)

    palavras = frase.replace(",", "").replace(".", "").split()

    anagramas = []
    for p in palavras:
        if sorted(p.lower()) == objetivo_ordenado:
            anagramas.append(p)

    print(f"Anagramas: {anagramas}")

if __name__ == "__main__":
    encontrar_anagramas()