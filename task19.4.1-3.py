'''import random
num_list = [random.randint(1, 4) for _ in range(1, 10)]
num_list1 = set(num_list)
print(num_list1)'''

'''signs = set(".,;:!?")
word = 'Я! Есть. Грут?! Я, Грут и Есть.'
print('Количество знаков пунктуации: ', len(signs.intersection(set(word))))'''

'''import  random
nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24,
          26, 3, 11, 2, 3, 16, 19, 21, 2, 3,
          8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5,
          21, 5, 19, 9, 12, 9, 15, 16, 29, 8,
          16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
nums1 = set(nums_1)
nums2 = set(nums_2)
print('Первое множество:', *nums1)
print('Второе множество:', *nums_2)
print()
print('Минимальный элемент 1-го множества: ', min(nums1))
print('Минимальный элемент 2-го множества: ', min(nums2))
nums1.discard(min(nums1))
nums2.discard(min(nums2))
print()
a = random.randint(100, 200)
b = random.randint(100, 200)
print('Случайное число для 1-го множества: ', a)
print('Случайное число для 2-го множества: ', b)
nums1.add(a)
nums2.add(b)
print()
print('Объединение множеств:', *nums1 | nums2)
print('Пересечение множеств:', *nums1 & nums2)
print('Элементы, входящие в nums_2, но не входящие в nums_1: ', *nums2 - nums1)'''