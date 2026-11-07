import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCheckBox, QPushButton, QLabel

class NicknameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор никнеймов")

        # Создаем элементы
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя")

        self.check_year = QCheckBox("Добавить год")
        self.check_underscore = QCheckBox("Добавить подчёркивание")

        self.generate_button = QPushButton("Сгенерировать")
        self.result_label = QLabel("")

        # Создаем layout и добавляем элементы
        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.check_year)
        layout.addWidget(self.check_underscore)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Подключаем сигнал
        self.generate_button.clicked.connect(self.on_generate)

    def on_generate(self):
        name = self.name_input.text().strip()
        
        if not name:
            self.result_label.setText("Сначала введите имя")
            return

        nickname = name
        need_year = self.check_year.isChecked()
        need_underscore = self.check_underscore.isChecked()
        current_year = str(datetime.now().year)

        if need_year and need_underscore:
            nickname = f"{name}_{current_year}"
        elif need_year:
            nickname = f"{name}{current_year}"
        elif need_underscore:
            nickname = f"{name}_"
        # Если ни один не включен - никнейм остается просто именем

        self.result_label.setText(nickname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NicknameWindow()
    window.show()
    sys.exit(app.exec())