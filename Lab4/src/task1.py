from multiprocessing import Pool
import random
from typing import List, Tuple, Generator

def rectangle_area_generator(length_range=(200, 10000), width_range=(500, 100000), count=100) -> Generator[int, None, None]:
    """Обычный генератор площадей прямоугольников."""
    for _ in range(count):
        try:
            length = random.randint(*length_range)
            width = random.randint(*width_range)
            yield length * width
        except Exception as e:
            print(f"Ошибка при расчете площади: {e}")
            continue

def calculate_area(args: Tuple[int, int]) -> int:
    """Функция для вычисления площади одного прямоугольника."""
    length_range, width_range = args
    length = random.randint(*length_range)
    width = random.randint(*width_range)
    return length * width

def parallel_rectangle_area_generator(count=100, length_range=(200, 10000), width_range=(500, 100000)) -> List[int]:
    """Параллельная версия генератора площадей прямоугольников с использованием multiprocessing.Pool."""
    with Pool() as pool:
        # Создаем список аргументов для каждого вызова calculate_area
        args = [(length_range, width_range) for _ in range(count)]
        # Параллельно вычисляем площади
        areas = pool.map(calculate_area, args)
    return areas
