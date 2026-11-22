import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)


class GreetingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приветствие")
        self.resize(300, 180)
        self.count = 0

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите ваше имя")

        self.greet_button = QPushButton("Поздороваться")
        self.reset_button = QPushButton("Сбросить")
        self.result_label = QLabel("")

        layout.addWidget(self.name_input)
        layout.addWidget(self.greet_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.greet_button.clicked.connect(self.on_greet)
        self.reset_button.clicked.connect(self.on_reset)

    def on_greet(self):
        name = self.name_input.text().strip()
        if not name:
            self.result_label.setText("Сначала введите имя")
        else:
            self.count += 1
            self.result_label.setText(
                f"Привет, {name}! Это ваше {self.count}-е приветствие"
            )

    def on_reset(self):
        self.count = 0
        self.name_input.clear()
        self.result_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GreetingWindow()
    window.show()
    sys.exit(app.exec())