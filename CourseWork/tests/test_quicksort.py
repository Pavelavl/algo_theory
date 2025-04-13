import pytest
from algo.quicksort import quicksort

def test_quicksort_empty():
    assert quicksort([]) == [], "Пустой массив должен остаться пустым"

def test_quicksort_single():
    assert quicksort([1]) == [1], "Один элемент не должен измениться"

def test_quicksort_sorted():
    assert quicksort([1, 2, 3, 4]) == [1, 2, 3, 4], "Уже отсортированный массив"

def test_quicksort_reverse():
    assert quicksort([4, 3, 2, 1]) == [1, 2, 3, 4], "Обратно отсортированный массив"

def test_quicksort_duplicates():
    assert quicksort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3], "Массив с дубликатами"