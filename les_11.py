#Задание 1
import sys

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout)

class CounterWidget(QWidget):

    countChanged = Signal(int)

    def counter(self):
        self.count += 1
        self.countChanged.emit(self.count)

    @Slot(int)
    def update(self, count):
        self.label.setText(f"Нажатий: {count}")

    def __init__(self):
        super().__init__()

        self.count = 0

        self.setWindowTitle("Счётчик нажатий")
        self.resize(500, 100)

        layout = QVBoxLayout(self)

        self.label = QLabel("Нажатий: 0")

        button = QPushButton("Нажать")
        button.clicked.connect(self.counter)

        self.countChanged.connect(self.update)

        layout.addWidget(button)
        layout.addWidget(self.label)
    
app = QApplication(sys.argv)

window = CounterWidget()
window.show()

sys.exit(app.exec())

#Задание 2
import sys

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout)

class MouseReporter(QWidget):

    mouseButtonPressed = Signal(Qt.MouseButton)

    def mousePressEvent(self, event):
        self.mouseButtonPressed.emit(event.button())

    @Slot(Qt.MouseButton)
    def showButton(self, value):
        if value == Qt.LeftButton:
            self.label.setText("Левая кнопка мыши")
        elif value == Qt.RightButton:
            self.label.setText("Правая кнопка мыши")
        else:
            self.label.setText("Другая кнопка")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание №2")
        self.resize(500,500)

        self.label = QLabel("Нажмите кнопку мыши в окне")

        self.mouseButtonPressed.connect(self.showButton)

        layout = QVBoxLayout(self)
              
        layout.addWidget(self.label)

app = QApplication(sys.argv)
window = MouseReporter()

window.show()

sys.exit(app.exec())

#Задание 3
import sys

from PySide6.QtWidgets import (QWidget, QApplication, QPushButton, QVBoxLayout)

class StyledButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание 3")
        self.resize(300, 100)

        button1 = QPushButton("Одна")
        button2 = QPushButton("Две")
        button3 = QPushButton("Три")

        button1.setStyleSheet("background-color: #FFCCCC;")

        layout = QVBoxLayout(self)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QPushButton { 
            background-color: #e7ecf8; color: #1f2d4d; 
        }
        QPushButton:hover{ 
            background-color: #d2ddf6; 
        }
    """)
    
    window = StyledButtons()
    window.show()

    sys.exit(app.exec())

#Задание 4
import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QWidget, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout)

class ColorTable(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задание 4 - Таблица цветов")
        self.resize(600, 320)

        colors = [("Red", "#FF0000", "Красный цвет"),
                  ("Green", "#00FF00", "Зеленый цвет"),
                  ("Blue", "#0000FF", "Синий цвет"),
                  ("Black", "#000000", "Черный цвет"),
                  ("White", "#FFFFFF", "Белый цвет"),
                  ("Electric Green", "#41CD52", "Темно-зеленый цвет"),
                  ("Dark Blue", "#222840", "Темно-синий цвет"),
                  ("Yellow", "#F9E56d", "Желтый цвет")]

        table = QTableWidget()
        table.setRowCount(len(colors))
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color", "Комментарий"])

        for i, (name, code, comm) in enumerate(colors):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)

            item_color = QTableWidgetItem()
            item_color.setBackground(QColor(code))

            item_comm = QTableWidgetItem(comm)

            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_code)
            table.setItem(i, 2, item_color)
            table.setItem(i, 3, item_comm)

        layout = QVBoxLayout(self)
        layout.addWidget(table)

app = QApplication(sys.argv)

window = ColorTable()
window.show()

sys.exit(app.exec())

#Задание 5
import sys

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QFormLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout)

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.filled_rows = 0

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.form = QFormLayout()
        self.form.addRow("Имя:", QLineEdit())
        self.form.addRow("Город:", QLineEdit())

        button = QPushButton("Добавить")
        button.clicked.connect(self.add_row)
        
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(5)
        self.table.setHorizontalHeaderLabels(["Имя", "Город"])

        layout.addLayout(self.form)
        layout.addWidget(button)
        layout.addWidget(self.table)

    def add_row(self):
        if self.filled_rows < 5:
            item1 = QTableWidgetItem(self.form.itemAt(0, QFormLayout.FieldRole).widget().text())
            item2 = QTableWidgetItem(self.form.itemAt(1, QFormLayout.FieldRole).widget().text())
            self.table.setItem(self.filled_rows, 0, item1)
            self.table.setItem(self.filled_rows, 1, item2)
            self.filled_rows += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QPushButton:hover{
           background-color: #989898;
           font-weight: 800;
           }
        QLineEdit{
           border: 3px solid black;
        }   
        """)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())