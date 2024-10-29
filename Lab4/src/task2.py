from multiprocessing import Pool
import random
from typing import Generator, List

NOTES = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

def note_list_generator(n: int, notes: List[str] = None) -> Generator[List[str], None, None]:
    """Обычный генератор для создания списка случайных нот длиной n."""
    notes = notes or NOTES
    for _ in range(n):
        yield [random.choice(notes) for _ in range(n)]

def generate_note_row(size: int) -> List[str]:
    """Генерирует одну строку случайных нот."""
    return [random.choice(NOTES) for _ in range(size)]

def parallel_note_matrix(size: int = 10) -> List[List[str]]:
    """Параллельная версия для создания матрицы случайных нот с использованием multiprocessing.Pool."""
    with Pool() as pool:
        # Генерируем строки параллельно
        matrix = pool.map(generate_note_row, [size] * size)
    return matrix
