def validador_cpf():
    cpf_input = input("Digite o CPF (XXX.XXX.XXX-XX): ")
    
    cpf_numeros = "".join(char for char in cpf_input if char.isdigit())

    if len(cpf_numeros) != 11:
        print("Inválido (quantidade de dígitos incorreta)")
        return

    if cpf_numeros == cpf_numeros[0] * 11:
        print("Inválido")
        return

    nove_digitos = cpf_numeros[:9]
    soma_1 = 0
    multiplicador_1 = 10
    
    for digito in nove_digitos:
        soma_1 += int(digito) * multiplicador_1
        multiplicador_1 -= 1
        
    resto_1 = soma_1 % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

    dez_digitos = nove_digitos + str(digito_1)
    soma_2 = 0
    multiplicador_2 = 11
    
    for digito in dez_digitos:
        soma_2 += int(digito) * multiplicador_2
        multiplicador_2 -= 1
        
    resto_2 = soma_2 % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2

    if str(digito_1) == cpf_numeros[9] and str(digito_2) == cpf_numeros[10]:
        print("Válido")
    else:
        print("Inválido")

if __name__ == "__main__":
    validador_cpf()