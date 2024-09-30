#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_distance():
    distances = {}
    for i in sites:
        distances[i] = {}
        for j in sites:
            if i != j:
                x1, y1 = sites[i]
                x2, y2 = sites[j]

                distance = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
                distances[i][j] = distance
    return distances

distances = get_distance()

print(distances)
