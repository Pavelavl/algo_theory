import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QTextEdit, QLabel, QLineEdit, QHBoxLayout
from src.task1 import rectangle_area_generator, parallel_rectangle_area_generator
from src.task2 import note_list_generator, parallel_note_matrix
from src.task3 import find_common_even_values, find_common_even_values_parallel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генераторы задач")
        self.setGeometry(100, 100, 800, 600)
        
        # Инициализация вкладок
        tabs = QTabWidget()
        
        # Вкладки для задач
        tabs.addTab(self.task1_ui(), "Задача 1")
        tabs.addTab(self.task2_ui(), "Задача 2")
        tabs.addTab(self.task3_ui(), "Задача 3")
        
        self.setCentralWidget(tabs)

    def task1_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Поле для ввода количества данных
        data_size_input = QLineEdit()
        data_size_input.setPlaceholderText("Введите количество данных (по умолчанию 100)")
        self.data_size_input_task1 = data_size_input

        # Обычная версия
        btn_generate_areas = QPushButton("Сгенерировать площади (обычно)")
        btn_generate_areas.clicked.connect(self.generate_areas)

        # Многопоточная версия
        btn_generate_areas_parallel = QPushButton("Сгенерировать площади (многопоточно)")
        btn_generate_areas_parallel.clicked.connect(self.generate_areas_parallel)

        # Поле для вывода
        self.task1_output = QTextEdit()
        self.task1_output.setReadOnly(True)

        # Компоновка
        layout.addWidget(data_size_input)
        layout.addWidget(btn_generate_areas)
        layout.addWidget(btn_generate_areas_parallel)
        layout.addWidget(self.task1_output)
        widget.setLayout(layout)
        return widget

    def generate_areas(self):
        self.task1_output.clear()
        count = int(self.data_size_input_task1.text() or 100)
        
        start_time = time.time()
        areas = list(rectangle_area_generator(count=count))
        elapsed_time = time.time() - start_time

        self.task1_output.append(f"Сгенерировано {len(areas)} площадей за {elapsed_time:.4f} секунд (обычно).")

    def generate_areas_parallel(self):
        self.task1_output.clear()
        count = int(self.data_size_input_task1.text() or 100)

        start_time = time.time()
        areas = parallel_rectangle_area_generator(count=count)
        elapsed_time = time.time() - start_time

        self.task1_output.append(f"Сгенерировано {len(areas)} площадей за {elapsed_time:.4f} секунд (многопоточно).")

    def task2_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Поле для ввода размера матрицы
        matrix_size_input = QLineEdit()
        matrix_size_input.setPlaceholderText("Введите размер матрицы (по умолчанию 10)")
        self.matrix_size_input = matrix_size_input

        # Обычная версия
        btn_generate_matrix = QPushButton("Сгенерировать матрицу нот (обычно)")
        btn_generate_matrix.clicked.connect(self.generate_matrix)

        # Многопоточная версия
        btn_generate_matrix_parallel = QPushButton("Сгенерировать матрицу нот (многопоточно)")
        btn_generate_matrix_parallel.clicked.connect(self.generate_matrix_parallel)

        # Поле для вывода
        self.task2_output = QTextEdit()
        self.task2_output.setReadOnly(True)

        # Компоновка
        layout.addWidget(matrix_size_input)
        layout.addWidget(btn_generate_matrix)
        layout.addWidget(btn_generate_matrix_parallel)
        layout.addWidget(self.task2_output)
        widget.setLayout(layout)
        return widget

    def generate_matrix(self):
        self.task2_output.clear()
        size = int(self.matrix_size_input.text() or 10)

        start_time = time.time()
        matrix = note_list_generator(n=size)
        elapsed_time = time.time() - start_time

        self.task2_output.append(f"Сгенерирована матрица {size}x{size} за {elapsed_time:.4f} секунд (обычно).")

    def generate_matrix_parallel(self):
        self.task2_output.clear()
        size = int(self.matrix_size_input.text() or 10)

        start_time = time.time()
        matrix = parallel_note_matrix(size=size)
        elapsed_time = time.time() - start_time

        self.task2_output.append(f"Сгенерирована матрица {size}x{size} за {elapsed_time:.4f} секунд (многопоточно).")

    def task3_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Поля для ввода номиналов
        self.coins1_input = QLineEdit()
        self.coins1_input.setPlaceholderText("Введите номиналы первой коллекции (через пробел)")

        self.coins2_input = QLineEdit()
        self.coins2_input.setPlaceholderText("Введите номиналы второй коллекции (через пробел)")

        # Кнопки запуска
        btn_find_common_even = QPushButton("Найти общие четные (обычно)")
        btn_find_common_even.clicked.connect(self.find_common_even)

        btn_find_common_even_parallel = QPushButton("Найти общие четные (многопоточно)")
        btn_find_common_even_parallel.clicked.connect(self.find_common_even_parallel)

        # Поле для вывода результата
        self.task3_output = QTextEdit()
        self.task3_output.setReadOnly(True)

        # Компоновка
        layout.addWidget(QLabel("Первая коллекция:"))
        layout.addWidget(self.coins1_input)
        layout.addWidget(QLabel("Вторая коллекция:"))
        layout.addWidget(self.coins2_input)
        layout.addWidget(btn_find_common_even)
        layout.addWidget(btn_find_common_even_parallel)
        layout.addWidget(self.task3_output)
        widget.setLayout(layout)
        return widget

    def find_common_even(self):
        self.task3_output.clear()
        coins1 = self.coins1_input.text()
        coins2 = self.coins2_input.text()

        start_time = time.time()
        result = find_common_even_values(coins1, coins2)
        elapsed_time = time.time() - start_time

        self.task3_output.append(f"Найдено {len(result)} общих четных значений за {elapsed_time:.4f} секунд (обычно).")

    def find_common_even_parallel(self):
        self.task3_output.clear()
        coins1 = self.coins1_input.text()
        coins2 = self.coins2_input.text()

        start_time = time.time()
        result = find_common_even_values_parallel(coins1, coins2)
        elapsed_time = time.time() - start_time

        self.task3_output.append(f"Найдено {len(result)} общих четных значений за {elapsed_time:.4f} секунд (многопоточно).")

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())