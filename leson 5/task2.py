import sys
from datetime import datetime
from PySide6.QtWidgets import (
QApplication, QWidget, QVBoxLayout,
QLineEdit, QCheckBox, QPushButton, QLabel
)


class NicknameApp(QWidget):
def __init__(self):
super().__init__()

self.setWindowTitle("Генератор никнеймов")
self.resize(300, 250)

self.edit = QLineEdit()
self.edit.setPlaceholderText("Введите имя")

self.year_checkbox = QCheckBox("Добавить год")
self.underscore_checkbox = QCheckBox("Добавить подчёркивание")

self.button = QPushButton("Сгенерировать")
self.label = QLabel("")

layout = QVBoxLayout()
layout.addWidget(self.edit)
layout.addWidget(self.year_checkbox)
layout.addWidget(self.underscore_checkbox)
layout.addWidget(self.button)
layout.addWidget(self.label)

self.setLayout(layout)

self.button.clicked.connect(self.generate)

def generate(self):
name = self.edit.text().strip()

if not name:
self.label.setText("Сначала введите имя")
return

nickname = name

add_year = self.year_checkbox.isChecked()
add_underscore = self.underscore_checkbox.isChecked()

if add_year and add_underscore:
nickname += "_" + str(datetime.now().year)

elif add_year:
nickname += str(datetime.now().year)

elif add_underscore:
nickname += "_"

self.label.setText(nickname)


app = QApplication(sys.argv)
window = NicknameApp()
window.show()
sys.exit(app.exec())