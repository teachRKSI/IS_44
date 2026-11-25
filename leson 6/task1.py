import sys
from PySide6.QtWidgets import (
QApplication, QMainWindow, QWidget,
QFormLayout, QVBoxLayout, QLineEdit,
QPushButton, QLabel
)


class MainWindow(QMainWindow):
def __init__(self):
super().__init__()

self.setWindowTitle("Анкета")
self.resize(350, 250)

central = QWidget()
self.setCentralWidget(central)

self.name_edit = QLineEdit()
self.age_edit = QLineEdit()
self.city_edit = QLineEdit()

form = QFormLayout()
form.addRow("Имя:", self.name_edit)
form.addRow("Возраст:", self.age_edit)
form.addRow("Город:", self.city_edit)

self.button = QPushButton("Показать")

self.label = QLabel("")
self.label.setWordWrap(True)

layout = QVBoxLayout(central)
layout.addLayout(form)
layout.addWidget(self.button)
layout.addWidget(self.label)

self.button.clicked.connect(self.show_info)

def show_info(self):
name = self.name_edit.text().strip()
age = self.age_edit.text().strip()
city = self.city_edit.text().strip()

if not name or not age or not city:
self.label.setText("Заполните все поля")
else:
self.label.setText(
f"Имя: {name}\n"
f"Возраст: {age}\n"
f"Город: {city}"
)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())