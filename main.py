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


num = int(input('Введите число: '))
dictt = {i: i**2 for i in range(1, num+1)}
print(dictt)