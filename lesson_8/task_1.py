import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_task_1 import Ui_Widget


class Task1Window(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnStart.clicked.connect(self.on_start)
        self.btnPause.clicked.connect(self.on_pause)
        self.btnStop.clicked.connect(self.on_stop)

    def on_start(self):
        print("Старт")

    def on_pause(self):
        print("Пауза")

    def on_stop(self):
        print("Стоп")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task1Window()
    window.show()
    sys.exit(app.exec())
