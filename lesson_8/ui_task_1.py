# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_1.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 120)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnStart = QPushButton(Widget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setStyleSheet(u"background-color: #4CAF50; color: white; font-weight: bold; font-size: 14px; padding: 10px; border-radius: 6px;")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnPause = QPushButton(Widget)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setStyleSheet(u"background-color: #FF9800; color: white; font-weight: bold; font-size: 14px; padding: 10px; border-radius: 6px;")

        self.horizontalLayout.addWidget(self.btnPause)

        self.btnStop = QPushButton(Widget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setStyleSheet(u"background-color: #F44336; color: white; font-weight: bold; font-size: 14px; padding: 10px; border-radius: 6px;")

        self.horizontalLayout.addWidget(self.btnStop)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1 - \u041a\u043d\u043e\u043f\u043a\u0438", None))
        self.btnStart.setText(QCoreApplication.translate("Widget", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.btnPause.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u0443\u0437\u0430", None))
        self.btnStop.setText(QCoreApplication.translate("Widget", u"\u0421\u0442\u043e\u043f", None))
    # retranslateUi

