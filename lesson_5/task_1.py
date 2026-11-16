import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

count = 0


def on_greet():
    global count
    name = name_input.text().strip()
    if not name:
        result_label.setText("Сначала введите имя")
    else:
        count += 1
        result_label.setText(f"Привет, {name}! Это ваше {count}-е приветствие")


def on_reset():
    global count
    count = 0
    name_input.clear()
    result_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Приветствие")
    window.resize(350, 200)

    name_input = QLineEdit()
    name_input.setPlaceholderText("Введите ваше имя")

    greet_button = QPushButton("Поздороваться")
    greet_button.clicked.connect(on_greet)

    reset_button = QPushButton("Сбросить")
    reset_button.clicked.connect(on_reset)

    result_label = QLabel("")

    layout = QVBoxLayout()
    layout.addWidget(name_input)
    layout.addWidget(greet_button)
    layout.addWidget(reset_button)
    layout.addWidget(result_label)

    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())
