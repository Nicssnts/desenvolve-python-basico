classe =  "guerreiro"
forca = 17
magia = 7

if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = (forca > 5 and magia > 5) and (forca <= 15 and magia <= 15)
else:
    valido = False

print("Pontos de atributo consistentes com a classe escolhida:", valido)
