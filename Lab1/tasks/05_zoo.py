#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
def new_animal(zoo: list, index: int, animal: str):
    zoo.insert(index, animal)
    return zoo

print(new_animal(zoo, 1, 'bear'))

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

def new_animals(zoo: list, animals: list):
    zoo.extend(animals)
    return zoo

print(new_animals(zoo, birds))

# уберите слона
#  и выведите список на консоль

def kill_the_beast(zoo: list, animal: str):
    zoo.remove(animal)
    return zoo

print(kill_the_beast(zoo, 'elephant'))

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

def get_animal_index_pretty(zoo: list, animal:str):
    return zoo.index(animal) + 1

ultra_zoo = ['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']
print(get_animal_index_pretty(ultra_zoo, 'lion') , get_animal_index_pretty(ultra_zoo, 'lark'))

def solve():
    print(new_animal(['lion', 'kangaroo', 'elephant', 'monkey', ], 1, 'bear'))
    print(new_animals(['lion', 'kangaroo', 'elephant', 'monkey', ], ['rooster', 'ostrich', 'lark', ]))
    print(free_the_beast(['lion', 'kangaroo', 'elephant', 'monkey', ], 'elephant'))
    print(get_animal_index_pretty(ultra_zoo, 'lion'), get_animal_index_pretty(ultra_zoo, 'lark'))
