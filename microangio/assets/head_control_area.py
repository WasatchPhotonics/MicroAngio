# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/head_control_area.ui'
#
# Created: Wed Apr 20 14:10:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(849, 577)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(70, 40, 661, 50))
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(60, 110, 671, 50))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logos/images/logos/110x36_wp_angio.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(412, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(60, 170, 741, 50))
        self.frame_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/logos/images/logos/110x36_wp_angio.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comboBox_2 = QtGui.QComboBox(self.frame_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtGui.QPushButton(self.frame_4)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.frame_4)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.frame_4)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addWidget(self.frame_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.frame_5 = QtGui.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(50, 240, 741, 45))
        self.frame_5.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.frame_6 = QtGui.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_5 = QtGui.QPushButton(self.frame_6)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.frame_6)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.frame_6)
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_8.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.frame_6)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_8.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.frame_6)
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_8.addWidget(self.pushButton_9)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addWidget(self.frame_6)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.frame_7 = QtGui.QFrame(Form)
        self.frame_7.setGeometry(QtCore.QRect(50, 310, 741, 45))
        self.frame_7.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.frame_8 = QtGui.QFrame(self.frame_7)
        self.frame_8.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_10 = QtGui.QPushButton(self.frame_8)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_11.addWidget(self.pushButton_10)
        self.pushButton_11 = QtGui.QPushButton(self.frame_8)
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_11.addWidget(self.pushButton_11)
        self.pushButton_13 = QtGui.QPushButton(self.frame_8)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_11.addWidget(self.pushButton_13)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9.addWidget(self.frame_8)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.frame_9 = QtGui.QFrame(Form)
        self.frame_9.setGeometry(QtCore.QRect(50, 380, 687, 50))
        self.frame_9.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.frame_9)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/logos/images/logos/110x36_wp_angio.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_mode = QtGui.QComboBox(self.frame_9)
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_mode)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.frame_10 = QtGui.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.stackedWidgetHeaderNavigation = QtGui.QStackedWidget(self.frame_9)
        self.stackedWidgetHeaderNavigation.setMinimumSize(QtCore.QSize(300, 0))
        self.stackedWidgetHeaderNavigation.setFrameShape(QtGui.QFrame.NoFrame)
        self.stackedWidgetHeaderNavigation.setObjectName("stackedWidgetHeaderNavigation")
        self.page_hardware = QtGui.QWidget()
        self.page_hardware.setObjectName("page_hardware")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.page_hardware)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_20 = QtGui.QPushButton(self.page_hardware)
        self.pushButton_20.setMinimumSize(QtCore.QSize(85, 0))
        self.pushButton_20.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setChecked(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_13.addWidget(self.pushButton_20)
        spacerItem9 = QtGui.QSpacerItem(212, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.stackedWidgetHeaderNavigation.addWidget(self.page_hardware)
        self.page_oct = QtGui.QWidget()
        self.page_oct.setObjectName("page_oct")
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.page_oct)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_16 = QtGui.QPushButton(self.page_oct)
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_20.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.page_oct)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setChecked(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_20.addWidget(self.pushButton_17)
        self.pushButton_18 = QtGui.QPushButton(self.page_oct)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_20.addWidget(self.pushButton_18)
        self.stackedWidgetHeaderNavigation.addWidget(self.page_oct)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidgetHeaderNavigation.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidgetHeaderNavigation)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 480, 269, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_19 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(85, 0))
        self.pushButton_19.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setChecked(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_15.addWidget(self.pushButton_19)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 530, 269, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.stackedWidgetHeaderNavigation_2 = QtGui.QStackedWidget(Form)
        self.stackedWidgetHeaderNavigation_2.setGeometry(QtCore.QRect(380, 480, 300, 47))
        self.stackedWidgetHeaderNavigation_2.setMinimumSize(QtCore.QSize(300, 0))
        self.stackedWidgetHeaderNavigation_2.setFrameShape(QtGui.QFrame.Box)
        self.stackedWidgetHeaderNavigation_2.setObjectName("stackedWidgetHeaderNavigation_2")
        self.page_oct_3 = QtGui.QWidget()
        self.page_oct_3.setObjectName("page_oct_3")
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.page_oct_3)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_31 = QtGui.QPushButton(self.page_oct_3)
        self.pushButton_31.setCheckable(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_21.addWidget(self.pushButton_31)
        self.pushButton_32 = QtGui.QPushButton(self.page_oct_3)
        self.pushButton_32.setCheckable(True)
        self.pushButton_32.setChecked(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_21.addWidget(self.pushButton_32)
        self.pushButton_33 = QtGui.QPushButton(self.page_oct_3)
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_21.addWidget(self.pushButton_33)
        self.stackedWidgetHeaderNavigation_2.addWidget(self.page_oct_3)
        self.page_hardware_3 = QtGui.QWidget()
        self.page_hardware_3.setObjectName("page_hardware_3")
        self.horizontalLayout_22 = QtGui.QHBoxLayout(self.page_hardware_3)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pushButton_34 = QtGui.QPushButton(self.page_hardware_3)
        self.pushButton_34.setMinimumSize(QtCore.QSize(85, 0))
        self.pushButton_34.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setChecked(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_22.addWidget(self.pushButton_34)
        spacerItem11 = QtGui.QSpacerItem(210, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem11)
        self.stackedWidgetHeaderNavigation_2.addWidget(self.page_hardware_3)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidgetHeaderNavigation_2.addWidget(self.page_5)

        self.retranslateUi(Form)
        self.comboBox_2.setCurrentIndex(1)
        self.comboBox_mode.setCurrentIndex(0)
        self.stackedWidgetHeaderNavigation.setCurrentIndex(0)
        self.stackedWidgetHeaderNavigation_2.setCurrentIndex(1)
        QtCore.QObject.connect(self.comboBox_mode, QtCore.SIGNAL("currentIndexChanged(int)"), self.stackedWidgetHeaderNavigation.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Form", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Form", "Live", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("Form", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(2, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_20.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("Form", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("Form", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_19.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_31.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_32.setText(QtGui.QApplication.translate("Form", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_33.setText(QtGui.QApplication.translate("Form", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_34.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))

import wasatch_logo_resources_rc
