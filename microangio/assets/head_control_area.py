# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/head_control_area.ui'
#
# Created: Mon Apr 25 09:59:12 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1196, 703)
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 671, 50))
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
        self.frame_3.setGeometry(QtCore.QRect(20, 70, 741, 50))
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
        self.frame_5.setGeometry(QtCore.QRect(20, 130, 741, 45))
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
        self.frame_7.setGeometry(QtCore.QRect(30, 190, 741, 45))
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
        self.frame_9.setGeometry(QtCore.QRect(30, 260, 687, 50))
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
        self.comboBox_modeold = QtGui.QComboBox(self.frame_9)
        self.comboBox_modeold.setObjectName("comboBox_modeold")
        self.comboBox_modeold.addItem("")
        self.comboBox_modeold.addItem("")
        self.comboBox_modeold.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_modeold)
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
        self.frame_top_navigation = QtGui.QFrame(Form)
        self.frame_top_navigation.setGeometry(QtCore.QRect(20, 340, 952, 50))
        self.frame_top_navigation.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_top_navigation.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_top_navigation.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top_navigation.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top_navigation.setObjectName("frame_top_navigation")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.frame_top_navigation)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_angio_logo = QtGui.QLabel(self.frame_top_navigation)
        self.label_angio_logo.setText("")
        self.label_angio_logo.setPixmap(QtGui.QPixmap(":/logos/images/logos/110x36_wp_angio.png"))
        self.label_angio_logo.setObjectName("label_angio_logo")
        self.horizontalLayout_16.addWidget(self.label_angio_logo)
        self.comboBox_hidden_mode = QtGui.QComboBox(self.frame_top_navigation)
        self.comboBox_hidden_mode.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_hidden_mode.setObjectName("comboBox_hidden_mode")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.comboBox_hidden_mode.addItem("")
        self.horizontalLayout_16.addWidget(self.comboBox_hidden_mode)
        self.comboBox_mode = QtGui.QComboBox(self.frame_top_navigation)
        self.comboBox_mode.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.horizontalLayout_16.addWidget(self.comboBox_mode)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.frame_11 = QtGui.QFrame(self.frame_top_navigation)
        self.frame_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.frame_11)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_16.addWidget(self.frame_11)
        self.stackedWidgetHeaderNavigation_3 = QtGui.QStackedWidget(self.frame_top_navigation)
        self.stackedWidgetHeaderNavigation_3.setMinimumSize(QtCore.QSize(300, 0))
        self.stackedWidgetHeaderNavigation_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.stackedWidgetHeaderNavigation_3.setObjectName("stackedWidgetHeaderNavigation_3")
        self.page_hardware_2 = QtGui.QWidget()
        self.page_hardware_2.setObjectName("page_hardware_2")
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.page_hardware_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_21 = QtGui.QPushButton(self.page_hardware_2)
        self.pushButton_21.setMinimumSize(QtCore.QSize(85, 0))
        self.pushButton_21.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setChecked(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_18.addWidget(self.pushButton_21)
        spacerItem12 = QtGui.QSpacerItem(210, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem12)
        self.stackedWidgetHeaderNavigation_3.addWidget(self.page_hardware_2)
        self.page_oct_2 = QtGui.QWidget()
        self.page_oct_2.setObjectName("page_oct_2")
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.page_oct_2)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.pushButton_nav_oct_setup = QtGui.QPushButton(self.page_oct_2)
        self.pushButton_nav_oct_setup.setCheckable(True)
        self.pushButton_nav_oct_setup.setObjectName("pushButton_nav_oct_setup")
        self.horizontalLayout_23.addWidget(self.pushButton_nav_oct_setup)
        self.pushButton_nav_oct_capture = QtGui.QPushButton(self.page_oct_2)
        self.pushButton_nav_oct_capture.setCheckable(True)
        self.pushButton_nav_oct_capture.setChecked(True)
        self.pushButton_nav_oct_capture.setObjectName("pushButton_nav_oct_capture")
        self.horizontalLayout_23.addWidget(self.pushButton_nav_oct_capture)
        self.pushButton_22 = QtGui.QPushButton(self.page_oct_2)
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_23.addWidget(self.pushButton_22)
        self.stackedWidgetHeaderNavigation_3.addWidget(self.page_oct_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidgetHeaderNavigation_3.addWidget(self.page_3)
        self.horizontalLayout_16.addWidget(self.stackedWidgetHeaderNavigation_3)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem13)
        self.frame_12 = QtGui.QFrame(Form)
        self.frame_12.setGeometry(QtCore.QRect(10, 410, 841, 60))
        self.frame_12.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem14)
        self.frame_13 = QtGui.QFrame(self.frame_12)
        self.frame_13.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_13.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_24 = QtGui.QHBoxLayout(self.frame_13)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.pushButton_12 = QtGui.QPushButton(self.frame_13)
        self.pushButton_12.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_25.addWidget(self.pushButton_12)
        self.pushButton_19 = QtGui.QPushButton(self.frame_13)
        self.pushButton_19.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon1)
        self.pushButton_19.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setChecked(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_25.addWidget(self.pushButton_19)
        self.pushButton_15 = QtGui.QPushButton(self.frame_13)
        self.pushButton_15.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/full_extent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_15.setCheckable(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_25.addWidget(self.pushButton_15)
        self.pushButton_23 = QtGui.QPushButton(self.frame_13)
        self.pushButton_23.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon3)
        self.pushButton_23.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setChecked(False)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_25.addWidget(self.pushButton_23)
        self.pushButton_24 = QtGui.QPushButton(self.frame_13)
        self.pushButton_24.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/reset.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon4)
        self.pushButton_24.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_24.setCheckable(False)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_25.addWidget(self.pushButton_24)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_19.addWidget(self.frame_13)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem15)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 500, 90, 27))
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(480, 500, 179, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.frame_14 = QtGui.QFrame(Form)
        self.frame_14.setGeometry(QtCore.QRect(90, 550, 484, 100))
        self.frame_14.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.frame_14)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem16)
        self.frame_35 = QtGui.QFrame(self.frame_14)
        self.frame_35.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_35.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_35.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_35.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.frame_35)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.toolButton = QtGui.QToolButton(self.frame_35)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(True)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_14.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(self.frame_35)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setChecked(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_14.addWidget(self.toolButton_2)
        self.toolButton_3 = QtGui.QToolButton(self.frame_35)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_3.setCheckable(False)
        self.toolButton_3.setChecked(False)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_14.addWidget(self.toolButton_3)
        self.toolButton_4 = QtGui.QToolButton(self.frame_35)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_4.setCheckable(False)
        self.toolButton_4.setChecked(False)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_14.addWidget(self.toolButton_4)
        self.toolButton_5 = QtGui.QToolButton(self.frame_35)
        self.toolButton_5.setIcon(icon2)
        self.toolButton_5.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_5.setCheckable(False)
        self.toolButton_5.setChecked(False)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_14.addWidget(self.toolButton_5)
        self.horizontalLayout_21.addWidget(self.frame_35)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem17)

        self.retranslateUi(Form)
        self.comboBox_2.setCurrentIndex(1)
        self.comboBox_modeold.setCurrentIndex(0)
        self.stackedWidgetHeaderNavigation.setCurrentIndex(0)
        self.comboBox_hidden_mode.setCurrentIndex(0)
        self.comboBox_mode.setCurrentIndex(2)
        self.stackedWidgetHeaderNavigation_3.setCurrentIndex(1)
        QtCore.QObject.connect(self.comboBox_modeold, QtCore.SIGNAL("currentIndexChanged(int)"), self.stackedWidgetHeaderNavigation.setCurrentIndex)
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
        self.comboBox_modeold.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_modeold.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_modeold.setItemText(2, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_20.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("Form", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("Form", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(0, QtGui.QApplication.translate("Form", "HS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(1, QtGui.QApplication.translate("Form", "OCTS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(2, QtGui.QApplication.translate("Form", "OCTC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(3, QtGui.QApplication.translate("Form", "OCTEV", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(4, QtGui.QApplication.translate("Form", "AngioS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(5, QtGui.QApplication.translate("Form", "AngioC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(6, QtGui.QApplication.translate("Form", "AngioEV", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(7, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(8, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_hidden_mode.setItemText(9, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(2, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_21.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_nav_oct_setup.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_nav_oct_capture.setText(QtGui.QApplication.translate("Form", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_22.setText(QtGui.QApplication.translate("Form", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("Form", "CommandLinkButton", None, QtGui.QApplication.UnicodeUTF8))

import wasatch_logo_resources_rc
import grey_icons_rc
