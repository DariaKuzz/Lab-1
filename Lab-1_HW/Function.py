from math import sqrt
# y = x ^ 0,5


BLACK = '\u001b[30m'
color = input('Введите цвет графика (от 0 до 255 включительно): ')
SET_COLOR = "\x1b[48;5;" + str(color) + 'm'
END = '\u001b[0m'


def sqr(x, y):
    return sqrt(x) == int(sqrt(x)) and y == sqrt(x)


print(f'{SET_COLOR}График функции: y = x ^ 0,5{END}', end ='')


for y in range(1, 10)[::-1]:
    for x in range(1, 26):
        if x == 1:
            print((f'{'\n'}{y}| {SET_COLOR}{'  '}{END}') if sqr(x, y) else (f'{'\n'}{y}| {BLACK}{'  '}{END}'), end =' ')
        elif sqr(x, y):
            print(f'{SET_COLOR}{'  '}{END}', end =' ')
        else:
            print(f'{BLACK}{'  '}{END}', end =' ')


print('\n' + "-" * 77)
print(f'   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25')
