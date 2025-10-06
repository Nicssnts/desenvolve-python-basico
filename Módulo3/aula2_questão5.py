genero = "F"
idade = 60
tempo_servico = 32

if genero == "F":
    pode_aposentar = idade > 60 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25)
elif genero == "M":
    pode_aposentar = idade > 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25)
else:
    pode_aposentar = False

print(pode_aposentar)
