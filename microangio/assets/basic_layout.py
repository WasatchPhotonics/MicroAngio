# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/basic_layout.ui'
#
# Created: Thu Apr 21 14:15:52 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayoutLower = QtGui.QHBoxLayout()
        self.horizontalLayoutLower.setObjectName("horizontalLayoutLower")
        self.verticalLayoutSaveArea = QtGui.QVBoxLayout()
        self.verticalLayoutSaveArea.setObjectName("verticalLayoutSaveArea")
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtGui.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.labelSnapshotThumbnail = QtGui.QLabel(self.frame_6)
        self.labelSnapshotThumbnail.setGeometry(QtCore.QRect(30, 220, 131, 91))
        self.labelSnapshotThumbnail.setText("")
        self.labelSnapshotThumbnail.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/Finger1.png"))
        self.labelSnapshotThumbnail.setScaledContents(True)
        self.labelSnapshotThumbnail.setObjectName("labelSnapshotThumbnail")
        self.pushButton = QtGui.QPushButton(self.frame_6)
        self.pushButton.setGeometry(QtCore.QRect(50, 150, 90, 27))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.frame_6)
        self.verticalLayoutSaveArea.addWidget(self.frame_4)
        self.horizontalLayoutLower.addLayout(self.verticalLayoutSaveArea)
        self.verticalLayoutCenterArea = QtGui.QVBoxLayout()
        self.verticalLayoutCenterArea.setSpacing(0)
        self.verticalLayoutCenterArea.setObjectName("verticalLayoutCenterArea")
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(560, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtGui.QStackedWidget(self.frame_2)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton = QtGui.QToolButton(self.page)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(self.page)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton_3 = QtGui.QToolButton(self.page)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout.addWidget(self.toolButton_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.stackedWidget_2 = QtGui.QStackedWidget(self.frame_2)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(self.page_5)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.page_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frameCenterArea = QtGui.QFrame(self.page_6)
        self.frameCenterArea.setMinimumSize(QtCore.QSize(200, 0))
        self.frameCenterArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameCenterArea.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCenterArea.setObjectName("frameCenterArea")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frameCenterArea)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_7 = QtGui.QFrame(self.frameCenterArea)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtGui.QLabel(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/30layerstape_fullsize11.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.horizontalLayout_9.addWidget(self.frame_7)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4.addWidget(self.frameCenterArea)
        self.stackedWidget_2.addWidget(self.page_6)
        self.verticalLayout_2.addWidget(self.stackedWidget_2)
        self.verticalLayoutCenterArea.addWidget(self.frame_2)
        self.horizontalLayoutLower.addLayout(self.verticalLayoutCenterArea)
        self.verticalLayoutControlsArea = QtGui.QVBoxLayout()
        self.verticalLayoutControlsArea.setObjectName("verticalLayoutControlsArea")
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setEnabled(False)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 59, 15))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutControlsArea.addWidget(self.frame_3)
        self.horizontalLayoutLower.addLayout(self.verticalLayoutControlsArea)
        self.verticalLayout.addLayout(self.horizontalLayoutLower)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "MicroAngio", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("MainWindow", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "center iamge area", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Controls Area", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
