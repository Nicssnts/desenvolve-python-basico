n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {n1} elementos da lista 1:")
for _ in range(n1):
    lista1.append(input())

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {n2} elementos da lista 2:")
for _ in range(n2):
    lista2.append(input())

lista_intercalada = []

menor_comprimento = min(len(lista1), len(lista2))

for i in range(menor_comprimento):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

lista_intercalada.extend(lista1[menor_comprimento:])
lista_intercalada.extend(lista2[menor_comprimento:])

print("Lista intercalada:", " ".join(map(str, lista_intercalada)))