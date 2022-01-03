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
'''b = 'quantity'
a = {
    ('quantity', 'price'): 510,
    ('jhgf', 'pri'): 520
}
for i in a.keys():
    if b == i[0]:
        print('OK')
    print(i[0])
print(list(a.items())[0][0][0])'''

'''import random


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0


current_speed_1 = Toyota()
current_speed_2 = Toyota()
current_speed_3 = Toyota()
current_speed_1.current_speed = random.randint(0, 200)
current_speed_2.current_speed = random.randint(0, 200)
current_speed_3.current_speed = random.randint(0, 200)
print(current_speed_1.current_speed)
print(current_speed_2.current_speed)
print(current_speed_3.current_speed)'''

'''class Monitors:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 60

class Headphones:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = True


monitor_freq_1 = Monitors()
monitor_freq_2 = Monitors()
monitor_freq_3 = Monitors()
monitor_freq_4 = Monitors()

monitor_freq_2.monitor_freq = 144
monitor_freq_3.monitor_freq = 70

headphones_micro_1 = Headphones()
headphones_micro_2 = Headphones()
headphones_micro_3 = Headphones()

headphones_micro_1.headphones_micro = False

print(monitor_freq_1.monitor_freq)
print(monitor_freq_2.monitor_freq)
print(monitor_freq_3.monitor_freq)
print(monitor_freq_4.monitor_freq)
print()
print(headphones_micro_1.headphones_micro)
print(headphones_micro_2.headphones_micro)
print(headphones_micro_3.headphones_micro)'''


'''class Car:
    model = 'Peugeot'
    engine = 2.0'''


'''class User:
    user_name = 'Admin'
    password = 'qwerty'
    is_banned = False
    friends = []


    def print_info(self):
        print(
            'Name: {}\nPassword: {}\nBan_dtatus: {}'.format(
                self.user_name, self.password, self.is_banned)
        )


    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.user_name)
        else:
            self.friends.append(friend)



user_1 = User()
user_2 = User()
user_2.user_name = 'Alina'
user_1.add_friend('Bob')
user_1.add_friend(user_2)
print(user_1.friends)'''


'''class Family:
    surname = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            'Family name: {}\nFamily founds: {}\nhaving a house: {}\n'.format(
                self.surname, self.money, self.have_a_house
            )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current value'.format(amount, self.money))


    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money>= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}\n'.format(self.money))
        else:
            print('Not enough money\n')

my_family = Family()
my_family.info()

print('Try to buy a house')
my_family.buy_house(10 ** 6)

if not my_family.have_a_house:
    my_family.earn_money(800000)
    print('Try to buy a house again')
    my_family.buy_house(10 ** 6, 10)

my_family.info()'''

'''import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        print('Создан воин {} со здоровьем {}'.format(self.name, self.health))

    def strike(self, enemyWarrior):
        if True:
            print('Воин {} нанес урон -20 воину {}'.format(self.name, enemyWarrior.name))
            enemyWarrior.setHealth(enemyWarrior.getHealth() - 20)

    def setHealth(self, health):
        self.health = health
        print('Установленно здоровье {} для воина {}'.format(self.health, self.name))

    def getHealth(self):
        try:
            return self.health
            print('Здоровье воина {} — {}'.format(self.name, self.health))
        except:
            return 'Здоровье не заданно'
            print('Здоровье для воина {} не заданно'.format(self.name))


one = Warrior('Георгий', 100)
two = Warrior('Луиза', 100)

while (one.health > 0) and (two.health > 0):
    round = random.randint(1, 2)

    if round == 1:
        one.strike(two)
    elif round == 2:
        two.strike(one)

if round == 1:
    name = one.name
    enemy_name = two.name
elif round == 2:
    name = two.name
    enemy_name = one.name

print('Поздравляем воина {}! Он одержал победу над воином {}'.format(name, enemy_name))'''

