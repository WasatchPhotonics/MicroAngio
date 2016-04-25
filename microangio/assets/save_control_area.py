# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/save_control_area.ui'
#
# Created: Mon Apr 25 10:04:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 620)
        Form.setMinimumSize(QtCore.QSize(200, 0))
        Form.setMaximumSize(QtCore.QSize(200, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelSnapshotThumbnail = QtGui.QLabel(self.frame)
        self.labelSnapshotThumbnail.setGeometry(QtCore.QRect(30, 220, 131, 91))
        self.labelSnapshotThumbnail.setText("")
        self.labelSnapshotThumbnail.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/Finger1.png"))
        self.labelSnapshotThumbnail.setScaledContents(True)
        self.labelSnapshotThumbnail.setObjectName("labelSnapshotThumbnail")
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 150, 90, 27))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(40, 350, 50, 23))
        self.spinBox.setObjectName("spinBox")
        self.fontComboBox = QtGui.QFontComboBox(self.frame)
        self.fontComboBox.setGeometry(QtCore.QRect(30, 390, 131, 27))
        self.fontComboBox.setObjectName("fontComboBox")
        self.spinBox_2 = QtGui.QSpinBox(self.frame)
        self.spinBox_2.setGeometry(QtCore.QRect(40, 440, 50, 23))
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalSlider = QtGui.QSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 490, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtGui.QSlider(self.frame)
        self.verticalSlider.setGeometry(QtCore.QRect(10, 20, 16, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 30, 59, 15))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 59, 15))
        self.label_2.setObjectName("label_2")
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 530, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(180, 100, 3, 61))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 540, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 582, 141, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 440, 62, 23))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 100, 90, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
