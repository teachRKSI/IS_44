#Задание 1
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel)

class Main(QWidget): 
    def __init__(self):
        super().__init__()
        self.n = 0

        self.setWindowTitle("Новый счётчик приветствий")

        self.layout = QVBoxLayout(self)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Введите ваше имя")

        self.button = QPushButton("Поздороваться")
        self.button.clicked.connect(self.say_hi)

        self.label = QLabel()

        self.clr_button = QPushButton("Сбросить")
        self.clr_button.clicked.connect(self.clear)

        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.clr_button)

    def say_hi(self):
        if self.input_box.text():
            self.n += 1
            self.label.setText(f"Привет, {self.input_box.text()}! Это ваше {self.n} приветствие")
        else:
            self.label.setText("Сначала введите имя!")

    def clear(self):
        self.n = 0
        self.input_box.setText("")
        self.label.setText("")

app = QApplication(sys.argv)
window = Main()

window.show()

sys.exit(app.exec())

#Задание 2
import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QApplication, QFormLayout, QLineEdit, QPushButton, QLabel, QVBoxLayout)

class Blank(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анкета")

        central = QWidget()
        self.setCentralWidget(central)

        self.form_layout = QFormLayout()
        self.main_layout = QVBoxLayout(central)

        self.form_layout.addRow("Имя", QLineEdit())
        self.form_layout.addRow("Возраст", QLineEdit())
        self.form_layout.addRow("Город", QLineEdit())

        self.button = QPushButton("Показать")
        self.button.clicked.connect(self.show_ts)

        self.label = QLabel()
        self.label.setWordWrap(True)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.label)

    def show_ts(self):
        text = ""
        items = {
            "Имя:" : None,
            "Возраст:" : None,
            "Город:" : None
        }
        for i, key in enumerate(items):
            items[key] = self.form_layout.itemAt(i, QFormLayout.FieldRole).widget().text()
        for key, value in items.items():
            if not value:
                text = "Заполните все поля!"
                break
            else:
                text += f"{key} {value}\n"
        self.label.setText(text)

app = QApplication(sys.argv)
blank = Blank()
blank.show()

sys.exit(app.exec())