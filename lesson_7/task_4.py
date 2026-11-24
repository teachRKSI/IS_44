import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class ColorTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget: таблица цветов")
        self.resize(600, 320)

        colors = [
            ("Red", "#FF0000", "Классический ярко-красный"),
            ("Green", "#00FF00", "Чистый зелёный цвет"),
            ("Blue", "#0000FF", "Чистый синий цвет"),
            ("Black", "#000000", "Глубокий чёрный"),
            ("White", "#FFFFFF", "Чистый белый фон"),
            ("Electric Green", "#41CD52", "Неоновый зелёный акцент"),
            ("Dark Blue", "#222840", "Тёмно-синий ночной оттенок"),
            ("Yellow", "#F9E56D", "Тёплый жёлтый цвет"),
        ]

        table = QTableWidget()
        table.setRowCount(len(colors))
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color", "Комментарий"])

        for i, (name, code, comment) in enumerate(colors):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)

            item_color = QTableWidgetItem()
            item_color.setBackground(QColor(code))

            item_comment = QTableWidgetItem(comment)

            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_code)
            table.setItem(i, 2, item_color)
            table.setItem(i, 3, item_comment)

        layout = QVBoxLayout(self)
        layout.addWidget(table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorTable()
    window.show()
    sys.exit(app.exec())
