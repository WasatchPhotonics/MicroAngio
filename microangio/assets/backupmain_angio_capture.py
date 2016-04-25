# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/backupmain_angio_capture.ui'
#
# Created: Mon Apr 25 15:58:57 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1703, 898)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtGui.QFrame(Form)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_main_angio_capture_left = QtGui.QFrame(self.frame_4)
        self.frame_main_angio_capture_left.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_main_angio_capture_left.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_main_angio_capture_left.setStyleSheet("QFrame#frame_main_angio_capture_left  {\n"
" border: 0px solid #444;\n"
" padding: -8px;\n"
"}")
        self.frame_main_angio_capture_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_main_angio_capture_left.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_main_angio_capture_left.setObjectName("frame_main_angio_capture_left")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frame_main_angio_capture_left)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_14 = QtGui.QGroupBox(self.frame_main_angio_capture_left)
        self.groupBox_14.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_14.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox_14.setFlat(False)
        self.groupBox_14.setCheckable(False)
        self.groupBox_14.setChecked(False)
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_23.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_54 = QtGui.QFrame(self.groupBox_14)
        self.frame_54.setMinimumSize(QtCore.QSize(195, 250))
        self.frame_54.setMaximumSize(QtCore.QSize(195, 250))
        self.frame_54.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.labelSnapshotThumbnail_15 = QtGui.QLabel(self.frame_54)
        self.labelSnapshotThumbnail_15.setGeometry(QtCore.QRect(2, 80, 191, 161))
        self.labelSnapshotThumbnail_15.setText("")
        self.labelSnapshotThumbnail_15.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/retina_angiograph_03.jpg"))
        self.labelSnapshotThumbnail_15.setScaledContents(True)
        self.labelSnapshotThumbnail_15.setObjectName("labelSnapshotThumbnail_15")
        self.toolButton_46 = QtGui.QToolButton(self.frame_54)
        self.toolButton_46.setGeometry(QtCore.QRect(7, 17, 40, 40))
        self.toolButton_46.setMinimumSize(QtCore.QSize(30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/badge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_46.setIcon(icon)
        self.toolButton_46.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_46.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_46.setObjectName("toolButton_46")
        self.toolButton_47 = QtGui.QToolButton(self.frame_54)
        self.toolButton_47.setGeometry(QtCore.QRect(49, 17, 40, 40))
        self.toolButton_47.setMinimumSize(QtCore.QSize(30, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_47.setIcon(icon1)
        self.toolButton_47.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_47.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_47.setObjectName("toolButton_47")
        self.toolButton_48 = QtGui.QToolButton(self.frame_54)
        self.toolButton_48.setGeometry(QtCore.QRect(90, 17, 40, 40))
        self.toolButton_48.setMinimumSize(QtCore.QSize(30, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_48.setIcon(icon2)
        self.toolButton_48.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_48.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_48.setObjectName("toolButton_48")
        self.toolButton_49 = QtGui.QToolButton(self.frame_54)
        self.toolButton_49.setGeometry(QtCore.QRect(132, 17, 40, 40))
        self.toolButton_49.setMinimumSize(QtCore.QSize(30, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_49.setIcon(icon3)
        self.toolButton_49.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_49.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_49.setObjectName("toolButton_49")
        self.horizontalLayout_23.addWidget(self.frame_54)
        self.verticalLayout_7.addWidget(self.groupBox_14)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.frame_main_angio_capture_left)
        self.frame_main_angio_capture_center = QtGui.QFrame(self.frame_4)
        self.frame_main_angio_capture_center.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_main_angio_capture_center.setStyleSheet("QFrame#frame_main_angio_capture_center {\n"
" border: 1px solid #444;\n"
" padding: -8px;\n"
"}")
        self.frame_main_angio_capture_center.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_main_angio_capture_center.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_main_angio_capture_center.setObjectName("frame_main_angio_capture_center")
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_main_angio_capture_center)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_34 = QtGui.QFrame(self.frame_main_angio_capture_center)
        self.frame_34.setMinimumSize(QtCore.QSize(0, 750))
        self.frame_34.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.frame_34.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_34)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtGui.QGroupBox(self.frame_34)
        self.groupBox_3.setMinimumSize(QtCore.QSize(373, 337))
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_56 = QtGui.QLabel(self.groupBox_3)
        self.label_56.setMaximumSize(QtCore.QSize(373, 337))
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/square_cat1_retina36s.jpg"))
        self.label_56.setScaledContents(True)
        self.label_56.setObjectName("label_56")
        self.gridLayout_2.addWidget(self.label_56, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.frame_34)
        self.groupBox_5.setMinimumSize(QtCore.QSize(373, 337))
        self.groupBox_5.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_57 = QtGui.QLabel(self.groupBox_5)
        self.label_57.setMinimumSize(QtCore.QSize(650, 650))
        self.label_57.setMaximumSize(QtCore.QSize(650, 650))
        self.label_57.setText("")
        self.label_57.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/retina_angiograph_03.jpg"))
        self.label_57.setScaledContents(True)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout.addWidget(self.label_57)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 1, 2, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.frame_34)
        self.groupBox_4.setMinimumSize(QtCore.QSize(373, 337))
        self.groupBox_4.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_61 = QtGui.QLabel(self.groupBox_4)
        self.label_61.setMaximumSize(QtCore.QSize(373, 337))
        self.label_61.setText("")
        self.label_61.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/square_retina11.jpg"))
        self.label_61.setScaledContents(True)
        self.label_61.setObjectName("label_61")
        self.gridLayout_3.addWidget(self.label_61, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_34, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_main_angio_capture_center)
        self.frame_main_angio_capture_right = QtGui.QFrame(self.frame_4)
        self.frame_main_angio_capture_right.setMinimumSize(QtCore.QSize(220, 500))
        self.frame_main_angio_capture_right.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_main_angio_capture_right.setStyleSheet("QFrame#frame_main_angio_capture_right {\n"
" border: 0px solid #444;\n"
" padding: -8px;\n"
"}")
        self.frame_main_angio_capture_right.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_main_angio_capture_right.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_main_angio_capture_right.setObjectName("frame_main_angio_capture_right")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.frame_main_angio_capture_right)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox = QtGui.QGroupBox(self.frame_main_angio_capture_right)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_39 = QtGui.QFrame(self.groupBox)
        self.frame_39.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_39.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_39.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.spinBox_28 = QtGui.QSpinBox(self.frame_39)
        self.spinBox_28.setGeometry(QtCore.QRect(51, 66, 108, 23))
        self.spinBox_28.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_28.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_28.setSuffix("")
        self.spinBox_28.setMaximum(10000)
        self.spinBox_28.setObjectName("spinBox_28")
        self.toolButton_14 = QtGui.QToolButton(self.frame_39)
        self.toolButton_14.setGeometry(QtCore.QRect(50, 10, 48, 48))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/pure_up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon4)
        self.toolButton_14.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_14.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_14.setObjectName("toolButton_14")
        self.toolButton_15 = QtGui.QToolButton(self.frame_39)
        self.toolButton_15.setGeometry(QtCore.QRect(110, 10, 48, 48))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/pure_down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon5)
        self.toolButton_15.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_15.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_15.setObjectName("toolButton_15")
        self.verticalSlider_2 = QtGui.QSlider(self.frame_39)
        self.verticalSlider_2.setGeometry(QtCore.QRect(20, 10, 16, 81))
        self.verticalSlider_2.setMaximum(999)
        self.verticalSlider_2.setProperty("value", 444)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout_5.addWidget(self.frame_39)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.frame_main_angio_capture_right)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_42 = QtGui.QFrame(self.groupBox_2)
        self.frame_42.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_42.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_42.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.label_34 = QtGui.QLabel(self.frame_42)
        self.label_34.setGeometry(QtCore.QRect(10, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtGui.QLabel(self.frame_42)
        self.label_35.setGeometry(QtCore.QRect(10, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.horizontalSlider_17 = QtGui.QSlider(self.frame_42)
        self.horizontalSlider_17.setGeometry(QtCore.QRect(70, 60, 71, 16))
        self.horizontalSlider_17.setSliderPosition(77)
        self.horizontalSlider_17.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_17.setInvertedAppearance(False)
        self.horizontalSlider_17.setInvertedControls(False)
        self.horizontalSlider_17.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_17.setObjectName("horizontalSlider_17")
        self.spinBox_26 = QtGui.QSpinBox(self.frame_42)
        self.spinBox_26.setGeometry(QtCore.QRect(150, 60, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_26.setFont(font)
        self.spinBox_26.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_26.setProperty("value", 99)
        self.spinBox_26.setObjectName("spinBox_26")
        self.horizontalSlider_18 = QtGui.QSlider(self.frame_42)
        self.horizontalSlider_18.setGeometry(QtCore.QRect(70, 30, 71, 16))
        self.horizontalSlider_18.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_18.setObjectName("horizontalSlider_18")
        self.spinBox_30 = QtGui.QSpinBox(self.frame_42)
        self.spinBox_30.setGeometry(QtCore.QRect(150, 30, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_30.setFont(font)
        self.spinBox_30.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_30.setObjectName("spinBox_30")
        self.horizontalLayout_6.addWidget(self.frame_42)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        spacerItem3 = QtGui.QSpacerItem(175, 49, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.groupBox_8 = QtGui.QGroupBox(self.frame_main_angio_capture_right)
        self.groupBox_8.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox_8.setFlat(False)
        self.groupBox_8.setCheckable(False)
        self.groupBox_8.setChecked(False)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_9.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_45 = QtGui.QFrame(self.groupBox_8)
        self.frame_45.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_45.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_45.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.toolButton_22 = QtGui.QToolButton(self.frame_45)
        self.toolButton_22.setGeometry(QtCore.QRect(70, 80, 48, 48))
        self.toolButton_22.setIcon(icon5)
        self.toolButton_22.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_22.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_22.setObjectName("toolButton_22")
        self.toolButton_23 = QtGui.QToolButton(self.frame_45)
        self.toolButton_23.setGeometry(QtCore.QRect(70, 20, 48, 48))
        self.toolButton_23.setIcon(icon4)
        self.toolButton_23.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_23.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_23.setObjectName("toolButton_23")
        self.toolButton_24 = QtGui.QToolButton(self.frame_45)
        self.toolButton_24.setGeometry(QtCore.QRect(40, 50, 48, 48))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/pure_left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_24.setIcon(icon6)
        self.toolButton_24.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_24.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_24.setObjectName("toolButton_24")
        self.toolButton_25 = QtGui.QToolButton(self.frame_45)
        self.toolButton_25.setGeometry(QtCore.QRect(100, 50, 48, 48))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/pure_right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_25.setIcon(icon7)
        self.toolButton_25.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_25.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_25.setObjectName("toolButton_25")
        self.spinBox_31 = QtGui.QSpinBox(self.frame_45)
        self.spinBox_31.setGeometry(QtCore.QRect(30, 170, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_31.setFont(font)
        self.spinBox_31.setSuffix("")
        self.spinBox_31.setMaximum(360)
        self.spinBox_31.setProperty("value", 300)
        self.spinBox_31.setObjectName("spinBox_31")
        self.spinBox_34 = QtGui.QSpinBox(self.frame_45)
        self.spinBox_34.setGeometry(QtCore.QRect(30, 140, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_34.setFont(font)
        self.spinBox_34.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_34.setSuffix("")
        self.spinBox_34.setMaximum(9999)
        self.spinBox_34.setProperty("value", 5555)
        self.spinBox_34.setObjectName("spinBox_34")
        self.horizontalLayout_9.addWidget(self.frame_45)
        self.verticalLayout_8.addWidget(self.groupBox_8)
        self.groupBox_7 = QtGui.QGroupBox(self.frame_main_angio_capture_right)
        self.groupBox_7.setStyleSheet("QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"  background-color: rgb(50, 50, 50);\n"
"}")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_8.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_46 = QtGui.QFrame(self.groupBox_7)
        self.frame_46.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_46.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_46.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.labelSnapshotThumbnail_9 = QtGui.QLabel(self.frame_46)
        self.labelSnapshotThumbnail_9.setGeometry(QtCore.QRect(2, 0, 191, 161))
        self.labelSnapshotThumbnail_9.setText("")
        self.labelSnapshotThumbnail_9.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_9.setScaledContents(True)
        self.labelSnapshotThumbnail_9.setObjectName("labelSnapshotThumbnail_9")
        self.spinBox_35 = QtGui.QSpinBox(self.frame_46)
        self.spinBox_35.setGeometry(QtCore.QRect(150, 170, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_35.setFont(font)
        self.spinBox_35.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_35.setObjectName("spinBox_35")
        self.horizontalSlider_20 = QtGui.QSlider(self.frame_46)
        self.horizontalSlider_20.setGeometry(QtCore.QRect(70, 170, 71, 16))
        self.horizontalSlider_20.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_20.setObjectName("horizontalSlider_20")
        self.label_37 = QtGui.QLabel(self.frame_46)
        self.label_37.setGeometry(QtCore.QRect(13, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_8.addWidget(self.frame_46)
        self.verticalLayout_8.addWidget(self.groupBox_7)
        self.horizontalLayout_3.addWidget(self.frame_main_angio_capture_right)
        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_14.setTitle(QtGui.QApplication.translate("Form", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_46.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_47.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_48.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_49.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Center B-scan", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Angiograph preview", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Continuous scan preview", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_28.setPrefix(QtGui.QApplication.translate("Form", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_14.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_15.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("Form", "Max. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("Form", "Min. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("Form", "Scan line control", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_22.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_23.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_24.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_25.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_31.setPrefix(QtGui.QApplication.translate("Form", "Angle: ", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_34.setPrefix(QtGui.QApplication.translate("Form", "Length: ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("Form", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("Form", "Exposure", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
import vis_gallery_resources_rc
import colormap_resources_rc
import grey_icons_rc
