# Словари

my_dict = {'Masha': 1985,  # создание словаря
           'Dasha': 1990,
           'Misha': 2001,
           'Sveta': 1977,
           'Vovan': 2015 }
print(my_dict)
print(my_dict['Misha'])                           # вывод значения по существующему ключу
print(my_dict.get('Sonya', 'Такого имени нет'))   # вывод значкния по несуществующему
                                                               # ключу без ошибки

my_dict.update({'Anna': 2020,                     # добавление пар в словарь
               'Amir': 2000})
print(my_dict)
a = my_dict.pop('Sveta')                          # удаление ключа и вывод значения пары
print(a)
print(my_dict)


# Множества

my_set = {4, 6, 0, 'top', (9, 8, 7), 4 , 0} # создание множества
print(my_set)

print(my_set.discard('top'))                # удаление элемента из множества
print(my_set)

print(my_set.add(888))                      # добавление элементов во мноество
print(my_set)
