#Exemplos de programas básicos em Python:

#01 TIPO NÚMERO INTEIRO:
idade = 25
print(idade)  # Saída: 25

#02 TIPO FLUTUANTE:
numero_float = 3.7
numero_int = int(numero_float)  # Resultado será 3

#03 MATEMÁTICA COM INTEIROS:
a = 10
b = 3
# Adição, Subtração, Multiplicação e Divisão
print(a + b)  # Saída: 13
print(a - b)  # Saída: 7
print(a * b)  # Saída: 30
print(a / b)  # Saída: 3.3333

# Potência, Divisão Inteira, e Módulo
print(a ** b)  # Saída: 1000 (10^3)
print(a // b)  # Saída: 3 (Divisão inteira)
print(a % b)   # Saída: 1 (Resto da divisão)

#04 DADOS BOOLEANOS:
ativo = True
print(ativo)  # Saída: True

#05 LISTAS COM DADOS:
frutas = ["maçã", "banana", "cereja"]
frutas.append("laranja")
print(frutas)  # Saída: ['maçã', 'banana', 'cereja', 'laranja']

[x * 2 for x in original_list]  # Dobra os valores de uma lista existente.

#06 TUPLAS:
cores = ("vermelho", "verde", "azul")
print(cores)  # Saída: ('vermelho', 'verde', 'azul')

#07 EXEMPLO COM STRINGS:
# Usando aspas duplas
string2 = "Python é incrível!"

# Usando três aspas para multiline
string3 = """Esta é uma string
que ocupa várias linhas."""

#08 ACESSO E MANIPULAÇÃO:
texto = "Python"
primeiro_caractere = texto[0]  # 'P'
substring = texto[1:4]         # 'yth'

#09 FUNÇÕES COMUNS:
texto = " Olá, Mundo! "
print(len(texto))          # Saída: 13
print(texto.strip())       # Saída: 'Olá, Mundo!'
print(texto.lower())       # Saída: 'olá, mundo!'

#10 TIPOS DE MAPEAMENTO: DICIONÁRIOS:
{'nome': 'Alice', 'idade': 30}

aluno = {"nome": "João", "idade": 20}
print(aluno["nome"])  # Saída: João

#11 TIPOS DE CONJUNTOS:
meu_conjunto = {1, 2, 3}
#ou
meu_conjunto = set([1, 2, 3])

numeros = {1, 2, 3, 4, 5}
numeros.add(6)
print(numeros)  # Saída: {1, 2, 3, 4, 5, 6}

#12 TIPO ESPECIAL NONETYPE:
resultado = None
print(resultado)  # Saída: None