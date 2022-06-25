#!/usr/bin/env python
# Атрибуты-данные аналогичны полям в терминологии большинства
# распространённых языков программирования.
# Атрибуты-данные не нужно описывать: как и переменные,
# они создаются в момент первого присваивания.


# Класс, описывающий человека
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, 'is', self.age)



# Создание экземпляров класса

# alex = Person()
# alex.name = 'Alex'
# alex.age = 18

# john = Person()
# john.name = 'John'
# john.age = 20

# Атрибуты-данные относятся только к отдельным экземплярам класса
# и никак не влияют на значения соответствующих атрибутов-данных
# других экземпляров
# print(alex.name, 'is', alex.age)
# print(john.name, 'is', john.age)
john = Person('John', '28')
alice = Person('Alice', "32")

john.print_info()
alice.print_info()