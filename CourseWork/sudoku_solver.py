def find_empty(board, size=9):
    """
    Находит пустую клетку (со значением 0) в судоку.
    Возвращает кортеж (row, col) или None, если пустых нет.
    Временная сложность: O(n^2), где n - размер доски (4 или 9).
    """
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos, size=9):
    """
    Проверяет, можно ли поставить число num в позицию pos (row, col).
    Временная сложность: O(n), где n - размер доски (4 или 9).
    """
    # Проверка строки
    for j in range(size):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    
    # Проверка столбца
    for i in range(size):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Проверка квадрата (2x2 для 4x4, 3x3 для 9x9)
    block_size = 2 if size == 4 else 3
    box_x = (pos[1] // block_size) * block_size
    box_y = (pos[0] // block_size) * block_size
    for i in range(box_y, box_y + block_size):
        for j in range(box_x, box_x + block_size):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve_sudoku(board, size=9):
    """
    Решает судоку с помощью алгоритма возврата (backtracking).
    Временная сложность: O(size^(size*size)) в худшем случае,
    но для фиксированного размера доски это полиномиально ограничено.
    """
    empty = find_empty(board, size)
    if not empty:
        return True  # Все клетки заполнены, решение найдено
    
    row, col = empty
    
    # Диапазон чисел: 1-4 для 4x4, 1-9 для 9x9
    for num in range(1, size + 1):
        if is_valid(board, num, (row, col), size):
            board[row][col] = num
            
            if solve_sudoku(board, size):
                return True
            
            board[row][col] = 0
    
    return False