# Sistema de Gerenciamento de Exercícios

## Descrição
Este programa é um sistema de gerenciamento de exercícios físicos que permite ao usuário cadastrar exercícios, visualizar relatórios diários, calcular IMC, definir metas semanais de calorias, receber frases motivacionais, calcular médias de calorias e visualizar gráficos de barras de calorias queimadas.

## Desenvolvedores
- Felipe Mendes Campos RA 10740655
- Vinicius Bizarria da Silva RA 10739202

## Funcionalidades

1. **Cadastrar exercício**: Permite ao usuário cadastrar um novo exercício com nome, tempo gasto, calorias queimadas e dia da semana.

2. **Relatório diário**: Exibe um relatório dos exercícios realizados em um dia específico, incluindo o tempo total e as calorias totais queimadas.

3. **Calcular IMC**: Calcula o Índice de Massa Corporal do usuário com base no peso e altura informados, e fornece a classificação correspondente (Baixo peso, Normal, Sobrepeso ou Obesidade).

4. **Definir/verificar meta semanal**: Permite ao usuário definir uma meta de calorias para a semana e verifica se a meta foi atingida com base nos exercícios cadastrados.

5. **Frase motivacional**: Exibe uma frase motivacional aleatória para incentivar o usuário a continuar se exercitando.

6. **Média de calorias por exercício**: Calcula e exibe a média de calorias queimadas por exercício.

7. **Gráfico de barras (calorias)**: Exibe um gráfico de barras simples representando as calorias queimadas em cada exercício, onde cada '#' representa 100 calorias.

## Como usar
1. Execute o programa
2. Selecione uma opção do menu digitando o número correspondente
3. Siga as instruções na tela para cada funcionalidade

## Estrutura de dados
O programa utiliza uma lista para armazenar os exercícios, onde cada exercício é representado por uma lista contendo:
- Nome do exercício [0]
- Tempo gasto em minutos [1]
- Calorias queimadas [2]
- Dia da semana [3]

## Requisitos
- Python 3.x
- Módulo random (incluído na biblioteca padrão do Python)

## Execução
Para executar o programa, basta rodar o arquivo Python:
