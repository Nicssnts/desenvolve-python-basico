idade = 16
jogou_3_ou_mais = True
vitorias = 4

apto = (16 <= idade <= 18) and jogou_3_ou_mais and (vitorias >= 1)

print("Apto para ingressar no clube de jogos de tabuleiro:", apto)
