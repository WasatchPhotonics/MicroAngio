# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/snapshot_widget.ui'
#
# Created: Tue Apr 26 07:45:37 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 647)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 30, 195, 200))
        self.frame.setMinimumSize(QtCore.QSize(195, 200))
        self.frame.setMaximumSize(QtCore.QSize(195, 200))
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
        self.labelSnapshotThumbnail.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/cat1_retina36s.jpg"))
        self.labelSnapshotThumbnail.setScaledContents(True)
        self.labelSnapshotThumbnail.setObjectName("labelSnapshotThumbnail")
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(50, 270, 195, 250))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(195, 250))
        self.frame_2.setMaximumSize(QtCore.QSize(195, 250))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.labelSnapshotThumbnail_2 = QtGui.QLabel(self.frame_2)
        self.labelSnapshotThumbnail_2.setGeometry(QtCore.QRect(20, 60, 161, 121))
        self.labelSnapshotThumbnail_2.setText("")
        self.labelSnapshotThumbnail_2.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/raw_image_pyqtgraph_plot.png"))
        self.labelSnapshotThumbnail_2.setScaledContents(True)
        self.labelSnapshotThumbnail_2.setObjectName("labelSnapshotThumbnail_2")
        self.label_42 = QtGui.QLabel(self.frame_2)
        self.label_42.setGeometry(QtCore.QRect(20, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.pushButton_10 = QtGui.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 190, 31, 26))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(60, 190, 31, 26))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(270, 270, 195, 251))
        self.frame_3.setMinimumSize(QtCore.QSize(195, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(195, 16777215))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_43 = QtGui.QLabel(self.frame_3)
        self.label_43.setGeometry(QtCore.QRect(20, 40, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.pushButton_12 = QtGui.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 70, 31, 26))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtGui.QPushButton(self.frame_3)
        self.pushButton_13.setGeometry(QtCore.QRect(60, 70, 31, 26))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "Cp", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "Ev", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Saved configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Form", "2016-04-18 07:49", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Form", "Ren", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("Form", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Load Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("Form", "LA OCT Config", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("Form", "Opn", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("Form", "Rel", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
import oct_gallery_resources_rc
