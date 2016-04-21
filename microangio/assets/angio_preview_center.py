# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/angio_preview_center.ui'
#
# Created: Thu Apr 21 10:45:01 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 487)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_9 = QtGui.QFrame(Form)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 380))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_20 = QtGui.QLabel(self.frame_9)
        self.label_20.setGeometry(QtCore.QRect(769, 32, 373, 337))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/retina_angiograph_03.jpg"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtGui.QLabel(self.frame_9)
        self.label_21.setGeometry(QtCore.QRect(11, 32, 373, 337))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/square_cat1_retina36s.jpg"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtGui.QLabel(self.frame_9)
        self.label_22.setGeometry(QtCore.QRect(390, 32, 373, 337))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/square_retina11.jpg"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label = QtGui.QLabel(self.frame_9)
        self.label.setGeometry(QtCore.QRect(769, 11, 125, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.frame_9)
        self.label_2.setGeometry(QtCore.QRect(390, 11, 158, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.frame_9)
        self.label_3.setGeometry(QtCore.QRect(11, 11, 91, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.frame_9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Angiograph preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Continuous scan preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Center B-scan", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
