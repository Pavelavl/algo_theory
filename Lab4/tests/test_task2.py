from src.task2 import note_list_generator, parallel_note_matrix
import time

def test_parallel_note_matrix():
    """Проверка многопоточной генерации матрицы нот на корректность размеров и значений."""
    matrix = parallel_note_matrix(size=10)
    
    assert len(matrix) == 10, "Матрица должна быть размером 10x10"
    for row in matrix:
        assert len(row) == 10, "Каждая строка матрицы должна содержать 10 элементов"
        for note in row:
            assert note in ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'], "Каждая нота должна быть из списка нот"

def test_performance_improvement_task2():
    """Сравнение производительности обычной и многопоточной версий генерации нот."""
    import time

    start_time = time.time()
    list(note_list_generator(n=1000))
    m1 = single_thread_time = time.time() - start_time
    print(f"Single-threaded time for task2: {single_thread_time}")

    start_time = time.time()
    parallel_note_matrix(size=1000)
    m2 = multi_thread_time = time.time() - start_time
    print(f"Multi-threaded time for task2: {multi_thread_time}")

    assert multi_thread_time < single_thread_time, "Ожидается, что многопоточная версия будет быстрее"
