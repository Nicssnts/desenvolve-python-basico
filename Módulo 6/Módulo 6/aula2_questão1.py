import random

lista_original = [random.randint(-100, 100) for _ in range(20)]

lista_ordenada = sorted(lista_original)
print("1. Lista ordenada:")
print(lista_ordenada)
print("-" * 40)

print("2. Lista original:")
print(lista_original)
print("-" * 40)

indice_maior = lista_original.index(max(lista_original))
print(f"3. O maior valor é {max(lista_original)} e está no índice: {indice_maior}")
print("-" * 40)

indice_menor = lista_original.index(min(lista_original))
print(f"4. O menor valor é {min(lista_original)} e está no índice: {indice_menor}")