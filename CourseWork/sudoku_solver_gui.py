import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, QComboBox, QMessageBox, QFrame, QHBoxLayout
from PyQt5.QtCore import Qt
from sudoku_solver import solve_sudoku

class SudokuSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku Solver")
        self.size = 9
        self.block_size = 3
        self.cells = []
        self.separators = []  # Для хранения разделителей
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Основной layout с отступами
        self.layout = QGridLayout(self.central_widget)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(20, 20, 20, 20)
        
        # Общий стиль для приложения
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f7fa;
            }
            QLabel {
                font-family: 'Segoe UI', Arial, sans-serif;
                color: #333;
            }
        """)

        # Стилизация фона центрального виджета
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border-radius: 8px;
                padding: 15px;
            }
        """)

        # Создаем горизонтальный layout для верхней панели
        top_panel = QHBoxLayout()
        top_panel.setSpacing(10)
        
        # Выбор размера сетки
        self.size_label = QLabel("Размер сетки:")
        self.size_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #4a5568;
                padding: 5px 0;
            }
        """)
        top_panel.addWidget(self.size_label)
        
        self.size_combo = QComboBox()
        self.size_combo.addItems(["4x4", "9x9"])
        self.size_combo.setCurrentText("9x9")
        self.size_combo.currentTextChanged.connect(self.change_size)
        self.size_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #e2e8f0;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #ffffff;
                font-size: 14px;
                min-width: 100px;
                color: #2d3748;
            }
            QComboBox:hover { 
                border: 1px solid #cbd5e0; 
            }
            QComboBox::drop-down { 
                border-left: 1px solid #e2e8f0; 
                width: 30px;
            }
            QComboBox::down-arrow {
                image: url(none);
            }
        """)
        top_panel.addWidget(self.size_combo)
        
        # Добавляем растягивающийся разделитель
        top_panel.addStretch(1)
        
        # Кнопки управления
        button_style = """
            QPushButton {
                background-color: #4299e1;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 1px 3px;
                font-size: 14px;
                font-weight: 600;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QPushButton:hover { 
                background-color: #3182ce; 
            }
            QPushButton:pressed { 
                background-color: #2b6cb0; 
            }
            QPushButton:disabled {
                background-color: #a0aec0;
            }
        """
        
        self.solve_button = QPushButton("Решить")
        self.solve_button.clicked.connect(self.solve)
        self.solve_button.setStyleSheet(button_style)
        top_panel.addWidget(self.solve_button)

        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.setStyleSheet(button_style)
        top_panel.addWidget(self.clear_button)

        self.load_button = QPushButton("Загрузить пример")
        self.load_button.clicked.connect(self.load_example)
        self.load_button.setStyleSheet(button_style)
        top_panel.addWidget(self.load_button)
        
        # Добавляем верхнюю панель в основной layout
        self.layout.addLayout(top_panel, 0, 0, 1, self.size)

        # Создание сетки
        self.create_grid()

        # Индикатор состояния
        self.status_label = QLabel("Введите судоку и нажмите 'Решить'")
        self.status_label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                color: #718096;
                padding: 8px 0;
                font-style: italic;
            }
        """)
        self.layout.addWidget(self.status_label, self.size + 3, 0, 1, self.size)

        self.adjustSize()
        self.setMinimumSize(600, 600)  # Увеличил минимальную ширину для кнопок

    def create_grid(self):
        """Создаёт сетку с разделителями, имитирующими display: grid"""
        # Удаляем старую сетку и разделители
        for row in self.cells:
            for cell in row:
                self.layout.removeWidget(cell)
                cell.deleteLater()
        for sep in self.separators:
            self.layout.removeWidget(sep)
            sep.deleteLater()
        self.cells = [[QLineEdit() for _ in range(self.size)] for _ in range(self.size)]
        self.separators = []

        # Стиль для клеток
        cell_style = """
            QLineEdit {
                border: 1px solid #e2e8f0;
                background-color: #ffffff;
                font-size: 18px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: 500;
                color: #2d3748;
                padding: 0px;
                border-radius: 4px;
                qproperty-alignment: AlignCenter;
            }
            QLineEdit:hover { 
                border: 1px solid #bee3f8; 
                background-color: #f0f9ff;
            }
            QLineEdit:focus { 
                border: 2px solid #63b3ed; 
                background-color: #ebf8ff;
            }
            QLineEdit:disabled { 
                background-color: #edf2f7; 
                color: #4a5568;
                font-weight: 600;
            }
        """

        # Заполнение сетки клетками
        for i in range(self.size):
            for j in range(self.size):
                cell = self.cells[i][j]
                cell.setFixedSize(45, 45)
                cell.setAlignment(Qt.AlignCenter)
                cell.setMaxLength(1)
                cell.setStyleSheet(cell_style)
                # Учитываем сдвиг для разделителей
                row = i + i // self.block_size
                col = j + j // self.block_size
                self.layout.addWidget(cell, row + 1, col)

        # Добавление разделителей (горизонтальные и вертикальные линии)
        sep_style = """
            background-color: #cbd5e0;
            border: none;
        """
        for i in range(1, self.size // self.block_size):
            # Горизонтальные линии
            h_sep = QFrame()
            h_sep.setFixedHeight(3)
            h_sep.setStyleSheet(sep_style)
            self.layout.addWidget(h_sep, i * (self.block_size + 1), 0, 1, 
                                 self.size + (self.size // self.block_size) - 1)
            self.separators.append(h_sep)
            # Вертикальные линии
            v_sep = QFrame()
            v_sep.setFixedWidth(3)
            v_sep.setStyleSheet(sep_style)
            self.layout.addWidget(v_sep, 1, i * (self.block_size + 1) - 1, 
                                 self.size + (self.size // self.block_size) - 1, 1)
            self.separators.append(v_sep)

    def change_size(self, text):
        """Меняет размер сетки"""
        self.size = 4 if text == "4x4" else 9
        self.block_size = 2 if self.size == 4 else 3
        self.create_grid()
        self.clear()
        self.status_label.setText(f"Сетка изменена на {self.size}x{self.size}")
        self.adjustSize()

    def get_board(self):
        """Получает текущее состояние доски"""
        board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                text = self.cells[i][j].text()
                board[i][j] = int(text) if text.isdigit() and 1 <= int(text) <= self.size else 0
        return board

    def set_board(self, board):
        """Обновляет интерфейс решённой доской"""
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] != 0:
                    self.cells[i][j].setText(str(board[i][j]))
                    self.cells[i][j].setReadOnly(True)

    def clear(self):
        """Очищает все поля"""
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].setText("")
                self.cells[i][j].setReadOnly(False)
        self.status_label.setText("Доска очищена")

    def load_example(self):
        """Загружает пример судоку"""
        if self.size == 9:
            example = [
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
        else:  # 4x4
            example = [
                [1, 0, 0, 4],
                [0, 2, 0, 0],
                [0, 0, 4, 0],
                [3, 0, 0, 2]
            ]
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].setText(str(example[i][j]) if example[i][j] != 0 else "")
                self.cells[i][j].setReadOnly(example[i][j] != 0)
        self.status_label.setText("Пример загружен")

    def solve(self):
        """Решает судоку"""
        board = self.get_board()
        if solve_sudoku(board, self.size):
            self.set_board(board)
            self.status_label.setText("Судоку решено!")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет решения для этого судоку!")
            self.status_label.setText("Решение не найдено")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SudokuSolver()
    window.show()
    sys.exit(app.exec_())