elementos = []

while len(elementos) < 4:
    entrada = input(f"Digite um número inteiro (mínimo 4, atual {len(elementos)}): ")
    if entrada.replace('-', '').isdigit():
        elementos.append(int(entrada))
        
        if len(elementos) >= 4:
            continuar = input("Deseja adicionar mais? (s/n): ").lower()
            if continuar == 'n':
                break
    else:
        print("Por favor, digite um valor inteiro válido.")

print("\n" + "="*30)

print(f"1. Lista original: {elementos}")

print(f"2. Os 3 primeiros elementos: {elementos[:3]}")

print(f"3. Os 2 últimos elementos: {elementos[-2:]}")

print(f"4. Lista invertida: {elementos[::-1]}")

print(f"5. Elementos de índice par: {elementos[::2]}")

print(f"6. Elementos de índice ímpar: {elementos[1::2]}")