from typing import List

def quicksort(arr: List[int]) -> List[int]:
    """
    Сортирует массив с помощью быстрой сортировки.
    Временная сложность: O(n log n) в среднем, O(n^2) в худшем случае.
    Возвращает отсортированный массив.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)