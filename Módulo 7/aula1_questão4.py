celular = input("Digite o número: ").strip()

if len(celular) == 8:
    celular = "9" + celular

elif len(celular) == 9:
    if celular[0] != "9":
        print("Aviso: O número tem 9 dígitos mas não começa com 9.")

numero_formatado = f"{celular[:5]}-{celular[5:]}"

print(f"Número completo: {numero_formatado}")