# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/border_group_test.ui'
#
# Created: Tue Apr 26 07:45:31 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1469, 880)
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_center_nest_13 = QtGui.QFrame(self.frame)
        self.frame_center_nest_13.setGeometry(QtCore.QRect(260, 6, 671, 43))
        self.frame_center_nest_13.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"}")
        self.frame_center_nest_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_13.setLineWidth(1)
        self.frame_center_nest_13.setObjectName("frame_center_nest_13")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_center_nest_13)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_36 = QtGui.QPushButton(self.frame_center_nest_13)
        self.pushButton_36.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_36.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("QPushButton:hover\n"
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
"border-radius: 0px;\n"
"    border-top-left-radius: 12px;\n"
"    border-bottom-left-radius: 12px;\n"
"}")
        self.pushButton_36.setObjectName("pushButton_36")
        self.horizontalLayout_6.addWidget(self.pushButton_36)
        self.pushButton_37 = QtGui.QPushButton(self.frame_center_nest_13)
        self.pushButton_37.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_37.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("QPushButton:hover\n"
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
"    background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.512195, y2:0, stop:0 rgba(137, 10, 10, 255), stop:1 rgba(186, 10, 10, 255));\n"
"border-radius: 0px;\n"
"}")
        self.pushButton_37.setObjectName("pushButton_37")
        self.horizontalLayout_6.addWidget(self.pushButton_37)
        self.pushButton_38 = QtGui.QPushButton(self.frame_center_nest_13)
        self.pushButton_38.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_38.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("QPushButton:hover\n"
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
"border-radius: 0px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"}")
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalLayout_6.addWidget(self.pushButton_38)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_23 = QtGui.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(0, 10, 109, 38))
        self.label_23.setStyleSheet("background-color: none;\n"
"border-color: none;\n"
"border: none;")
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/logos/images/logos/92x30_placeholder_logo.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.comboBox_6 = QtGui.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(109, 14, 121, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_6.setStyleSheet("QPushButton:hover\n"
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
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_center_nest = QtGui.QFrame(self.centralwidget)
        self.frame_center_nest.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_center_nest.setStyleSheet("QFrame#frame_center_nest {\n"
"    /*border: 1px solid #ff0000;*/\n"
"    border: none;\n"
"}")
        self.frame_center_nest.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest.setLineWidth(1)
        self.frame_center_nest.setObjectName("frame_center_nest")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_center_nest)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_badge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_64.setIcon(icon)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_65.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/1opc_gray_trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_66.setIcon(icon2)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_67.setIcon(icon3)
        self.pushButton_67.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_67.setObjectName("pushButton_67")
        self.labelSnapshotThumbnail_14 = QtGui.QLabel(self.frame_75)
        self.labelSnapshotThumbnail_14.setGeometry(QtCore.QRect(13, 60, 161, 131))
        self.labelSnapshotThumbnail_14.setStyleSheet("border: none;")
        self.labelSnapshotThumbnail_14.setText("")
        self.labelSnapshotThumbnail_14.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat_retina36.jpg"))
        self.labelSnapshotThumbnail_14.setScaledContents(True)
        self.labelSnapshotThumbnail_14.setObjectName("labelSnapshotThumbnail_14")
        self.gridLayout_14.addWidget(self.frame_center_nest_7, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_white_border_10)
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
        self.frame_white_border_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.label = QtGui.QLabel(self.frame_button_bar_7)
        self.label.setStyleSheet("border: none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat1_retina_bv34s.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_button_bar_7, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_white_border_4, 1, 0, 1, 1)
        self.frame_white_border_5 = QtGui.QFrame(self.frame_center_nest_4)
        self.frame_white_border_5.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_white_border_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.label_2 = QtGui.QLabel(self.frame_button_bar_8)
        self.label_2.setStyleSheet("border: none;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat1_retina_bv34s.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
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
        spacerItem1 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_130.setIcon(icon4)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_131.setIcon(icon5)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_record.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_132.setIcon(icon6)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_update_background.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_133.setIcon(icon7)
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_134.setIcon(icon8)
        self.pushButton_134.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_134.setObjectName("pushButton_134")
        self.horizontalLayout_5.addWidget(self.frame_23)
        spacerItem2 = QtGui.QSpacerItem(173, 37, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
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
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("border: none; background: none;")
        self.label_24.setObjectName("label_24")
        self.gridLayout_8.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_button_bar_9)
        self.label_3.setStyleSheet("border: none;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat1_retina_bv34s.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_button_bar_9, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_white_border_6, 1, 1, 2, 1)
        self.gridLayout_15.addWidget(self.frame_center_nest_4, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_white_border_01)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_52.setIcon(icon9)
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_53.setIcon(icon10)
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
        spacerItem3 = QtGui.QSpacerItem(20, 61, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
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
        self.pushButton_56.setIcon(icon9)
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
        self.pushButton_57.setIcon(icon10)
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
        self.pushButton_58.setIcon(icon4)
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/greys/images/grey_icons/10pc_gray_pure_left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_59.setIcon(icon11)
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
        self.horizontalLayout.addWidget(self.frame_white_border_11)
        self.verticalLayout_2.addWidget(self.frame_center_nest)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_36.setText(QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_37.setText(QtGui.QApplication.translate("MainWindow", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_38.setText(QtGui.QApplication.translate("MainWindow", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(0, QtGui.QApplication.translate("MainWindow", " Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(1, QtGui.QApplication.translate("MainWindow", " OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(2, QtGui.QApplication.translate("MainWindow", " OCT 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(3, QtGui.QApplication.translate("MainWindow", " Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_130.setShortcut(QtGui.QApplication.translate("MainWindow", "Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
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
import style_rc
import oct_gallery_resources_rc
import grey_icons_rc
import vis_gallery_resources_rc
