distancia = 120
peso = 34

if distancia <= 100:
    valor_kg = 1.00
elif distancia <= 300:
    valor_kg = 1.50
else:
    valor_kg = 2.00

frete = peso * valor_kg

if peso > 10:
    frete += 10

print(f"Valor total do frete: R${frete:.2f}")
