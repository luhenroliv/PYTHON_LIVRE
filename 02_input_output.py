#Version1
print("What's your name?")
name = input()
print('Welcome %s' % name  )
print("How old are you?")
old = input()
print('%s is %s years old' % (name, old   ))

#Version2
print("What's your name?")
name = input()
print('Welcome {0}'.format(name))
print("How old are you?")
old = input()
print('{0} is {1} years old'.format(name, old))

#Version3
print("What's your name?")
name = input()
print(f'Welcome {name} ')
print("How old are you?")
old = input()
print(f'{name} is {old} years old')
print(f'{name} born in {2023 - int(old)}')

#Version4
name = input('What's your name ')
print(f'Welcome {name}')
old = input('How old are you? ')
print(f'{name} born in {2023 - int(old)}')