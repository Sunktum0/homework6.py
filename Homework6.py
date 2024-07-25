my_dict = {'Татьяна': 1999, 'Владислав': 1999, 'Роман': 2023}
print(my_dict)
print(my_dict.get('Роман'))
print(my_dict.get('Ева'))
print((my_dict.get('Ева', 'Такого ключа не существует')))
my_dict.update({'Никита': 2005, 'Елизавета': 2006})
print(my_dict)
print(my_dict.pop('Никита'))
my_set = {0, 1, 2, 2, 3, 4, 4, True, False, False, 'VLAD', 'VLAD', 'TANYA'}
print(my_set)
my_set.update((5,6))
my_set.discard(2)
print(my_set)
