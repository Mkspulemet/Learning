
try:
    numbers_file = open('numbers.txt', 'r')
    for i_line in numbers_file:
        print(i_line, end='')
    numbers_file.close()
except FileNotFoundError:
    print('Такого файла не существует')