import sys

from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анкета")
        self.resize(350, 250)

        central = QWidget()
        self.setCentralWidget(central)

        form_layout = QFormLayout()

        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.city_edit = QLineEdit()

        form_layout.addRow("Имя:", self.name_edit)
        form_layout.addRow("Возраст:", self.age_edit)
        form_layout.addRow("Город:", self.city_edit)

        self.button = QPushButton("Показать")
        self.button.clicked.connect(self.on_show)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)

        main_layout = QVBoxLayout(central)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.result_label)

    def on_show(self):
        name = self.name_edit.text().strip()
        age = self.age_edit.text().strip()
        city = self.city_edit.text().strip()

        if not name or not age or not city:
            self.result_label.setText("Заполните все поля")
        else:
            self.result_label.setText(f"Имя: {name}\nВозраст: {age}\nГород: {city}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
