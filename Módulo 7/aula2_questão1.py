def formatar_data():
    
    data_input = input("Digite uma data de nascimento (dd/mm/aaaa): ")

    partes = data_input.split("/")

    dia = int(partes[0])
    mes_indice = int(partes[1])
    ano = int(partes[2])

    meses = [
        "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    mes_extenso = meses[mes_indice]

    print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")

if __name__ == "__main__":
    formatar_data()