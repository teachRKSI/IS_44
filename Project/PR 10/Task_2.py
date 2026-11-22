import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анкета")
        self.resize(320, 220)

        central = QWidget()
        self.setCentralWidget(central)

        self.form_layout = QFormLayout(central)

        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.city_edit = QLineEdit()

        self.show_button = QPushButton("Показать")
        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)

        self.form_layout.addRow("Имя:", self.name_edit)
        self.form_layout.addRow("Возраст:", self.age_edit)
        self.form_layout.addRow("Город:", self.city_edit)
        self.form_layout.addRow(self.show_button)
        self.form_layout.addRow(self.result_label)

        self.show_button.clicked.connect(self.show_profile)

    def show_profile(self):
        name = self.name_edit.text().strip()
        age = self.age_edit.text().strip()
        city = self.city_edit.text().strip()

        if not name or not age or not city:
            self.result_label.setText("Заполните все поля")
        else:
            self.result_label.setText(
                f"Имя: {name}\nВозраст: {age}\nГород: {city}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())