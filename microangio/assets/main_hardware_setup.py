# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/main_hardware_setup.ui'
#
# Created: Mon Apr 25 15:59:00 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 888)
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
        self.frame_mhs_saved_config = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_mhs_saved_config.sizePolicy().hasHeightForWidth())
        self.frame_mhs_saved_config.setSizePolicy(sizePolicy)
        self.frame_mhs_saved_config.setMinimumSize(QtCore.QSize(195, 250))
        self.frame_mhs_saved_config.setMaximumSize(QtCore.QSize(195, 250))
        self.frame_mhs_saved_config.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_mhs_saved_config.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_mhs_saved_config.setObjectName("frame_mhs_saved_config")
        self.label_2 = QtGui.QLabel(self.frame_mhs_saved_config)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.labelSnapshotThumbnail_2 = QtGui.QLabel(self.frame_mhs_saved_config)
        self.labelSnapshotThumbnail_2.setGeometry(QtCore.QRect(20, 60, 161, 121))
        self.labelSnapshotThumbnail_2.setText("")
        self.labelSnapshotThumbnail_2.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/raw_image_pyqtgraph_plot.png"))
        self.labelSnapshotThumbnail_2.setScaledContents(True)
        self.labelSnapshotThumbnail_2.setObjectName("labelSnapshotThumbnail_2")
        self.label_42 = QtGui.QLabel(self.frame_mhs_saved_config)
        self.label_42.setGeometry(QtCore.QRect(20, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.pushButton_10 = QtGui.QPushButton(self.frame_mhs_saved_config)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 190, 31, 26))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(self.frame_mhs_saved_config)
        self.pushButton_11.setGeometry(QtCore.QRect(60, 190, 31, 26))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.frame_mhs_saved_config)
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
        self.label = QtGui.QLabel(self.frame_8)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/raw_image_pyqtgraph_plot.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.frame_13 = QtGui.QFrame(self.frame_8)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem1)
        self.frame_15 = QtGui.QFrame(self.frame_13)
        self.frame_15.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.frame_15)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_6 = QtGui.QPushButton(self.frame_15)
        self.pushButton_6.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_18.addWidget(self.pushButton_6)
        self.pushButton_22 = QtGui.QPushButton(self.frame_15)
        self.pushButton_22.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_22.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setChecked(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_18.addWidget(self.pushButton_22)
        self.pushButton_24 = QtGui.QPushButton(self.frame_15)
        self.pushButton_24.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_24.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setChecked(False)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_18.addWidget(self.pushButton_24)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_16.addWidget(self.frame_15)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.gridLayout_4.addWidget(self.frame_13, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_12 = QtGui.QFrame(self.frame_4)
        self.frame_12.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_12.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_21 = QtGui.QLabel(self.frame_12)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_21.setObjectName("label_21")
        self.spinBox_16 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_16.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_16.setFont(font)
        self.spinBox_16.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_16.setProperty("value", 50)
        self.spinBox_16.setObjectName("spinBox_16")
        self.label_22 = QtGui.QLabel(self.frame_12)
        self.label_22.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalSlider_8 = QtGui.QSlider(self.frame_12)
        self.horizontalSlider_8.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_8.setProperty("value", 50)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.horizontalSlider_9 = QtGui.QSlider(self.frame_12)
        self.horizontalSlider_9.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_9.setSliderPosition(77)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setInvertedAppearance(False)
        self.horizontalSlider_9.setInvertedControls(False)
        self.horizontalSlider_9.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.label_23 = QtGui.QLabel(self.frame_12)
        self.label_23.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.spinBox_17 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_17.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_17.setFont(font)
        self.spinBox_17.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_17.setMaximum(100)
        self.spinBox_17.setProperty("value", 100)
        self.spinBox_17.setObjectName("spinBox_17")
        self.spinBox_25 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_25.setGeometry(QtCore.QRect(150, 100, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_25.setFont(font)
        self.spinBox_25.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_25.setMaximum(100)
        self.spinBox_25.setProperty("value", 100)
        self.spinBox_25.setObjectName("spinBox_25")
        self.horizontalSlider_15 = QtGui.QSlider(self.frame_12)
        self.horizontalSlider_15.setGeometry(QtCore.QRect(70, 100, 71, 16))
        self.horizontalSlider_15.setSliderPosition(77)
        self.horizontalSlider_15.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_15.setInvertedAppearance(False)
        self.horizontalSlider_15.setInvertedControls(False)
        self.horizontalSlider_15.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_15.setObjectName("horizontalSlider_15")
        self.label_33 = QtGui.QLabel(self.frame_12)
        self.label_33.setGeometry(QtCore.QRect(10, 100, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.spinBox_32 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_32.setGeometry(QtCore.QRect(150, 130, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_32.setFont(font)
        self.spinBox_32.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_32.setMaximum(100)
        self.spinBox_32.setProperty("value", 100)
        self.spinBox_32.setObjectName("spinBox_32")
        self.horizontalSlider_22 = QtGui.QSlider(self.frame_12)
        self.horizontalSlider_22.setGeometry(QtCore.QRect(70, 130, 71, 16))
        self.horizontalSlider_22.setSliderPosition(77)
        self.horizontalSlider_22.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_22.setInvertedAppearance(False)
        self.horizontalSlider_22.setInvertedControls(False)
        self.horizontalSlider_22.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_22.setObjectName("horizontalSlider_22")
        self.label_45 = QtGui.QLabel(self.frame_12)
        self.label_45.setGeometry(QtCore.QRect(10, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_2.addWidget(self.frame_12)
        self.frame_11 = QtGui.QFrame(self.frame_4)
        self.frame_11.setMinimumSize(QtCore.QSize(195, 150))
        self.frame_11.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_20 = QtGui.QLabel(self.frame_11)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_20.setObjectName("label_20")
        self.verticalScrollBar_2 = QtGui.QScrollBar(self.frame_11)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(20, 40, 16, 91))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.pushButton_16 = QtGui.QPushButton(self.frame_11)
        self.pushButton_16.setGeometry(QtCore.QRect(50, 40, 41, 27))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtGui.QPushButton(self.frame_11)
        self.pushButton_17.setGeometry(QtCore.QRect(50, 110, 41, 27))
        self.pushButton_17.setObjectName("pushButton_17")
        self.spinBox_15 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_15.setGeometry(QtCore.QRect(50, 70, 91, 31))
        self.spinBox_15.setSuffix("")
        self.spinBox_15.setMaximum(10000)
        self.spinBox_15.setObjectName("spinBox_15")
        self.verticalLayout_2.addWidget(self.frame_11)
        self.frame_14 = QtGui.QFrame(self.frame_4)
        self.frame_14.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_14.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_25 = QtGui.QLabel(self.frame_14)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_25.setObjectName("label_25")
        self.pushButton_18 = QtGui.QPushButton(self.frame_14)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 30, 51, 27))
        self.pushButton_18.setObjectName("pushButton_18")
        self.spinBox_33 = QtGui.QSpinBox(self.frame_14)
        self.spinBox_33.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_33.setFont(font)
        self.spinBox_33.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_33.setMaximum(100)
        self.spinBox_33.setProperty("value", 100)
        self.spinBox_33.setObjectName("spinBox_33")
        self.horizontalSlider_23 = QtGui.QSlider(self.frame_14)
        self.horizontalSlider_23.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_23.setSliderPosition(77)
        self.horizontalSlider_23.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_23.setInvertedAppearance(False)
        self.horizontalSlider_23.setInvertedControls(False)
        self.horizontalSlider_23.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_23.setObjectName("horizontalSlider_23")
        self.label_46 = QtGui.QLabel(self.frame_14)
        self.label_46.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_2.addWidget(self.frame_14)
        spacerItem3 = QtGui.QSpacerItem(175, 149, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
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
        self.spinBox_18.setGeometry(QtCore.QRect(150, 180, 77, 16))
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
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Saved configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Form", "2016-04-18 07:49", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Form", "Ren", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("Form", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_22.setText(QtGui.QApplication.translate("Form", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_24.setText(QtGui.QApplication.translate("Form", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Form", "OCT Camera Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Form", "Int. Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Form", "Line Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("Form", "Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("Form", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Form", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("Form", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("Form", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_15.setPrefix(QtGui.QApplication.translate("Form", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Form", "Light source", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("Form", "Off/On", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("Form", "Power", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Form", "Exposure", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
import style_rc
import vis_gallery_resources_rc
