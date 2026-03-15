import random

lista = [random.randint(-10, 10) for _ in range(20)]
print(f"Original: {lista}")

inicio_maior = 0
tamanho_maior = 0

inicio_atual = 0
tamanho_atual = 0

for i, num in enumerate(lista):
    if num < 0:
        if tamanho_atual == 0:
            inicio_atual = i
        tamanho_atual += 1
    else:
    
        if tamanho_atual > tamanho_maior:
            tamanho_maior = tamanho_atual
            inicio_maior = inicio_atual
        tamanho_atual = 0

if tamanho_atual > tamanho_maior:
    tamanho_maior = tamanho_atual
    inicio_maior = inicio_atual

if tamanho_maior > 0:
    del lista[inicio_maior : inicio_maior + tamanho_maior]

print(f"Editada:  {lista}")