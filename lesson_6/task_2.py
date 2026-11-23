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

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.form_layout = QFormLayout()

        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.city_edit = QLineEdit()

        self.form_layout.addRow("Имя:", self.name_edit)
        self.form_layout.addRow("Возраст:", self.age_edit)
        self.form_layout.addRow("Город:", self.city_edit)

        self.button = QPushButton("Показать")
        self.button.clicked.connect(self.on_show)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)

        self.main_layout = QVBoxLayout(self.central)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.result_label)

    def on_show(self):
        self.name = self.name_edit.text().strip()
        self.age = self.age_edit.text().strip()
        self.city = self.city_edit.text().strip()

        if not self.name or not self.age or not self.city:
            self.result_label.setText("Заполните все поля")
        else:
            self.result_label.setText(f"Имя: {self.name}\nВозраст: {self.age}\nГород: {self.city}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
