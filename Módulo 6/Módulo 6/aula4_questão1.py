pares = [x for x in range(20, 51) if x % 2 == 0]

quadrados = [x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]

print(f"1. Pares (20-50): {pares}")
print("-" * 30)
print(f"2. Quadrados: {quadrados}")
print("-" * 30)
print(f"3. Divisíveis por 7: {divisiveis_por_7}")
print("-" * 30)
print(f"4. Paridade: {paridade}")