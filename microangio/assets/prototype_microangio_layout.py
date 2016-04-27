# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/prototype_microangio_layout.ui'
#
# Created: Wed Apr 27 06:48:28 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1315, 967)
        MainWindow.setStyleSheet("/*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"\n"
"/* NJH Modifications for microangio ux:\n"
"main background color: rgb(56, 56, 56)\n"
"vertical slider background none at widget level\n"
"spinbox minimum width to 50 (looks ok if you turn the arrows off)\n"
"*/\n"
"\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: rgb(56, 56, 56);\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/qss_icons/rc/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 5px 30px 5px 30px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/qss_icons/rc/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/qss_icons/rc/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/qss_icons/rc/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/qss_icons/rc/close.png);\n"
"    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    border: 1px solid #444;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover\n"
"{\n"
"    background: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/qss_icons/rc/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/qss_icons/rc/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider {\n"
"    background: none;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px transparent #4A4949;\n"
"    border-radius: 2px;\n"
"    margin: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 1px transparent #4A4949;\n"
" border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 1px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    background-color: transparent;\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"        QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 8px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #444;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget_top = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget_top.setMaximumSize(QtCore.QSize(16777215, 70))
        self.stackedWidget_top.setObjectName("stackedWidget_top")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_main_navigation = QtGui.QFrame(self.page)
        self.frame_main_navigation.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_main_navigation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_main_navigation.setStyleSheet("border: none;")
        self.frame_main_navigation.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_main_navigation.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_main_navigation.setObjectName("frame_main_navigation")
        self.frame_nav_buttonbar = QtGui.QFrame(self.frame_main_navigation)
        self.frame_nav_buttonbar.setGeometry(QtCore.QRect(260, 8, 671, 43))
        self.frame_nav_buttonbar.setStyleSheet("QFrame {\n"
"    border-style: solid;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    background: none;\n"
"}")
        self.frame_nav_buttonbar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_nav_buttonbar.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_nav_buttonbar.setLineWidth(1)
        self.frame_nav_buttonbar.setObjectName("frame_nav_buttonbar")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_nav_buttonbar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_setup = QtGui.QPushButton(self.frame_nav_buttonbar)
        self.pushButton_setup.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_setup.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_setup.setFont(font)
        self.pushButton_setup.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton {\n"
"    /* Grey Inactive */\n"
"    background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"    border-radius: 0px;\n"
"    border-top-left-radius: 12px;\n"
"    border-bottom-left-radius: 12px;\n"
"}")
        self.pushButton_setup.setObjectName("pushButton_setup")
        self.horizontalLayout_6.addWidget(self.pushButton_setup)
        self.pushButton_capture = QtGui.QPushButton(self.frame_nav_buttonbar)
        self.pushButton_capture.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_capture.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_capture.setFont(font)
        self.pushButton_capture.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton {\n"
"    /* Grey Inactive */\n"
"    border-color: rgb(0,0,0);\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 0px;\n"
"}")
        self.pushButton_capture.setCheckable(False)
        self.pushButton_capture.setChecked(False)
        self.pushButton_capture.setObjectName("pushButton_capture")
        self.horizontalLayout_6.addWidget(self.pushButton_capture)
        self.pushButton_evaluate = QtGui.QPushButton(self.frame_nav_buttonbar)
        self.pushButton_evaluate.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_evaluate.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_evaluate.setFont(font)
        self.pushButton_evaluate.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton {\n"
"    /* Grey Inactive */\n"
"    background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"}")
        self.pushButton_evaluate.setObjectName("pushButton_evaluate")
        self.horizontalLayout_6.addWidget(self.pushButton_evaluate)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_angio_logo = QtGui.QLabel(self.frame_main_navigation)
        self.label_angio_logo.setGeometry(QtCore.QRect(0, 10, 109, 38))
        self.label_angio_logo.setStyleSheet("background-color: none;\n"
"border-color: none;\n"
"border: none;")
        self.label_angio_logo.setText("")
        self.label_angio_logo.setPixmap(QtGui.QPixmap(":/logos/images/logos/92x30_wp_angio.png"))
        self.label_angio_logo.setScaledContents(True)
        self.label_angio_logo.setObjectName("label_angio_logo")
        self.comboBox_mode_navigation = QtGui.QComboBox(self.frame_main_navigation)
        self.comboBox_mode_navigation.setGeometry(QtCore.QRect(109, 14, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_mode_navigation.setFont(font)
        self.comboBox_mode_navigation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_mode_navigation.setStyleSheet("QComboBox:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"\n"
"}")
        self.comboBox_mode_navigation.setObjectName("comboBox_mode_navigation")
        self.comboBox_mode_navigation.addItem("")
        self.comboBox_mode_navigation.addItem("")
        self.comboBox_mode_navigation.addItem("")
        self.comboBox_selector = QtGui.QComboBox(self.frame_main_navigation)
        self.comboBox_selector.setGeometry(QtCore.QRect(1000, 10, 121, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_selector.setFont(font)
        self.comboBox_selector.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_selector.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"\n"
"}")
        self.comboBox_selector.setObjectName("comboBox_selector")
        self.comboBox_selector.addItem("")
        self.comboBox_selector.addItem("")
        self.comboBox_selector.addItem("")
        self.comboBox_selector.addItem("")
        self.comboBox_selector.addItem("")
        self.pushButton_hidden = QtGui.QPushButton(self.frame_main_navigation)
        self.pushButton_hidden.setGeometry(QtCore.QRect(1129, 6, 101, 41))
        self.pushButton_hidden.setStyleSheet("background: none;")
        self.pushButton_hidden.setText("")
        self.pushButton_hidden.setObjectName("pushButton_hidden")
        self.pushButton_capture_hidden_red = QtGui.QPushButton(self.frame_main_navigation)
        self.pushButton_capture_hidden_red.setGeometry(QtCore.QRect(860, 10, 130, 30))
        self.pushButton_capture_hidden_red.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_capture_hidden_red.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_capture_hidden_red.setFont(font)
        self.pushButton_capture_hidden_red.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.512195, y2:0, stop:0 rgba(137, 10, 10, 255), stop:1 rgba(186, 10, 10, 255));\n"
"border-radius: 0px;\n"
"}")
        self.pushButton_capture_hidden_red.setCheckable(False)
        self.pushButton_capture_hidden_red.setChecked(False)
        self.pushButton_capture_hidden_red.setObjectName("pushButton_capture_hidden_red")
        self.horizontalLayout.addWidget(self.frame_main_navigation)
        self.stackedWidget_top.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_top.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget_top)
        self.stackedWidget_bottom = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget_bottom.setStyleSheet("border:none;")
        self.stackedWidget_bottom.setObjectName("stackedWidget_bottom")
        self.page_hardware_setup = QtGui.QWidget()
        self.page_hardware_setup.setObjectName("page_hardware_setup")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.page_hardware_setup)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_hardware_setup_main = QtGui.QFrame(self.page_hardware_setup)
        self.frame_hardware_setup_main.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_hardware_setup_main.setStyleSheet("QFrame#frame_center_nest {\n"
"    /*border: 1px solid #ff0000;*/\n"
"    border: none;\n"
"}")
        self.frame_hardware_setup_main.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_hardware_setup_main.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_hardware_setup_main.setLineWidth(1)
        self.frame_hardware_setup_main.setObjectName("frame_hardware_setup_main")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_hardware_setup_main)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_white_border_12 = QtGui.QFrame(self.frame_hardware_setup_main)
        self.frame_white_border_12.setMinimumSize(QtCore.QSize(225, 0))
        self.frame_white_border_12.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_white_border_12.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_12.setLineWidth(1)
        self.frame_white_border_12.setObjectName("frame_white_border_12")
        self.gridLayout_16 = QtGui.QGridLayout(self.frame_white_border_12)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.frame_center_nest_8 = QtGui.QFrame(self.frame_white_border_12)
        self.frame_center_nest_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_center_nest_8.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_8.setLineWidth(1)
        self.frame_center_nest_8.setObjectName("frame_center_nest_8")
        self.frame_14 = QtGui.QFrame(self.frame_center_nest_8)
        self.frame_14.setGeometry(QtCore.QRect(7, 10, 211, 241))
        self.frame_14.setStyleSheet("border: none;")
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_15 = QtGui.QLabel(self.frame_14)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border: none;")
        self.label_15.setObjectName("label_15")
        self.frame_76 = QtGui.QFrame(self.frame_14)
        self.frame_76.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_76.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_76.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_76.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_76.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_76.setObjectName("frame_76")
        self.frame_77 = QtGui.QFrame(self.frame_76)
        self.frame_77.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_77.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_77.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_77.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_77.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.labelSnapshotThumbnail_15 = QtGui.QLabel(self.frame_77)
        self.labelSnapshotThumbnail_15.setGeometry(QtCore.QRect(13, 32, 151, 121))
        self.labelSnapshotThumbnail_15.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_15.setText("")
        self.labelSnapshotThumbnail_15.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/raw_image_pyqtgraph_plot.png"))
        self.labelSnapshotThumbnail_15.setScaledContents(True)
        self.labelSnapshotThumbnail_15.setObjectName("labelSnapshotThumbnail_15")
        self.label_30 = QtGui.QLabel(self.frame_77)
        self.label_30.setGeometry(QtCore.QRect(15, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("border: none;\n"
"background:none;")
        self.label_30.setObjectName("label_30")
        self.pushButton_69 = QtGui.QPushButton(self.frame_77)
        self.pushButton_69.setGeometry(QtCore.QRect(14, 160, 35, 30))
        self.pushButton_69.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_69.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_69.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_rename.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_69.setIcon(icon)
        self.pushButton_69.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtGui.QPushButton(self.frame_77)
        self.pushButton_70.setGeometry(QtCore.QRect(60, 160, 35, 30))
        self.pushButton_70.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_70.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_70.setFont(font)
        self.pushButton_70.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_70.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/1opc_gray_trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_70.setIcon(icon1)
        self.pushButton_70.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_70.setObjectName("pushButton_70")
        self.gridLayout_16.addWidget(self.frame_center_nest_8, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_white_border_12)
        self.frame_white_border_2 = QtGui.QFrame(self.frame_hardware_setup_main)
        self.frame_white_border_2.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_white_border_2.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_2.setLineWidth(1)
        self.frame_white_border_2.setObjectName("frame_white_border_2")
        self.gridLayout_17 = QtGui.QGridLayout(self.frame_white_border_2)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.frame_center_nest_5 = QtGui.QFrame(self.frame_white_border_2)
        self.frame_center_nest_5.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_center_nest_5.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_5.setLineWidth(1)
        self.frame_center_nest_5.setObjectName("frame_center_nest_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_center_nest_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_white_border_9 = QtGui.QFrame(self.frame_center_nest_5)
        self.frame_white_border_9.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_white_border_9.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_9.setLineWidth(1)
        self.frame_white_border_9.setObjectName("frame_white_border_9")
        self.gridLayout_18 = QtGui.QGridLayout(self.frame_white_border_9)
        self.gridLayout_18.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.frame_button_bar_6 = QtGui.QFrame(self.frame_white_border_9)
        self.frame_button_bar_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_6.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_6.setLineWidth(1)
        self.frame_button_bar_6.setObjectName("frame_button_bar_6")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_button_bar_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.frame_24 = QtGui.QFrame(self.frame_button_bar_6)
        self.frame_24.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_24.setStyleSheet("border: none; background: none;")
        self.frame_24.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.pushButton_135 = QtGui.QPushButton(self.frame_24)
        self.pushButton_135.setGeometry(QtCore.QRect(100, 3, 67, 30))
        self.pushButton_135.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_135.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_135.setFont(font)
        self.pushButton_135.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_135.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_135.setIcon(icon2)
        self.pushButton_135.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_135.setObjectName("pushButton_135")
        self.pushButton_136 = QtGui.QPushButton(self.frame_24)
        self.pushButton_136.setGeometry(QtCore.QRect(247, 3, 67, 30))
        self.pushButton_136.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_136.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_136.setFont(font)
        self.pushButton_136.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_136.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_136.setIcon(icon3)
        self.pushButton_136.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_136.setObjectName("pushButton_136")
        self.pushButton_139 = QtGui.QPushButton(self.frame_24)
        self.pushButton_139.setGeometry(QtCore.QRect(173, 3, 67, 30))
        self.pushButton_139.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_139.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_139.setFont(font)
        self.pushButton_139.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_139.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_139.setIcon(icon4)
        self.pushButton_139.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_139.setObjectName("pushButton_139")
        self.horizontalLayout_7.addWidget(self.frame_24)
        spacerItem2 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_18.addWidget(self.frame_button_bar_6, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_white_border_9)
        self.frame_white_border_13 = QtGui.QFrame(self.frame_center_nest_5)
        self.frame_white_border_13.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_white_border_13.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_13.setLineWidth(1)
        self.frame_white_border_13.setObjectName("frame_white_border_13")
        self.gridLayout_19 = QtGui.QGridLayout(self.frame_white_border_13)
        self.gridLayout_19.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.frame_button_bar_12 = QtGui.QFrame(self.frame_white_border_13)
        self.frame_button_bar_12.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_12.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_12.setLineWidth(1)
        self.frame_button_bar_12.setObjectName("frame_button_bar_12")
        self.gridLayout_20 = QtGui.QGridLayout(self.frame_button_bar_12)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_7 = QtGui.QLabel(self.frame_button_bar_12)
        self.label_7.setStyleSheet("border: none;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/raw_image_pyqtgraph_plot.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_20.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.frame_button_bar_12, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_white_border_13)
        self.gridLayout_17.addWidget(self.frame_center_nest_5, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_white_border_2)
        self.frame_white_border_14 = QtGui.QFrame(self.frame_hardware_setup_main)
        self.frame_white_border_14.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_white_border_14.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_white_border_14.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_14.setLineWidth(1)
        self.frame_white_border_14.setObjectName("frame_white_border_14")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.frame_white_border_14)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_center_nest_6 = QtGui.QFrame(self.frame_white_border_14)
        self.frame_center_nest_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_6.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_center_nest_6.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_6.setLineWidth(1)
        self.frame_center_nest_6.setObjectName("frame_center_nest_6")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_center_nest_6)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(3, -1, 0, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_15 = QtGui.QFrame(self.frame_center_nest_6)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_15.setStyleSheet("border: none;")
        self.frame_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_20 = QtGui.QLabel(self.frame_15)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("border: none;")
        self.label_20.setObjectName("label_20")
        self.frame_white_border_15 = QtGui.QFrame(self.frame_15)
        self.frame_white_border_15.setGeometry(QtCore.QRect(10, 34, 190, 170))
        self.frame_white_border_15.setMinimumSize(QtCore.QSize(190, 170))
        self.frame_white_border_15.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_white_border_15.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_15.setLineWidth(1)
        self.frame_white_border_15.setObjectName("frame_white_border_15")
        self.gridLayout_21 = QtGui.QGridLayout(self.frame_white_border_15)
        self.gridLayout_21.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.frame_button_bar_10 = QtGui.QFrame(self.frame_white_border_15)
        self.frame_button_bar_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_10.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_10.setLineWidth(1)
        self.frame_button_bar_10.setObjectName("frame_button_bar_10")
        self.spinBox_16 = QtGui.QSpinBox(self.frame_button_bar_10)
        self.spinBox_16.setGeometry(QtCore.QRect(134, 30, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_16.setFont(font)
        self.spinBox_16.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_16.setProperty("value", 50)
        self.spinBox_16.setObjectName("spinBox_16")
        self.horizontalSlider_9 = QtGui.QSlider(self.frame_button_bar_10)
        self.horizontalSlider_9.setGeometry(QtCore.QRect(66, 30, 65, 16))
        self.horizontalSlider_9.setProperty("value", 50)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.label_25 = QtGui.QLabel(self.frame_button_bar_10)
        self.label_25.setGeometry(QtCore.QRect(8, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("border: none; background: none;")
        self.label_25.setObjectName("label_25")
        self.spinBox_17 = QtGui.QSpinBox(self.frame_button_bar_10)
        self.spinBox_17.setGeometry(QtCore.QRect(134, 60, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_17.setFont(font)
        self.spinBox_17.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_17.setProperty("value", 50)
        self.spinBox_17.setObjectName("spinBox_17")
        self.label_27 = QtGui.QLabel(self.frame_button_bar_10)
        self.label_27.setGeometry(QtCore.QRect(8, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("border: none; background: none;")
        self.label_27.setObjectName("label_27")
        self.horizontalSlider_10 = QtGui.QSlider(self.frame_button_bar_10)
        self.horizontalSlider_10.setGeometry(QtCore.QRect(66, 60, 65, 16))
        self.horizontalSlider_10.setProperty("value", 50)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")
        self.horizontalSlider_11 = QtGui.QSlider(self.frame_button_bar_10)
        self.horizontalSlider_11.setGeometry(QtCore.QRect(66, 90, 65, 16))
        self.horizontalSlider_11.setProperty("value", 50)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.label_28 = QtGui.QLabel(self.frame_button_bar_10)
        self.label_28.setGeometry(QtCore.QRect(8, 90, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("border: none; background: none;")
        self.label_28.setObjectName("label_28")
        self.spinBox_18 = QtGui.QSpinBox(self.frame_button_bar_10)
        self.spinBox_18.setGeometry(QtCore.QRect(134, 90, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_18.setFont(font)
        self.spinBox_18.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_18.setProperty("value", 50)
        self.spinBox_18.setObjectName("spinBox_18")
        self.spinBox_19 = QtGui.QSpinBox(self.frame_button_bar_10)
        self.spinBox_19.setGeometry(QtCore.QRect(134, 124, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_19.setFont(font)
        self.spinBox_19.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_19.setProperty("value", 50)
        self.spinBox_19.setObjectName("spinBox_19")
        self.label_31 = QtGui.QLabel(self.frame_button_bar_10)
        self.label_31.setGeometry(QtCore.QRect(8, 124, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("border: none; background: none;")
        self.label_31.setObjectName("label_31")
        self.horizontalSlider_12 = QtGui.QSlider(self.frame_button_bar_10)
        self.horizontalSlider_12.setGeometry(QtCore.QRect(66, 124, 65, 16))
        self.horizontalSlider_12.setProperty("value", 50)
        self.horizontalSlider_12.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_12.setObjectName("horizontalSlider_12")
        self.gridLayout_21.addWidget(self.frame_button_bar_10, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_15)
        self.frame_17 = QtGui.QFrame(self.frame_center_nest_6)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 165))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_17.setStyleSheet("border: none;")
        self.frame_17.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_23 = QtGui.QLabel(self.frame_17)
        self.label_23.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("border: none;")
        self.label_23.setObjectName("label_23")
        self.frame_white_border_16 = QtGui.QFrame(self.frame_17)
        self.frame_white_border_16.setGeometry(QtCore.QRect(10, 34, 190, 120))
        self.frame_white_border_16.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_white_border_16.setMaximumSize(QtCore.QSize(190, 140))
        self.frame_white_border_16.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_16.setLineWidth(1)
        self.frame_white_border_16.setObjectName("frame_white_border_16")
        self.gridLayout_22 = QtGui.QGridLayout(self.frame_white_border_16)
        self.gridLayout_22.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.frame_button_bar_11 = QtGui.QFrame(self.frame_white_border_16)
        self.frame_button_bar_11.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_11.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_11.setLineWidth(1)
        self.frame_button_bar_11.setObjectName("frame_button_bar_11")
        self.verticalSlider_17 = QtGui.QSlider(self.frame_button_bar_11)
        self.verticalSlider_17.setGeometry(QtCore.QRect(14, 20, 16, 81))
        self.verticalSlider_17.setMaximum(999)
        self.verticalSlider_17.setProperty("value", 444)
        self.verticalSlider_17.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_17.setObjectName("verticalSlider_17")
        self.pushButton_54 = QtGui.QPushButton(self.frame_button_bar_11)
        self.pushButton_54.setGeometry(QtCore.QRect(116, 30, 50, 30))
        self.pushButton_54.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_54.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_54.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_54.setIcon(icon5)
        self.pushButton_54.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_54.setObjectName("pushButton_54")
        self.spinBox_43 = QtGui.QSpinBox(self.frame_button_bar_11)
        self.spinBox_43.setGeometry(QtCore.QRect(57, 76, 108, 23))
        self.spinBox_43.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_43.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_43.setSuffix("")
        self.spinBox_43.setMaximum(10000)
        self.spinBox_43.setObjectName("spinBox_43")
        self.pushButton_55 = QtGui.QPushButton(self.frame_button_bar_11)
        self.pushButton_55.setGeometry(QtCore.QRect(56, 30, 50, 30))
        self.pushButton_55.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_55.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_55.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_55.setIcon(icon6)
        self.pushButton_55.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout_22.addWidget(self.frame_button_bar_11, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_17)
        self.frame_18 = QtGui.QFrame(self.frame_center_nest_6)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 130))
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_18.setStyleSheet("border: none;")
        self.frame_18.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_36 = QtGui.QLabel(self.frame_18)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("border: none;")
        self.label_36.setObjectName("label_36")
        self.frame_white_border_17 = QtGui.QFrame(self.frame_18)
        self.frame_white_border_17.setGeometry(QtCore.QRect(10, 34, 190, 80))
        self.frame_white_border_17.setMinimumSize(QtCore.QSize(190, 50))
        self.frame_white_border_17.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_white_border_17.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_17.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_17.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_17.setLineWidth(1)
        self.frame_white_border_17.setObjectName("frame_white_border_17")
        self.gridLayout_23 = QtGui.QGridLayout(self.frame_white_border_17)
        self.gridLayout_23.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.frame_button_bar_13 = QtGui.QFrame(self.frame_white_border_17)
        self.frame_button_bar_13.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_13.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_13.setLineWidth(1)
        self.frame_button_bar_13.setObjectName("frame_button_bar_13")
        self.spinBox_27 = QtGui.QSpinBox(self.frame_button_bar_13)
        self.spinBox_27.setGeometry(QtCore.QRect(134, 50, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_27.setFont(font)
        self.spinBox_27.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_27.setProperty("value", 50)
        self.spinBox_27.setObjectName("spinBox_27")
        self.label_42 = QtGui.QLabel(self.frame_button_bar_13)
        self.label_42.setGeometry(QtCore.QRect(8, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("border: none; background: none;")
        self.label_42.setObjectName("label_42")
        self.horizontalSlider_20 = QtGui.QSlider(self.frame_button_bar_13)
        self.horizontalSlider_20.setGeometry(QtCore.QRect(66, 50, 65, 16))
        self.horizontalSlider_20.setProperty("value", 50)
        self.horizontalSlider_20.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_20.setObjectName("horizontalSlider_20")
        self.pushButton_71 = QtGui.QPushButton(self.frame_button_bar_13)
        self.pushButton_71.setGeometry(QtCore.QRect(10, 10, 35, 30))
        self.pushButton_71.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_71.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_71.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_power_onoff_active.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_power_onoff.svg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_71.setIcon(icon7)
        self.pushButton_71.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_71.setCheckable(True)
        self.pushButton_71.setObjectName("pushButton_71")
        self.gridLayout_23.addWidget(self.frame_button_bar_13, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_18)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.frame_16 = QtGui.QFrame(self.frame_center_nest_6)
        self.frame_16.setMinimumSize(QtCore.QSize(0, 232))
        self.frame_16.setStyleSheet("border: none;")
        self.frame_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_29 = QtGui.QLabel(self.frame_16)
        self.label_29.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("border: none;")
        self.label_29.setObjectName("label_29")
        self.frame_80 = QtGui.QFrame(self.frame_16)
        self.frame_80.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_80.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_80.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_80.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_80.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_80.setObjectName("frame_80")
        self.frame_81 = QtGui.QFrame(self.frame_80)
        self.frame_81.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_81.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_81.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_81.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_81.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.labelSnapshotThumbnail_13 = QtGui.QLabel(self.frame_81)
        self.labelSnapshotThumbnail_13.setGeometry(QtCore.QRect(3, 3, 182, 158))
        self.labelSnapshotThumbnail_13.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_13.setText("")
        self.labelSnapshotThumbnail_13.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_13.setScaledContents(True)
        self.labelSnapshotThumbnail_13.setObjectName("labelSnapshotThumbnail_13")
        self.label_41 = QtGui.QLabel(self.frame_81)
        self.label_41.setGeometry(QtCore.QRect(6, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("border:none; background: none;")
        self.label_41.setObjectName("label_41")
        self.horizontalSlider_24 = QtGui.QSlider(self.frame_81)
        self.horizontalSlider_24.setGeometry(QtCore.QRect(63, 170, 65, 16))
        self.horizontalSlider_24.setProperty("value", 22)
        self.horizontalSlider_24.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_24.setObjectName("horizontalSlider_24")
        self.spinBox_53 = QtGui.QSpinBox(self.frame_81)
        self.spinBox_53.setGeometry(QtCore.QRect(133, 168, 50, 20))
        self.spinBox_53.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_53.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_53.setFont(font)
        self.spinBox_53.setStyleSheet("")
        self.spinBox_53.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_53.setProperty("value", 77)
        self.spinBox_53.setObjectName("spinBox_53")
        self.verticalLayout_4.addWidget(self.frame_16)
        self.verticalLayout_10.addWidget(self.frame_center_nest_6)
        self.horizontalLayout_4.addWidget(self.frame_white_border_14)
        self.horizontalLayout_8.addWidget(self.frame_hardware_setup_main)
        self.stackedWidget_bottom.addWidget(self.page_hardware_setup)
        self.page_oct_setup = QtGui.QWidget()
        self.page_oct_setup.setObjectName("page_oct_setup")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.page_oct_setup)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_oct_setup = QtGui.QFrame(self.page_oct_setup)
        self.frame_oct_setup.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_oct_setup.setStyleSheet("QFrame#frame_center_nest {\n"
"    /*border: 1px solid #ff0000;*/\n"
"    border: none;\n"
"}")
        self.frame_oct_setup.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_oct_setup.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_oct_setup.setLineWidth(1)
        self.frame_oct_setup.setObjectName("frame_oct_setup")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_oct_setup)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_white_border_18 = QtGui.QFrame(self.frame_oct_setup)
        self.frame_white_border_18.setMinimumSize(QtCore.QSize(225, 0))
        self.frame_white_border_18.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_white_border_18.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_18.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_18.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_18.setLineWidth(1)
        self.frame_white_border_18.setObjectName("frame_white_border_18")
        self.gridLayout_24 = QtGui.QGridLayout(self.frame_white_border_18)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.frame_center_nest_9 = QtGui.QFrame(self.frame_white_border_18)
        self.frame_center_nest_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_center_nest_9.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_9.setLineWidth(1)
        self.frame_center_nest_9.setObjectName("frame_center_nest_9")
        self.frame_19 = QtGui.QFrame(self.frame_center_nest_9)
        self.frame_19.setGeometry(QtCore.QRect(7, 10, 211, 241))
        self.frame_19.setStyleSheet("border: none;")
        self.frame_19.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_32 = QtGui.QLabel(self.frame_19)
        self.label_32.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("border: none;")
        self.label_32.setObjectName("label_32")
        self.frame_78 = QtGui.QFrame(self.frame_19)
        self.frame_78.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_78.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_78.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_78.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_78.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.frame_79 = QtGui.QFrame(self.frame_78)
        self.frame_79.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_79.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_79.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_79.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_79.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_79.setObjectName("frame_79")
        self.label_33 = QtGui.QLabel(self.frame_79)
        self.label_33.setGeometry(QtCore.QRect(15, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("border: none;\n"
"background:none;")
        self.label_33.setObjectName("label_33")
        self.pushButton_72 = QtGui.QPushButton(self.frame_79)
        self.pushButton_72.setGeometry(QtCore.QRect(20, 150, 35, 30))
        self.pushButton_72.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_72.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_72.setText("")
        self.pushButton_72.setIcon(icon)
        self.pushButton_72.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_73 = QtGui.QPushButton(self.frame_79)
        self.pushButton_73.setGeometry(QtCore.QRect(66, 150, 35, 30))
        self.pushButton_73.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_73.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_73.setText("")
        self.pushButton_73.setIcon(icon1)
        self.pushButton_73.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_144 = QtGui.QPushButton(self.frame_79)
        self.pushButton_144.setGeometry(QtCore.QRect(30, 40, 31, 31))
        self.pushButton_144.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_144.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_144.setFont(font)
        self.pushButton_144.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_144.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_oct_volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_144.setIcon(icon8)
        self.pushButton_144.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_144.setObjectName("pushButton_144")
        self.pushButton_145 = QtGui.QPushButton(self.frame_79)
        self.pushButton_145.setGeometry(QtCore.QRect(70, 40, 31, 31))
        self.pushButton_145.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_145.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_145.setFont(font)
        self.pushButton_145.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_145.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_raw_oct_data.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_145.setIcon(icon9)
        self.pushButton_145.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_145.setObjectName("pushButton_145")
        self.pushButton_146 = QtGui.QPushButton(self.frame_79)
        self.pushButton_146.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.pushButton_146.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_146.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_146.setFont(font)
        self.pushButton_146.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_146.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_visible_camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_146.setIcon(icon10)
        self.pushButton_146.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_146.setObjectName("pushButton_146")
        self.gridLayout_24.addWidget(self.frame_center_nest_9, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.frame_white_border_18)
        self.frame_white_border_7 = QtGui.QFrame(self.frame_oct_setup)
        self.frame_white_border_7.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_white_border_7.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_7.setLineWidth(1)
        self.frame_white_border_7.setObjectName("frame_white_border_7")
        self.gridLayout_25 = QtGui.QGridLayout(self.frame_white_border_7)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.frame_center_nest_10 = QtGui.QFrame(self.frame_white_border_7)
        self.frame_center_nest_10.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_center_nest_10.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_10.setLineWidth(1)
        self.frame_center_nest_10.setObjectName("frame_center_nest_10")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_center_nest_10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_white_border_19 = QtGui.QFrame(self.frame_center_nest_10)
        self.frame_white_border_19.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_white_border_19.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_19.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_19.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_19.setLineWidth(1)
        self.frame_white_border_19.setObjectName("frame_white_border_19")
        self.gridLayout_26 = QtGui.QGridLayout(self.frame_white_border_19)
        self.gridLayout_26.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.frame_button_bar_14 = QtGui.QFrame(self.frame_white_border_19)
        self.frame_button_bar_14.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_14.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_14.setLineWidth(1)
        self.frame_button_bar_14.setObjectName("frame_button_bar_14")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_button_bar_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.frame_25 = QtGui.QFrame(self.frame_button_bar_14)
        self.frame_25.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_25.setStyleSheet("border: none; background: none;")
        self.frame_25.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.pushButton_138 = QtGui.QPushButton(self.frame_25)
        self.pushButton_138.setGeometry(QtCore.QRect(170, 3, 67, 30))
        self.pushButton_138.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_138.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_138.setFont(font)
        self.pushButton_138.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_138.setText("")
        self.pushButton_138.setIcon(icon3)
        self.pushButton_138.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_138.setObjectName("pushButton_138")
        self.horizontalLayout_10.addWidget(self.frame_25)
        spacerItem5 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.gridLayout_26.addWidget(self.frame_button_bar_14, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_white_border_19)
        self.frame_white_border_20 = QtGui.QFrame(self.frame_center_nest_10)
        self.frame_white_border_20.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_white_border_20.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_20.setLineWidth(1)
        self.frame_white_border_20.setObjectName("frame_white_border_20")
        self.gridLayout_27 = QtGui.QGridLayout(self.frame_white_border_20)
        self.gridLayout_27.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.frame_button_bar_15 = QtGui.QFrame(self.frame_white_border_20)
        self.frame_button_bar_15.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_15.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_15.setLineWidth(1)
        self.frame_button_bar_15.setObjectName("frame_button_bar_15")
        self.label_37 = QtGui.QLabel(self.frame_button_bar_15)
        self.label_37.setGeometry(QtCore.QRect(10, 20, 636, 18))
        self.label_37.setStyleSheet("border: none; background: none;")
        self.label_37.setObjectName("label_37")
        self.pushButton_141 = QtGui.QPushButton(self.frame_button_bar_15)
        self.pushButton_141.setGeometry(QtCore.QRect(170, 170, 130, 61))
        self.pushButton_141.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_141.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_141.setFont(font)
        self.pushButton_141.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_rectangle_scan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_141.setIcon(icon11)
        self.pushButton_141.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_141.setObjectName("pushButton_141")
        self.checkBox_10 = QtGui.QCheckBox(self.frame_button_bar_15)
        self.checkBox_10.setGeometry(QtCore.QRect(22, 72, 636, 18))
        self.checkBox_10.setStyleSheet("border: none; background: none;")
        self.checkBox_10.setIcon(icon9)
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_9 = QtGui.QCheckBox(self.frame_button_bar_15)
        self.checkBox_9.setGeometry(QtCore.QRect(22, 100, 636, 21))
        self.checkBox_9.setStyleSheet("border: none; background: none;")
        self.checkBox_9.setIcon(icon10)
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.pushButton_140 = QtGui.QPushButton(self.frame_button_bar_15)
        self.pushButton_140.setGeometry(QtCore.QRect(20, 170, 130, 61))
        self.pushButton_140.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_140.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_140.setFont(font)
        self.pushButton_140.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_spiral_scan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_140.setIcon(icon12)
        self.pushButton_140.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_140.setObjectName("pushButton_140")
        self.pushButton_142 = QtGui.QPushButton(self.frame_button_bar_15)
        self.pushButton_142.setGeometry(QtCore.QRect(320, 170, 130, 61))
        self.pushButton_142.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_142.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_142.setFont(font)
        self.pushButton_142.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_square_scan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_142.setIcon(icon13)
        self.pushButton_142.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_142.setObjectName("pushButton_142")
        self.label_11 = QtGui.QLabel(self.frame_button_bar_15)
        self.label_11.setGeometry(QtCore.QRect(10, 140, 171, 16))
        self.label_11.setStyleSheet("border: none; background: none;")
        self.label_11.setObjectName("label_11")
        self.pushButton_143 = QtGui.QPushButton(self.frame_button_bar_15)
        self.pushButton_143.setGeometry(QtCore.QRect(470, 170, 130, 61))
        self.pushButton_143.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_143.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_143.setFont(font)
        self.pushButton_143.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_circle_scan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_143.setIcon(icon14)
        self.pushButton_143.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_143.setObjectName("pushButton_143")
        self.checkBox_4 = QtGui.QCheckBox(self.frame_button_bar_15)
        self.checkBox_4.setGeometry(QtCore.QRect(22, 44, 636, 18))
        self.checkBox_4.setStyleSheet("border: none; background: none;")
        self.checkBox_4.setIcon(icon8)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_27.addWidget(self.frame_button_bar_15, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_white_border_20)
        self.gridLayout_25.addWidget(self.frame_center_nest_10, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.frame_white_border_7)
        self.frame_white_border_21 = QtGui.QFrame(self.frame_oct_setup)
        self.frame_white_border_21.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_white_border_21.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_white_border_21.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_21.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_21.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_21.setLineWidth(1)
        self.frame_white_border_21.setObjectName("frame_white_border_21")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.frame_white_border_21)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_center_nest_11 = QtGui.QFrame(self.frame_white_border_21)
        self.frame_center_nest_11.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_11.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_center_nest_11.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_11.setLineWidth(1)
        self.frame_center_nest_11.setObjectName("frame_center_nest_11")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_center_nest_11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setContentsMargins(3, -1, 0, 20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.frame_26 = QtGui.QFrame(self.frame_center_nest_11)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 232))
        self.frame_26.setStyleSheet("border: none;")
        self.frame_26.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.label_47 = QtGui.QLabel(self.frame_26)
        self.label_47.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("border: none;")
        self.label_47.setObjectName("label_47")
        self.frame_82 = QtGui.QFrame(self.frame_26)
        self.frame_82.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_82.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_82.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_82.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_82.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_82.setObjectName("frame_82")
        self.frame_83 = QtGui.QFrame(self.frame_82)
        self.frame_83.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_83.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_83.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_83.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_83.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_83.setObjectName("frame_83")
        self.labelSnapshotThumbnail_17 = QtGui.QLabel(self.frame_83)
        self.labelSnapshotThumbnail_17.setGeometry(QtCore.QRect(3, 3, 182, 158))
        self.labelSnapshotThumbnail_17.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_17.setText("")
        self.labelSnapshotThumbnail_17.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_17.setScaledContents(True)
        self.labelSnapshotThumbnail_17.setObjectName("labelSnapshotThumbnail_17")
        self.label_48 = QtGui.QLabel(self.frame_83)
        self.label_48.setGeometry(QtCore.QRect(6, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("border:none; background: none;")
        self.label_48.setObjectName("label_48")
        self.horizontalSlider_25 = QtGui.QSlider(self.frame_83)
        self.horizontalSlider_25.setGeometry(QtCore.QRect(63, 170, 65, 16))
        self.horizontalSlider_25.setProperty("value", 22)
        self.horizontalSlider_25.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_25.setObjectName("horizontalSlider_25")
        self.spinBox_54 = QtGui.QSpinBox(self.frame_83)
        self.spinBox_54.setGeometry(QtCore.QRect(133, 168, 50, 20))
        self.spinBox_54.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_54.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_54.setFont(font)
        self.spinBox_54.setStyleSheet("")
        self.spinBox_54.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_54.setProperty("value", 77)
        self.spinBox_54.setObjectName("spinBox_54")
        self.verticalLayout_6.addWidget(self.frame_26)
        self.verticalLayout_11.addWidget(self.frame_center_nest_11)
        self.horizontalLayout_9.addWidget(self.frame_white_border_21)
        self.horizontalLayout_11.addWidget(self.frame_oct_setup)
        self.stackedWidget_bottom.addWidget(self.page_oct_setup)
        self.page_oct_capture = QtGui.QWidget()
        self.page_oct_capture.setObjectName("page_oct_capture")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.page_oct_capture)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_oct_capture = QtGui.QFrame(self.page_oct_capture)
        self.frame_oct_capture.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_oct_capture.setStyleSheet("QFrame#frame_center_nest {\n"
"    /*border: 1px solid #ff0000;*/\n"
"    border: none;\n"
"}")
        self.frame_oct_capture.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_oct_capture.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_oct_capture.setLineWidth(1)
        self.frame_oct_capture.setObjectName("frame_oct_capture")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.frame_oct_capture)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_white_border_22 = QtGui.QFrame(self.frame_oct_capture)
        self.frame_white_border_22.setMinimumSize(QtCore.QSize(225, 0))
        self.frame_white_border_22.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_white_border_22.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_22.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_22.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_22.setLineWidth(1)
        self.frame_white_border_22.setObjectName("frame_white_border_22")
        self.gridLayout_28 = QtGui.QGridLayout(self.frame_white_border_22)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.frame_center_nest_12 = QtGui.QFrame(self.frame_white_border_22)
        self.frame_center_nest_12.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_center_nest_12.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_12.setLineWidth(1)
        self.frame_center_nest_12.setObjectName("frame_center_nest_12")
        self.frame_20 = QtGui.QFrame(self.frame_center_nest_12)
        self.frame_20.setGeometry(QtCore.QRect(7, 10, 211, 241))
        self.frame_20.setStyleSheet("border: none;")
        self.frame_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_34 = QtGui.QLabel(self.frame_20)
        self.label_34.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("border: none;")
        self.label_34.setObjectName("label_34")
        self.frame_84 = QtGui.QFrame(self.frame_20)
        self.frame_84.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_84.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_84.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_84.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_84.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_84.setObjectName("frame_84")
        self.frame_85 = QtGui.QFrame(self.frame_84)
        self.frame_85.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_85.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_85.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_85.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_85.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_85.setObjectName("frame_85")
        self.labelSnapshotThumbnail_16 = QtGui.QLabel(self.frame_85)
        self.labelSnapshotThumbnail_16.setGeometry(QtCore.QRect(13, 32, 151, 121))
        self.labelSnapshotThumbnail_16.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_16.setText("")
        self.labelSnapshotThumbnail_16.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat_retina36.jpg"))
        self.labelSnapshotThumbnail_16.setScaledContents(True)
        self.labelSnapshotThumbnail_16.setObjectName("labelSnapshotThumbnail_16")
        self.label_35 = QtGui.QLabel(self.frame_85)
        self.label_35.setGeometry(QtCore.QRect(15, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("border: none;\n"
"background:none;")
        self.label_35.setObjectName("label_35")
        self.pushButton_74 = QtGui.QPushButton(self.frame_85)
        self.pushButton_74.setGeometry(QtCore.QRect(14, 160, 35, 30))
        self.pushButton_74.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_74.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_74.setText("")
        self.pushButton_74.setIcon(icon)
        self.pushButton_74.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtGui.QPushButton(self.frame_85)
        self.pushButton_75.setGeometry(QtCore.QRect(60, 160, 35, 30))
        self.pushButton_75.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_75.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_75.setText("")
        self.pushButton_75.setIcon(icon1)
        self.pushButton_75.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_75.setObjectName("pushButton_75")
        self.gridLayout_28.addWidget(self.frame_center_nest_12, 0, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_white_border_22)
        self.frame_white_border_8 = QtGui.QFrame(self.frame_oct_capture)
        self.frame_white_border_8.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_white_border_8.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_8.setLineWidth(1)
        self.frame_white_border_8.setObjectName("frame_white_border_8")
        self.gridLayout_29 = QtGui.QGridLayout(self.frame_white_border_8)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.frame_center_nest_14 = QtGui.QFrame(self.frame_white_border_8)
        self.frame_center_nest_14.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_center_nest_14.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_14.setLineWidth(1)
        self.frame_center_nest_14.setObjectName("frame_center_nest_14")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frame_center_nest_14)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_white_border_23 = QtGui.QFrame(self.frame_center_nest_14)
        self.frame_white_border_23.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_23.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_white_border_23.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_23.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_23.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_23.setLineWidth(1)
        self.frame_white_border_23.setObjectName("frame_white_border_23")
        self.gridLayout_30 = QtGui.QGridLayout(self.frame_white_border_23)
        self.gridLayout_30.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.frame_button_bar_16 = QtGui.QFrame(self.frame_white_border_23)
        self.frame_button_bar_16.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_16.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_16.setLineWidth(1)
        self.frame_button_bar_16.setObjectName("frame_button_bar_16")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.frame_button_bar_16)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem7 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.frame_27 = QtGui.QFrame(self.frame_button_bar_16)
        self.frame_27.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_27.setStyleSheet("border: none; background: none;")
        self.frame_27.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.pushButton_137 = QtGui.QPushButton(self.frame_27)
        self.pushButton_137.setGeometry(QtCore.QRect(240, 3, 67, 30))
        self.pushButton_137.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_137.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_137.setFont(font)
        self.pushButton_137.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_137.setText("")
        self.pushButton_137.setIcon(icon3)
        self.pushButton_137.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_137.setObjectName("pushButton_137")
        self.pushButton_147 = QtGui.QPushButton(self.frame_27)
        self.pushButton_147.setGeometry(QtCore.QRect(313, 3, 67, 30))
        self.pushButton_147.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_147.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_147.setFont(font)
        self.pushButton_147.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_147.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_record.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_147.setIcon(icon15)
        self.pushButton_147.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_147.setObjectName("pushButton_147")
        self.pushButton_148 = QtGui.QPushButton(self.frame_27)
        self.pushButton_148.setGeometry(QtCore.QRect(21, 3, 67, 30))
        self.pushButton_148.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_148.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_148.setFont(font)
        self.pushButton_148.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_148.setText("")
        self.pushButton_148.setIcon(icon2)
        self.pushButton_148.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_148.setObjectName("pushButton_148")
        self.pushButton_149 = QtGui.QPushButton(self.frame_27)
        self.pushButton_149.setGeometry(QtCore.QRect(94, 3, 67, 30))
        self.pushButton_149.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_149.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_149.setFont(font)
        self.pushButton_149.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_149.setText("")
        self.pushButton_149.setIcon(icon4)
        self.pushButton_149.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_149.setObjectName("pushButton_149")
        self.pushButton_150 = QtGui.QPushButton(self.frame_27)
        self.pushButton_150.setGeometry(QtCore.QRect(167, 3, 67, 30))
        self.pushButton_150.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_150.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_150.setFont(font)
        self.pushButton_150.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_150.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_update_background.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_150.setIcon(icon16)
        self.pushButton_150.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_150.setObjectName("pushButton_150")
        self.horizontalLayout_13.addWidget(self.frame_27)
        spacerItem8 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.gridLayout_30.addWidget(self.frame_button_bar_16, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_white_border_23)
        self.frame_white_border_24 = QtGui.QFrame(self.frame_center_nest_14)
        self.frame_white_border_24.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_white_border_24.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_24.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_24.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_24.setLineWidth(1)
        self.frame_white_border_24.setObjectName("frame_white_border_24")
        self.gridLayout_31 = QtGui.QGridLayout(self.frame_white_border_24)
        self.gridLayout_31.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.frame_button_bar_17 = QtGui.QFrame(self.frame_white_border_24)
        self.frame_button_bar_17.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_17.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_17.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_17.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_17.setLineWidth(1)
        self.frame_button_bar_17.setObjectName("frame_button_bar_17")
        self.gridLayout_32 = QtGui.QGridLayout(self.frame_button_bar_17)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.label_oct_image = QtGui.QLabel(self.frame_button_bar_17)
        self.label_oct_image.setStyleSheet("border: none;")
        self.label_oct_image.setText("")
        self.label_oct_image.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat_retina36.jpg"))
        self.label_oct_image.setScaledContents(True)
        self.label_oct_image.setObjectName("label_oct_image")
        self.gridLayout_32.addWidget(self.label_oct_image, 0, 0, 1, 1)
        self.gridLayout_31.addWidget(self.frame_button_bar_17, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_white_border_24)
        self.gridLayout_29.addWidget(self.frame_center_nest_14, 0, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_white_border_8)
        self.frame_white_border_25 = QtGui.QFrame(self.frame_oct_capture)
        self.frame_white_border_25.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_white_border_25.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_white_border_25.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_25.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_25.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_25.setLineWidth(1)
        self.frame_white_border_25.setObjectName("frame_white_border_25")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.frame_white_border_25)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_center_nest_15 = QtGui.QFrame(self.frame_white_border_25)
        self.frame_center_nest_15.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_15.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_center_nest_15.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_15.setLineWidth(1)
        self.frame_center_nest_15.setObjectName("frame_center_nest_15")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.frame_center_nest_15)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(3, 0, 0, 20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_reference_arm = QtGui.QFrame(self.frame_center_nest_15)
        self.frame_reference_arm.setMinimumSize(QtCore.QSize(0, 144))
        self.frame_reference_arm.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_reference_arm.setStyleSheet("border: none;")
        self.frame_reference_arm.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_reference_arm.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_reference_arm.setObjectName("frame_reference_arm")
        self.label_49 = QtGui.QLabel(self.frame_reference_arm)
        self.label_49.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("border: none;")
        self.label_49.setObjectName("label_49")
        self.frame_white_border_27 = QtGui.QFrame(self.frame_reference_arm)
        self.frame_white_border_27.setGeometry(QtCore.QRect(10, 34, 190, 109))
        self.frame_white_border_27.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_white_border_27.setMaximumSize(QtCore.QSize(190, 140))
        self.frame_white_border_27.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_27.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_27.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_27.setLineWidth(1)
        self.frame_white_border_27.setObjectName("frame_white_border_27")
        self.gridLayout_34 = QtGui.QGridLayout(self.frame_white_border_27)
        self.gridLayout_34.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.frame_button_bar_19 = QtGui.QFrame(self.frame_white_border_27)
        self.frame_button_bar_19.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_19.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_19.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_19.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_19.setLineWidth(1)
        self.frame_button_bar_19.setObjectName("frame_button_bar_19")
        self.verticalSlider_18 = QtGui.QSlider(self.frame_button_bar_19)
        self.verticalSlider_18.setGeometry(QtCore.QRect(14, 13, 16, 81))
        self.verticalSlider_18.setMaximum(999)
        self.verticalSlider_18.setProperty("value", 444)
        self.verticalSlider_18.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_18.setObjectName("verticalSlider_18")
        self.pushButton_60 = QtGui.QPushButton(self.frame_button_bar_19)
        self.pushButton_60.setGeometry(QtCore.QRect(116, 23, 50, 30))
        self.pushButton_60.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_60.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_60.setText("")
        self.pushButton_60.setIcon(icon5)
        self.pushButton_60.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_60.setObjectName("pushButton_60")
        self.spinBox_44 = QtGui.QSpinBox(self.frame_button_bar_19)
        self.spinBox_44.setGeometry(QtCore.QRect(57, 69, 108, 23))
        self.spinBox_44.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_44.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_44.setSuffix("")
        self.spinBox_44.setMaximum(10000)
        self.spinBox_44.setObjectName("spinBox_44")
        self.pushButton_61 = QtGui.QPushButton(self.frame_button_bar_19)
        self.pushButton_61.setGeometry(QtCore.QRect(56, 23, 50, 30))
        self.pushButton_61.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_61.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_61.setText("")
        self.pushButton_61.setIcon(icon6)
        self.pushButton_61.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_61.setObjectName("pushButton_61")
        self.gridLayout_34.addWidget(self.frame_button_bar_19, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_reference_arm)
        self.frame_oct_image_control_3 = QtGui.QFrame(self.frame_center_nest_15)
        self.frame_oct_image_control_3.setMinimumSize(QtCore.QSize(0, 151))
        self.frame_oct_image_control_3.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_oct_image_control_3.setStyleSheet("border: none;")
        self.frame_oct_image_control_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_oct_image_control_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_oct_image_control_3.setObjectName("frame_oct_image_control_3")
        self.label_60 = QtGui.QLabel(self.frame_oct_image_control_3)
        self.label_60.setGeometry(QtCore.QRect(10, 7, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("border: none;")
        self.label_60.setObjectName("label_60")
        self.frame_white_border_32 = QtGui.QFrame(self.frame_oct_image_control_3)
        self.frame_white_border_32.setGeometry(QtCore.QRect(10, 30, 190, 114))
        self.frame_white_border_32.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_white_border_32.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_white_border_32.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_32.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_32.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_32.setLineWidth(1)
        self.frame_white_border_32.setObjectName("frame_white_border_32")
        self.gridLayout_39 = QtGui.QGridLayout(self.frame_white_border_32)
        self.gridLayout_39.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.frame_button_bar_24 = QtGui.QFrame(self.frame_white_border_32)
        self.frame_button_bar_24.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_24.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_24.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_24.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_24.setLineWidth(1)
        self.frame_button_bar_24.setObjectName("frame_button_bar_24")
        self.spinBox_26 = QtGui.QSpinBox(self.frame_button_bar_24)
        self.spinBox_26.setGeometry(QtCore.QRect(134, 9, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_26.setFont(font)
        self.spinBox_26.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_26.setProperty("value", 50)
        self.spinBox_26.setObjectName("spinBox_26")
        self.horizontalSlider_19 = QtGui.QSlider(self.frame_button_bar_24)
        self.horizontalSlider_19.setGeometry(QtCore.QRect(66, 9, 65, 16))
        self.horizontalSlider_19.setProperty("value", 33)
        self.horizontalSlider_19.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_19.setObjectName("horizontalSlider_19")
        self.label_61 = QtGui.QLabel(self.frame_button_bar_24)
        self.label_61.setGeometry(QtCore.QRect(8, 9, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("border: none; background: none;")
        self.label_61.setObjectName("label_61")
        self.spinBox_30 = QtGui.QSpinBox(self.frame_button_bar_24)
        self.spinBox_30.setGeometry(QtCore.QRect(134, 39, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_30.setFont(font)
        self.spinBox_30.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_30.setProperty("value", 50)
        self.spinBox_30.setObjectName("spinBox_30")
        self.label_62 = QtGui.QLabel(self.frame_button_bar_24)
        self.label_62.setGeometry(QtCore.QRect(8, 39, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("border: none; background: none;")
        self.label_62.setObjectName("label_62")
        self.horizontalSlider_27 = QtGui.QSlider(self.frame_button_bar_24)
        self.horizontalSlider_27.setGeometry(QtCore.QRect(66, 39, 65, 16))
        self.horizontalSlider_27.setProperty("value", 77)
        self.horizontalSlider_27.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_27.setObjectName("horizontalSlider_27")
        self.label_63 = QtGui.QLabel(self.frame_button_bar_24)
        self.label_63.setGeometry(QtCore.QRect(10, 79, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("border: none; background: none;")
        self.label_63.setObjectName("label_63")
        self.pushButton_78 = QtGui.QPushButton(self.frame_button_bar_24)
        self.pushButton_78.setGeometry(QtCore.QRect(139, 70, 35, 30))
        self.pushButton_78.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_78.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_78.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/thumbnails/images/colormaps/gray.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_78.setIcon(icon17)
        self.pushButton_78.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_78.setCheckable(True)
        self.pushButton_78.setObjectName("pushButton_78")
        self.gridLayout_39.addWidget(self.frame_button_bar_24, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_oct_image_control_3)
        self.frame_oct_image_control_2 = QtGui.QFrame(self.frame_center_nest_15)
        self.frame_oct_image_control_2.setMinimumSize(QtCore.QSize(0, 162))
        self.frame_oct_image_control_2.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_oct_image_control_2.setStyleSheet("border: none;")
        self.frame_oct_image_control_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_oct_image_control_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_oct_image_control_2.setObjectName("frame_oct_image_control_2")
        self.label_57 = QtGui.QLabel(self.frame_oct_image_control_2)
        self.label_57.setGeometry(QtCore.QRect(10, 6, 191, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("border: none;")
        self.label_57.setObjectName("label_57")
        self.frame_white_border_31 = QtGui.QFrame(self.frame_oct_image_control_2)
        self.frame_white_border_31.setGeometry(QtCore.QRect(10, 28, 190, 130))
        self.frame_white_border_31.setMinimumSize(QtCore.QSize(190, 130))
        self.frame_white_border_31.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_white_border_31.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_31.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_31.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_31.setLineWidth(1)
        self.frame_white_border_31.setObjectName("frame_white_border_31")
        self.gridLayout_38 = QtGui.QGridLayout(self.frame_white_border_31)
        self.gridLayout_38.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.frame_button_bar_23 = QtGui.QFrame(self.frame_white_border_31)
        self.frame_button_bar_23.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_23.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_23.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_23.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_23.setLineWidth(1)
        self.frame_button_bar_23.setObjectName("frame_button_bar_23")
        self.doubleSpinBox_24 = QtGui.QDoubleSpinBox(self.frame_button_bar_23)
        self.doubleSpinBox_24.setGeometry(QtCore.QRect(122, 7, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.doubleSpinBox_24.setFont(font)
        self.doubleSpinBox_24.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_24.setProperty("value", 1.38)
        self.doubleSpinBox_24.setObjectName("doubleSpinBox_24")
        self.horizontalSlider_17 = QtGui.QSlider(self.frame_button_bar_23)
        self.horizontalSlider_17.setGeometry(QtCore.QRect(66, 10, 51, 16))
        self.horizontalSlider_17.setProperty("value", 33)
        self.horizontalSlider_17.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_17.setObjectName("horizontalSlider_17")
        self.label_58 = QtGui.QLabel(self.frame_button_bar_23)
        self.label_58.setGeometry(QtCore.QRect(8, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("border: none; background: none;")
        self.label_58.setObjectName("label_58")
        self.label_59 = QtGui.QLabel(self.frame_button_bar_23)
        self.label_59.setGeometry(QtCore.QRect(8, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("border: none; background: none;")
        self.label_59.setObjectName("label_59")
        self.horizontalSlider_18 = QtGui.QSlider(self.frame_button_bar_23)
        self.horizontalSlider_18.setGeometry(QtCore.QRect(66, 40, 51, 16))
        self.horizontalSlider_18.setProperty("value", 77)
        self.horizontalSlider_18.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_18.setObjectName("horizontalSlider_18")
        self.doubleSpinBox_25 = QtGui.QDoubleSpinBox(self.frame_button_bar_23)
        self.doubleSpinBox_25.setGeometry(QtCore.QRect(122, 37, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.doubleSpinBox_25.setFont(font)
        self.doubleSpinBox_25.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_25.setProperty("value", 5.79)
        self.doubleSpinBox_25.setObjectName("doubleSpinBox_25")
        self.label_44 = QtGui.QLabel(self.frame_button_bar_23)
        self.label_44.setGeometry(QtCore.QRect(10, 98, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("border: none; background: none;")
        self.label_44.setObjectName("label_44")
        self.horizontalSlider_13 = QtGui.QSlider(self.frame_button_bar_23)
        self.horizontalSlider_13.setGeometry(QtCore.QRect(68, 68, 51, 16))
        self.horizontalSlider_13.setProperty("value", 33)
        self.horizontalSlider_13.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_13.setObjectName("horizontalSlider_13")
        self.horizontalSlider_14 = QtGui.QSlider(self.frame_button_bar_23)
        self.horizontalSlider_14.setGeometry(QtCore.QRect(68, 98, 51, 16))
        self.horizontalSlider_14.setProperty("value", 77)
        self.horizontalSlider_14.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_14.setObjectName("horizontalSlider_14")
        self.spinBox_21 = QtGui.QSpinBox(self.frame_button_bar_23)
        self.spinBox_21.setGeometry(QtCore.QRect(131, 98, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_21.setFont(font)
        self.spinBox_21.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_21.setProperty("value", 50)
        self.spinBox_21.setObjectName("spinBox_21")
        self.label_43 = QtGui.QLabel(self.frame_button_bar_23)
        self.label_43.setGeometry(QtCore.QRect(10, 68, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("border: none; background: none;")
        self.label_43.setObjectName("label_43")
        self.spinBox_20 = QtGui.QSpinBox(self.frame_button_bar_23)
        self.spinBox_20.setGeometry(QtCore.QRect(131, 68, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_20.setFont(font)
        self.spinBox_20.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_20.setProperty("value", 50)
        self.spinBox_20.setObjectName("spinBox_20")
        self.gridLayout_38.addWidget(self.frame_button_bar_23, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_oct_image_control_2)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.frame_reference_arm_2 = QtGui.QFrame(self.frame_center_nest_15)
        self.frame_reference_arm_2.setMinimumSize(QtCore.QSize(0, 211))
        self.frame_reference_arm_2.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_reference_arm_2.setStyleSheet("border: none;")
        self.frame_reference_arm_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_reference_arm_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_reference_arm_2.setObjectName("frame_reference_arm_2")
        self.label_50 = QtGui.QLabel(self.frame_reference_arm_2)
        self.label_50.setGeometry(QtCore.QRect(10, 5, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("border: none;")
        self.label_50.setObjectName("label_50")
        self.frame_white_border_28 = QtGui.QFrame(self.frame_reference_arm_2)
        self.frame_white_border_28.setGeometry(QtCore.QRect(10, 25, 190, 185))
        self.frame_white_border_28.setMinimumSize(QtCore.QSize(190, 185))
        self.frame_white_border_28.setMaximumSize(QtCore.QSize(190, 140))
        self.frame_white_border_28.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_28.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_28.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_28.setLineWidth(1)
        self.frame_white_border_28.setObjectName("frame_white_border_28")
        self.gridLayout_35 = QtGui.QGridLayout(self.frame_white_border_28)
        self.gridLayout_35.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.frame_button_bar_20 = QtGui.QFrame(self.frame_white_border_28)
        self.frame_button_bar_20.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_20.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_20.setLineWidth(1)
        self.frame_button_bar_20.setObjectName("frame_button_bar_20")
        self.spinBox_40 = QtGui.QSpinBox(self.frame_button_bar_20)
        self.spinBox_40.setGeometry(QtCore.QRect(31, 147, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_40.setFont(font)
        self.spinBox_40.setSuffix("")
        self.spinBox_40.setMaximum(360)
        self.spinBox_40.setProperty("value", 300)
        self.spinBox_40.setObjectName("spinBox_40")
        self.pushButton_62 = QtGui.QPushButton(self.frame_button_bar_20)
        self.pushButton_62.setGeometry(QtCore.QRect(20, 44, 50, 30))
        self.pushButton_62.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_62.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_62.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_62.setIcon(icon18)
        self.pushButton_62.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_63 = QtGui.QPushButton(self.frame_button_bar_20)
        self.pushButton_63.setGeometry(QtCore.QRect(70, 14, 50, 30))
        self.pushButton_63.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_63.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_63.setText("")
        self.pushButton_63.setIcon(icon6)
        self.pushButton_63.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_63.setObjectName("pushButton_63")
        self.spinBox_45 = QtGui.QSpinBox(self.frame_button_bar_20)
        self.spinBox_45.setGeometry(QtCore.QRect(31, 119, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_45.setFont(font)
        self.spinBox_45.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_45.setSuffix("")
        self.spinBox_45.setMaximum(9999)
        self.spinBox_45.setProperty("value", 5555)
        self.spinBox_45.setObjectName("spinBox_45")
        self.pushButton_68 = QtGui.QPushButton(self.frame_button_bar_20)
        self.pushButton_68.setGeometry(QtCore.QRect(120, 44, 50, 30))
        self.pushButton_68.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_68.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_68.setText("")
        self.pushButton_68.setIcon(icon2)
        self.pushButton_68.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_76 = QtGui.QPushButton(self.frame_button_bar_20)
        self.pushButton_76.setGeometry(QtCore.QRect(70, 75, 50, 30))
        self.pushButton_76.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_76.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_76.setText("")
        self.pushButton_76.setIcon(icon5)
        self.pushButton_76.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_76.setObjectName("pushButton_76")
        self.gridLayout_35.addWidget(self.frame_button_bar_20, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_reference_arm_2)
        self.frame_29 = QtGui.QFrame(self.frame_center_nest_15)
        self.frame_29.setMinimumSize(QtCore.QSize(0, 232))
        self.frame_29.setStyleSheet("border: none;")
        self.frame_29.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.label_52 = QtGui.QLabel(self.frame_29)
        self.label_52.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("border: none;")
        self.label_52.setObjectName("label_52")
        self.frame_86 = QtGui.QFrame(self.frame_29)
        self.frame_86.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_86.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_86.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_86.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_86.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_86.setObjectName("frame_86")
        self.frame_87 = QtGui.QFrame(self.frame_86)
        self.frame_87.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_87.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_87.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_87.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_87.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_87.setObjectName("frame_87")
        self.labelSnapshotThumbnail_18 = QtGui.QLabel(self.frame_87)
        self.labelSnapshotThumbnail_18.setGeometry(QtCore.QRect(3, 3, 182, 158))
        self.labelSnapshotThumbnail_18.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_18.setText("")
        self.labelSnapshotThumbnail_18.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_18.setScaledContents(True)
        self.labelSnapshotThumbnail_18.setObjectName("labelSnapshotThumbnail_18")
        self.label_53 = QtGui.QLabel(self.frame_87)
        self.label_53.setGeometry(QtCore.QRect(6, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("border:none; background: none;")
        self.label_53.setObjectName("label_53")
        self.horizontalSlider_26 = QtGui.QSlider(self.frame_87)
        self.horizontalSlider_26.setGeometry(QtCore.QRect(63, 170, 65, 16))
        self.horizontalSlider_26.setProperty("value", 22)
        self.horizontalSlider_26.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_26.setObjectName("horizontalSlider_26")
        self.spinBox_55 = QtGui.QSpinBox(self.frame_87)
        self.spinBox_55.setGeometry(QtCore.QRect(133, 168, 50, 20))
        self.spinBox_55.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_55.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_55.setFont(font)
        self.spinBox_55.setStyleSheet("")
        self.spinBox_55.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_55.setProperty("value", 77)
        self.spinBox_55.setObjectName("spinBox_55")
        self.verticalLayout_8.addWidget(self.frame_29)
        self.verticalLayout_12.addWidget(self.frame_center_nest_15)
        self.horizontalLayout_12.addWidget(self.frame_white_border_25)
        self.horizontalLayout_14.addWidget(self.frame_oct_capture)
        self.stackedWidget_bottom.addWidget(self.page_oct_capture)
        self.page_angio_setup = QtGui.QWidget()
        self.page_angio_setup.setObjectName("page_angio_setup")
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.page_angio_setup)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_angio_setup = QtGui.QFrame(self.page_angio_setup)
        self.frame_angio_setup.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_angio_setup.setStyleSheet("QFrame#frame_center_nest {\n"
"    /*border: 1px solid #ff0000;*/\n"
"    border: none;\n"
"}")
        self.frame_angio_setup.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_angio_setup.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_angio_setup.setLineWidth(1)
        self.frame_angio_setup.setObjectName("frame_angio_setup")
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.frame_angio_setup)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_white_border_35 = QtGui.QFrame(self.frame_angio_setup)
        self.frame_white_border_35.setMinimumSize(QtCore.QSize(225, 0))
        self.frame_white_border_35.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_white_border_35.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_35.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_35.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_35.setLineWidth(1)
        self.frame_white_border_35.setObjectName("frame_white_border_35")
        self.gridLayout_41 = QtGui.QGridLayout(self.frame_white_border_35)
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.frame_center_nest_22 = QtGui.QFrame(self.frame_white_border_35)
        self.frame_center_nest_22.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_center_nest_22.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_22.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_22.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_22.setLineWidth(1)
        self.frame_center_nest_22.setObjectName("frame_center_nest_22")
        self.frame_22 = QtGui.QFrame(self.frame_center_nest_22)
        self.frame_22.setGeometry(QtCore.QRect(7, 10, 211, 241))
        self.frame_22.setStyleSheet("border: none;")
        self.frame_22.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.label_45 = QtGui.QLabel(self.frame_22)
        self.label_45.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("border: none;")
        self.label_45.setObjectName("label_45")
        self.frame_92 = QtGui.QFrame(self.frame_22)
        self.frame_92.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_92.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_92.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_92.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_92.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_92.setObjectName("frame_92")
        self.frame_93 = QtGui.QFrame(self.frame_92)
        self.frame_93.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_93.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_93.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_93.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_93.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_93.setObjectName("frame_93")
        self.label_46 = QtGui.QLabel(self.frame_93)
        self.label_46.setGeometry(QtCore.QRect(15, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("border: none;\n"
"background:none;")
        self.label_46.setObjectName("label_46")
        self.pushButton_80 = QtGui.QPushButton(self.frame_93)
        self.pushButton_80.setGeometry(QtCore.QRect(20, 150, 35, 30))
        self.pushButton_80.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_80.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_80.setFont(font)
        self.pushButton_80.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_80.setText("")
        self.pushButton_80.setIcon(icon)
        self.pushButton_80.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtGui.QPushButton(self.frame_93)
        self.pushButton_81.setGeometry(QtCore.QRect(66, 150, 35, 30))
        self.pushButton_81.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_81.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_81.setText("")
        self.pushButton_81.setIcon(icon1)
        self.pushButton_81.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_155 = QtGui.QPushButton(self.frame_93)
        self.pushButton_155.setGeometry(QtCore.QRect(30, 40, 31, 31))
        self.pushButton_155.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_155.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_155.setFont(font)
        self.pushButton_155.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_155.setText("")
        self.pushButton_155.setIcon(icon8)
        self.pushButton_155.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_155.setObjectName("pushButton_155")
        self.pushButton_156 = QtGui.QPushButton(self.frame_93)
        self.pushButton_156.setGeometry(QtCore.QRect(70, 40, 31, 31))
        self.pushButton_156.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_156.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_156.setFont(font)
        self.pushButton_156.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_156.setText("")
        self.pushButton_156.setIcon(icon9)
        self.pushButton_156.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_156.setObjectName("pushButton_156")
        self.pushButton_157 = QtGui.QPushButton(self.frame_93)
        self.pushButton_157.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.pushButton_157.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_157.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_157.setFont(font)
        self.pushButton_157.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_157.setText("")
        self.pushButton_157.setIcon(icon10)
        self.pushButton_157.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_157.setObjectName("pushButton_157")
        self.pushButton_176 = QtGui.QPushButton(self.frame_93)
        self.pushButton_176.setGeometry(QtCore.QRect(110, 80, 31, 31))
        self.pushButton_176.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_176.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_176.setFont(font)
        self.pushButton_176.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_176.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_angio_projection.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_176.setIcon(icon19)
        self.pushButton_176.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_176.setObjectName("pushButton_176")
        self.pushButton_177 = QtGui.QPushButton(self.frame_93)
        self.pushButton_177.setGeometry(QtCore.QRect(30, 80, 31, 31))
        self.pushButton_177.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_177.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_177.setFont(font)
        self.pushButton_177.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_177.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_angio_bscan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_177.setIcon(icon20)
        self.pushButton_177.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_177.setObjectName("pushButton_177")
        self.pushButton_178 = QtGui.QPushButton(self.frame_93)
        self.pushButton_178.setGeometry(QtCore.QRect(70, 80, 31, 31))
        self.pushButton_178.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_178.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_178.setFont(font)
        self.pushButton_178.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_178.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_angio_volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_178.setIcon(icon21)
        self.pushButton_178.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_178.setObjectName("pushButton_178")
        self.pushButton_179 = QtGui.QPushButton(self.frame_93)
        self.pushButton_179.setGeometry(QtCore.QRect(150, 80, 31, 31))
        self.pushButton_179.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_179.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_179.setFont(font)
        self.pushButton_179.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_179.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_intensity_and_phase.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_179.setIcon(icon22)
        self.pushButton_179.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_179.setObjectName("pushButton_179")
        self.gridLayout_41.addWidget(self.frame_center_nest_22, 0, 0, 1, 1)
        self.horizontalLayout_18.addWidget(self.frame_white_border_35)
        self.frame_white_border_36 = QtGui.QFrame(self.frame_angio_setup)
        self.frame_white_border_36.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_white_border_36.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_36.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_36.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_36.setLineWidth(1)
        self.frame_white_border_36.setObjectName("frame_white_border_36")
        self.gridLayout_42 = QtGui.QGridLayout(self.frame_white_border_36)
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.frame_center_nest_20 = QtGui.QFrame(self.frame_white_border_36)
        self.frame_center_nest_20.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_center_nest_20.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_20.setLineWidth(1)
        self.frame_center_nest_20.setObjectName("frame_center_nest_20")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.frame_center_nest_20)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_white_border_37 = QtGui.QFrame(self.frame_center_nest_20)
        self.frame_white_border_37.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_37.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_white_border_37.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_37.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_37.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_37.setLineWidth(1)
        self.frame_white_border_37.setObjectName("frame_white_border_37")
        self.gridLayout_43 = QtGui.QGridLayout(self.frame_white_border_37)
        self.gridLayout_43.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.frame_button_bar_22 = QtGui.QFrame(self.frame_white_border_37)
        self.frame_button_bar_22.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_22.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_22.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_22.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_22.setLineWidth(1)
        self.frame_button_bar_22.setObjectName("frame_button_bar_22")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.frame_button_bar_22)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem10 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.frame_31 = QtGui.QFrame(self.frame_button_bar_22)
        self.frame_31.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_31.setStyleSheet("border: none; background: none;")
        self.frame_31.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.pushButton_158 = QtGui.QPushButton(self.frame_31)
        self.pushButton_158.setGeometry(QtCore.QRect(170, 3, 67, 30))
        self.pushButton_158.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_158.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_158.setFont(font)
        self.pushButton_158.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_158.setText("")
        self.pushButton_158.setIcon(icon3)
        self.pushButton_158.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_158.setObjectName("pushButton_158")
        self.horizontalLayout_19.addWidget(self.frame_31)
        spacerItem11 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem11)
        self.gridLayout_43.addWidget(self.frame_button_bar_22, 0, 0, 1, 1)
        self.verticalLayout_16.addWidget(self.frame_white_border_37)
        self.frame_white_border_38 = QtGui.QFrame(self.frame_center_nest_20)
        self.frame_white_border_38.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_38.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_white_border_38.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_38.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_38.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_38.setLineWidth(1)
        self.frame_white_border_38.setObjectName("frame_white_border_38")
        self.gridLayout_44 = QtGui.QGridLayout(self.frame_white_border_38)
        self.gridLayout_44.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.frame_button_bar_25 = QtGui.QFrame(self.frame_white_border_38)
        self.frame_button_bar_25.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_25.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_25.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_25.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_25.setLineWidth(1)
        self.frame_button_bar_25.setObjectName("frame_button_bar_25")
        self.label_55 = QtGui.QLabel(self.frame_button_bar_25)
        self.label_55.setGeometry(QtCore.QRect(10, 20, 636, 18))
        self.label_55.setStyleSheet("border: none; background: none;")
        self.label_55.setObjectName("label_55")
        self.pushButton_159 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_159.setGeometry(QtCore.QRect(170, 200, 130, 61))
        self.pushButton_159.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_159.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_159.setFont(font)
        self.pushButton_159.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_159.setIcon(icon11)
        self.pushButton_159.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_159.setObjectName("pushButton_159")
        self.checkBox_11 = QtGui.QCheckBox(self.frame_button_bar_25)
        self.checkBox_11.setGeometry(QtCore.QRect(22, 72, 636, 18))
        self.checkBox_11.setStyleSheet("border: none; background: none;")
        self.checkBox_11.setIcon(icon9)
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtGui.QCheckBox(self.frame_button_bar_25)
        self.checkBox_12.setGeometry(QtCore.QRect(22, 100, 636, 21))
        self.checkBox_12.setStyleSheet("border: none; background: none;")
        self.checkBox_12.setIcon(icon10)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.pushButton_160 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_160.setGeometry(QtCore.QRect(20, 200, 130, 61))
        self.pushButton_160.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_160.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_160.setFont(font)
        self.pushButton_160.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_160.setIcon(icon12)
        self.pushButton_160.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_160.setObjectName("pushButton_160")
        self.pushButton_161 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_161.setGeometry(QtCore.QRect(320, 200, 130, 61))
        self.pushButton_161.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_161.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_161.setFont(font)
        self.pushButton_161.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_161.setIcon(icon13)
        self.pushButton_161.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_161.setObjectName("pushButton_161")
        self.label_13 = QtGui.QLabel(self.frame_button_bar_25)
        self.label_13.setGeometry(QtCore.QRect(10, 170, 171, 16))
        self.label_13.setStyleSheet("border: none; background: none;")
        self.label_13.setObjectName("label_13")
        self.pushButton_162 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_162.setGeometry(QtCore.QRect(470, 200, 130, 61))
        self.pushButton_162.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_162.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_162.setFont(font)
        self.pushButton_162.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_162.setIcon(icon14)
        self.pushButton_162.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_162.setObjectName("pushButton_162")
        self.checkBox_5 = QtGui.QCheckBox(self.frame_button_bar_25)
        self.checkBox_5.setGeometry(QtCore.QRect(22, 44, 636, 18))
        self.checkBox_5.setStyleSheet("border: none; background: none;")
        self.checkBox_5.setIcon(icon8)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_66 = QtGui.QLabel(self.frame_button_bar_25)
        self.label_66.setGeometry(QtCore.QRect(10, 280, 171, 16))
        self.label_66.setStyleSheet("border: none; background: none;")
        self.label_66.setObjectName("label_66")
        self.pushButton_163 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_163.setGeometry(QtCore.QRect(170, 300, 130, 61))
        self.pushButton_163.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_163.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_163.setFont(font)
        self.pushButton_163.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_subtract.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_163.setIcon(icon23)
        self.pushButton_163.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_163.setObjectName("pushButton_163")
        self.pushButton_164 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_164.setGeometry(QtCore.QRect(20, 300, 130, 61))
        self.pushButton_164.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_164.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_164.setFont(font)
        self.pushButton_164.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_average.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_164.setIcon(icon24)
        self.pushButton_164.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_164.setObjectName("pushButton_164")
        self.pushButton_165 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_165.setGeometry(QtCore.QRect(170, 400, 130, 61))
        self.pushButton_165.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_165.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_165.setFont(font)
        self.pushButton_165.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_phase_algorithm.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_165.setIcon(icon25)
        self.pushButton_165.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_165.setObjectName("pushButton_165")
        self.label_68 = QtGui.QLabel(self.frame_button_bar_25)
        self.label_68.setGeometry(QtCore.QRect(10, 380, 171, 16))
        self.label_68.setStyleSheet("border: none; background: none;")
        self.label_68.setObjectName("label_68")
        self.pushButton_166 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_166.setGeometry(QtCore.QRect(20, 400, 130, 61))
        self.pushButton_166.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_166.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_166.setFont(font)
        self.pushButton_166.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_speckle_algorithm.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_166.setIcon(icon26)
        self.pushButton_166.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_166.setObjectName("pushButton_166")
        self.checkBox_16 = QtGui.QCheckBox(self.frame_button_bar_25)
        self.checkBox_16.setGeometry(QtCore.QRect(310, 130, 359, 19))
        self.checkBox_16.setStyleSheet("border: none; background: none;")
        self.checkBox_16.setIcon(icon22)
        self.checkBox_16.setChecked(True)
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_2 = QtGui.QCheckBox(self.frame_button_bar_25)
        self.checkBox_2.setGeometry(QtCore.QRect(310, 42, 359, 19))
        self.checkBox_2.setStyleSheet("border: none; background: none;")
        self.checkBox_2.setIcon(icon20)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_17 = QtGui.QCheckBox(self.frame_button_bar_25)
        self.checkBox_17.setGeometry(QtCore.QRect(310, 72, 359, 19))
        self.checkBox_17.setStyleSheet("border: none; background: none;")
        self.checkBox_17.setIcon(icon21)
        self.checkBox_17.setChecked(True)
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtGui.QCheckBox(self.frame_button_bar_25)
        self.checkBox_18.setGeometry(QtCore.QRect(310, 100, 359, 20))
        self.checkBox_18.setStyleSheet("border: none; background: none;")
        self.checkBox_18.setIcon(icon19)
        self.checkBox_18.setChecked(True)
        self.checkBox_18.setObjectName("checkBox_18")
        self.pushButton_175 = QtGui.QPushButton(self.frame_button_bar_25)
        self.pushButton_175.setGeometry(QtCore.QRect(320, 400, 130, 61))
        self.pushButton_175.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_175.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_175.setFont(font)
        self.pushButton_175.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_complex_differential_algorithm.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_175.setIcon(icon27)
        self.pushButton_175.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_175.setObjectName("pushButton_175")
        self.gridLayout_44.addWidget(self.frame_button_bar_25, 0, 0, 1, 1)
        self.verticalLayout_16.addWidget(self.frame_white_border_38)
        self.gridLayout_42.addWidget(self.frame_center_nest_20, 0, 0, 1, 1)
        self.horizontalLayout_18.addWidget(self.frame_white_border_36)
        self.frame_white_border_39 = QtGui.QFrame(self.frame_angio_setup)
        self.frame_white_border_39.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_white_border_39.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_white_border_39.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_39.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_39.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_39.setLineWidth(1)
        self.frame_white_border_39.setObjectName("frame_white_border_39")
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.frame_white_border_39)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_center_nest_21 = QtGui.QFrame(self.frame_white_border_39)
        self.frame_center_nest_21.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_21.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_center_nest_21.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_21.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_21.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_21.setLineWidth(1)
        self.frame_center_nest_21.setObjectName("frame_center_nest_21")
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.frame_center_nest_21)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setContentsMargins(3, -1, 0, 20)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem12)
        self.frame_32 = QtGui.QFrame(self.frame_center_nest_21)
        self.frame_32.setMinimumSize(QtCore.QSize(0, 232))
        self.frame_32.setStyleSheet("border: none;")
        self.frame_32.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.label_56 = QtGui.QLabel(self.frame_32)
        self.label_56.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("border: none;")
        self.label_56.setObjectName("label_56")
        self.frame_94 = QtGui.QFrame(self.frame_32)
        self.frame_94.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_94.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_94.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_94.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_94.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_94.setObjectName("frame_94")
        self.frame_95 = QtGui.QFrame(self.frame_94)
        self.frame_95.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_95.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_95.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_95.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_95.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_95.setObjectName("frame_95")
        self.labelSnapshotThumbnail_20 = QtGui.QLabel(self.frame_95)
        self.labelSnapshotThumbnail_20.setGeometry(QtCore.QRect(3, 3, 182, 158))
        self.labelSnapshotThumbnail_20.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_20.setText("")
        self.labelSnapshotThumbnail_20.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_20.setScaledContents(True)
        self.labelSnapshotThumbnail_20.setObjectName("labelSnapshotThumbnail_20")
        self.label_64 = QtGui.QLabel(self.frame_95)
        self.label_64.setGeometry(QtCore.QRect(6, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("border:none; background: none;")
        self.label_64.setObjectName("label_64")
        self.horizontalSlider_29 = QtGui.QSlider(self.frame_95)
        self.horizontalSlider_29.setGeometry(QtCore.QRect(63, 170, 65, 16))
        self.horizontalSlider_29.setProperty("value", 22)
        self.horizontalSlider_29.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_29.setObjectName("horizontalSlider_29")
        self.spinBox_57 = QtGui.QSpinBox(self.frame_95)
        self.spinBox_57.setGeometry(QtCore.QRect(133, 168, 50, 20))
        self.spinBox_57.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_57.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_57.setFont(font)
        self.spinBox_57.setStyleSheet("")
        self.spinBox_57.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_57.setProperty("value", 77)
        self.spinBox_57.setObjectName("spinBox_57")
        self.verticalLayout_18.addWidget(self.frame_32)
        self.verticalLayout_17.addWidget(self.frame_center_nest_21)
        self.horizontalLayout_18.addWidget(self.frame_white_border_39)
        self.horizontalLayout_20.addWidget(self.frame_angio_setup)
        self.stackedWidget_bottom.addWidget(self.page_angio_setup)
        self.page_angio_capture = QtGui.QWidget()
        self.page_angio_capture.setObjectName("page_angio_capture")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.page_angio_capture)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_center_nest = QtGui.QFrame(self.page_angio_capture)
        self.frame_center_nest.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_center_nest.setStyleSheet("QFrame#frame_center_nest {\n"
"    /*border: 1px solid #ff0000;*/\n"
"    border: none;\n"
"}")
        self.frame_center_nest.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest.setLineWidth(1)
        self.frame_center_nest.setObjectName("frame_center_nest")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_center_nest)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_white_border_10 = QtGui.QFrame(self.frame_center_nest)
        self.frame_white_border_10.setMinimumSize(QtCore.QSize(225, 0))
        self.frame_white_border_10.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_white_border_10.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_10.setLineWidth(1)
        self.frame_white_border_10.setObjectName("frame_white_border_10")
        self.gridLayout_14 = QtGui.QGridLayout(self.frame_white_border_10)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_center_nest_7 = QtGui.QFrame(self.frame_white_border_10)
        self.frame_center_nest_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_center_nest_7.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_7.setLineWidth(1)
        self.frame_center_nest_7.setObjectName("frame_center_nest_7")
        self.frame_13 = QtGui.QFrame(self.frame_center_nest_7)
        self.frame_13.setGeometry(QtCore.QRect(7, 10, 211, 241))
        self.frame_13.setStyleSheet("border: none;")
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_14 = QtGui.QLabel(self.frame_13)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border: none;")
        self.label_14.setObjectName("label_14")
        self.frame_74 = QtGui.QFrame(self.frame_13)
        self.frame_74.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_74.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_74.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_74.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_74.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.frame_75 = QtGui.QFrame(self.frame_74)
        self.frame_75.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_75.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_75.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_75.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_75.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.pushButton_64 = QtGui.QPushButton(self.frame_75)
        self.pushButton_64.setGeometry(QtCore.QRect(9, 20, 35, 30))
        self.pushButton_64.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_64.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_64.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_badge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_64.setIcon(icon28)
        self.pushButton_64.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_65 = QtGui.QPushButton(self.frame_75)
        self.pushButton_65.setGeometry(QtCore.QRect(53, 20, 35, 30))
        self.pushButton_65.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_65.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_65.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_65.setIcon(icon29)
        self.pushButton_65.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtGui.QPushButton(self.frame_75)
        self.pushButton_66.setGeometry(QtCore.QRect(99, 20, 35, 30))
        self.pushButton_66.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_66.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_66.setText("")
        self.pushButton_66.setIcon(icon1)
        self.pushButton_66.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtGui.QPushButton(self.frame_75)
        self.pushButton_67.setGeometry(QtCore.QRect(145, 20, 35, 30))
        self.pushButton_67.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_67.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_67.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_67.setIcon(icon30)
        self.pushButton_67.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_67.setObjectName("pushButton_67")
        self.labelSnapshotThumbnail_14 = QtGui.QLabel(self.frame_75)
        self.labelSnapshotThumbnail_14.setGeometry(QtCore.QRect(13, 60, 161, 131))
        self.labelSnapshotThumbnail_14.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_14.setText("")
        self.labelSnapshotThumbnail_14.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat1_retina_bv34s.jpg"))
        self.labelSnapshotThumbnail_14.setScaledContents(True)
        self.labelSnapshotThumbnail_14.setObjectName("labelSnapshotThumbnail_14")
        self.gridLayout_14.addWidget(self.frame_center_nest_7, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_white_border_10)
        self.frame_white_border_01 = QtGui.QFrame(self.frame_center_nest)
        self.frame_white_border_01.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_white_border_01.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_01.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_01.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_01.setLineWidth(1)
        self.frame_white_border_01.setObjectName("frame_white_border_01")
        self.gridLayout_15 = QtGui.QGridLayout(self.frame_white_border_01)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.frame_center_nest_4 = QtGui.QFrame(self.frame_white_border_01)
        self.frame_center_nest_4.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_center_nest_4.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_4.setLineWidth(1)
        self.frame_center_nest_4.setObjectName("frame_center_nest_4")
        self.gridLayout_9 = QtGui.QGridLayout(self.frame_center_nest_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_white_border_4 = QtGui.QFrame(self.frame_center_nest_4)
        self.frame_white_border_4.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_4.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_white_border_4.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_4.setLineWidth(1)
        self.frame_white_border_4.setObjectName("frame_white_border_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_white_border_4)
        self.gridLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_button_bar_7 = QtGui.QFrame(self.frame_white_border_4)
        self.frame_button_bar_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_7.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_7.setLineWidth(1)
        self.frame_button_bar_7.setObjectName("frame_button_bar_7")
        self.gridLayout = QtGui.QGridLayout(self.frame_button_bar_7)
        self.gridLayout.setObjectName("gridLayout")
        self.label_21 = QtGui.QLabel(self.frame_button_bar_7)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border: none; background: none;")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_angio_center_bscan_image = QtGui.QLabel(self.frame_button_bar_7)
        self.label_angio_center_bscan_image.setStyleSheet("border: none;")
        self.label_angio_center_bscan_image.setText("")
        self.label_angio_center_bscan_image.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat_retina36.jpg"))
        self.label_angio_center_bscan_image.setScaledContents(True)
        self.label_angio_center_bscan_image.setObjectName("label_angio_center_bscan_image")
        self.gridLayout.addWidget(self.label_angio_center_bscan_image, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_button_bar_7, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_white_border_4, 1, 0, 1, 1)
        self.frame_white_border_5 = QtGui.QFrame(self.frame_center_nest_4)
        self.frame_white_border_5.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_5.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_white_border_5.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_5.setLineWidth(1)
        self.frame_white_border_5.setObjectName("frame_white_border_5")
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_white_border_5)
        self.gridLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_button_bar_8 = QtGui.QFrame(self.frame_white_border_5)
        self.frame_button_bar_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_8.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_8.setLineWidth(1)
        self.frame_button_bar_8.setObjectName("frame_button_bar_8")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_button_bar_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_22 = QtGui.QLabel(self.frame_button_bar_8)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border: none; background: none;")
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_angio_current_bscan_image = QtGui.QLabel(self.frame_button_bar_8)
        self.label_angio_current_bscan_image.setStyleSheet("border: none;")
        self.label_angio_current_bscan_image.setText("")
        self.label_angio_current_bscan_image.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat_retina36.jpg"))
        self.label_angio_current_bscan_image.setScaledContents(True)
        self.label_angio_current_bscan_image.setObjectName("label_angio_current_bscan_image")
        self.gridLayout_2.addWidget(self.label_angio_current_bscan_image, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_button_bar_8, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_white_border_5, 2, 0, 1, 1)
        self.frame_white_border_3 = QtGui.QFrame(self.frame_center_nest_4)
        self.frame_white_border_3.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_white_border_3.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_3.setLineWidth(1)
        self.frame_white_border_3.setObjectName("frame_white_border_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_white_border_3)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_button_bar_5 = QtGui.QFrame(self.frame_white_border_3)
        self.frame_button_bar_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_5.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_5.setLineWidth(1)
        self.frame_button_bar_5.setObjectName("frame_button_bar_5")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_button_bar_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem13 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.frame_23 = QtGui.QFrame(self.frame_button_bar_5)
        self.frame_23.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_23.setStyleSheet("border: none; background: none;")
        self.frame_23.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.pushButton_130 = QtGui.QPushButton(self.frame_23)
        self.pushButton_130.setGeometry(QtCore.QRect(20, 3, 67, 30))
        self.pushButton_130.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_130.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_130.setFont(font)
        self.pushButton_130.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_130.setText("")
        self.pushButton_130.setIcon(icon2)
        self.pushButton_130.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_130.setObjectName("pushButton_130")
        self.pushButton_131 = QtGui.QPushButton(self.frame_23)
        self.pushButton_131.setGeometry(QtCore.QRect(239, 3, 67, 30))
        self.pushButton_131.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_131.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_131.setFont(font)
        self.pushButton_131.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_131.setText("")
        self.pushButton_131.setIcon(icon3)
        self.pushButton_131.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_131.setObjectName("pushButton_131")
        self.pushButton_132 = QtGui.QPushButton(self.frame_23)
        self.pushButton_132.setGeometry(QtCore.QRect(312, 3, 67, 30))
        self.pushButton_132.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_132.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_132.setFont(font)
        self.pushButton_132.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_132.setText("")
        self.pushButton_132.setIcon(icon15)
        self.pushButton_132.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_132.setObjectName("pushButton_132")
        self.pushButton_133 = QtGui.QPushButton(self.frame_23)
        self.pushButton_133.setGeometry(QtCore.QRect(166, 3, 67, 30))
        self.pushButton_133.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_133.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_133.setFont(font)
        self.pushButton_133.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_133.setText("")
        self.pushButton_133.setIcon(icon16)
        self.pushButton_133.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_133.setObjectName("pushButton_133")
        self.pushButton_134 = QtGui.QPushButton(self.frame_23)
        self.pushButton_134.setGeometry(QtCore.QRect(93, 3, 67, 30))
        self.pushButton_134.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_134.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_134.setFont(font)
        self.pushButton_134.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_134.setText("")
        self.pushButton_134.setIcon(icon4)
        self.pushButton_134.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_134.setObjectName("pushButton_134")
        self.horizontalLayout_5.addWidget(self.frame_23)
        spacerItem14 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.gridLayout_3.addWidget(self.frame_button_bar_5, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_white_border_3, 0, 0, 1, 2)
        self.frame_white_border_6 = QtGui.QFrame(self.frame_center_nest_4)
        self.frame_white_border_6.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_white_border_6.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_6.setLineWidth(1)
        self.frame_white_border_6.setObjectName("frame_white_border_6")
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_white_border_6)
        self.gridLayout_7.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_button_bar_9 = QtGui.QFrame(self.frame_white_border_6)
        self.frame_button_bar_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_button_bar_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_button_bar_9.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"}")
        self.frame_button_bar_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_button_bar_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_button_bar_9.setLineWidth(1)
        self.frame_button_bar_9.setObjectName("frame_button_bar_9")
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_button_bar_9)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_24 = QtGui.QLabel(self.frame_button_bar_9)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("border: none; background: none;")
        self.label_24.setObjectName("label_24")
        self.gridLayout_8.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_angio_preview_image = QtGui.QLabel(self.frame_button_bar_9)
        self.label_angio_preview_image.setStyleSheet("border: none;")
        self.label_angio_preview_image.setText("")
        self.label_angio_preview_image.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat1_retina_bv34s.jpg"))
        self.label_angio_preview_image.setScaledContents(True)
        self.label_angio_preview_image.setObjectName("label_angio_preview_image")
        self.gridLayout_8.addWidget(self.label_angio_preview_image, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_button_bar_9, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_white_border_6, 1, 1, 2, 1)
        self.gridLayout_15.addWidget(self.frame_center_nest_4, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_white_border_01)
        self.frame_white_border_11 = QtGui.QFrame(self.frame_center_nest)
        self.frame_white_border_11.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_white_border_11.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_white_border_11.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"    border-radius: 6px;\n"
"}")
        self.frame_white_border_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_white_border_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_white_border_11.setLineWidth(1)
        self.frame_white_border_11.setObjectName("frame_white_border_11")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.frame_white_border_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_center_nest_2 = QtGui.QFrame(self.frame_white_border_11)
        self.frame_center_nest_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center_nest_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_center_nest_2.setStyleSheet("QFrame {\n"
"  background: rgb(74, 74, 74);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_2.setLineWidth(1)
        self.frame_center_nest_2.setObjectName("frame_center_nest_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_center_nest_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(3, -1, 0, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtGui.QFrame(self.frame_center_nest_2)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 141))
        self.frame_6.setStyleSheet("border: none;")
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_5 = QtGui.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;")
        self.label_5.setObjectName("label_5")
        self.frame_60 = QtGui.QFrame(self.frame_6)
        self.frame_60.setGeometry(QtCore.QRect(10, 30, 190, 100))
        self.frame_60.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_60.setMaximumSize(QtCore.QSize(190, 100))
        self.frame_60.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_60.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.frame_61 = QtGui.QFrame(self.frame_60)
        self.frame_61.setGeometry(QtCore.QRect(1, 1, 188, 98))
        self.frame_61.setMinimumSize(QtCore.QSize(100, 50))
        self.frame_61.setMaximumSize(QtCore.QSize(190, 100))
        self.frame_61.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_61.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.spinBox_42 = QtGui.QSpinBox(self.frame_61)
        self.spinBox_42.setGeometry(QtCore.QRect(51, 66, 108, 23))
        self.spinBox_42.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_42.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_42.setSuffix("")
        self.spinBox_42.setMaximum(10000)
        self.spinBox_42.setObjectName("spinBox_42")
        self.verticalSlider_16 = QtGui.QSlider(self.frame_61)
        self.verticalSlider_16.setGeometry(QtCore.QRect(8, 10, 16, 81))
        self.verticalSlider_16.setMaximum(999)
        self.verticalSlider_16.setProperty("value", 444)
        self.verticalSlider_16.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_16.setObjectName("verticalSlider_16")
        self.pushButton_52 = QtGui.QPushButton(self.frame_61)
        self.pushButton_52.setGeometry(QtCore.QRect(50, 20, 50, 30))
        self.pushButton_52.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_52.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_52.setText("")
        self.pushButton_52.setIcon(icon6)
        self.pushButton_52.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtGui.QPushButton(self.frame_61)
        self.pushButton_53.setGeometry(QtCore.QRect(110, 20, 50, 30))
        self.pushButton_53.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_53.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_53.setText("")
        self.pushButton_53.setIcon(icon5)
        self.pushButton_53.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_53.setObjectName("pushButton_53")
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_11 = QtGui.QFrame(self.frame_center_nest_2)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 141))
        self.frame_11.setStyleSheet("border: none;")
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_16 = QtGui.QLabel(self.frame_11)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border: none;")
        self.label_16.setObjectName("label_16")
        self.frame_70 = QtGui.QFrame(self.frame_11)
        self.frame_70.setGeometry(QtCore.QRect(10, 30, 190, 100))
        self.frame_70.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_70.setMaximumSize(QtCore.QSize(190, 100))
        self.frame_70.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_70.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.frame_71 = QtGui.QFrame(self.frame_70)
        self.frame_71.setGeometry(QtCore.QRect(1, 1, 188, 98))
        self.frame_71.setMinimumSize(QtCore.QSize(100, 50))
        self.frame_71.setMaximumSize(QtCore.QSize(190, 100))
        self.frame_71.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_71.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.horizontalSlider_7 = QtGui.QSlider(self.frame_71)
        self.horizontalSlider_7.setGeometry(QtCore.QRect(75, 19, 50, 20))
        self.horizontalSlider_7.setProperty("value", 33)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.label_17 = QtGui.QLabel(self.frame_71)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border: none;\n"
"background:none;")
        self.label_17.setObjectName("label_17")
        self.spinBox_48 = QtGui.QSpinBox(self.frame_71)
        self.spinBox_48.setGeometry(QtCore.QRect(133, 20, 50, 20))
        self.spinBox_48.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_48.setFont(font)
        self.spinBox_48.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_48.setProperty("value", 33)
        self.spinBox_48.setObjectName("spinBox_48")
        self.label_18 = QtGui.QLabel(self.frame_71)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border: none;\n"
"background:none;")
        self.label_18.setObjectName("label_18")
        self.horizontalSlider_8 = QtGui.QSlider(self.frame_71)
        self.horizontalSlider_8.setGeometry(QtCore.QRect(75, 59, 50, 20))
        self.horizontalSlider_8.setProperty("value", 77)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.spinBox_49 = QtGui.QSpinBox(self.frame_71)
        self.spinBox_49.setGeometry(QtCore.QRect(133, 60, 50, 20))
        self.spinBox_49.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_49.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_49.setFont(font)
        self.spinBox_49.setStyleSheet("")
        self.spinBox_49.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_49.setProperty("value", 77)
        self.spinBox_49.setObjectName("spinBox_49")
        self.verticalLayout_3.addWidget(self.frame_11)
        spacerItem15 = QtGui.QSpacerItem(20, 61, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.frame_9 = QtGui.QFrame(self.frame_center_nest_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 241))
        self.frame_9.setStyleSheet("border: none;")
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_12 = QtGui.QLabel(self.frame_9)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border: none;")
        self.label_12.setObjectName("label_12")
        self.frame_66 = QtGui.QFrame(self.frame_9)
        self.frame_66.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_66.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_66.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_66.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_66.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.frame_67 = QtGui.QFrame(self.frame_66)
        self.frame_67.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_67.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_67.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_67.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_67.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.spinBox_39 = QtGui.QSpinBox(self.frame_67)
        self.spinBox_39.setGeometry(QtCore.QRect(30, 160, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_39.setFont(font)
        self.spinBox_39.setSuffix("")
        self.spinBox_39.setMaximum(360)
        self.spinBox_39.setProperty("value", 300)
        self.spinBox_39.setObjectName("spinBox_39")
        self.spinBox_41 = QtGui.QSpinBox(self.frame_67)
        self.spinBox_41.setGeometry(QtCore.QRect(30, 130, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_41.setFont(font)
        self.spinBox_41.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_41.setSuffix("")
        self.spinBox_41.setMaximum(9999)
        self.spinBox_41.setProperty("value", 5555)
        self.spinBox_41.setObjectName("spinBox_41")
        self.pushButton_56 = QtGui.QPushButton(self.frame_67)
        self.pushButton_56.setGeometry(QtCore.QRect(69, 18, 50, 30))
        self.pushButton_56.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_56.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_56.setText("")
        self.pushButton_56.setIcon(icon6)
        self.pushButton_56.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtGui.QPushButton(self.frame_67)
        self.pushButton_57.setGeometry(QtCore.QRect(69, 79, 50, 30))
        self.pushButton_57.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_57.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_57.setText("")
        self.pushButton_57.setIcon(icon5)
        self.pushButton_57.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtGui.QPushButton(self.frame_67)
        self.pushButton_58.setGeometry(QtCore.QRect(119, 48, 50, 30))
        self.pushButton_58.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_58.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_58.setText("")
        self.pushButton_58.setIcon(icon2)
        self.pushButton_58.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtGui.QPushButton(self.frame_67)
        self.pushButton_59.setGeometry(QtCore.QRect(19, 48, 50, 30))
        self.pushButton_59.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_59.setMaximumSize(QtCore.QSize(130, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 5px;\n"
"}")
        self.pushButton_59.setText("")
        self.pushButton_59.setIcon(icon18)
        self.pushButton_59.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_59.setObjectName("pushButton_59")
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_12 = QtGui.QFrame(self.frame_center_nest_2)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 232))
        self.frame_12.setStyleSheet("border: none;")
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_19 = QtGui.QLabel(self.frame_12)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border: none;")
        self.label_19.setObjectName("label_19")
        self.frame_72 = QtGui.QFrame(self.frame_12)
        self.frame_72.setGeometry(QtCore.QRect(10, 30, 190, 200))
        self.frame_72.setMinimumSize(QtCore.QSize(190, 100))
        self.frame_72.setMaximumSize(QtCore.QSize(190, 200))
        self.frame_72.setStyleSheet("QFrame {\n"
"background-color: none;\n"
"border: 1px solid rgb(95, 95, 95)\n"
"}")
        self.frame_72.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.frame_73 = QtGui.QFrame(self.frame_72)
        self.frame_73.setGeometry(QtCore.QRect(1, 1, 188, 198))
        self.frame_73.setMinimumSize(QtCore.QSize(100, 198))
        self.frame_73.setMaximumSize(QtCore.QSize(190, 198))
        self.frame_73.setStyleSheet("QFrame {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(23, 23, 23, 255), stop:0.497561 rgba(50, 50, 50, 255), stop:1 rgba(44, 44, 44, 255));\n"
"border: 2px solid black;\n"
"}")
        self.frame_73.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.labelSnapshotThumbnail_12 = QtGui.QLabel(self.frame_73)
        self.labelSnapshotThumbnail_12.setGeometry(QtCore.QRect(3, 3, 182, 158))
        self.labelSnapshotThumbnail_12.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_12.setText("")
        self.labelSnapshotThumbnail_12.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_12.setScaledContents(True)
        self.labelSnapshotThumbnail_12.setObjectName("labelSnapshotThumbnail_12")
        self.label_40 = QtGui.QLabel(self.frame_73)
        self.label_40.setGeometry(QtCore.QRect(6, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("border:none; background: none;")
        self.label_40.setObjectName("label_40")
        self.horizontalSlider_23 = QtGui.QSlider(self.frame_73)
        self.horizontalSlider_23.setGeometry(QtCore.QRect(63, 170, 65, 16))
        self.horizontalSlider_23.setProperty("value", 22)
        self.horizontalSlider_23.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_23.setObjectName("horizontalSlider_23")
        self.spinBox_50 = QtGui.QSpinBox(self.frame_73)
        self.spinBox_50.setGeometry(QtCore.QRect(133, 168, 50, 20))
        self.spinBox_50.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_50.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_50.setFont(font)
        self.spinBox_50.setStyleSheet("")
        self.spinBox_50.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_50.setProperty("value", 77)
        self.spinBox_50.setObjectName("spinBox_50")
        self.verticalLayout_3.addWidget(self.frame_12)
        self.verticalLayout_9.addWidget(self.frame_center_nest_2)
        self.horizontalLayout_2.addWidget(self.frame_white_border_11)
        self.horizontalLayout_3.addWidget(self.frame_center_nest)
        self.stackedWidget_bottom.addWidget(self.page_angio_capture)
        self.verticalLayout.addWidget(self.stackedWidget_bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_bottom.setCurrentIndex(2)
        QtCore.QObject.connect(self.comboBox_selector, QtCore.SIGNAL("currentIndexChanged(int)"), self.stackedWidget_bottom.setCurrentIndex)
        QtCore.QObject.connect(self.pushButton_hidden, QtCore.SIGNAL("clicked()"), self.comboBox_selector.hide)
        QtCore.QObject.connect(self.pushButton_hidden, QtCore.SIGNAL("clicked()"), self.pushButton_capture_hidden_red.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MicroAngio", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setup.setText(QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_capture.setText(QtGui.QApplication.translate("MainWindow", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_evaluate.setText(QtGui.QApplication.translate("MainWindow", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode_navigation.setItemText(0, QtGui.QApplication.translate("MainWindow", " Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode_navigation.setItemText(1, QtGui.QApplication.translate("MainWindow", " OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode_navigation.setItemText(2, QtGui.QApplication.translate("MainWindow", " Angiograph", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_selector.setItemText(0, QtGui.QApplication.translate("MainWindow", "HS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_selector.setItemText(1, QtGui.QApplication.translate("MainWindow", "OCTS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_selector.setItemText(2, QtGui.QApplication.translate("MainWindow", "OCTCAP", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_selector.setItemText(3, QtGui.QApplication.translate("MainWindow", "ANGIOS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_selector.setItemText(4, QtGui.QApplication.translate("MainWindow", "ANGIOCAP", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_capture_hidden_red.setText(QtGui.QApplication.translate("MainWindow", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Saved Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("MainWindow", "2016-04-29 17:54", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_135.setShortcut(QtGui.QApplication.translate("MainWindow", "Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "OCT Camera Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Int. Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "Line Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("MainWindow", "Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("MainWindow", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_43.setPrefix(QtGui.QApplication.translate("MainWindow", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("MainWindow", "Light Source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("MainWindow", "Power", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("MainWindow", "Saved Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("MainWindow", "2016-04-29 17:55", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("MainWindow", "OCT Volume Save configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_141.setText(QtGui.QApplication.translate("MainWindow", "Rectangle", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_10.setText(QtGui.QApplication.translate("MainWindow", "Raw OCT data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_9.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_140.setText(QtGui.QApplication.translate("MainWindow", "Spiral", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_142.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Scan Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_143.setText(QtGui.QApplication.translate("MainWindow", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("MainWindow", "OCT Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_48.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("MainWindow", "Saved Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("MainWindow", "2016-04-29 17:54", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_148.setShortcut(QtGui.QApplication.translate("MainWindow", "Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.label_49.setText(QtGui.QApplication.translate("MainWindow", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_44.setPrefix(QtGui.QApplication.translate("MainWindow", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_61.setText(QtGui.QApplication.translate("MainWindow", "Min. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setText(QtGui.QApplication.translate("MainWindow", "Max Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_63.setText(QtGui.QApplication.translate("MainWindow", "Colormap: Grey-Gist", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setText(QtGui.QApplication.translate("MainWindow", "Dispersion, Polarization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setText(QtGui.QApplication.translate("MainWindow", "Coeff. B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_59.setText(QtGui.QApplication.translate("MainWindow", "Coeff. C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("MainWindow", "Quar. Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("MainWindow", "Half Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setText(QtGui.QApplication.translate("MainWindow", "Scan line control", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_40.setPrefix(QtGui.QApplication.translate("MainWindow", "Angle: ", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_45.setPrefix(QtGui.QApplication.translate("MainWindow", "Length: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_52.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("MainWindow", "Saved Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("MainWindow", "2016-04-29 17:55", None, QtGui.QApplication.UnicodeUTF8))
        self.label_55.setText(QtGui.QApplication.translate("MainWindow", "Angio Save configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_159.setText(QtGui.QApplication.translate("MainWindow", "Rectangle", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_11.setText(QtGui.QApplication.translate("MainWindow", "Raw OCT data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_12.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_160.setText(QtGui.QApplication.translate("MainWindow", "Spiral", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_161.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Scan Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_162.setText(QtGui.QApplication.translate("MainWindow", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("MainWindow", "OCT Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.label_66.setText(QtGui.QApplication.translate("MainWindow", "Motion Correction", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_163.setText(QtGui.QApplication.translate("MainWindow", "Subtract", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_164.setText(QtGui.QApplication.translate("MainWindow", "Average", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_165.setText(QtGui.QApplication.translate("MainWindow", "Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_68.setText(QtGui.QApplication.translate("MainWindow", "Angiography Algorithm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_166.setText(QtGui.QApplication.translate("MainWindow", "Speckle", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_16.setText(QtGui.QApplication.translate("MainWindow", "Intensity and Phase data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "Angio B-scan", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_17.setText(QtGui.QApplication.translate("MainWindow", "Angio Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_18.setText(QtGui.QApplication.translate("MainWindow", "Angio Projection", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_175.setText(QtGui.QApplication.translate("MainWindow", "Complex \n"
"Differential \n"
"Variance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_64.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Center B-scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Current B-Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_130.setShortcut(QtGui.QApplication.translate("MainWindow", "Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Angiograph Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_42.setPrefix(QtGui.QApplication.translate("MainWindow", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Min. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Max. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Scan line control", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_39.setPrefix(QtGui.QApplication.translate("MainWindow", "Angle: ", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_41.setPrefix(QtGui.QApplication.translate("MainWindow", "Length: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))

import wasatch_logo_resources_rc
import colormap_resources_rc
import oct_gallery_resources_rc
import style_rc
import grey_icons_rc
import vis_gallery_resources_rc
