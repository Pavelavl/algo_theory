from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, QTextEdit, QMessageBox, QFrame
from PyQt5.QtCore import Qt
from algo.dijkstra import dijkstra

class DijkstraWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 4  # Размер графа по умолчанию
        self.cells = []
        self.init_ui()

    def init_ui(self):
        self.layout = QGridLayout(self)
        self.setStyleSheet("background-color: #f0f4f8;")

        # Размер графа
        self.size_label = QLabel("Размер графа (вершины):")
        self.size_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.size_label, 0, 0, 1, 2)
        
        self.size_input = QLineEdit("4")
        self.size_input.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 14px;")
        self.size_input.textChanged.connect(self.change_size)
        self.layout.addWidget(self.size_input, 0, 2, 1, 2)

        # Сетка для матрицы смежности
        self.create_grid()

        # Начальная вершина
        self.start_label = QLabel("Начальная вершина (A, B, ...):")
        self.start_label.setStyleSheet("font-size: 14px; color: #333;")
        self.layout.addWidget(self.start_label, self.size + 2, 0, 1, 2)
        self.start_input = QLineEdit("A")
        self.start_input.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 14px;")
        self.layout.addWidget(self.start_input, self.size + 2, 2, 1, 2)

        # Конечная вершина
        self.end_label = QLabel("Конечная вершина (A, B, ...):")
        self.end_label.setStyleSheet("font-size: 14px; color: #333;")
        self.layout.addWidget(self.end_label, self.size + 3, 0, 1, 2)
        self.end_input = QLineEdit("D")
        self.end_input.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 14px;")
        self.layout.addWidget(self.end_input, self.size + 3, 2, 1, 2)

        # Кнопки
        button_style = """
            QPushButton { background-color: #4a90e2; color: white; border: none; border-radius: 5px; padding: 8px; font-size: 14px; font-weight: bold; }
            QPushButton:hover { background-color: #357abd; }
            QPushButton:pressed { background-color: #2a6395; }
        """
        self.solve_button = QPushButton("Найти путь")
        self.solve_button.clicked.connect(self.solve)
        self.solve_button.setStyleSheet(button_style)
        self.layout.addWidget(self.solve_button, self.size + 4, 0, 1, 2)

        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.setStyleSheet(button_style)
        self.layout.addWidget(self.clear_button, self.size + 4, 2, 1, 2)

        self.load_button = QPushButton("Загрузить пример")
        self.load_button.clicked.connect(self.load_example)
        self.load_button.setStyleSheet(button_style)
        self.layout.addWidget(self.load_button, self.size + 4, 4, 1, 2)

        # Результат
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; font-size: 14px; background-color: #fff;")
        self.layout.addWidget(self.result_text, self.size + 5, 0, 2, 6)

    def create_grid(self):
        # Удаляем старую сетку
        for row in self.cells:
            for cell in row:
                self.layout.removeWidget(cell)
                cell.deleteLater()
        self.cells = [[QLineEdit() for _ in range(self.size)] for _ in range(self.size)]
        
        cell_style = """
            QLineEdit { border: 1px solid #d0d7de; background-color: #ffffff; font-size: 14px; font-family: Arial; color: #333; padding: 2px; }
            QLineEdit:hover { border: 1px solid #88b7f5; }
            QLineEdit:focus { border: 1px solid #4a90e2; background-color: #f0f8ff; }
        """
        label_style = "font-size: 14px; font-weight: bold; color: #333; text-align: center;"
        
        # Добавляем буквенные метки (A, B, C, ...)
        for i in range(self.size):
            row_label = QLabel(chr(65 + i))  # A=65 в ASCII
            row_label.setStyleSheet(label_style)
            self.layout.addWidget(row_label, i + 2, 0)
            
            col_label = QLabel(chr(65 + i))
            col_label.setStyleSheet(label_style)
            self.layout.addWidget(col_label, 1, i + 1)
        
        # Создаём сетку
        for i in range(self.size):
            for j in range(self.size):
                cell = self.cells[i][j]
                cell.setFixedSize(50, 30)
                cell.setAlignment(Qt.AlignCenter)
                cell.setStyleSheet(cell_style)
                self.layout.addWidget(cell, i + 2, j + 1)

    def change_size(self):
        try:
            new_size = int(self.size_input.text())
            if 2 <= new_size <= 26:  # Ограничиваем до Z
                self.size = new_size
                self.create_grid()
                self.clear()
            else:
                self.size_input.setText(str(self.size))
        except ValueError:
            self.size_input.setText(str(self.size))

    def get_graph(self):
        graph = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                text = self.cells[i][j].text()
                graph[i][j] = int(text) if text.isdigit() else 0
        return graph

    def letter_to_index(self, letter):
        """Преобразует букву (A, B, ...) в индекс (0, 1, ...)."""
        letter = letter.upper()
        if not letter.isalpha() or ord(letter) < 65 or ord(letter) > 64 + self.size:
            raise ValueError(f"Вершина должна быть буквой от A до {chr(64 + self.size)}")
        return ord(letter) - 65

    def index_to_letter(self, index):
        """Преобразует индекс в букву."""
        return chr(65 + index)

    def clear(self):
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].setText("")
        self.start_input.setText("A")
        self.end_input.setText(self.index_to_letter(self.size - 1))
        self.result_text.setText("")

    def load_example(self):
        # Пример графа: 4 вершины (A, B, C, D), путь A -> B -> D = 6
        example = [
            [0, 1, 4, 0],
            [1, 0, 2, 5],
            [4, 2, 0, 3],
            [0, 5, 3, 0]
        ]
        self.size = 4
        self.size_input.setText("4")
        self.create_grid()
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].setText(str(example[i][j]) if example[i][j] != 0 else "")
        self.start_input.setText("A")
        self.end_input.setText("D")
        self.result_text.setText("Пример загружен: граф с вершинами A, B, C, D. Нажмите 'Найти путь' для решения.")

    def solve(self):
        try:
            graph = self.get_graph()
            start = self.letter_to_index(self.start_input.text())
            end = self.letter_to_index(self.end_input.text())
            path, distance = dijkstra(graph, start, end)
            if path is None:
                self.result_text.setText("Пути не существует")
            else:
                path_letters = [self.index_to_letter(i) for i in path]
                self.result_text.setText(f"Кратчайший путь: {' -> '.join(path_letters)}\nДлина пути: {distance}")
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))