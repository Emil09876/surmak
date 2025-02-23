number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
x = input('Выберите операцию( + , - , * , / ): ')

if x == '+':
    a = number_1 + number_2
    print(f'Результат {x} чисел {number_1},{number_2} равняется >>{a}<<')
elif x == '-':
    b = number_1 - number_2
    print(f'Результат {x} чисел {number_1},{number_2} равняется >>{b}<<')
elif x == '*':
    c = number_1 * number_2
    print(f'Результат {x} чисел {number_1},{number_2} равняется >>{c}<<')
else:
    d = number_1 / number_2
    print(f'Результат {x} чисел {number_1},{number_2} равняется >>{d}<<')
