import sys
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def on_generate():
    name = name_input.text().strip()

    if not name:
        result_label.setText("Сначала введите имя")
        return

    has_year = year_checkbox.isChecked()
    has_underscore = underscore_checkbox.isChecked()
    current_year = datetime.now().year

    if has_year and has_underscore:
        nickname = f"{name}_{current_year}"
    elif has_year:
        nickname = f"{name}{current_year}"
    elif has_underscore:
        nickname = f"{name}_"
    else:
        nickname = name

    result_label.setText(nickname)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Генератор никнеймов")
    window.resize(350, 250)

    name_input = QLineEdit()
    name_input.setPlaceholderText("Введите имя")

    year_checkbox = QCheckBox("Добавить год")
    underscore_checkbox = QCheckBox("Добавить подчёркивание")

    generate_button = QPushButton("Сгенерировать")
    generate_button.clicked.connect(on_generate)

    result_label = QLabel("")

    layout = QVBoxLayout()
    layout.addWidget(name_input)
    layout.addWidget(year_checkbox)
    layout.addWidget(underscore_checkbox)
    layout.addWidget(generate_button)
    layout.addWidget(result_label)

    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())
