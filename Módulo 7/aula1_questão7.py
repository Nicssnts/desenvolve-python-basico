import random

def encrypt(lista_nomes):
    n = random.randint(1, 10)
    nomes_cript = []

    for nome in lista_nomes:
        nome_novo = ""
        for c in nome:
        
            codigo = ord(c)
            novo_codigo = codigo + n
            
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            
            nome_novo += chr(novo_codigo)
        
        nomes_cript.append(nome_novo)
    
    return nomes_cript, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)

print(f"Chave aleatória: {chave}")
print(f"Nomes criptografados: {nomes_cript}")