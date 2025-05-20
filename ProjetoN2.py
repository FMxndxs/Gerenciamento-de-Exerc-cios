# Felipe Mendes Campos RA 10740655
# Vinicius Bizarria da Silva RA 10739202

import random

# criar lista para os exercicios
exercicios = []  # [nome, tempo, calorias, dia da semana] [0, 1, 2, 3]


frases_para_incentivar = [
    "Independente de motivação, siga em frente e corra atrás dos seus sonhos!",
    "Você é mais forte do que pensa, continue treinando!",
    "O dia só vai ser triste se você não sair para treinar",
    "Não desista até se tornar a melhor versão de você mesmo!",
    "Seu corpo ouve tudo o que sua mente diz e sua mente diz para você treinar",
    "Não seja um frango, vá para a academia"
]

# Criar menu de opções


def menu():
    sair = False
    while sair == False:
        print("+----------------------+")
        print("|         MENU         |")
        print("|       ACADEMACK      |")
        print("+----------------------+")
        print("1. Cadastrar exercício")
        print("2. Relatório diário")
        print("3. Calcular IMC")
        print("4. Definir meta semanal")
        print("5. Verificar meta semanal")
        print("6. Frase motivacional")
        print("7. Média de calorias por exercício")
        print("8. Gráfico de barras (calorias)")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_de_exercicio()
        elif opcao == "2":
            relatorio_diario()
        elif opcao == "3":
            imc()
        elif opcao == "4":
            define_meta()
        elif opcao == "5":
            verifica_meta()
        elif opcao == "6":
            frase_motivacional()
        elif opcao == "7":
            media_cal()
        elif opcao == "8":
            grafico_calorico()
        elif opcao == "0":
            print("Encerrando o programa, bons treinos e mantenha o foco")
            sair = True
        else:
            print("Opção inválida, tente novamente")

# funcao de cadastro


def cadastro_de_exercicio():
    nome = input("Digite o nome do exercício: ")
    tempo_gasto = int(input("Digite o tempo gasto no exercício (minutos): "))
    calorias = int(input("Insira a quantidade de calorias queimadas: "))
    # tornar o dia da semana em maiúsculo e evitar erros
    dia_da_semana = input("Insira o dia da semana: ").capitalize()
    exercicios.append([nome, tempo_gasto, calorias, dia_da_semana])
    print("Exercício cadastrado com sucesso!\n")

# funcao do relatório


def relatorio_diario():
    dia = input("Digite o dia da semana para o relatório: ").capitalize()
    tempo_total = 0
    calorias_total = 0
    encontrou = False  # cursos para varrer o dia e procurar exercício

    print(f"\nRelatório de {dia}:")
    for exercicio in exercicios:  # varrer a lista de exercícios
        if exercicio[3] == dia:  # se o dia da semana do exercício for igual ao dia escolhido
            # imprimir o nome do exercício, tempo gasto e calorias queimadas
            print(f"- {exercicio[0]}: {exercicio[1]} min, {exercicio[2]} cal")
            # somar o tempo gasto de cada exercício
            tempo_total += exercicio[1]
            # somar as calorias queimadas de cada exercício
            calorias_total += exercicio[2]
            encontrou = True  # se o exercício foi encontrado, encontrou recebe True
    if encontrou:  # Se o exercício foi encontrado, informe ao usuario o tempo total e calorias queimadas
        print(f"Tempo total: {tempo_total} minutos")  # imprimir o tempo total
        # imprimir as calorias queimadas
        print(f"Calorias queimadas: {calorias_total} cal\n")
    else:
        # não houve exercício no dia informado
        print("Nenhum exercício encontrado para esse dia.\n")


def imc():
    peso = float(input("Digite seu peso (Kilos): "))
    altura = float(input("Digite sua altura (Metros): "))
    # formula imc = peso / altura * altura
    imc = peso / (altura ** 2)
    print(f"Seu Índice de Massa Corporea é: {imc:.2f}")
    if imc < 18.5:
        print("Classificação: Baixo peso\n")
    elif imc > 18.5 and imc < 25:
        print("Classificação: Normal\n")
    elif imc > 25 and imc < 30:
        print("Classificação: Sobrepeso\n")
    else:
        print("Classificação: Obesidade\n")


# Variaveis para definir e verificar meta semanal
meta_semanal = 0
total_calorias_semana = 0


def define_meta():
    global meta_semanal, total_calorias_semana  # chamar variaveis globais

    meta_semanal = int(input("Defina a meta de calorias para a semana: "))
    total_calorias_semana = 0  # iniciar contador
    for i in exercicios:
        # somar as calorias queimadas de cada exercício em todos os dias
        total_calorias_semana += i[2]
    print(f"Meta definida: {meta_semanal} calorias")
    print(f"Total atual de calorias queimadas: {total_calorias_semana}")


def verifica_meta():
    global meta_semanal, total_calorias_semana  # chamar variaveis globais
    # somar total de calorias novamente caso o usuario tenha inserido novos exercicios
    total_calorias_semana = 0
    for i in exercicios:
        total_calorias_semana += i[2]
    if meta_semanal == 0:  # caso define_meta() nao tenha sido chamada anteriormente
        print(
            "Você ainda não definiu uma meta semanal. Use a opção 'Definir meta' primeiro.")
    else:  # se meta foi definida, entao verifique se a meta foi atingida
        print(f"Meta atual: {meta_semanal} calorias")
        print(
            f"O total de calorias queimadas na semana é: {total_calorias_semana}")
        if total_calorias_semana >= meta_semanal:  # verificar meta atingida
            print("Meus parabéns guerreiro(a), você atingiu a sua meta semanal!")
        else:
            print("Poxa vida, essa semana você não atingiu a meta :(")


def frase_motivacional():  # randomizar as frases e imprimir
    frase = random.choice(frases_para_incentivar)
    print(f"Motivação do dia: {frase}\n")


def media_cal():  # pegar o total de calorias e dividir pelo total de exercicios
    total_calorias = 0
    # verificar quantos exercícios foram feitos
    total_exercicios = len(exercicios)
    for i in exercicios:
        total_calorias += i[2]  # somar as calorias armazenadas na lista
    media_de_calorias = total_calorias / total_exercicios
    print(f"A média de calorias por exercício é: {media_de_calorias:.2f} cal")


def grafico_calorico():  # para cada exercicio verificar o total de calorias e imprimir uma # para cada 50 calorias
    if len(exercicios) == 0:
        print("Não há registros de exercícios\n")
        return
    else:
        print("Gráfico de calorias queimadas: ")
        for i in exercicios:
            # cada # representa 50 calorias queimadas
            barras = '#' * (i[2] // 50)
            # exercicio: #### x calorias
            print(f"{i[0]}: {barras} ({i[2]} calorias)")
        print()


# funcao principal
if __name__ == "__main__":
    menu()
