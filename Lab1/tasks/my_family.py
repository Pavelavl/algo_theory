#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
# (нету)

my_family = [
]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['mother', 170],
    ['dad', 175],
    ['me', 185]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

dad_key = 'dad'

def get_father_height(my_family_h):
    for person in my_family_height:
        if person[0] == dad_key:
            return f"dad's height - {person[1]} sm"
    return "no dad"

print(get_father_height(my_family_height))

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

def get_family_height(my_family_h):
    sum = 0
    for i in my_family_height:
        sum += i[1]
    return "total height - "+str(sum)+" sm"

print(get_family_height(my_family_height))

def solve():
    return get_father_height(my_family_height), get_family_height(my_family_height)