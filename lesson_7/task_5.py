import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHeaderView,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Форма + Таблица")
        self.resize(500, 400)

        # Счётчик заполненных строк
        self.filled_rows = 0

        # Центральный виджет и его вертикальный layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Форма ввода сверху
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя")
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Введите город")

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.on_add_clicked)

        form_layout.addRow("Имя:", self.name_input)
        form_layout.addRow("Город:", self.city_input)
        form_layout.addRow(self.add_button)

        main_layout.addLayout(form_layout)

        # Таблица снизу
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Имя", "Город"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        main_layout.addWidget(self.table)

        # Стилизация QSS
        self.setStyleSheet("""
            QLineEdit {
                padding: 6px;
                border: 1px solid #b0b8c5;
                border-radius: 4px;
                background-color: #ffffff;
                color: #1f2d4d;
            }
            QLineEdit:focus {
                border: 1px solid #0078d4;
            }
            QPushButton {
                background-color: #0078d4;
                color: #ffffff;
                border-radius: 4px;
                padding: 6px 12px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #106ebe;
            }
            QPushButton:pressed {
                background-color: #005a9e;
            }
        """)

    @Slot()
    def on_add_clicked(self):
        if self.filled_rows >= 5:
            return

        name = self.name_input.text().strip()
        city = self.city_input.text().strip()

        if not name and not city:
            return

        self.table.setItem(self.filled_rows, 0, QTableWidgetItem(name))
        self.table.setItem(self.filled_rows, 1, QTableWidgetItem(city))

        self.filled_rows += 1

        self.name_input.clear()
        self.city_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
