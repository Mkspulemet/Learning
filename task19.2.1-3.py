'''def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

text = input('Введите текст: ').lower()
hist = histogram(text)
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

print('Максимальная частота: ', max(hist.values()))'''

'''phonebook = {
    'Ваня': 110,
    'Петя': 100,
    'Алиса': 200
}

other_phonebook = {
    'Игорь': 1000,
    'Петя': 800,
    'Алена': 350
}
phonebook.update(other_phonebook)
phonebook['Гоша'] = phonebook.pop('Игорь')
print(phonebook)
print(phonebook.get('Степан'))'''

#Поиск товара
'''small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}
big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)
print(big_storage)
while True:
    name = input('Введите наименование товара: ')
    if name not in big_storage:
        print('Ошибка, попробуйте еще раз')
    else:
        print(big_storage.get(name))
        break'''
#Магазин
'''incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
sorted(incomes)
print('Общий доход составил:', sum(incomes.values()))

print('Самый маленький доход у', min(incomes, key=incomes.get),
      'он составляет', min(incomes.values()))'''


#Гистограмма
def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

text = input('Введите текст: ')
hist = histogram(text)
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

print('Максимальная частота:', max(hist.values()))
