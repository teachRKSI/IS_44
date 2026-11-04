import sys
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QLineEdit, QPushButton, QCheckBox)

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Генератор никнейма")
    window.resize(300, 250)

    layout = QVBoxLayout()

    edit = QLineEdit()
    edit.setPlaceholderText("Введите имя")

    year_checkbox = QCheckBox("Добавить год")
    underscore_checkbox = QCheckBox("Добавить подчёркивание")

    button = QPushButton("Сгенерировать")
    label = QLabel("")

    layout.addWidget(edit)
    layout.addWidget(year_checkbox)
    layout.addWidget(underscore_checkbox)
    layout.addWidget(button)
    layout.addWidget(label)

    window.setLayout(layout)

    def generate():
        name = edit.text().strip()
        if not name:
            label.setText("Сначала введите имя")
            return

        add_year = year_checkbox.isChecked()
        add_underscore = underscore_checkbox.isChecked()

        nickname = name

        if add_year and add_underscore:
            nickname = f"{name}_{datetime.now().year}"
        elif add_year:
            nickname = f"{name}{datetime.now().year}"
        elif add_underscore:
            nickname = f"{name}_"

        label.setText(nickname)

    button.clicked.connect(generate)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
