import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
)
from ui_task_3 import Ui_MainWindow


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.first_num: float | None = None
        self.operation: str | None = None
        self.new_entry: bool = False

        digits = [
            self.btn0,
            self.btn1,
            self.btn2,
            self.btn3,
            self.btn4,
            self.btn5,
            self.btn6,
            self.btn7,
            self.btn8,
            self.btn9,
        ]
        for btn in digits:
            btn.clicked.connect(self.on_digit)

        self.btnDot.clicked.connect(self.on_dot)

        operations = [self.btnAdd, self.btnSub, self.btnMul, self.btnDiv]
        for btn in operations:
            btn.clicked.connect(self.on_operator)

        self.btnEqual.clicked.connect(self.on_equal)

        self.btnClear.clicked.connect(self.on_clear)
        self.btnBackspace.clicked.connect(self.on_backspace)

        self.actionAbout.triggered.connect(self.on_about)

    def on_digit(self):
        button = self.sender()
        if not isinstance(button, QPushButton):
            return
        digit = button.text()

        if self.new_entry:
            self.display.setText(digit)
            self.new_entry = False
        else:
            current = self.display.text()
            if current == "0":
                self.display.setText(digit)
            else:
                self.display.setText(current + digit)

    def on_dot(self):
        if self.new_entry and self.operation:
            self.display.setText("0.")
        elif "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.new_entry = False

    def on_operator(self):
        button = self.sender()
        if not isinstance(button, QPushButton):
            return

        if self.operation and not self.new_entry:
            self.calculate()

        self.first_num = float(self.display.text())
        self.operation = button.text()
        self.new_entry = True

    def calculate(self) -> bool:
        if self.first_num is None or self.operation is None:
            return True

        second_num = float(self.display.text())

        if self.operation == "÷" and second_num == 0:
            QMessageBox.warning(self, "Ошибка", "Деление на ноль невозможно!")
            return False

        if self.operation == "+":
            result = self.first_num + second_num
        elif self.operation == "−":
            result = self.first_num - second_num
        elif self.operation == "×":
            result = self.first_num * second_num
        elif self.operation == "÷":
            result = self.first_num / second_num
        else:
            return True

        if result.is_integer():
            self.display.setText(str(int(result)))
        else:
            self.display.setText(str(round(result, 2)))

        self.first_num = result
        return True

    def on_equal(self):
        if self.calculate():
            self.operation = None
            self.first_num = None
            self.new_entry = True

    def on_clear(self):
        self.display.setText("0")
        self.first_num = None
        self.operation = None
        self.new_entry = False

    def on_backspace(self):
        self.new_entry = False
        text = self.display.text()
        if len(text) <= 1:
            self.display.setText("0")
        else:
            self.display.setText(text[:-1])

    def on_about(self):
        QMessageBox.about(
            self,
            "О калькуляторе",
            "Простой калькулятор :)",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
