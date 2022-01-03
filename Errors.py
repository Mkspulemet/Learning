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

'''def devide(number):
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
    print(answer_file.closed)'''

'''BRUCE_WILLIS = 42



input_data = input('Введите строку: ')

leeloo = int(input_data[4])

result = BRUCE_WILLIS * leeloo

print(f'- Leeloo Dallas! Multi-pass № {result}!')'''


'''sym_sum = 0
line_count = 0
try:
    people_file = open('people.txt', 'r')
    for i_line in people_file:
        line_count += 1
        lenght = len(i_line)
        if i_line.endswith('\n'):
            lenght -= 1
        if lenght < 3:
            raise BaseException('Длина {} строки меньше 3 символов'.format(line_count))
        sym_sum += lenght
    people_file.close()
except FileNotFoundError:
    print('Файл не найден.')
finally:
    print('Найденная сумма символов: ', sym_sum)'''

'''names_list = []

while True:
    try:
        name = input('Введите имя: ')
        if name == 'error':
            raise BaseException('Ты сломал программу')
        if not name.isalpha():
            raise TypeError
        names_list.append(name)
        if len(names_list) == 5:
            print('Место закончилось')
            break
    except TypeError:
        print('Ты чего ввел?')
    except BaseException:
        names_list = []
        print('Введено стоп-слово')
        raise TypeError('Не вводите стоп-слово')'''

'''good_log = open('registrations_good.log', 'w')
bad_log = open('registrations_bad.log', 'w')
file = open('registrations.txt', 'r', encoding='utf-8')
for i_line in file.readlines():
    try:
        new_line = i_line.split()
        index = name = syntax = value = False
        if len(new_line) == 3:
            index = True
        if 10 < int(new_line[2]) < 99:
            syntax = True
        if new_line[0].isalpha() is True:
            name = True
        if '@' and '.' in new_line[1]:
            syntax = True
    except IndexError:
        print('НЕ присутствуют все три поля: IndexError')
    except ValueError:
        print('поле возраст НЕ является числом от 10 до 99: ValueError')
    except NameError:
        print('поле имени содержит НЕ только буквы: NameError')
    except SyntaxError:
        print('поле емейл НЕ содержит @ и .(точку): SyntaxError')'''


class Add():
    def __init__(self, argument):
        self.argument = argument

    def __add__(self, other):
        return other + self.argument
z = Add(' water ')
x = Add(' fire ')
t = z + x
print(t)

