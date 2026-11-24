# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_3.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 420)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setMinimumSize(QSize(0, 55))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.display.setFont(font)
        self.display.setStyleSheet(u"background-color: #1e1e1e; color: #ffffff; border: 1px solid #444; border-radius: 6px; padding: 6px 10px;")
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.display.setReadOnly(True)

        self.verticalLayout.addWidget(self.display)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setMinimumSize(QSize(0, 45))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.btnClear.setFont(font1)
        self.btnClear.setStyleSheet(u"background-color: #ff9500; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnClear, 0, 0, 1, 1)

        self.btnBackspace = QPushButton(self.centralwidget)
        self.btnBackspace.setObjectName(u"btnBackspace")
        self.btnBackspace.setMinimumSize(QSize(0, 45))
        self.btnBackspace.setFont(font1)
        self.btnBackspace.setStyleSheet(u"background-color: #ff9500; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnBackspace, 0, 1, 1, 1)

        self.btnDiv = QPushButton(self.centralwidget)
        self.btnDiv.setObjectName(u"btnDiv")
        self.btnDiv.setMinimumSize(QSize(0, 45))
        self.btnDiv.setFont(font1)
        self.btnDiv.setStyleSheet(u"background-color: #ff9500; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnDiv, 0, 2, 1, 1)

        self.btnMul = QPushButton(self.centralwidget)
        self.btnMul.setObjectName(u"btnMul")
        self.btnMul.setMinimumSize(QSize(0, 45))
        self.btnMul.setFont(font1)
        self.btnMul.setStyleSheet(u"background-color: #ff9500; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnMul, 0, 3, 1, 1)

        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(0, 45))
        self.btn7.setFont(font1)
        self.btn7.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn7, 1, 0, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(0, 45))
        self.btn8.setFont(font1)
        self.btn8.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn8, 1, 1, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(0, 45))
        self.btn9.setFont(font1)
        self.btn9.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn9, 1, 2, 1, 1)

        self.btnSub = QPushButton(self.centralwidget)
        self.btnSub.setObjectName(u"btnSub")
        self.btnSub.setMinimumSize(QSize(0, 45))
        self.btnSub.setFont(font1)
        self.btnSub.setStyleSheet(u"background-color: #ff9500; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnSub, 1, 3, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(0, 45))
        self.btn4.setFont(font1)
        self.btn4.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(0, 45))
        self.btn5.setFont(font1)
        self.btn5.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)

        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(0, 45))
        self.btn6.setFont(font1)
        self.btn6.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(0, 45))
        self.btnAdd.setFont(font1)
        self.btnAdd.setStyleSheet(u"background-color: #ff9500; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnAdd, 2, 3, 1, 1)

        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(0, 45))
        self.btn1.setFont(font1)
        self.btn1.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn1, 3, 0, 1, 1)

        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(0, 45))
        self.btn2.setFont(font1)
        self.btn2.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn2, 3, 1, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(0, 45))
        self.btn3.setFont(font1)
        self.btn3.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn3, 3, 2, 1, 1)

        self.btnEqual = QPushButton(self.centralwidget)
        self.btnEqual.setObjectName(u"btnEqual")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEqual.sizePolicy().hasHeightForWidth())
        self.btnEqual.setSizePolicy(sizePolicy)
        self.btnEqual.setMinimumSize(QSize(0, 95))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.btnEqual.setFont(font2)
        self.btnEqual.setStyleSheet(u"background-color: #2196f3; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnEqual, 3, 3, 2, 1)

        self.btn0 = QPushButton(self.centralwidget)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setMinimumSize(QSize(0, 45))
        self.btn0.setFont(font1)
        self.btn0.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btn0, 4, 0, 1, 2)

        self.btnDot = QPushButton(self.centralwidget)
        self.btnDot.setObjectName(u"btnDot")
        self.btnDot.setMinimumSize(QSize(0, 45))
        self.btnDot.setFont(font1)
        self.btnDot.setStyleSheet(u"background-color: #4a4a4a; color: white; border-radius: 6px;")

        self.gridLayout.addWidget(self.btnDot, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 24))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.display.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btnBackspace.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.btnDiv.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btnMul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btnSub.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btnEqual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

