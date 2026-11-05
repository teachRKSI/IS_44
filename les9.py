#Задание 1
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel)

n = 0

def say_hi():
    global n
    if input_box.text():
        n += 1
        label.setText(f"Привет, {input_box.text()}! Это ваше {n} приветствие")
    else:
        label.setText("Сначала введите имя!")

def clear():
    global n
    n = 0
    input_box.setText("")
    label.setText("")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Задание 1")
window.resize(400, 200)

layout = QVBoxLayout()

input_box = QLineEdit(window)
input_box.setPlaceholderText("Введите ваше имя")

button = QPushButton("Поздороваться", window)
button.clicked.connect(say_hi)

clr_button = QPushButton("Сбросить", window)
clr_button.clicked.connect(clear)


label = QLabel(window)

layout.addWidget(input_box)
layout.addWidget(button)
layout.addWidget(clr_button)
layout.addWidget(label)

window.setLayout(layout)
window.show()

sys.exit(app.exec())

#Задание 2

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QCheckBox, QPushButton, QLabel)
from datetime import datetime

def generate():
    result = name_input.text()
    if underline_box.isChecked():
        result += "_"
    if year_box.isChecked():
        result += f"{datetime.now().year}"
    result_label.setText(result)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Генератор никнеймов")
window.resize(400, 200)

name_input = QLineEdit(window)
name_input.setPlaceholderText("Введите ваше имя")

year_box = QCheckBox("Добавить год", window)

underline_box = QCheckBox("Добавить подчеркивание", window)

generate_button = QPushButton("Сгенерировать", window)
generate_button.clicked.connect(generate)

result_label = QLabel(window)

layout = QVBoxLayout(window)

layout.addWidget(name_input)
layout.addWidget(year_box)
layout.addWidget(underline_box)
layout.addWidget(result_label)
layout.addWidget(generate_button)

window.show()

sys.exit(app.exec())
