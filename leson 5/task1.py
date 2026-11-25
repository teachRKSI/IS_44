import sys
from PySide6.QtWidgets import (
QApplication, QWidget, QVBoxLayout,
QLineEdit, QPushButton, QLabel
)


class GreetingApp(QWidget):
def __init__(self):
super().__init__()

self.counter = 0

self.setWindowTitle("Приветствие")
self.resize(300, 200)

self.edit = QLineEdit()
self.edit.setPlaceholderText("Введите ваше имя")

self.greet_button = QPushButton("Поздороваться")
self.reset_button = QPushButton("Сбросить")

self.label = QLabel("")

layout = QVBoxLayout()
layout.addWidget(self.edit)
layout.addWidget(self.greet_button)
layout.addWidget(self.label)
layout.addWidget(self.reset_button)

self.setLayout(layout)

self.greet_button.clicked.connect(self.greet)
self.reset_button.clicked.connect(self.reset)

def greet(self):
self.counter += 1
name = self.edit.text().strip()

if not name:
self.label.setText("Сначала введите имя")
else:
self.label.setText(
f"Привет, {name}! Это ваше {self.counter}-е приветствие"
)

def reset(self):
self.counter = 0
self.edit.clear()
self.label.clear()


app = QApplication(sys.argv)
window = GreetingApp()
window.show()
sys.exit(app.exec())