import sys

from PySide6.QtWidgets import QApplication, QDialog
from ui_task_2 import Ui_Dialog


class ConfirmDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.on_accepted)
        self.buttonBox.rejected.connect(self.on_rejected)

    def on_accepted(self):
        print("Файл удален")
        self.accept()

    def on_rejected(self):
        print("Удаление отменено")
        self.reject()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ConfirmDialog()
    dialog.show()

    result = dialog.exec()
    if result == QDialog.DialogCode.Accepted:
        print("Нажата ok")
    else:
        print("Нажата cancel")
