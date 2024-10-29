import time
from src.task1 import rectangle_area_generator, parallel_rectangle_area_generator

def test_parallel_rectangle_area_generator():
    """Проверка многопоточного генератора площадей прямоугольников."""
    areas = parallel_rectangle_area_generator(count=100)
    
    assert len(areas) == 100, "Многопоточная версия должна вернуть 100 значений"
    for area in areas:
        assert isinstance(area, int) and area > 0, "Площадь должна быть положительным целым числом"

def test_performance_improvement_task1():
    """Сравнение производительности обычной и многопоточной версий генератора площадей."""
    start_time = time.time()
    list(rectangle_area_generator(count=10000000))
    single_thread_time = time.time() - start_time
    print(f"Single-threaded time for task1: {single_thread_time}")

    start_time = time.time()
    parallel_rectangle_area_generator(count=10000000)
    multi_thread_time = time.time() - start_time
    print(f"Multi-threaded time for task1: {multi_thread_time}")

    assert multi_thread_time < single_thread_time, "Ожидается, что многопоточная версия будет быстрее"
