'''phonebook_dict = {
    'Ваня': 88006663636,
    'Петя': 88006633869,
    'Лена': 88006635891
}
name = input('Введите имя: ')
if name in phonebook_dict:
    print(phonebook_dict[name])
else:
    print('Ошибка: человек с именем {0} не найден'.format(name))'''

'''student_str = input(
    'Введите информацию о студенте через пробел\n'
    '(имя, фамилия, город, место учебы, оценки):'
)
student_info = student_str.split()
student = dict()
student['Имя'] = student_info[0]
student['Фамилия'] = student_info[1]
student['Город'] = student_info[2]
student['Место учебы'] = student_info[3]
student['Оценки'] = []
for i_grade in student_info[4:]:
    student['Оценки'].append(int(i_grade))
for i in student:
    print(i, '-', student[i])'''


'''num = int(input('Введите число: '))
dictt = {i: i**2 for i in range(1, num+1)}
print(dictt)'''

'''count = 0
contacts = dict()
while count < 10:
    print('Текущие контакты на телефоне:')
    for i in contacts:
        print(i, '-', contacts[i])
    contacts[input('Введите имя: ' )] = int(input('Введите номер телефона: '))
    count += 1'''

'''count = 0
contacts = dict()
while count < 10:
    print('Текущие контакты на телефоне:')
    for i in contacts:
        print(i, '-', contacts[i])
    k = input('Введите имя: ')
    if k in contacts:
        print('Ошибка: такое имя уже существует.')
        continue
    v = input('Введите номер телефона: ')
    contacts[k] = v
    count += 1'''


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

print('\nОригинальный словарь частот:')
for i_sym in hist.keys():
    print(i_sym, ':', hist[i_sym])'''


'''my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]
print(type(my_list))
reg_dict = {}
for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]

print(reg_dict)'''

'''import collections
inv_original = {}
text = input('Введите текст: ')
print(collections.Counter(text).items())
for k, v in collections.Counter(text).items():
    print(k, v)
    inv_original.setdefault(v, []).append(k)
for i in inv_original:
    print(i, ':', inv_original[i])'''


'''a = input()
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
for i in sorted(d):
    print(i, ':', d[i])'''


'''nums = int(input('Введите количество заказов: '))
orders = dict()
for i in range(nums):
    v = input(f' {i + 1} заказ: ').split()
    customer = v[0]
    pizza_name = v[1]
    count = v[2]
    if customer not in orders:
        orders[customer] = {pizza_name: int(count)}
    else:
        if pizza_name in orders[customer]:
            orders[customer][pizza_name] += int(count)
        else:
            orders[customer].update({pizza_name: int(count)})
print(orders)
for i_customer in orders.keys():
    print('{}:'.format(i_customer))
    for j_pizza in orders[i_customer].keys():
        print('\t\t{}: {}'.format(j_pizza, orders[i_customer][j_pizza]))'''

'''n = int(input('Введите максимальное число: '))
a = set(range(1, n+1))
for x in iter(lambda: input('Нужное число есть среди вот этих чисел: '), 'Помогите!'):
    b = set(map(int, x.split()))
    if input('Ответ Артёма: ') == 'Да':
        a &= b
    else:
        a -= b
print(*a)'''

'''let = list(input('Введите строку: '))
for i in range(len(let)):
    let.insert(-1, let.pop(0))
    print(let)'''
b = 'quantity'
a = {
    ('quantity', 'price'): 510,
    ('jhgf', 'pri'): 520
}
for i in a.keys():
    if b == i[0]:
        print('OK')
    print(i[0])
print(list(a.items())[0][0][0])