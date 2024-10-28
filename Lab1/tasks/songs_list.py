#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

target_songs = ['Halo', 'Enjoy the Silence', 'Clean']

def total_songs_time_list(song_list: list, songs: [str]):
    song_map = {song[0]: song[1] for song in song_list}
    time = 0
    for i in songs:
        time += song_map[i]
    return time

time1 = total_songs_time_list(violator_songs_list, target_songs)

print(f"total time for {len(target_songs)} songs - {time1:.2f} min")

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

def total_songs_time_dict(song_dict: dict, songs: []):
    time = 0
    for i in songs:
        time+=song_dict[i]
    return time

target_songs2 = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']

time2 = total_songs_time_dict(violator_songs_dict, target_songs2)
print(f"other {len(target_songs2)} songs total time - {round(time2)} min")