def verificar_palindromo():
    while True:
        entrada = input('Digite uma frase (digite "fim" para encerrar): ')
        
        if entrada.strip().lower() == "fim":
            break
            
        frase_limpa = "".join(char.lower() for char in entrada if char.isalnum())
        
        if frase_limpa == frase_limpa[::-1]:
            print(f'"{entrada}" é palíndromo')
        else:
            print(f'"{entrada}" não é palíndromo')

if __name__ == "__main__":
    verificar_palindromo()