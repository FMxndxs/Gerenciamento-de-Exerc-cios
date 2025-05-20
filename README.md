# ACADEMACK - Sistema de Gerenciamento de Exercícios Físicos

## Descrição
O ACADEMACK é um sistema de gerenciamento de exercícios físicos desenvolvido em Python que permite aos usuários acompanhar suas atividades físicas, definir metas de calorias, calcular IMC e receber motivação para manter a rotina de exercícios.

## Desenvolvedores
- Felipe Mendes Campos (RA 10740655)
- Vinicius Bizarria da Silva (RA 10739202)

## Funcionalidades

### 1. Cadastrar exercício
Permite registrar exercícios realizados com informações como:
- Nome do exercício
- Tempo gasto (em minutos)
- Calorias queimadas
- Dia da semana

### 2. Relatório diário
Exibe um resumo dos exercícios realizados em um dia específico, incluindo:
- Lista de exercícios
- Tempo total de atividade
- Total de calorias queimadas

### 3. Calcular IMC
Calcula o Índice de Massa Corporal com base no peso e altura informados, classificando o resultado em:
- Baixo peso (IMC < 18.5)
- Normal (IMC entre 18.5 e 25)
- Sobrepeso (IMC entre 25 e 30)
- Obesidade (IMC > 30)

### 4. Definir meta semanal
Permite estabelecer uma meta de calorias a serem queimadas durante a semana.

### 5. Verificar meta semanal
Compara o total de calorias queimadas com a meta estabelecida, informando se o objetivo foi alcançado.

### 6. Frase motivacional
Exibe uma frase aleatória para motivar o usuário a continuar se exercitando.

### 7. Média de calorias por exercício
Calcula a média de calorias queimadas por exercício registrado.

### 8. Gráfico de barras (calorias)
Apresenta um gráfico visual simples mostrando as calorias queimadas em cada exercício, onde cada "#" representa 50 calorias.

## Como usar
1. Execute o arquivo `ProjetoN2.py`
2. Navegue pelo menu digitando o número da opção desejada
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
