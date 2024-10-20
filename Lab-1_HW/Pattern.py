LENGHT = 9
center = LENGHT // 2
centers_2 = LENGHT // 4
line = "  " * LENGHT


def draw_pattern(x, y):
    color = input('Введите цвет узора (от 0 до 255 включительно): ')
    SET_COLOR = "\x1b[48;5;" + str(color) + 'm'
    END = "\x1b[0m"


    for i in range(y):
        if i < 1:
            print(f'{SET_COLOR}{line * x}{END}')
        print(f'{"  " * center}{SET_COLOR}{"  "}{END}{"  " * center}' * x)
        print(f'{SET_COLOR}{line * x}{END}')
        print(f'{"  " * centers_2}{SET_COLOR}{"  "}{END}{"  " * (centers_2 + 1)}{SET_COLOR}{"  "}{END}{"  " * centers_2}' * x)
        print(f'{SET_COLOR}{line * x}{END}')
    return ''



x = int(input('Введите количество повторений узора по горизонтали: '))
y = int(input('Введите количество повторений узора по вертикали: '))


if __name__ == "__main__":
    print(draw_pattern(x, y))
