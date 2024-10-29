from concurrent.futures import ProcessPoolExecutor
from typing import List, Set

def find_common_even_values(coins1: str, coins2: str) -> list:
    """
    Обычная версия поиска общих четных значений в двух строках номиналов монет.
    """
    try:
        set1 = set(map(int, coins1.split()))
        set2 = set(map(int, coins2.split()))
        common_even_values = list(filter(lambda x: x % 2 == 0, set1 & set2))
        return common_even_values
    except ValueError:
        print("Ошибка: Входные данные должны содержать только целые числа.")
        return []

def filter_even_numbers_from_string(coins: str) -> Set[int]:
    """Преобразует строку номиналов в множество четных чисел."""
    return {int(x) for x in coins.split() if int(x) % 2 == 0}

def find_common_even_values_parallel(coins1: str, coins2: str) -> Set[int]:
    """Оптимизированная параллельная версия поиска общих четных значений в двух строках номиналов."""
    with ProcessPoolExecutor() as executor:
        # Параллельно обрабатываем строки, чтобы сразу получить множества четных чисел
        even_set1, even_set2 = executor.map(filter_even_numbers_from_string, [coins1, coins2])

    # Находим пересечение двух множеств четных чисел
    common_even_values = even_set1 & even_set2
    return list(common_even_values)
