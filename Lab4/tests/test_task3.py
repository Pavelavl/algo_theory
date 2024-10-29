import pytest
from src.task3 import find_common_even_values, find_common_even_values_parallel
import time

def test_find_common_even_values():
    """Проверка функции на корректное нахождение общих четных значений."""
    coins1 = "2 4 6 8 10"
    coins2 = "4 6 12 14 16"
    result = find_common_even_values(coins1, coins2)
    
    assert result == [4, 6], "Ожидается список [4, 6] для общих четных значений"

def test_no_common_values():
    """Проверка случая, когда нет общих значений."""
    coins1 = "1 3 5 7"
    coins2 = "2 4 6 8"
    result = find_common_even_values(coins1, coins2)
    
    assert result == [], "Ожидается пустой список, так как общих четных значений нет"

def test_empty_input():
    """Проверка обработки пустого ввода."""
    coins1 = ""
    coins2 = ""
    result = find_common_even_values(coins1, coins2)
    
    assert result == [], "Ожидается пустой список при пустых входных данных"

def test_invalid_input():
    """Проверка обработки некорректного ввода (нечисловые значения)."""
    coins1 = "2 a 4 6"
    coins2 = "4 6 8 b"
    result = find_common_even_values(coins1, coins2)
    
    assert result == [], "Ожидается пустой список при некорректных входных данных"

def test_find_common_even_values_parallel():
    """Проверка многопоточной версии на корректное нахождение общих четных значений."""
    coins1 = "2 4 6 8 10"
    coins2 = "4 6 12 14 16"
    result = find_common_even_values_parallel(coins1, coins2)
    
    assert result == [4, 6], "Ожидается список [4, 6] для общих четных значений"

def test_performance_improvement_task3():
    """Сравнение производительности обычной и многопоточной версий функции."""
    
    coins1 = " ".join(map(str, range(10000000)))
    coins2 = " ".join(map(str, range(500, 15000000)))

    start_time = time.time()
    res1 = find_common_even_values(coins1, coins2)
    single_thread_time = time.time() - start_time
    print(f"Single-threaded time for task3: {single_thread_time}")

    start_time = time.time()
    res2 = find_common_even_values_parallel(coins1, coins2)
    multi_thread_time = time.time() - start_time
    print(f"Multi-threaded time for task3: {multi_thread_time}")

    assert multi_thread_time < single_thread_time, "Ожидается, что многопоточная версия будет быстрее"

