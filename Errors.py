'''nums_sum = 0
nums_count = 0
try:
    numbers_file = open('numbers.txt', 'r')
    for i_line in numbers_file:
        nums_count += 1
        nums_sum += int(i_line)
    numbers_file.close()
    print('Среднее фрифметическое: ', nums_sum/nums_count)
except FileNotFoundError:
    print('Такого файла не существует')
except TypeError:
    print('Это строка, а не число')
except ValueError:
    print('Нельзя!')'''

def devide(number):
    return 10 / number

def sum_of_devided(left, right):
    div_sum = 0
    for i_num in range(left, right +1):
        try:
            div_sum += devide(i_num)
            print(div_sum)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
    return div_sum

total = 0
try:
    numbers_file = open('numbers.txt', 'r')
    for i_line in numbers_file:
        num_list = i_line.split()
        first_num = int(num_list[0])
        second_num = int(num_list[1])
        total += sum_of_devided(first_num, second_num)
    print('Общая сумма: ', total)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
answer_file = open('answer.txt', 'w')
try:
    answer_file.write('The answer is: ')
    answer_file.write(str(total))
except TypeError:
    print('Ошибка записи в файлю Тип данных не строка.')
else:
    print('Программа выполнилась без ошибок')
finally:
    answer_file.close()
    print(answer_file.closed)

'''BRUCE_WILLIS = 42



input_data = input('Введите строку: ')

leeloo = int(input_data[4])

result = BRUCE_WILLIS * leeloo

print(f'- Leeloo Dallas! Multi-pass № {result}!')'''

