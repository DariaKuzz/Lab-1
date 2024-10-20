file = open('sequence.txt').read().strip()
list = [abs(float(i)) for i in file.split()]

BLUE = '\u001b[46m'
BLUE2 = '\u001b[44m'
END = '\u001b[0m'

first = list[:125]
sum1 = sum(first)
k1 = len(first)

second = list[125:]
sum2 = sum(second)
k2 = len(second)

sr1 = sum1 // k1
sr2 = sum2 // k2
sr = sr1 + sr2
pr1 = sr1 / sr
pr2 = sr2 / sr

if __name__ == "__main__":
    print(f'''{BLUE}Первые 125:{END}
    Среднее арифметическое по модулю = {sr1}. Процентное соотношение: {pr1}%

{BLUE2}Вторые 125:{END}
    Среднее арифметическое по модулю = {sr2}. Процентное соотношение: {pr2}%

    {pr1}% {BLUE}{' ' * int(round(pr1, 2) * 100)}{END}{BLUE2}{' ' * int(round(pr2, 2) * 100)}{END} {pr2}%
    ''')
