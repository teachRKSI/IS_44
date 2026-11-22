import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QCheckBox,
    QPushButton,
    QLabel,
)


class NicknameGeneratorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор никнеймов")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя")

        self.year_checkbox = QCheckBox("Добавить год")
        self.underscore_checkbox = QCheckBox("Добавить подчёркивание")

        self.generate_button = QPushButton("Сгенерировать")
        self.result_label = QLabel("")

        layout.addWidget(self.name_input)
        layout.addWidget(self.year_checkbox)
        layout.addWidget(self.underscore_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.generate_button.clicked.connect(self.generate_nickname)

    def generate_nickname(self):
        name = self.name_input.text().strip()
        if not name:
            self.result_label.setText("Сначала введите имя")
            return

        add_year = self.year_checkbox.isChecked()
        add_underscore = self.underscore_checkbox.isChecked()
        current_year = datetime.now().year

        nickname = name
        if add_underscore and add_year:
            nickname += f"_{current_year}"
        elif add_year:
            nickname += str(current_year)
        elif add_underscore:
            nickname += "_"

        self.result_label.setText(nickname)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NicknameGeneratorWindow()
    window.show()
    sys.exit(app.exec())