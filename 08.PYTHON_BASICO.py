#Exemplos de programas básicos em Python:

#01 EXIBINDO INFORMAÇÃO NA TELA:
print("Olá, Mundo!")
print("Bem-vindo ao programa de exemplo!")
print("Por favor, siga as instruções abaixo:")
print("Programa concluído com sucesso!")

#02 INPUT (INSERINDO DADO):
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.")

#03 ENTENDENDO VARIÁVEIS:
nome = "Asimov Academy"  # String
idade = 5  # Inteiro
esta_ativo = True  # Booleano

print("Nome:", nome)
print("Idade:", idade)
print("Está ativo?", esta_ativo)

#04 CODIGO COM LISTA:
numeros = [1, 2, 3, 4, 5]
numeros.append(6)

for numero in numeros:
    print(numero)

#05 CODIGO COM DICIONÁRIO:
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}

aluno["matriculado"] = True

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

#06 MATEMÁTICA SIMPLES:
a = 5
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}")

#07 MODULO E EXPONENCIAÇÃO:
a = 5
b = 3

resto = a % b  # Módulo
potencia = a ** b  # Exponenciação

print(f"Resto da divisão: {resto}, {a} elevado a {b} é: {potencia}")

#08 TRATAMENTO DE ERROS:
a = 5

try:
    resultado = a / 0
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")

#09 ESTRUTURAS CONDICIONAIS:
idade = 20

if idade >= 18:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

#10 USO DO ELIF:
temperatura = 25

if temperatura > 30:
    print("Está muito quente.")
elif temperatura > 20:
    print("Está quente.")
elif temperatura > 10:
    print("Está agradável.")
else:
    print("Está frio.")

#11 USO DO IF E ELSE:
idade = 15
altura = 1.60

if idade >= 12:
    if altura >= 1.50:
        print("Você pode entrar no brinquedo.")
    else:
        print("Você não tem altura suficiente para entrar no brinquedo.")
else:
    print("Você não tem idade suficiente para entrar no brinquedo.")

#12 ESTRUTURA DE REPETIÇÃO:
valores = [10, 20, 30, 40, 50]

for valor in valores:
    print(f'O valor atual é: {valor}')

#13 EXEMPLO COM WHILE:
x = 0

while x < 10:
    print(f'x é atualmente: {x}')
    x += 1

#14 EXEMPLO COMPLEXO COM WHILE:
numero = 1

while numero <= 5:
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
    numero += 1

#15 CODIGO COM DEF:
def diga_ola():
    print('Olá!')

diga_ola()

#16 ARGUMENTO DE RETORNO:
def saudar(nome):
    return f'Olá, {nome}!'

mensagem = saudar('Asimov')
print(mensagem)

#17 CODIGO COM LAMBDA:
soma = lambda x, y: x + y

resultado = soma(3, 5)
print(resultado)

#18 LAMBDA COM FILTER:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

#19 LEITURA DE ARQUIVOS:
import os

with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#20 SALVAR ARQUIVOS:
with open('saida.txt', 'w') as arquivo:
    arquivo.write('Este é um exemplo de escrita em arquivo.\n')
    arquivo.write('Python facilita a manipulação de arquivos!')

#21 EXEMPLO DE CRIAÇÃO DE GRÁFICO:
import matplotlib.pyplot as plt
from random import sample

x = sample(range(1, 1000), 100)
y = sample(range(1, 1000), 100)

plt.scatter(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')
plt.show()

#22 GRÁFICO DE DISPERSÃO (HISTOGRAMA):
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.75, color='blue')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.show()

#23 EXEMPLO BOXPLOT:
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)
plt.xlabel('Grupo')
plt.ylabel('Valor')
plt.title('Box Plot')
plt.show()

#24 EXEMPLO COM PLOTLY:
import plotly.graph_objects as go
import numpy as np

t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(data=go.Scatter(x=t, y=y, mode='lines', name='Seno'))
fig.update_layout(title='Gráfico de Linhas', xaxis_title='Tempo', yaxis_title='Amplitude')
fig.show()

#25 GRÁFICO DE BARRAS:
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valor': [4, 7, 1, 8]
})

fig = px.bar(df, x='Categoria', y='Valor', title='Gráfico de Barras')
fig.show()

#26 GRÁFICO DE PIZZA:
import plotly.graph_objects as go

labels = ['Oxigênio', 'Hidrogênio', 'Gás Carbônico', 'Nitrogênio']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title='Gráfico de Pizza')
fig.show()

#27 CALCULADORA DE IMC:
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

#28 VERIFICADOR DE NÚMEROS PRIMOS:
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))

if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

#29 CONTADOR DE PALAVRAS:
from collections import Counter

def contar_palavras(texto):
    palavras = texto.lower().split()
    contagem = Counter(palavras)
    return contagem

texto = input("Digite um texto: ")

contagem = contar_palavras(texto)

for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")

#30 CALCULADORA DE DESCONTO:
def calcular_desconto(preco, desconto):
    valor_final = preco - (preco * (desconto / 100))
    return valor_final

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_final = calcular_desconto(preco, desconto)
print(f"O valor final com desconto é: R${valor_final:.2f}")