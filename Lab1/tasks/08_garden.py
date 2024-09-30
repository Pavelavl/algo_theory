#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
def set_from_tuple(your_tuple: tuple):
    return set(your_tuple)

garden_set = set_from_tuple(garden)
meadow_set = set_from_tuple(meadow)

# выведите на консоль все виды цветов

def union(set1: set, set2:set):
    return set1.union(set2)

all_flowers = union(garden_set, meadow_set)

print(", ".join(all_flowers))

# выведите на консоль те, которые растут и там и там

def get_similar_elem_from_set(set1:set, set2:set):
    return set1 & set2

gm_flowers = get_similar_elem_from_set(garden_set, meadow_set)

print(", ".join(gm_flowers))

# выведите на консоль те, которые растут в саду, но не растут на лугу

def get_unique_set_elem(set1: set, set2: set):
    return set1 - set2

u_garden_flowers = get_unique_set_elem(garden_set,meadow_set)

print(", ".join(u_garden_flowers))

# выведите на консоль те, которые растут на лугу, но не растут в саду

u_meadow_flowers = get_unique_set_elem(meadow_set, garden_set)

print(", ".join(u_meadow_flowers))
