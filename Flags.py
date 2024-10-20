RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

x = int(input('Введите ширину флага: '))
y = int(input('Введите высоту флага: '))

for i in range(y):
    if i < y // 2:
        print(f'{WHITE}{"  " * x}{END}')
    else:
        print(f'{RED}{"  " * x}{END}')
