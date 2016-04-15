# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/snapshot_widget.ui'
#
# Created: Fri Apr 15 15:03:24 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 647)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 30, 195, 211))
        self.frame.setMinimumSize(QtCore.QSize(195, 0))
        self.frame.setMaximumSize(QtCore.QSize(195, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 31, 26))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 30, 31, 26))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 30, 31, 26))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 30, 31, 26))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.labelSnapshotThumbnail = QtGui.QLabel(self.frame)
        self.labelSnapshotThumbnail.setGeometry(QtCore.QRect(20, 70, 161, 121))
        self.labelSnapshotThumbnail.setText("")
        self.labelSnapshotThumbnail.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/Finger1.png"))
        self.labelSnapshotThumbnail.setScaledContents(True)
        self.labelSnapshotThumbnail.setObjectName("labelSnapshotThumbnail")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "E", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
import oct_gallery_resources_rc
