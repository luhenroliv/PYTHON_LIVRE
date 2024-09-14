#VERSION1
print("What's your name?")
name = input()
print('Welcome %s' % name  )
print("How old are you?")
old = input()
print('%s is %s years old' % (name, old   ))

#VERSION2
print("What's your name?")
name = input()
print('Welcome {0}'.format(name))
print("How old are you?")
old = input()
print('{0} is {1} years old'.format(name, old))

#VERSION3
print("What's your name?")
name = input()
print(f'Welcome {name} ')
print("How old are you?")
old = input()
print(f'{name} is {old} years old')
print(f'{name} born in {2024 - int(old)}')

#VERSION4
# Solicita o nome do usuário
name = input("What's your name? ")
print(f'Welcome {name}')

# Solicita a idade do usuário
old = input("How old are you? ")
try:
    # Calcula o ano de nascimento e exibe a mensagem
    year_of_birth = 2024 - int(old)
    print(f'{name} was born in {year_of_birth}')
except ValueError:
    # Trata o caso em que a idade fornecida não é um número
    print("Please enter a valid number for age.")
