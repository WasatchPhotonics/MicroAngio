# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/microangio_layout.ui'
#
# Created: Fri Apr 15 15:24:09 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 940)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("/*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining\n"
" * a copy\n"
" * of this software and associated documentation files (the \"Software\"),\n"
" * to deal\n"
" * in the Software without restriction, including without limitation the\n"
" * rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or\n"
" * sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be\n"
" * included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND,\n"
" * EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF\n"
" * MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT\n"
" * SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR\n"
" * OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\n"
" * ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n"
" * DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545,\n"
"x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146,\n"
"255));\n"
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
"    background-color: #302F2F;\n"
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
"    border: 1px solid transparent; /* reserve space for selection border\n"
"*/\n"
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
"/* exclusive indicator = radio button style indicator (see\n"
" * QActionGroup::setExclusive) */\n"
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
"QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:on\n"
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
"    min-width: 75px;\n"
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
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off\n"
"{\n"
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
"QListView::item:!selected:hover, QListView::item:!selected:hover,\n"
"QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover,\n"
"QTreeView::item:selected:hover  {\n"
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
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0\n"
"silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
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
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup\n"
" * mode */\n"
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
"QTableView::item:pressed, QListView::item:pressed,\n"
"QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active,\n"
"QListView::item:selected:active  {\n"
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
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
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
"}\n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidgetCenter_3 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidgetCenter_3.setMinimumSize(QtCore.QSize(0, 60))
        self.stackedWidgetCenter_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.stackedWidgetCenter_3.setLineWidth(0)
        self.stackedWidgetCenter_3.setObjectName("stackedWidgetCenter_3")
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtGui.QFrame(self.page_9)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtGui.QLabel(self.frame_5)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/logos/images/logos/110x36_wp_angio.png"))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.comboBox_3 = QtGui.QComboBox(self.frame_5)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.frame_6 = QtGui.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_3 = QtGui.QPushButton(self.frame_6)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.pushButton_7 = QtGui.QPushButton(self.frame_6)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.frame_6)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7.addWidget(self.frame_6)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.stackedWidgetCenter_3.addWidget(self.page_9)
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_7 = QtGui.QLabel(self.page_10)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.label_7.setObjectName("label_7")
        self.stackedWidgetCenter_3.addWidget(self.page_10)
        self.gridLayout.addWidget(self.stackedWidgetCenter_3, 0, 0, 1, 3)
        self.stackedWidgetCenter_4 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidgetCenter_4.setMinimumSize(QtCore.QSize(210, 50))
        self.stackedWidgetCenter_4.setMaximumSize(QtCore.QSize(210, 16777215))
        self.stackedWidgetCenter_4.setObjectName("stackedWidgetCenter_4")
        self.page_13 = QtGui.QWidget()
        self.page_13.setObjectName("page_13")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page_13)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtGui.QFrame(self.page_13)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 10, 195, 211))
        self.frame_3.setMinimumSize(QtCore.QSize(195, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(195, 16777215))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_4 = QtGui.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 30, 31, 26))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtGui.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 30, 31, 26))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtGui.QPushButton(self.frame_3)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 30, 31, 26))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtGui.QPushButton(self.frame_3)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 30, 31, 26))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.labelSnapshotThumbnail_3 = QtGui.QLabel(self.frame_3)
        self.labelSnapshotThumbnail_3.setGeometry(QtCore.QRect(20, 70, 161, 121))
        self.labelSnapshotThumbnail_3.setText("")
        self.labelSnapshotThumbnail_3.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/fingernail_fullsize.png"))
        self.labelSnapshotThumbnail_3.setScaledContents(True)
        self.labelSnapshotThumbnail_3.setObjectName("labelSnapshotThumbnail_3")
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidgetCenter_4.addWidget(self.page_13)
        self.page_14 = QtGui.QWidget()
        self.page_14.setObjectName("page_14")
        self.label_9 = QtGui.QLabel(self.page_14)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.label_9.setObjectName("label_9")
        self.stackedWidgetCenter_4.addWidget(self.page_14)
        self.gridLayout.addWidget(self.stackedWidgetCenter_4, 1, 0, 2, 1)
        self.stackedWidgetCenter_2 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidgetCenter_2.setMinimumSize(QtCore.QSize(0, 50))
        self.stackedWidgetCenter_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.stackedWidgetCenter_2.setObjectName("stackedWidgetCenter_2")
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtGui.QFrame(self.page_7)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.frame_9 = QtGui.QFrame(self.frame_7)
        self.frame_9.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_5 = QtGui.QPushButton(self.frame_9)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_15.addWidget(self.pushButton_5)
        self.pushButton_15 = QtGui.QPushButton(self.frame_9)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setChecked(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_15.addWidget(self.pushButton_15)
        self.pushButton_16 = QtGui.QPushButton(self.frame_9)
        self.pushButton_16.setCheckable(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_15.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.frame_9)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setChecked(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_15.addWidget(self.pushButton_17)
        self.pushButton_18 = QtGui.QPushButton(self.frame_9)
        self.pushButton_18.setCheckable(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_15.addWidget(self.pushButton_18)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13.addWidget(self.frame_9)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.stackedWidgetCenter_2.addWidget(self.page_7)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_6 = QtGui.QLabel(self.page_8)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.label_6.setObjectName("label_6")
        self.stackedWidgetCenter_2.addWidget(self.page_8)
        self.gridLayout.addWidget(self.stackedWidgetCenter_2, 1, 1, 1, 1)
        self.stackedWidgetCenter_5 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidgetCenter_5.setMinimumSize(QtCore.QSize(210, 50))
        self.stackedWidgetCenter_5.setMaximumSize(QtCore.QSize(210, 16777215))
        self.stackedWidgetCenter_5.setObjectName("stackedWidgetCenter_5")
        self.page_15 = QtGui.QWidget()
        self.page_15.setObjectName("page_15")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.page_15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QtGui.QFrame(self.page_15)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtGui.QFrame(self.frame_2)
        self.frame_10.setMinimumSize(QtCore.QSize(195, 150))
        self.frame_10.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_11 = QtGui.QLabel(self.frame_10)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_11.setObjectName("label_11")
        self.verticalScrollBar = QtGui.QScrollBar(self.frame_10)
        self.verticalScrollBar.setGeometry(QtCore.QRect(20, 40, 16, 91))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.pushButton_19 = QtGui.QPushButton(self.frame_10)
        self.pushButton_19.setGeometry(QtCore.QRect(50, 40, 41, 27))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtGui.QPushButton(self.frame_10)
        self.pushButton_20.setGeometry(QtCore.QRect(50, 110, 41, 27))
        self.pushButton_20.setObjectName("pushButton_20")
        self.spinBox_6 = QtGui.QSpinBox(self.frame_10)
        self.spinBox_6.setGeometry(QtCore.QRect(50, 70, 91, 31))
        self.spinBox_6.setSuffix("")
        self.spinBox_6.setMaximum(10000)
        self.spinBox_6.setObjectName("spinBox_6")
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_11 = QtGui.QFrame(self.frame_2)
        self.frame_11.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_11.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_13 = QtGui.QLabel(self.frame_11)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_13.setObjectName("label_13")
        self.spinBox_7 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_7.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_7.setFont(font)
        self.spinBox_7.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_15 = QtGui.QLabel(self.frame_11)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalSlider_2 = QtGui.QSlider(self.frame_11)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtGui.QSlider(self.frame_11)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_3.setSliderPosition(77)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setInvertedAppearance(False)
        self.horizontalSlider_3.setInvertedControls(False)
        self.horizontalSlider_3.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_16 = QtGui.QLabel(self.frame_11)
        self.label_16.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.spinBox_8 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_8.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_8.setFont(font)
        self.spinBox_8.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_8.setProperty("value", 99)
        self.spinBox_8.setObjectName("spinBox_8")
        self.verticalLayout_2.addWidget(self.frame_11)
        self.frame_12 = QtGui.QFrame(self.frame_2)
        self.frame_12.setMinimumSize(QtCore.QSize(195, 70))
        self.frame_12.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_17 = QtGui.QLabel(self.frame_12)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_17.setObjectName("label_17")
        self.comboBox_4 = QtGui.QComboBox(self.frame_12)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 30, 81, 27))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.labelSnapshotThumbnail_5 = QtGui.QLabel(self.frame_12)
        self.labelSnapshotThumbnail_5.setGeometry(QtCore.QRect(90, 30, 24, 24))
        self.labelSnapshotThumbnail_5.setText("")
        self.labelSnapshotThumbnail_5.setPixmap(QtGui.QPixmap(":/thumbnails/images/colormaps/gray.jpg"))
        self.labelSnapshotThumbnail_5.setScaledContents(True)
        self.labelSnapshotThumbnail_5.setObjectName("labelSnapshotThumbnail_5")
        self.verticalLayout_2.addWidget(self.frame_12)
        self.frame_13 = QtGui.QFrame(self.frame_2)
        self.frame_13.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_13.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_18 = QtGui.QLabel(self.frame_13)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_18.setObjectName("label_18")
        self.spinBox_11 = QtGui.QSpinBox(self.frame_13)
        self.spinBox_11.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_11.setFont(font)
        self.spinBox_11.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_11.setObjectName("spinBox_11")
        self.label_19 = QtGui.QLabel(self.frame_13)
        self.label_19.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalSlider_4 = QtGui.QSlider(self.frame_13)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_5 = QtGui.QSlider(self.frame_13)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_5.setSliderPosition(77)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setInvertedAppearance(False)
        self.horizontalSlider_5.setInvertedControls(False)
        self.horizontalSlider_5.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.label_20 = QtGui.QLabel(self.frame_13)
        self.label_20.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.spinBox_12 = QtGui.QSpinBox(self.frame_13)
        self.spinBox_12.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_12.setFont(font)
        self.spinBox_12.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_12.setProperty("value", 99)
        self.spinBox_12.setObjectName("spinBox_12")
        self.verticalLayout_2.addWidget(self.frame_13)
        self.frame_14 = QtGui.QFrame(self.frame_2)
        self.frame_14.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_14.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_21 = QtGui.QLabel(self.frame_14)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_21.setObjectName("label_21")
        self.spinBox_13 = QtGui.QSpinBox(self.frame_14)
        self.spinBox_13.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_13.setFont(font)
        self.spinBox_13.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_13.setObjectName("spinBox_13")
        self.label_22 = QtGui.QLabel(self.frame_14)
        self.label_22.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalSlider_6 = QtGui.QSlider(self.frame_14)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.horizontalSlider_7 = QtGui.QSlider(self.frame_14)
        self.horizontalSlider_7.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_7.setSliderPosition(77)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setInvertedAppearance(False)
        self.horizontalSlider_7.setInvertedControls(False)
        self.horizontalSlider_7.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.label_23 = QtGui.QLabel(self.frame_14)
        self.label_23.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.spinBox_14 = QtGui.QSpinBox(self.frame_14)
        self.spinBox_14.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_14.setFont(font)
        self.spinBox_14.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_14.setProperty("value", 99)
        self.spinBox_14.setObjectName("spinBox_14")
        self.verticalLayout_2.addWidget(self.frame_14)
        spacerItem4 = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.frame_15 = QtGui.QFrame(self.frame_2)
        self.frame_15.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_15.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_5 = QtGui.QLabel(self.frame_15)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_5.setObjectName("label_5")
        self.labelSnapshotThumbnail_4 = QtGui.QLabel(self.frame_15)
        self.labelSnapshotThumbnail_4.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.labelSnapshotThumbnail_4.setText("")
        self.labelSnapshotThumbnail_4.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_4.setScaledContents(True)
        self.labelSnapshotThumbnail_4.setObjectName("labelSnapshotThumbnail_4")
        self.label_24 = QtGui.QLabel(self.frame_15)
        self.label_24.setGeometry(QtCore.QRect(13, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.spinBox_5 = QtGui.QSpinBox(self.frame_15)
        self.spinBox_5.setGeometry(QtCore.QRect(150, 180, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_5.setFont(font)
        self.spinBox_5.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalSlider = QtGui.QSlider(self.frame_15)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 180, 71, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.frame_15)
        self.frame_16 = QtGui.QFrame(self.frame_2)
        self.frame_16.setMinimumSize(QtCore.QSize(195, 150))
        self.frame_16.setMaximumSize(QtCore.QSize(195, 150))
        self.frame_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_25 = QtGui.QLabel(self.frame_16)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_25.setObjectName("label_25")
        self.pushButton_21 = QtGui.QPushButton(self.frame_16)
        self.pushButton_21.setGeometry(QtCore.QRect(80, 40, 41, 27))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtGui.QPushButton(self.frame_16)
        self.pushButton_22.setGeometry(QtCore.QRect(80, 80, 41, 27))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtGui.QPushButton(self.frame_16)
        self.pushButton_23.setGeometry(QtCore.QRect(130, 60, 41, 27))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtGui.QPushButton(self.frame_16)
        self.pushButton_24.setGeometry(QtCore.QRect(30, 60, 41, 27))
        self.pushButton_24.setObjectName("pushButton_24")
        self.spinBox_9 = QtGui.QSpinBox(self.frame_16)
        self.spinBox_9.setGeometry(QtCore.QRect(10, 120, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_9.setFont(font)
        self.spinBox_9.setSuffix("")
        self.spinBox_9.setMaximum(9999)
        self.spinBox_9.setProperty("value", 5555)
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtGui.QSpinBox(self.frame_16)
        self.spinBox_10.setGeometry(QtCore.QRect(110, 120, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_10.setFont(font)
        self.spinBox_10.setSuffix("")
        self.spinBox_10.setMaximum(360)
        self.spinBox_10.setProperty("value", 300)
        self.spinBox_10.setObjectName("spinBox_10")
        self.verticalLayout_2.addWidget(self.frame_16)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.stackedWidgetCenter_5.addWidget(self.page_15)
        self.page_16 = QtGui.QWidget()
        self.page_16.setObjectName("page_16")
        self.label_10 = QtGui.QLabel(self.page_16)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.label_10.setObjectName("label_10")
        self.stackedWidgetCenter_5.addWidget(self.page_16)
        self.gridLayout.addWidget(self.stackedWidgetCenter_5, 1, 2, 2, 1)
        self.stackedWidgetCenter = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidgetCenter.setObjectName("stackedWidgetCenter")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameCenterArea = QtGui.QFrame(self.page_3)
        self.frameCenterArea.setMinimumSize(QtCore.QSize(200, 0))
        self.frameCenterArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameCenterArea.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCenterArea.setObjectName("frameCenterArea")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frameCenterArea)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtGui.QFrame(self.frameCenterArea)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/30layerstape_fullsize11.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.frame_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frameCenterArea)
        self.stackedWidgetCenter.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.label = QtGui.QLabel(self.page_4)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.label.setObjectName("label")
        self.stackedWidgetCenter.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidgetCenter, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidgetCenter_3.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(1)
        self.stackedWidgetCenter_4.setCurrentIndex(0)
        self.stackedWidgetCenter_2.setCurrentIndex(0)
        self.stackedWidgetCenter_5.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.stackedWidgetCenter.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("MainWindow", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("MainWindow", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("MainWindow", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Top area", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Left control area", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("MainWindow", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("MainWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Top center button area", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_19.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_20.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_6.setPrefix(QtGui.QApplication.translate("MainWindow", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Min. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Max. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Colormap", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(0, QtGui.QApplication.translate("MainWindow", "Gray", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(1, QtGui.QApplication.translate("MainWindow", "HSV", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(2, QtGui.QApplication.translate("MainWindow", "Jet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Dispersion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Coeff. B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Oceff. C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Polarization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Half Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Quar. Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Scan line control", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_21.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_22.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_23.setText(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_24.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_9.setPrefix(QtGui.QApplication.translate("MainWindow", "Length: ", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_10.setPrefix(QtGui.QApplication.translate("MainWindow", "Angle: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Left control area", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Center image area", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
import wasatch_logo_resources_rc
import vis_gallery_resources_rc
import colormap_resources_rc
