import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приветствие")
        self.counter = 0  # Счетчик нажатий

        # Создаем элементы
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите ваше имя")

        self.greet_button = QPushButton("Поздороваться")
        self.reset_button = QPushButton("Сбросить")
        self.result_label = QLabel("")

        # Создаем layout и добавляем элементы
        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.greet_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Подключаем сигналы к слотам
        self.greet_button.clicked.connect(self.on_greet)
        self.reset_button.clicked.connect(self.on_reset)

    def on_greet(self):
        name = self.name_input.text().strip()
        if not name:
            self.result_label.setText("Сначала введите имя")
        else:
            self.counter += 1
            self.result_label.setText(f"Привет, {name}! Это ваше {self.counter}-е приветствие")

    def on_reset(self):
        self.counter = 0
        self.name_input.clear()
        self.result_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())