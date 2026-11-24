import sys

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class MouseReporter(QWidget):
    mouseButtonPressed = Signal(Qt.MouseButton)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кнопка мыши")
        self.resize(350, 200)

        self.label = QLabel("Нажмите кнопку мыши в окне")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        self.mouseButtonPressed.connect(self.on_mouse_button_pressed)

    def mousePressEvent(self, event):
        self.mouseButtonPressed.emit(event.button())

    @Slot(Qt.MouseButton)
    def on_mouse_button_pressed(self, button: Qt.MouseButton):
        if button == Qt.MouseButton.LeftButton:
            self.label.setText("Левая кнопка")
        elif button == Qt.MouseButton.RightButton:
            self.label.setText("Правая кнопка")
        else:
            self.label.setText("Другая кнопка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseReporter()
    window.show()
    sys.exit(app.exec())
