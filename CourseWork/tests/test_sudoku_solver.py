import pytest
from algo.sudoku_solver import find_empty, is_valid, solve_sudoku

# Тестовые доски для 9x9
@pytest.fixture
def empty_board_9x9():
    """Пустая доска 9x9"""
    return [[0 for _ in range(9)] for _ in range(9)]

@pytest.fixture
def partial_board_9x9():
    """Частично заполненная доска 9x9"""
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

@pytest.fixture
def invalid_board_9x9():
    """Нерешаемая доска 9x9"""
    return [
        [5, 5, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

# Тестовые доски для 4x4
@pytest.fixture
def empty_board_4x4():
    """Пустая доска 4x4"""
    return [[0 for _ in range(4)] for _ in range(4)]

@pytest.fixture
def partial_board_4x4():
    """Частично заполненная доска 4x4"""
    return [
        [1, 0, 0, 4],
        [0, 2, 0, 0],
        [0, 0, 4, 0],
        [3, 0, 0, 2]
    ]

@pytest.fixture
def invalid_board_4x4():
    """Нерешаемая доска 4x4"""
    return [
        [1, 1, 0, 4],
        [0, 2, 1, 0],
        [0, 1, 4, 0],
        [4, 0, 0, 2]
    ]

# Тесты для find_empty
def test_find_empty_in_empty_board_9x9(empty_board_9x9):
    assert find_empty(empty_board_9x9, size=9) == (0, 0), "Должна быть найдена первая пустая клетка в 9x9"

def test_find_empty_in_partial_board_9x9(partial_board_9x9):
    assert find_empty(partial_board_9x9, size=9) == (0, 2), "Должна быть найдена первая пустая клетка (0, 2) в 9x9"

def test_find_empty_in_full_board_9x9():
    full_board = [[1 for _ in range(9)] for _ in range(9)]
    assert find_empty(full_board, size=9) is None, "Не должно быть пустых клеток в 9x9"

def test_find_empty_in_empty_board_4x4(empty_board_4x4):
    assert find_empty(empty_board_4x4, size=4) == (0, 0), "Должна быть найдена первая пустая клетка в 4x4"

def test_find_empty_in_partial_board_4x4(partial_board_4x4):
    assert find_empty(partial_board_4x4, size=4) == (0, 1), "Должна быть найдена первая пустая клетка (0, 1) в 4x4"

def test_find_empty_in_full_board_4x4():
    full_board = [[1 for _ in range(4)] for _ in range(4)]
    assert find_empty(full_board, size=4) is None, "Не должно быть пустых клеток в 4x4"

# Тесты для is_valid
def test_is_valid_row_conflict_9x9(partial_board_9x9):
    assert not is_valid(partial_board_9x9, 5, (0, 2), size=9), "5 уже есть в строке в 9x9"

def test_is_valid_col_conflict_9x9(partial_board_9x9):
    assert not is_valid(partial_board_9x9, 6, (2, 0), size=9), "6 уже есть в столбце в 9x9"

def test_is_valid_box_conflict_9x9(partial_board_9x9):
    assert not is_valid(partial_board_9x9, 8, (1, 1), size=9), "8 уже есть в квадрате 3x3 в 9x9"

def test_is_valid_valid_move_9x9(partial_board_9x9):
    assert is_valid(partial_board_9x9, 2, (0, 2), size=9), "2 можно поставить в (0, 2) в 9x9"

def test_is_valid_row_conflict_4x4(partial_board_4x4):
    assert not is_valid(partial_board_4x4, 1, (0, 1), size=4), "1 уже есть в строке в 4x4"

def test_is_valid_col_conflict_4x4(partial_board_4x4):
    assert not is_valid(partial_board_4x4, 2, (0, 1), size=4), "2 уже есть в столбце в 4x4"

def test_is_valid_box_conflict_4x4(partial_board_4x4):
    assert not is_valid(partial_board_4x4, 1, (2, 0), size=4), "1 уже есть в квадрате 2x2 в 4x4"

def test_is_valid_valid_move_4x4(partial_board_4x4):
    assert is_valid(partial_board_4x4, 3, (0, 1), size=4), "3 можно поставить в (0, 1) в 4x4"

# Тесты для solve_sudoku
def test_solve_sudoku_solvable_9x9(partial_board_9x9):
    original = [row[:] for row in partial_board_9x9]
    assert solve_sudoku(partial_board_9x9, size=9), "Доска 9x9 должна быть решена"
    assert find_empty(partial_board_9x9, size=9) is None, "Все клетки должны быть заполнены в 9x9"
    for i in range(9):
        for j in range(9):
            if original[i][j] != 0:
                assert partial_board_9x9[i][j] == original[i][j], "Исходные значения не должны измениться в 9x9"

def test_solve_sudoku_unsolvable_9x9(invalid_board_9x9):
    assert not solve_sudoku(invalid_board_9x9, size=9), "Нерешаемая доска 9x9 не должна быть решена"

def test_solve_sudoku_solvable_4x4(partial_board_4x4):
    original = [row[:] for row in partial_board_4x4]
    result = solve_sudoku(partial_board_4x4, size=4)
    print("Result:", result)
    print("Board after solving:", partial_board_4x4)
    assert result, "Доска 4x4 должна быть решена"
    assert find_empty(partial_board_4x4, size=4) is None, "Все клетки должны быть заполнены в 4x4"
    for i in range(4):
        for j in range(4):
            if original[i][j] != 0:
                assert partial_board_4x4[i][j] == original[i][j], "Исходные значения не должны измениться в 4x4"

def test_solve_sudoku_unsolvable_4x4(invalid_board_4x4):
    assert not solve_sudoku(invalid_board_4x4, size=4), "Нерешаемая доска 4x4 не должна быть решена"

if __name__ == "__main__":
    pytest.main(["-v"])