import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QLineEdit, QPushButton)

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Привет!!!!!!!!!!!!!!!!!!!!!!")
    window.resize(300, 200)

    layout = QVBoxLayout()

    edit = QLineEdit()
    edit.setPlaceholderText("Введите ваше имя")

    greet_button = QPushButton("Поздороваться")
    reset_button = QPushButton("Сбросить")

    label = QLabel("")

    layout.addWidget(edit)
    layout.addWidget(greet_button)
    layout.addWidget(reset_button)
    layout.addWidget(label)

    window.setLayout(layout)

    counter = {"value": 0}

    def greet():
        name = edit.text().strip()
        if not name:
            label.setText("Сначала введите имя")
            return
        counter["value"] += 1
        label.setText(f"Привет, {name}! Это ваше {counter['value']}-е приветствие")

    def reset():
        counter["value"] = 0
        edit.clear()
        label.clear()

    greet_button.clicked.connect(greet)
    reset_button.clicked.connect(reset)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
