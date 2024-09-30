#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

def search_films(my_favorite_movies: str):
    pos = [-2]
    for i in range(len(my_favorite_movies)):
        if my_favorite_movies[i] == ',':
            pos.append(i)
    pos.append(len(my_favorite_movies))

    first = my_favorite_movies[:pos[1]]
    last = my_favorite_movies[pos[-2] + 2:]
    second = my_favorite_movies[pos[1] + 2:pos[2]]
    second_last = my_favorite_movies[pos[-3] + 2:pos[-2]]
    return f"{first}\n{last}\n{second}\n{second_last}"

def solve(): 
    return search_films(my_favorite_movies)
