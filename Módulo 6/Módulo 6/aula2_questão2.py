import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma = sum(elementos)
media = soma / num_elementos

print(f"Quantidade de elementos gerados (num_elementos): {num_elementos}")
print("-" * 40)

print("1. Lista 'elementos':")
print(elementos)
print("-" * 40)

print(f"2. A soma dos valores da lista:")
print(soma)
print("-" * 40)

print(f"3. A média dos valores da lista:")
print(f"{media:.2f}")