import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class GreetingCounterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Счётчик приветствий")
        self.resize(350, 200)

        self.count = 0

        main_layout = QVBoxLayout(self)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Введите ваше имя")

        self.button = QPushButton("Поздороваться")
        self.button.clicked.connect(self.on_greet)

        self.reset_button = QPushButton("Сбросить")
        self.reset_button.clicked.connect(self.on_reset)

        self.label = QLabel("")

        main_layout.addWidget(self.edit)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.reset_button)
        main_layout.addWidget(self.label)

    def on_greet(self):
        name = self.edit.text().strip()
        if not name:
            self.label.setText("Сначала введите имя")
        else:
            self.count += 1
            self.label.setText(f"Привет, {name}! Это ваше {self.count}-е приветствие")

    def on_reset(self):
        self.count = 0
        self.edit.clear()
        self.label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GreetingCounterWindow()
    window.show()
    sys.exit(app.exec())
