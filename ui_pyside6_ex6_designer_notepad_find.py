# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyside6_ex6_designer_notepad_findSJvMOQ.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(425, 169)
        self.label_findstr = QLabel(Dialog)
        self.label_findstr.setObjectName(u"label_findstr")
        self.label_findstr.setGeometry(QRect(10, 10, 81, 30))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font.setPointSize(10)
        self.label_findstr.setFont(font)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 10, 221, 30))
        self.lineEdit.setFont(font)
        self.pushButton_findnext = QPushButton(Dialog)
        self.pushButton_findnext.setObjectName(u"pushButton_findnext")
        self.pushButton_findnext.setEnabled(False)
        self.pushButton_findnext.setGeometry(QRect(330, 10, 75, 30))
        self.pushButton_findnext.setFont(font)
        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setEnabled(True)
        self.pushButton_cancel.setGeometry(QRect(330, 50, 75, 30))
        self.pushButton_cancel.setFont(font)
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 100, 101, 20))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(30, 120, 101, 20))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(130, 50, 181, 51))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(80, 20, 61, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 20, 51, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\ucc3e\uae30", None))
        self.label_findstr.setText(QCoreApplication.translate("Dialog", u"\ucc3e\uc744 \ub0b4\uc6a9 : ", None))
        self.pushButton_findnext.setText(QCoreApplication.translate("Dialog", u"\ub2e4\uc74c\ucc3e\uae30", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"\ucde8\uc18c", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\ub300\uc18c\ubb38\uc790\uad6c\ubd84", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\uc8fc\uc704\uc5d0 \ubc30\uce58", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\ubc29\ud5a5", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\uc544\ub798\ub85c", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\uc704\ub85c", None))
    # retranslateUi

