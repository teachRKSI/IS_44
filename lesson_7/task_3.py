import sys

from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class StyledButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Стилизация кнопок")
        self.resize(300, 200)

        layout = QVBoxLayout(self)

        self.btn1 = QPushButton("Одна")
        self.btn2 = QPushButton("Две")
        self.btn3 = QPushButton("Три")

        self.btn2.setStyleSheet("background-color: #ffcccc;")

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QPushButton {
            background-color: #e7ecf8;
            color: #1f2d4d;
        }
        QPushButton:hover {
            background-color: #d2ddf6;
        }
    """)

    window = StyledButtons()
    window.show()
    sys.exit(app.exec())
