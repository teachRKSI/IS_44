import sys

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class CounterWidget(QWidget):
    countChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Счётчик нажатий")
        self.resize(300, 150)

        self.count = 0

        self.label = QLabel(f"Нажатий: {self.count}")
        self.button = QPushButton("Нажать")

        self.button.clicked.connect(self.on_button_clicked)

        self.countChanged.connect(self.on_count_changed)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def on_button_clicked(self):
        self.count += 1
        self.countChanged.emit(self.count)

    @Slot(int)
    def on_count_changed(self, count: int):
        self.label.setText(f"Нажатий: {count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CounterWidget()
    window.show()
    sys.exit(app.exec())
