def substituir_vogais():
    
    frase = input("Digite uma frase: ")
    
    vogais = "aeiouAEIOU"
    
    frase_modificada = ""
    
    for letra in frase:
        if letra in vogais:
            frase_modificada += "*"
        else:
            frase_modificada += letra
            
    print(f"Frase modificada: {frase_modificada}")

if __name__ == "__main__":
    substituir_vogais()