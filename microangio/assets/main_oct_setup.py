# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/main_oct_setup.ui'
#
# Created: Thu Apr 21 15:39:28 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 758)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(195, 250))
        self.frame_3.setMaximumSize(QtCore.QSize(195, 250))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_42 = QtGui.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(20, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.pushButton_10 = QtGui.QPushButton(self.frame_3)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 190, 31, 26))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(60, 190, 31, 26))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.frame_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_8 = QtGui.QFrame(self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_9 = QtGui.QFrame(self.frame_8)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_9 = QtGui.QLabel(self.frame_9)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_28 = QtGui.QPushButton(self.frame_9)
        self.pushButton_28.setGeometry(QtCore.QRect(330, 40, 91, 61))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtGui.QPushButton(self.frame_9)
        self.pushButton_29.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtGui.QPushButton(self.frame_9)
        self.pushButton_30.setGeometry(QtCore.QRect(230, 40, 91, 61))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtGui.QPushButton(self.frame_9)
        self.pushButton_31.setGeometry(QtCore.QRect(130, 40, 91, 61))
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_4.addWidget(self.frame_9, 2, 0, 1, 1)
        self.frame_10 = QtGui.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_7 = QtGui.QCheckBox(self.frame_10)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_5.addWidget(self.checkBox_7, 2, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame_10)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.frame_10)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_8 = QtGui.QCheckBox(self.frame_10)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_5.addWidget(self.checkBox_8, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_10, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 3, 0, 1, 1)
        self.frame_14 = QtGui.QFrame(self.frame_8)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.frame_19 = QtGui.QFrame(self.frame_14)
        self.frame_19.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_19.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_24 = QtGui.QPushButton(self.frame_19)
        self.pushButton_24.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_24.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setChecked(False)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_18.addWidget(self.pushButton_24)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_16.addWidget(self.frame_19)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.gridLayout_4.addWidget(self.frame_14, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem4 = QtGui.QSpacerItem(175, 617, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.frame_7 = QtGui.QFrame(self.frame_4)
        self.frame_7.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_7.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_5 = QtGui.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_5.setObjectName("label_5")
        self.labelSnapshotThumbnail_6 = QtGui.QLabel(self.frame_7)
        self.labelSnapshotThumbnail_6.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.labelSnapshotThumbnail_6.setText("")
        self.labelSnapshotThumbnail_6.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_6.setScaledContents(True)
        self.labelSnapshotThumbnail_6.setObjectName("labelSnapshotThumbnail_6")
        self.label_24 = QtGui.QLabel(self.frame_7)
        self.label_24.setGeometry(QtCore.QRect(13, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.spinBox_18 = QtGui.QSpinBox(self.frame_7)
        self.spinBox_18.setGeometry(QtCore.QRect(150, 180, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_18.setFont(font)
        self.spinBox_18.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_18.setObjectName("spinBox_18")
        self.horizontalSlider_10 = QtGui.QSlider(self.frame_7)
        self.horizontalSlider_10.setGeometry(QtCore.QRect(70, 180, 71, 16))
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.horizontalLayout.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Saved configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Form", "2016-04-18 07:49", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Form", "Ren", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("Form", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Scan Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_28.setText(QtGui.QApplication.translate("Form", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_29.setText(QtGui.QApplication.translate("Form", "Spiral", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_30.setText(QtGui.QApplication.translate("Form", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_31.setText(QtGui.QApplication.translate("Form", "Rect", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_7.setText(QtGui.QApplication.translate("Form", "Raw OCT data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "OCT Volume Save configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Form", "OCT Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_8.setText(QtGui.QApplication.translate("Form", "Visible Camera image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_24.setText(QtGui.QApplication.translate("Form", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Form", "Exposure", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
import vis_gallery_resources_rc
