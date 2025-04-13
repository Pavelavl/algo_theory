from PyQt5.QtWidgets import QMainWindow, QTabWidget
from gui.sudoku_solver_gui import SudokuSolverWidget
from gui.dijkstra_gui import DijkstraWidget
from gui.quicksort_gui import QuicksortWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решение задач полиномиальной сложности")
        self.setGeometry(100, 100, 800, 600)
        
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        self.tabs.addTab(SudokuSolverWidget(), "Судоку")
        self.tabs.addTab(DijkstraWidget(), "Кратчайший путь (Дейкстра)")
        self.tabs.addTab(QuicksortWidget(), "Быстрая сортировка")