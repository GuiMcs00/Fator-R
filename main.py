import re
import os
import locale

locale.setlocale(locale.LC_ALL, '')
padrao = r'^\d+(?:[,.]\d{0,2})?$'
final = r'^\d{1,3}(\.\d{3})*,\d{2}$'
opcao = int

while opcao != 0:

    print("\n[1] - Descubra receita\n[2] - Descubra folha\n[0] - Sair")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        while True:
            os.system('cls')
            print("--- DESCUBRA RECEITA ---")
            while True:
                folha = input("Para saber o valor da receita, digite o valor da folha: ")
                if re.match(padrao, folha):
                    folha = folha.replace(',', '.')
                    folha = float(folha)
                    receita = 0.0
                    receita = folha / 0.28
                    receita = round(receita, 2)  # arredonda o valor da receita para 2 casas decimais
                    formatado = locale.format_string('%.2f', receita, grouping=True)
                    print("O valor da receita deve ser:", formatado)
                    break
                else:
                    print("Valor inválido, tente novamente.")
                    break
            break

    if opcao == 2:
        while True:
            os.system('cls')
            print("--- DESCUBRA FOLHA ---")
            while True:
                receita = input("Para saber o valor da folha, digite o valor da receita: ")
                if re.match(padrao, receita):
                    receita = receita.replace(',', '.')
                    receita = float(receita)
                    folha = 0.0
                    folha = receita * 0.28
                    folha = round(folha, 2)  # arredonda o valor da folha para 2 casas decimais
                    formatado = locale.format_string('%.2f', folha, grouping=True)
                    print("O valor da folha deve ser:", formatado)
                    break
                else:
                    print("Valor inválido, tente novamente.")
                    break
            break
    if opcao == 0:
        break
