'''data = dict()
data['server'] = {
    "host": "127.0.0.1",
    "port": "10"
}
data['configuration'] = {
    "ssh": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
print(data)
print(data['server']['port'])
data['configuration']['ssh']['login'] = 'Vova'
print(data['configuration']['ssh']['login'])
print()
for i_value in data.values():
    for j_key in i_value:
        print(j_key, i_value[j_key])'''


'''data = dict()
#До этого что-то происходит
print(data.get('server'))
data['server'] = {
    "host": "127.0.0.1",
    "port": "10"
}

#До этого что-то происходит
if data.get('configuration', {}).get('ssh', {}).get('login', {}):
    print('В строке уже есть логин')
data['configuration'] = {
    "ssh": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
print(data)'''

'''plauers_dict = {
    1: {'name': 'Ваня', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Лена', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Толик', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Егор', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Максим', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Света', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Захар', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Виталик', 'team': 'C', 'status': 'Travel'}
}
team_a_members = [
    plauer['name']
    for plauer in plauers_dict.values()
    if plauer['team'] == 'A' and plauer['status'] == 'Rest'
]
print(team_a_members)'''

'''family_member = {
    'name': 'Jane',
    'surname': 'Doe',
    'hobbies': {'running', 'sky diving', 'singing'},
    'age': 35,
    'children': {
    1: {'name': 'Alice', 'age': 6},
    2: {'name': 'Bob', 'age': 6}}
}

name1 = family_member.get('children', {}).get(2, {}).get('name')
if name1 == 'Bob':
    print('Есть тако е имя')
print(family_member.get('children', {}).get(2, {}).get('name'))'''
