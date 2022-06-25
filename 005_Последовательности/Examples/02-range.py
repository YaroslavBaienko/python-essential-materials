"""
Некоторые итерабельные объекты обладают определёнными общими свойствами.

Итерабельные объекты, которые поддерживают эффективный доступ к элементам
с использованием целочисленных индексов через специальный метод __getitem__()
и поддерживают метод __len__(), который возвращает количество элеметов,
называются последовательностями.

Уже были рассмотрены три типа данных, которые являются последовательностями.
"""

# Список
my_range = range(10)

# Итерирование
print('Iterating:')
for element in my_range:
    print(element)

print()

# Получение доступа к элементам при помощи целочисленных ключей (индексация)
print('Indexing:')
print(my_range[0])
print(my_range[2])
print(my_range[-1])

print()

# Длина последовательности
print('Length:', len(my_range))
