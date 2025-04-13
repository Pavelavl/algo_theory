from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit, QMessageBox
from algo.quicksort import quicksort

class QuicksortWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: #f0f4f8;")

        self.input_label = QLabel("Введите числа (через пробел):")
        self.input_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.input_label)

        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 14px;")
        self.layout.addWidget(self.input_field)

        button_style = """
            QPushButton { background-color: #4a90e2; color: white; border: none; border-radius: 5px; padding: 8px; font-size: 14px; font-weight: bold; }
            QPushButton:hover { background-color: #357abd; }
            QPushButton:pressed { background-color: #2a6395; }
        """
        self.sort_button = QPushButton("Сортировать")
        self.sort_button.clicked.connect(self.sort)
        self.sort_button.setStyleSheet(button_style)
        self.layout.addWidget(self.sort_button)

        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.setStyleSheet(button_style)
        self.layout.addWidget(self.clear_button)

        self.load_button = QPushButton("Загрузить пример")
        self.load_button.clicked.connect(self.load_example)
        self.load_button.setStyleSheet(button_style)
        self.layout.addWidget(self.load_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; font-size: 14px; background-color: #fff;")
        self.layout.addWidget(self.result_text)

    def clear(self):
        self.input_field.setText("")
        self.result_text.setText("")

    def load_example(self):
        self.input_field.setText("5 2 8 1 9 3")
        self.result_text.setText("Пример загружен")

    def sort(self):
        try:
            numbers = [int(x) for x in self.input_field.text().split()]
            if not numbers:
                raise ValueError("Введите хотя бы одно число")
            sorted_numbers = quicksort(numbers)
            self.result_text.setText(f"Отсортированный массив: {', '.join(map(str, sorted_numbers))}")
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))