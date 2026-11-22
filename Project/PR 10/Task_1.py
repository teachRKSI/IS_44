import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)


class GreetingCounterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Счётчик приветствий")
        self.resize(300, 180)
        self.count = 0

        self.layout = QVBoxLayout(self)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Введите ваше имя")

        self.button = QPushButton("Поздороваться")
        self.reset_button = QPushButton("Сбросить")
        self.label = QLabel("")

        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.label)

        self.button.clicked.connect(self.on_greet)
        self.reset_button.clicked.connect(self.on_reset)

    def on_greet(self):
        name = self.edit.text().strip()
        if not name:
            self.label.setText("Сначала введите имя")
        else:
            self.count += 1
            self.label.setText(
                f"Привет, {name}! Это ваше {self.count}-е приветствие"
            )

    def on_reset(self):
        self.count = 0
        self.edit.clear()
        self.label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GreetingCounterWindow()
    window.show()
    sys.exit(app.exec())