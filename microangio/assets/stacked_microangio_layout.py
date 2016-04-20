# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/stacked_microangio_layout.ui'
#
# Created: Wed Apr 20 14:11:02 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 1075)
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
"\n"
"\n"
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
"\n"
"/******************************************************************************************/\n"
"QFrame\n"
"{\n"
"  border: none;\n"
"}")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_top_navigation = QtGui.QFrame(self.centralwidget)
        self.frame_top_navigation.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_top_navigation.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_top_navigation.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top_navigation.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top_navigation.setObjectName("frame_top_navigation")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_top_navigation)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.frame_top_navigation)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/logos/images/logos/110x36_wp_angio.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_mode = QtGui.QComboBox(self.frame_top_navigation)
        self.comboBox_mode.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_mode)
        self.comboBox_mode_2 = QtGui.QComboBox(self.frame_top_navigation)
        self.comboBox_mode_2.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.comboBox_mode_2.setObjectName("comboBox_mode_2")
        self.comboBox_mode_2.addItem("")
        self.comboBox_mode_2.addItem("")
        self.comboBox_mode_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_mode_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_10 = QtGui.QFrame(self.frame_top_navigation)
        self.frame_10.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.stackedWidgetHeaderNavigation = QtGui.QStackedWidget(self.frame_top_navigation)
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
        spacerItem1 = QtGui.QSpacerItem(210, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.stackedWidgetHeaderNavigation.addWidget(self.page_hardware)
        self.page_oct = QtGui.QWidget()
        self.page_oct.setObjectName("page_oct")
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.page_oct)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_nav_oct_setup = QtGui.QPushButton(self.page_oct)
        self.pushButton_nav_oct_setup.setCheckable(True)
        self.pushButton_nav_oct_setup.setObjectName("pushButton_nav_oct_setup")
        self.horizontalLayout_20.addWidget(self.pushButton_nav_oct_setup)
        self.pushButton_nav_oct_capture = QtGui.QPushButton(self.page_oct)
        self.pushButton_nav_oct_capture.setCheckable(True)
        self.pushButton_nav_oct_capture.setChecked(True)
        self.pushButton_nav_oct_capture.setObjectName("pushButton_nav_oct_capture")
        self.horizontalLayout_20.addWidget(self.pushButton_nav_oct_capture)
        self.pushButton_18 = QtGui.QPushButton(self.page_oct)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_20.addWidget(self.pushButton_18)
        self.stackedWidgetHeaderNavigation.addWidget(self.page_oct)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidgetHeaderNavigation.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidgetHeaderNavigation)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addWidget(self.frame_top_navigation, 0, 0, 1, 1)
        self.stackedWidget_main = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_main_hardware_setup = QtGui.QWidget()
        self.page_main_hardware_setup.setObjectName("page_main_hardware_setup")
        self.gridLayout_2 = QtGui.QGridLayout(self.page_main_hardware_setup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtGui.QFrame(self.page_main_hardware_setup)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_hws_left_frame = QtGui.QFrame(self.frame)
        self.frame_hws_left_frame.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_hws_left_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_hws_left_frame.setStyleSheet("QFrame#frame_hws_left_frame {\n"
" border: 1px solid #444;\n"
" padding: -8px;\n"
"}")
        self.frame_hws_left_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_hws_left_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_hws_left_frame.setObjectName("frame_hws_left_frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_hws_left_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_hws_saved = QtGui.QFrame(self.frame_hws_left_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_hws_saved.sizePolicy().hasHeightForWidth())
        self.frame_hws_saved.setSizePolicy(sizePolicy)
        self.frame_hws_saved.setMinimumSize(QtCore.QSize(195, 250))
        self.frame_hws_saved.setMaximumSize(QtCore.QSize(195, 250))
        self.frame_hws_saved.setStyleSheet("QFrame {\n"
"  border: none;\n"
"  padding: -4px;\n"
"}")
        self.frame_hws_saved.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_hws_saved.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_hws_saved.setObjectName("frame_hws_saved")
        self.label_2 = QtGui.QLabel(self.frame_hws_saved)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.labelSnapshotThumbnail_2 = QtGui.QLabel(self.frame_hws_saved)
        self.labelSnapshotThumbnail_2.setGeometry(QtCore.QRect(20, 60, 161, 121))
        self.labelSnapshotThumbnail_2.setText("")
        self.labelSnapshotThumbnail_2.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/raw_image_pyqtgraph_plot.png"))
        self.labelSnapshotThumbnail_2.setScaledContents(True)
        self.labelSnapshotThumbnail_2.setObjectName("labelSnapshotThumbnail_2")
        self.label_42 = QtGui.QLabel(self.frame_hws_saved)
        self.label_42.setGeometry(QtCore.QRect(20, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.pushButton_10 = QtGui.QPushButton(self.frame_hws_saved)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 190, 41, 26))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(self.frame_hws_saved)
        self.pushButton_11.setGeometry(QtCore.QRect(70, 190, 41, 26))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.frame_hws_saved)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frame_hws_left_frame)
        self.frame_hws_center_frame = QtGui.QFrame(self.frame)
        self.frame_hws_center_frame.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_hws_center_frame.setStyleSheet("QFrame#frame_hws_center_frame {\n"
" border: 1px solid #444;\n"
" padding: -8px;\n"
"}")
        self.frame_hws_center_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_hws_center_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_hws_center_frame.setObjectName("frame_hws_center_frame")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_hws_center_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtGui.QLabel(self.frame_hws_center_frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/raw_image_pyqtgraph_plot.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.frame_14 = QtGui.QFrame(self.frame_hws_center_frame)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
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
        self.pushButton_6 = QtGui.QPushButton(self.frame_19)
        self.pushButton_6.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_18.addWidget(self.pushButton_6)
        self.pushButton_22 = QtGui.QPushButton(self.frame_19)
        self.pushButton_22.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_22.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setChecked(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_18.addWidget(self.pushButton_22)
        self.pushButton_24 = QtGui.QPushButton(self.frame_19)
        self.pushButton_24.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_24.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setChecked(False)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_18.addWidget(self.pushButton_24)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_16.addWidget(self.frame_19)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.gridLayout_4.addWidget(self.frame_14, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_hws_center_frame)
        self.frame_hws_right_frame = QtGui.QFrame(self.frame)
        self.frame_hws_right_frame.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_hws_right_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_hws_right_frame.setStyleSheet("QFrame#frame_hws_right_frame {\n"
" border: 1px solid #444;\n"
" padding: -8px;\n"
"}")
        self.frame_hws_right_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_hws_right_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_hws_right_frame.setObjectName("frame_hws_right_frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_hws_right_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_12 = QtGui.QFrame(self.frame_hws_right_frame)
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
        self.frame_11 = QtGui.QFrame(self.frame_hws_right_frame)
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
        self.frame_20 = QtGui.QFrame(self.frame_hws_right_frame)
        self.frame_20.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_20.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_25 = QtGui.QLabel(self.frame_20)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_25.setObjectName("label_25")
        self.pushButton_19 = QtGui.QPushButton(self.frame_20)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 30, 51, 27))
        self.pushButton_19.setObjectName("pushButton_19")
        self.spinBox_33 = QtGui.QSpinBox(self.frame_20)
        self.spinBox_33.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_33.setFont(font)
        self.spinBox_33.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_33.setMaximum(100)
        self.spinBox_33.setProperty("value", 100)
        self.spinBox_33.setObjectName("spinBox_33")
        self.horizontalSlider_23 = QtGui.QSlider(self.frame_20)
        self.horizontalSlider_23.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_23.setSliderPosition(77)
        self.horizontalSlider_23.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_23.setInvertedAppearance(False)
        self.horizontalSlider_23.setInvertedControls(False)
        self.horizontalSlider_23.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_23.setObjectName("horizontalSlider_23")
        self.label_46 = QtGui.QLabel(self.frame_20)
        self.label_46.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_2.addWidget(self.frame_20)
        spacerItem6 = QtGui.QSpacerItem(175, 149, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.frame_7 = QtGui.QFrame(self.frame_hws_right_frame)
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
        self.horizontalLayout.addWidget(self.frame_hws_right_frame)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget_main.addWidget(self.page_main_hardware_setup)
        self.page_main_oct_setup = QtGui.QWidget()
        self.page_main_oct_setup.setObjectName("page_main_oct_setup")
        self.gridLayout_3 = QtGui.QGridLayout(self.page_main_oct_setup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_5 = QtGui.QFrame(self.page_main_oct_setup)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtGui.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_9 = QtGui.QFrame(self.frame_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QtCore.QSize(195, 250))
        self.frame_9.setMaximumSize(QtCore.QSize(195, 250))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_4 = QtGui.QLabel(self.frame_9)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_43 = QtGui.QLabel(self.frame_9)
        self.label_43.setGeometry(QtCore.QRect(20, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.pushButton_12 = QtGui.QPushButton(self.frame_9)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 190, 31, 26))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtGui.QPushButton(self.frame_9)
        self.pushButton_13.setGeometry(QtCore.QRect(60, 190, 31, 26))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_3.addWidget(self.frame_9)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_13 = QtGui.QFrame(self.frame_5)
        self.frame_13.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_13)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_15 = QtGui.QFrame(self.frame_13)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_9 = QtGui.QLabel(self.frame_15)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_28 = QtGui.QPushButton(self.frame_15)
        self.pushButton_28.setGeometry(QtCore.QRect(330, 40, 91, 61))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtGui.QPushButton(self.frame_15)
        self.pushButton_29.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtGui.QPushButton(self.frame_15)
        self.pushButton_30.setGeometry(QtCore.QRect(230, 40, 91, 61))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtGui.QPushButton(self.frame_15)
        self.pushButton_31.setGeometry(QtCore.QRect(130, 40, 91, 61))
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_5.addWidget(self.frame_15, 2, 0, 1, 1)
        self.frame_16 = QtGui.QFrame(self.frame_13)
        self.frame_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_16)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkBox_7 = QtGui.QCheckBox(self.frame_16)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_6.addWidget(self.checkBox_7, 2, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame_16)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.frame_16)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_6.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_8 = QtGui.QCheckBox(self.frame_16)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_6.addWidget(self.checkBox_8, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_16, 1, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem8, 3, 0, 1, 1)
        self.frame_17 = QtGui.QFrame(self.frame_13)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_17.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem9)
        self.frame_21 = QtGui.QFrame(self.frame_17)
        self.frame_21.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pushButton_25 = QtGui.QPushButton(self.frame_21)
        self.pushButton_25.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_25.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setChecked(False)
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_22.addWidget(self.pushButton_25)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_19.addWidget(self.frame_21)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.gridLayout_5.addWidget(self.frame_17, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_13)
        self.frame_18 = QtGui.QFrame(self.frame_5)
        self.frame_18.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_18.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_18.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_18)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem11 = QtGui.QSpacerItem(175, 617, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.frame_22 = QtGui.QFrame(self.frame_18)
        self.frame_22.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_22.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_22.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.label_6 = QtGui.QLabel(self.frame_22)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_6.setObjectName("label_6")
        self.labelSnapshotThumbnail_7 = QtGui.QLabel(self.frame_22)
        self.labelSnapshotThumbnail_7.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.labelSnapshotThumbnail_7.setText("")
        self.labelSnapshotThumbnail_7.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_7.setScaledContents(True)
        self.labelSnapshotThumbnail_7.setObjectName("labelSnapshotThumbnail_7")
        self.label_26 = QtGui.QLabel(self.frame_22)
        self.label_26.setGeometry(QtCore.QRect(13, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.spinBox_19 = QtGui.QSpinBox(self.frame_22)
        self.spinBox_19.setGeometry(QtCore.QRect(150, 180, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_19.setFont(font)
        self.spinBox_19.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_19.setObjectName("spinBox_19")
        self.horizontalSlider_11 = QtGui.QSlider(self.frame_22)
        self.horizontalSlider_11.setGeometry(QtCore.QRect(70, 180, 71, 16))
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.verticalLayout_4.addWidget(self.frame_22)
        self.horizontalLayout_2.addWidget(self.frame_18)
        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)
        self.stackedWidget_main.addWidget(self.page_main_oct_setup)
        self.page_main_oct_capture = QtGui.QWidget()
        self.page_main_oct_capture.setObjectName("page_main_oct_capture")
        self.gridLayout_14 = QtGui.QGridLayout(self.page_main_oct_capture)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_33 = QtGui.QFrame(self.page_main_oct_capture)
        self.frame_33.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_64 = QtGui.QHBoxLayout(self.frame_33)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.frame_223 = QtGui.QFrame(self.frame_33)
        self.frame_223.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_223.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_223.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_223.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_223.setObjectName("frame_223")
        self.verticalLayout_42 = QtGui.QVBoxLayout(self.frame_223)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.frame_224 = QtGui.QFrame(self.frame_223)
        self.frame_224.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_224.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_224.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_224.setObjectName("frame_224")
        self.label_307 = QtGui.QLabel(self.frame_224)
        self.label_307.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_307.setObjectName("label_307")
        self.pushButton_252 = QtGui.QPushButton(self.frame_224)
        self.pushButton_252.setGeometry(QtCore.QRect(20, 30, 31, 26))
        self.pushButton_252.setCheckable(True)
        self.pushButton_252.setObjectName("pushButton_252")
        self.pushButton_253 = QtGui.QPushButton(self.frame_224)
        self.pushButton_253.setGeometry(QtCore.QRect(60, 30, 31, 26))
        self.pushButton_253.setCheckable(True)
        self.pushButton_253.setObjectName("pushButton_253")
        self.pushButton_254 = QtGui.QPushButton(self.frame_224)
        self.pushButton_254.setGeometry(QtCore.QRect(100, 30, 31, 26))
        self.pushButton_254.setCheckable(True)
        self.pushButton_254.setObjectName("pushButton_254")
        self.pushButton_255 = QtGui.QPushButton(self.frame_224)
        self.pushButton_255.setGeometry(QtCore.QRect(140, 30, 31, 26))
        self.pushButton_255.setCheckable(True)
        self.pushButton_255.setObjectName("pushButton_255")
        self.labelSnapshotThumbnail_38 = QtGui.QLabel(self.frame_224)
        self.labelSnapshotThumbnail_38.setGeometry(QtCore.QRect(20, 70, 161, 121))
        self.labelSnapshotThumbnail_38.setText("")
        self.labelSnapshotThumbnail_38.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/cat1_retina36s.jpg"))
        self.labelSnapshotThumbnail_38.setScaledContents(True)
        self.labelSnapshotThumbnail_38.setObjectName("labelSnapshotThumbnail_38")
        self.verticalLayout_42.addWidget(self.frame_224)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_42.addItem(spacerItem12)
        self.horizontalLayout_64.addWidget(self.frame_223)
        self.frame_225 = QtGui.QFrame(self.frame_33)
        self.frame_225.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_225.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_225.setObjectName("frame_225")
        self.verticalLayout_43 = QtGui.QVBoxLayout(self.frame_225)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.frame_226 = QtGui.QFrame(self.frame_225)
        self.frame_226.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_226.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_226.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_226.setObjectName("frame_226")
        self.horizontalLayout_65 = QtGui.QHBoxLayout(self.frame_226)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem13)
        self.frame_227 = QtGui.QFrame(self.frame_226)
        self.frame_227.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_227.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_227.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_227.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_227.setObjectName("frame_227")
        self.horizontalLayout_66 = QtGui.QHBoxLayout(self.frame_227)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.horizontalLayout_67 = QtGui.QHBoxLayout()
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.pushButton_256 = QtGui.QPushButton(self.frame_227)
        self.pushButton_256.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_256.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_256.setCheckable(True)
        self.pushButton_256.setChecked(True)
        self.pushButton_256.setObjectName("pushButton_256")
        self.horizontalLayout_67.addWidget(self.pushButton_256)
        self.pushButton_257 = QtGui.QPushButton(self.frame_227)
        self.pushButton_257.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_257.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_257.setCheckable(True)
        self.pushButton_257.setChecked(False)
        self.pushButton_257.setObjectName("pushButton_257")
        self.horizontalLayout_67.addWidget(self.pushButton_257)
        self.pushButton_258 = QtGui.QPushButton(self.frame_227)
        self.pushButton_258.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_258.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_258.setCheckable(True)
        self.pushButton_258.setChecked(False)
        self.pushButton_258.setObjectName("pushButton_258")
        self.horizontalLayout_67.addWidget(self.pushButton_258)
        self.pushButton_259 = QtGui.QPushButton(self.frame_227)
        self.pushButton_259.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_259.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_259.setCheckable(True)
        self.pushButton_259.setChecked(False)
        self.pushButton_259.setObjectName("pushButton_259")
        self.horizontalLayout_67.addWidget(self.pushButton_259)
        self.pushButton_260 = QtGui.QPushButton(self.frame_227)
        self.pushButton_260.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_260.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_260.setCheckable(True)
        self.pushButton_260.setChecked(False)
        self.pushButton_260.setObjectName("pushButton_260")
        self.horizontalLayout_67.addWidget(self.pushButton_260)
        self.horizontalLayout_66.addLayout(self.horizontalLayout_67)
        self.horizontalLayout_65.addWidget(self.frame_227)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem14)
        self.verticalLayout_43.addWidget(self.frame_226)
        self.frame_228 = QtGui.QFrame(self.frame_225)
        self.frame_228.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_228.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_228.setObjectName("frame_228")
        self.gridLayout_25 = QtGui.QGridLayout(self.frame_228)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.labelSnapshotThumbnail_39 = QtGui.QLabel(self.frame_228)
        self.labelSnapshotThumbnail_39.setText("")
        self.labelSnapshotThumbnail_39.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/cat1_retina36s.jpg"))
        self.labelSnapshotThumbnail_39.setScaledContents(True)
        self.labelSnapshotThumbnail_39.setObjectName("labelSnapshotThumbnail_39")
        self.gridLayout_25.addWidget(self.labelSnapshotThumbnail_39, 0, 0, 1, 1)
        self.verticalLayout_43.addWidget(self.frame_228)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_43.addItem(spacerItem15)
        self.horizontalLayout_64.addWidget(self.frame_225)
        self.frame_229 = QtGui.QFrame(self.frame_33)
        self.frame_229.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_229.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_229.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_229.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_229.setObjectName("frame_229")
        self.verticalLayout_44 = QtGui.QVBoxLayout(self.frame_229)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.frame_230 = QtGui.QFrame(self.frame_229)
        self.frame_230.setMinimumSize(QtCore.QSize(195, 150))
        self.frame_230.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_230.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_230.setObjectName("frame_230")
        self.label_308 = QtGui.QLabel(self.frame_230)
        self.label_308.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_308.setObjectName("label_308")
        self.verticalScrollBar_19 = QtGui.QScrollBar(self.frame_230)
        self.verticalScrollBar_19.setGeometry(QtCore.QRect(20, 40, 16, 91))
        self.verticalScrollBar_19.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_19.setObjectName("verticalScrollBar_19")
        self.pushButton_261 = QtGui.QPushButton(self.frame_230)
        self.pushButton_261.setGeometry(QtCore.QRect(50, 40, 41, 27))
        self.pushButton_261.setObjectName("pushButton_261")
        self.pushButton_262 = QtGui.QPushButton(self.frame_230)
        self.pushButton_262.setGeometry(QtCore.QRect(50, 110, 41, 27))
        self.pushButton_262.setObjectName("pushButton_262")
        self.spinBox_184 = QtGui.QSpinBox(self.frame_230)
        self.spinBox_184.setGeometry(QtCore.QRect(50, 70, 91, 31))
        self.spinBox_184.setSuffix("")
        self.spinBox_184.setMaximum(10000)
        self.spinBox_184.setObjectName("spinBox_184")
        self.verticalLayout_44.addWidget(self.frame_230)
        self.frame_231 = QtGui.QFrame(self.frame_229)
        self.frame_231.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_231.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_231.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_231.setObjectName("frame_231")
        self.label_309 = QtGui.QLabel(self.frame_231)
        self.label_309.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_309.setObjectName("label_309")
        self.spinBox_185 = QtGui.QSpinBox(self.frame_231)
        self.spinBox_185.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_185.setFont(font)
        self.spinBox_185.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_185.setObjectName("spinBox_185")
        self.label_310 = QtGui.QLabel(self.frame_231)
        self.label_310.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_310.setFont(font)
        self.label_310.setObjectName("label_310")
        self.horizontalSlider_128 = QtGui.QSlider(self.frame_231)
        self.horizontalSlider_128.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_128.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_128.setObjectName("horizontalSlider_128")
        self.horizontalSlider_129 = QtGui.QSlider(self.frame_231)
        self.horizontalSlider_129.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_129.setSliderPosition(77)
        self.horizontalSlider_129.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_129.setInvertedAppearance(False)
        self.horizontalSlider_129.setInvertedControls(False)
        self.horizontalSlider_129.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_129.setObjectName("horizontalSlider_129")
        self.label_311 = QtGui.QLabel(self.frame_231)
        self.label_311.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_311.setFont(font)
        self.label_311.setObjectName("label_311")
        self.spinBox_186 = QtGui.QSpinBox(self.frame_231)
        self.spinBox_186.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_186.setFont(font)
        self.spinBox_186.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_186.setProperty("value", 99)
        self.spinBox_186.setObjectName("spinBox_186")
        self.verticalLayout_44.addWidget(self.frame_231)
        self.label_312 = QtGui.QLabel(self.frame_229)
        self.label_312.setObjectName("label_312")
        self.verticalLayout_44.addWidget(self.label_312)
        self.frame_232 = QtGui.QFrame(self.frame_229)
        self.frame_232.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_232.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_232.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_232.setObjectName("frame_232")
        self.label_313 = QtGui.QLabel(self.frame_232)
        self.label_313.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_313.setObjectName("label_313")
        self.spinBox_187 = QtGui.QSpinBox(self.frame_232)
        self.spinBox_187.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_187.setFont(font)
        self.spinBox_187.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_187.setObjectName("spinBox_187")
        self.label_314 = QtGui.QLabel(self.frame_232)
        self.label_314.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_314.setFont(font)
        self.label_314.setObjectName("label_314")
        self.horizontalSlider_130 = QtGui.QSlider(self.frame_232)
        self.horizontalSlider_130.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_130.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_130.setObjectName("horizontalSlider_130")
        self.horizontalSlider_131 = QtGui.QSlider(self.frame_232)
        self.horizontalSlider_131.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_131.setSliderPosition(77)
        self.horizontalSlider_131.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_131.setInvertedAppearance(False)
        self.horizontalSlider_131.setInvertedControls(False)
        self.horizontalSlider_131.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_131.setObjectName("horizontalSlider_131")
        self.label_315 = QtGui.QLabel(self.frame_232)
        self.label_315.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_315.setFont(font)
        self.label_315.setObjectName("label_315")
        self.spinBox_188 = QtGui.QSpinBox(self.frame_232)
        self.spinBox_188.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_188.setFont(font)
        self.spinBox_188.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_188.setProperty("value", 99)
        self.spinBox_188.setObjectName("spinBox_188")
        self.verticalLayout_44.addWidget(self.frame_232)
        self.frame_233 = QtGui.QFrame(self.frame_229)
        self.frame_233.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_233.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_233.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_233.setObjectName("frame_233")
        self.label_316 = QtGui.QLabel(self.frame_233)
        self.label_316.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_316.setObjectName("label_316")
        self.spinBox_189 = QtGui.QSpinBox(self.frame_233)
        self.spinBox_189.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_189.setFont(font)
        self.spinBox_189.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_189.setObjectName("spinBox_189")
        self.label_317 = QtGui.QLabel(self.frame_233)
        self.label_317.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_317.setFont(font)
        self.label_317.setObjectName("label_317")
        self.horizontalSlider_132 = QtGui.QSlider(self.frame_233)
        self.horizontalSlider_132.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_132.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_132.setObjectName("horizontalSlider_132")
        self.horizontalSlider_133 = QtGui.QSlider(self.frame_233)
        self.horizontalSlider_133.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_133.setSliderPosition(77)
        self.horizontalSlider_133.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_133.setInvertedAppearance(False)
        self.horizontalSlider_133.setInvertedControls(False)
        self.horizontalSlider_133.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_133.setObjectName("horizontalSlider_133")
        self.label_318 = QtGui.QLabel(self.frame_233)
        self.label_318.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_318.setFont(font)
        self.label_318.setObjectName("label_318")
        self.spinBox_190 = QtGui.QSpinBox(self.frame_233)
        self.spinBox_190.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_190.setFont(font)
        self.spinBox_190.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_190.setProperty("value", 99)
        self.spinBox_190.setObjectName("spinBox_190")
        self.verticalLayout_44.addWidget(self.frame_233)
        spacerItem16 = QtGui.QSpacerItem(175, 49, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_44.addItem(spacerItem16)
        self.frame_234 = QtGui.QFrame(self.frame_229)
        self.frame_234.setMinimumSize(QtCore.QSize(195, 150))
        self.frame_234.setMaximumSize(QtCore.QSize(195, 150))
        self.frame_234.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_234.setObjectName("frame_234")
        self.label_319 = QtGui.QLabel(self.frame_234)
        self.label_319.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_319.setObjectName("label_319")
        self.pushButton_263 = QtGui.QPushButton(self.frame_234)
        self.pushButton_263.setGeometry(QtCore.QRect(80, 40, 41, 27))
        self.pushButton_263.setObjectName("pushButton_263")
        self.pushButton_264 = QtGui.QPushButton(self.frame_234)
        self.pushButton_264.setGeometry(QtCore.QRect(80, 80, 41, 27))
        self.pushButton_264.setObjectName("pushButton_264")
        self.pushButton_265 = QtGui.QPushButton(self.frame_234)
        self.pushButton_265.setGeometry(QtCore.QRect(130, 60, 41, 27))
        self.pushButton_265.setObjectName("pushButton_265")
        self.pushButton_266 = QtGui.QPushButton(self.frame_234)
        self.pushButton_266.setGeometry(QtCore.QRect(30, 60, 41, 27))
        self.pushButton_266.setObjectName("pushButton_266")
        self.spinBox_191 = QtGui.QSpinBox(self.frame_234)
        self.spinBox_191.setGeometry(QtCore.QRect(10, 120, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_191.setFont(font)
        self.spinBox_191.setSuffix("")
        self.spinBox_191.setMaximum(9999)
        self.spinBox_191.setProperty("value", 5555)
        self.spinBox_191.setObjectName("spinBox_191")
        self.spinBox_192 = QtGui.QSpinBox(self.frame_234)
        self.spinBox_192.setGeometry(QtCore.QRect(110, 120, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_192.setFont(font)
        self.spinBox_192.setSuffix("")
        self.spinBox_192.setMaximum(360)
        self.spinBox_192.setProperty("value", 300)
        self.spinBox_192.setObjectName("spinBox_192")
        self.verticalLayout_44.addWidget(self.frame_234)
        self.frame_235 = QtGui.QFrame(self.frame_229)
        self.frame_235.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_235.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_235.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_235.setObjectName("frame_235")
        self.label_320 = QtGui.QLabel(self.frame_235)
        self.label_320.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_320.setObjectName("label_320")
        self.labelSnapshotThumbnail_40 = QtGui.QLabel(self.frame_235)
        self.labelSnapshotThumbnail_40.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.labelSnapshotThumbnail_40.setText("")
        self.labelSnapshotThumbnail_40.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_40.setScaledContents(True)
        self.labelSnapshotThumbnail_40.setObjectName("labelSnapshotThumbnail_40")
        self.label_321 = QtGui.QLabel(self.frame_235)
        self.label_321.setGeometry(QtCore.QRect(13, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_321.setFont(font)
        self.label_321.setObjectName("label_321")
        self.spinBox_193 = QtGui.QSpinBox(self.frame_235)
        self.spinBox_193.setGeometry(QtCore.QRect(150, 180, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_193.setFont(font)
        self.spinBox_193.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_193.setObjectName("spinBox_193")
        self.horizontalSlider_134 = QtGui.QSlider(self.frame_235)
        self.horizontalSlider_134.setGeometry(QtCore.QRect(70, 180, 71, 16))
        self.horizontalSlider_134.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_134.setObjectName("horizontalSlider_134")
        self.verticalLayout_44.addWidget(self.frame_235)
        self.horizontalLayout_64.addWidget(self.frame_229)
        self.gridLayout_14.addWidget(self.frame_33, 0, 0, 1, 1)
        self.stackedWidget_main.addWidget(self.page_main_oct_capture)
        self.page_main_oct_evaluate = QtGui.QWidget()
        self.page_main_oct_evaluate.setObjectName("page_main_oct_evaluate")
        self.label_81 = QtGui.QLabel(self.page_main_oct_evaluate)
        self.label_81.setGeometry(QtCore.QRect(120, 60, 301, 16))
        self.label_81.setObjectName("label_81")
        self.stackedWidget_main.addWidget(self.page_main_oct_evaluate)
        self.page_main_angio_setup = QtGui.QWidget()
        self.page_main_angio_setup.setObjectName("page_main_angio_setup")
        self.gridLayout_10 = QtGui.QGridLayout(self.page_main_angio_setup)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_23 = QtGui.QFrame(self.page_main_angio_setup)
        self.frame_23.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_23)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_24 = QtGui.QFrame(self.frame_23)
        self.frame_24.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_24.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_24.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_24)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_25 = QtGui.QFrame(self.frame_24)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QtCore.QSize(195, 250))
        self.frame_25.setMaximumSize(QtCore.QSize(195, 250))
        self.frame_25.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.label_7 = QtGui.QLabel(self.frame_25)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_44 = QtGui.QLabel(self.frame_25)
        self.label_44.setGeometry(QtCore.QRect(20, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.pushButton_14 = QtGui.QPushButton(self.frame_25)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 190, 31, 26))
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtGui.QPushButton(self.frame_25)
        self.pushButton_15.setGeometry(QtCore.QRect(60, 190, 31, 26))
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_5.addWidget(self.frame_25)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem17)
        self.horizontalLayout_4.addWidget(self.frame_24)
        self.frame_26 = QtGui.QFrame(self.frame_23)
        self.frame_26.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_26.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_26)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frameCenterArea = QtGui.QFrame(self.frame_26)
        self.frameCenterArea.setMinimumSize(QtCore.QSize(200, 0))
        self.frameCenterArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameCenterArea.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCenterArea.setObjectName("frameCenterArea")
        self.frame_27 = QtGui.QFrame(self.frameCenterArea)
        self.frame_27.setGeometry(QtCore.QRect(30, 20, 441, 121))
        self.frame_27.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.label_12 = QtGui.QLabel(self.frame_27)
        self.label_12.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_41 = QtGui.QPushButton(self.frame_27)
        self.pushButton_41.setGeometry(QtCore.QRect(330, 40, 91, 61))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtGui.QPushButton(self.frame_27)
        self.pushButton_42.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtGui.QPushButton(self.frame_27)
        self.pushButton_43.setGeometry(QtCore.QRect(230, 40, 91, 61))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtGui.QPushButton(self.frame_27)
        self.pushButton_44.setGeometry(QtCore.QRect(130, 40, 91, 61))
        self.pushButton_44.setObjectName("pushButton_44")
        self.frame_28 = QtGui.QFrame(self.frameCenterArea)
        self.frame_28.setGeometry(QtCore.QRect(30, 150, 441, 121))
        self.frame_28.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.label_16 = QtGui.QLabel(self.frame_28)
        self.label_16.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label_16.setObjectName("label_16")
        self.pushButton_45 = QtGui.QPushButton(self.frame_28)
        self.pushButton_45.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtGui.QPushButton(self.frame_28)
        self.pushButton_46.setGeometry(QtCore.QRect(130, 40, 91, 61))
        self.pushButton_46.setObjectName("pushButton_46")
        self.frame_29 = QtGui.QFrame(self.frameCenterArea)
        self.frame_29.setGeometry(QtCore.QRect(30, 280, 441, 121))
        self.frame_29.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.label_17 = QtGui.QLabel(self.frame_29)
        self.label_17.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label_17.setObjectName("label_17")
        self.pushButton_47 = QtGui.QPushButton(self.frame_29)
        self.pushButton_47.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtGui.QPushButton(self.frame_29)
        self.pushButton_48.setGeometry(QtCore.QRect(230, 40, 91, 61))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtGui.QPushButton(self.frame_29)
        self.pushButton_49.setGeometry(QtCore.QRect(130, 40, 91, 61))
        self.pushButton_49.setObjectName("pushButton_49")
        self.frame_30 = QtGui.QFrame(self.frameCenterArea)
        self.frame_30.setGeometry(QtCore.QRect(90, 410, 381, 219))
        self.frame_30.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.gridLayout_9 = QtGui.QGridLayout(self.frame_30)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox = QtGui.QCheckBox(self.frame_30)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_9.addWidget(self.checkBox, 1, 0, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.frame_30)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_9.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.checkBox_9 = QtGui.QCheckBox(self.frame_30)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_9.addWidget(self.checkBox_9, 6, 0, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.frame_30)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_9.addWidget(self.checkBox_5, 4, 0, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.frame_30)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_9.addWidget(self.checkBox_6, 2, 0, 1, 1)
        self.checkBox_10 = QtGui.QCheckBox(self.frame_30)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_9.addWidget(self.checkBox_10, 7, 0, 1, 1)
        self.checkBox_11 = QtGui.QCheckBox(self.frame_30)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_9.addWidget(self.checkBox_11, 5, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.frame_30)
        self.label_18.setObjectName("label_18")
        self.gridLayout_9.addWidget(self.label_18, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frameCenterArea, 2, 0, 1, 1)
        self.frame_31 = QtGui.QFrame(self.frame_26)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_31.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_68 = QtGui.QHBoxLayout(self.frame_31)
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem18)
        self.frame_32 = QtGui.QFrame(self.frame_31)
        self.frame_32.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_32.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_32.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_69 = QtGui.QHBoxLayout(self.frame_32)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.horizontalLayout_70 = QtGui.QHBoxLayout()
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.pushButton_267 = QtGui.QPushButton(self.frame_32)
        self.pushButton_267.setMinimumSize(QtCore.QSize(34, 0))
        self.pushButton_267.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_267.setCheckable(True)
        self.pushButton_267.setChecked(False)
        self.pushButton_267.setObjectName("pushButton_267")
        self.horizontalLayout_70.addWidget(self.pushButton_267)
        self.horizontalLayout_69.addLayout(self.horizontalLayout_70)
        self.horizontalLayout_68.addWidget(self.frame_32)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem19)
        self.gridLayout_8.addWidget(self.frame_31, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_26)
        self.frame_236 = QtGui.QFrame(self.frame_23)
        self.frame_236.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_236.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_236.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_236.setObjectName("frame_236")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_236)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem20 = QtGui.QSpacerItem(175, 617, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem20)
        self.frame_237 = QtGui.QFrame(self.frame_236)
        self.frame_237.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_237.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_237.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_237.setObjectName("frame_237")
        self.label_8 = QtGui.QLabel(self.frame_237)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_8.setObjectName("label_8")
        self.labelSnapshotThumbnail_8 = QtGui.QLabel(self.frame_237)
        self.labelSnapshotThumbnail_8.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.labelSnapshotThumbnail_8.setText("")
        self.labelSnapshotThumbnail_8.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_8.setScaledContents(True)
        self.labelSnapshotThumbnail_8.setObjectName("labelSnapshotThumbnail_8")
        self.label_27 = QtGui.QLabel(self.frame_237)
        self.label_27.setGeometry(QtCore.QRect(13, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.spinBox_20 = QtGui.QSpinBox(self.frame_237)
        self.spinBox_20.setGeometry(QtCore.QRect(150, 180, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_20.setFont(font)
        self.spinBox_20.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_20.setObjectName("spinBox_20")
        self.horizontalSlider_12 = QtGui.QSlider(self.frame_237)
        self.horizontalSlider_12.setGeometry(QtCore.QRect(70, 180, 71, 16))
        self.horizontalSlider_12.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_12.setObjectName("horizontalSlider_12")
        self.verticalLayout_6.addWidget(self.frame_237)
        self.horizontalLayout_4.addWidget(self.frame_236)
        self.gridLayout_10.addWidget(self.frame_23, 0, 0, 1, 1)
        self.stackedWidget_main.addWidget(self.page_main_angio_setup)
        self.page_main_angio_capture = QtGui.QWidget()
        self.page_main_angio_capture.setObjectName("page_main_angio_capture")
        self.gridLayout_16 = QtGui.QGridLayout(self.page_main_angio_capture)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.frame_66 = QtGui.QFrame(self.page_main_angio_capture)
        self.frame_66.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_66)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_67 = QtGui.QFrame(self.frame_66)
        self.frame_67.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_67.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_67.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.frame_67)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_68 = QtGui.QFrame(self.frame_67)
        self.frame_68.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_68.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_68.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.label_82 = QtGui.QLabel(self.frame_68)
        self.label_82.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_82.setObjectName("label_82")
        self.pushButton_67 = QtGui.QPushButton(self.frame_68)
        self.pushButton_67.setGeometry(QtCore.QRect(20, 30, 31, 26))
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtGui.QPushButton(self.frame_68)
        self.pushButton_68.setGeometry(QtCore.QRect(60, 30, 31, 26))
        self.pushButton_68.setCheckable(True)
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtGui.QPushButton(self.frame_68)
        self.pushButton_69.setGeometry(QtCore.QRect(100, 30, 31, 26))
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtGui.QPushButton(self.frame_68)
        self.pushButton_70.setGeometry(QtCore.QRect(140, 30, 31, 26))
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.setObjectName("pushButton_70")
        self.labelSnapshotThumbnail_14 = QtGui.QLabel(self.frame_68)
        self.labelSnapshotThumbnail_14.setGeometry(QtCore.QRect(20, 70, 161, 121))
        self.labelSnapshotThumbnail_14.setText("")
        self.labelSnapshotThumbnail_14.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/cat1_retina36s.jpg"))
        self.labelSnapshotThumbnail_14.setScaledContents(True)
        self.labelSnapshotThumbnail_14.setObjectName("labelSnapshotThumbnail_14")
        self.verticalLayout_13.addWidget(self.frame_68)
        spacerItem21 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem21)
        self.horizontalLayout_8.addWidget(self.frame_67)
        self.frame_69 = QtGui.QFrame(self.frame_66)
        self.frame_69.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_69.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.gridLayout_15 = QtGui.QGridLayout(self.frame_69)
        self.gridLayout_15.setObjectName("gridLayout_15")
        spacerItem22 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem22, 1, 0, 1, 1)
        self.frame_70 = QtGui.QFrame(self.frame_69)
        self.frame_70.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_70.setMaximumSize(QtCore.QSize(16777215, 380))
        self.frame_70.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.label_83 = QtGui.QLabel(self.frame_70)
        self.label_83.setGeometry(QtCore.QRect(769, 32, 373, 337))
        self.label_83.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_83.setText("")
        self.label_83.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/retina_angiograph_03.jpg"))
        self.label_83.setScaledContents(True)
        self.label_83.setObjectName("label_83")
        self.label_84 = QtGui.QLabel(self.frame_70)
        self.label_84.setGeometry(QtCore.QRect(11, 32, 373, 337))
        self.label_84.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_84.setText("")
        self.label_84.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/square_cat1_retina36s.jpg"))
        self.label_84.setScaledContents(True)
        self.label_84.setObjectName("label_84")
        self.label_85 = QtGui.QLabel(self.frame_70)
        self.label_85.setGeometry(QtCore.QRect(390, 32, 373, 337))
        self.label_85.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_85.setText("")
        self.label_85.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/square_retina11.jpg"))
        self.label_85.setScaledContents(True)
        self.label_85.setObjectName("label_85")
        self.label_86 = QtGui.QLabel(self.frame_70)
        self.label_86.setGeometry(QtCore.QRect(769, 11, 125, 16))
        self.label_86.setObjectName("label_86")
        self.label_87 = QtGui.QLabel(self.frame_70)
        self.label_87.setGeometry(QtCore.QRect(390, 11, 158, 16))
        self.label_87.setObjectName("label_87")
        self.label_88 = QtGui.QLabel(self.frame_70)
        self.label_88.setGeometry(QtCore.QRect(11, 11, 91, 16))
        self.label_88.setObjectName("label_88")
        self.gridLayout_15.addWidget(self.frame_70, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.frame_69)
        self.frame_71 = QtGui.QFrame(self.frame_66)
        self.frame_71.setMinimumSize(QtCore.QSize(200, 500))
        self.frame_71.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_71.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.frame_71)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_72 = QtGui.QFrame(self.frame_71)
        self.frame_72.setMinimumSize(QtCore.QSize(195, 150))
        self.frame_72.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_72.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.label_89 = QtGui.QLabel(self.frame_72)
        self.label_89.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_89.setObjectName("label_89")
        self.verticalScrollBar_5 = QtGui.QScrollBar(self.frame_72)
        self.verticalScrollBar_5.setGeometry(QtCore.QRect(20, 40, 16, 91))
        self.verticalScrollBar_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_5.setObjectName("verticalScrollBar_5")
        self.pushButton_71 = QtGui.QPushButton(self.frame_72)
        self.pushButton_71.setGeometry(QtCore.QRect(50, 40, 41, 27))
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtGui.QPushButton(self.frame_72)
        self.pushButton_72.setGeometry(QtCore.QRect(50, 110, 41, 27))
        self.pushButton_72.setObjectName("pushButton_72")
        self.spinBox_44 = QtGui.QSpinBox(self.frame_72)
        self.spinBox_44.setGeometry(QtCore.QRect(50, 70, 91, 31))
        self.spinBox_44.setSuffix("")
        self.spinBox_44.setMaximum(10000)
        self.spinBox_44.setObjectName("spinBox_44")
        self.verticalLayout_14.addWidget(self.frame_72)
        self.frame_73 = QtGui.QFrame(self.frame_71)
        self.frame_73.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_73.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_73.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.label_90 = QtGui.QLabel(self.frame_73)
        self.label_90.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_90.setObjectName("label_90")
        self.spinBox_45 = QtGui.QSpinBox(self.frame_73)
        self.spinBox_45.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_45.setFont(font)
        self.spinBox_45.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_45.setObjectName("spinBox_45")
        self.label_91 = QtGui.QLabel(self.frame_73)
        self.label_91.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.horizontalSlider_30 = QtGui.QSlider(self.frame_73)
        self.horizontalSlider_30.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_30.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_30.setObjectName("horizontalSlider_30")
        self.horizontalSlider_31 = QtGui.QSlider(self.frame_73)
        self.horizontalSlider_31.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_31.setSliderPosition(77)
        self.horizontalSlider_31.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_31.setInvertedAppearance(False)
        self.horizontalSlider_31.setInvertedControls(False)
        self.horizontalSlider_31.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_31.setObjectName("horizontalSlider_31")
        self.label_92 = QtGui.QLabel(self.frame_73)
        self.label_92.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_92.setFont(font)
        self.label_92.setObjectName("label_92")
        self.spinBox_46 = QtGui.QSpinBox(self.frame_73)
        self.spinBox_46.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_46.setFont(font)
        self.spinBox_46.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_46.setProperty("value", 99)
        self.spinBox_46.setObjectName("spinBox_46")
        self.verticalLayout_14.addWidget(self.frame_73)
        self.label_93 = QtGui.QLabel(self.frame_71)
        self.label_93.setObjectName("label_93")
        self.verticalLayout_14.addWidget(self.label_93)
        self.frame_74 = QtGui.QFrame(self.frame_71)
        self.frame_74.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_74.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_74.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.label_94 = QtGui.QLabel(self.frame_74)
        self.label_94.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_94.setObjectName("label_94")
        self.spinBox_47 = QtGui.QSpinBox(self.frame_74)
        self.spinBox_47.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_47.setFont(font)
        self.spinBox_47.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_47.setObjectName("spinBox_47")
        self.label_95 = QtGui.QLabel(self.frame_74)
        self.label_95.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_95.setFont(font)
        self.label_95.setObjectName("label_95")
        self.horizontalSlider_32 = QtGui.QSlider(self.frame_74)
        self.horizontalSlider_32.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_32.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_32.setObjectName("horizontalSlider_32")
        self.horizontalSlider_33 = QtGui.QSlider(self.frame_74)
        self.horizontalSlider_33.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_33.setSliderPosition(77)
        self.horizontalSlider_33.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_33.setInvertedAppearance(False)
        self.horizontalSlider_33.setInvertedControls(False)
        self.horizontalSlider_33.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_33.setObjectName("horizontalSlider_33")
        self.label_96 = QtGui.QLabel(self.frame_74)
        self.label_96.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_96.setFont(font)
        self.label_96.setObjectName("label_96")
        self.spinBox_48 = QtGui.QSpinBox(self.frame_74)
        self.spinBox_48.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_48.setFont(font)
        self.spinBox_48.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_48.setProperty("value", 99)
        self.spinBox_48.setObjectName("spinBox_48")
        self.verticalLayout_14.addWidget(self.frame_74)
        self.frame_75 = QtGui.QFrame(self.frame_71)
        self.frame_75.setMinimumSize(QtCore.QSize(195, 100))
        self.frame_75.setMaximumSize(QtCore.QSize(195, 100))
        self.frame_75.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.label_97 = QtGui.QLabel(self.frame_75)
        self.label_97.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_97.setObjectName("label_97")
        self.spinBox_49 = QtGui.QSpinBox(self.frame_75)
        self.spinBox_49.setGeometry(QtCore.QRect(150, 40, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_49.setFont(font)
        self.spinBox_49.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_49.setObjectName("spinBox_49")
        self.label_98 = QtGui.QLabel(self.frame_75)
        self.label_98.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_98.setFont(font)
        self.label_98.setObjectName("label_98")
        self.horizontalSlider_34 = QtGui.QSlider(self.frame_75)
        self.horizontalSlider_34.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.horizontalSlider_34.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_34.setObjectName("horizontalSlider_34")
        self.horizontalSlider_35 = QtGui.QSlider(self.frame_75)
        self.horizontalSlider_35.setGeometry(QtCore.QRect(70, 70, 71, 16))
        self.horizontalSlider_35.setSliderPosition(77)
        self.horizontalSlider_35.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_35.setInvertedAppearance(False)
        self.horizontalSlider_35.setInvertedControls(False)
        self.horizontalSlider_35.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_35.setObjectName("horizontalSlider_35")
        self.label_99 = QtGui.QLabel(self.frame_75)
        self.label_99.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_99.setFont(font)
        self.label_99.setObjectName("label_99")
        self.spinBox_50 = QtGui.QSpinBox(self.frame_75)
        self.spinBox_50.setGeometry(QtCore.QRect(150, 70, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_50.setFont(font)
        self.spinBox_50.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_50.setProperty("value", 99)
        self.spinBox_50.setObjectName("spinBox_50")
        self.verticalLayout_14.addWidget(self.frame_75)
        spacerItem23 = QtGui.QSpacerItem(175, 49, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem23)
        self.frame_76 = QtGui.QFrame(self.frame_71)
        self.frame_76.setMinimumSize(QtCore.QSize(195, 150))
        self.frame_76.setMaximumSize(QtCore.QSize(195, 150))
        self.frame_76.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_76.setObjectName("frame_76")
        self.label_100 = QtGui.QLabel(self.frame_76)
        self.label_100.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_100.setObjectName("label_100")
        self.pushButton_73 = QtGui.QPushButton(self.frame_76)
        self.pushButton_73.setGeometry(QtCore.QRect(80, 40, 41, 27))
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_74 = QtGui.QPushButton(self.frame_76)
        self.pushButton_74.setGeometry(QtCore.QRect(80, 80, 41, 27))
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtGui.QPushButton(self.frame_76)
        self.pushButton_75.setGeometry(QtCore.QRect(130, 60, 41, 27))
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtGui.QPushButton(self.frame_76)
        self.pushButton_76.setGeometry(QtCore.QRect(30, 60, 41, 27))
        self.pushButton_76.setObjectName("pushButton_76")
        self.spinBox_51 = QtGui.QSpinBox(self.frame_76)
        self.spinBox_51.setGeometry(QtCore.QRect(10, 120, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_51.setFont(font)
        self.spinBox_51.setSuffix("")
        self.spinBox_51.setMaximum(9999)
        self.spinBox_51.setProperty("value", 5555)
        self.spinBox_51.setObjectName("spinBox_51")
        self.spinBox_52 = QtGui.QSpinBox(self.frame_76)
        self.spinBox_52.setGeometry(QtCore.QRect(110, 120, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_52.setFont(font)
        self.spinBox_52.setSuffix("")
        self.spinBox_52.setMaximum(360)
        self.spinBox_52.setProperty("value", 300)
        self.spinBox_52.setObjectName("spinBox_52")
        self.verticalLayout_14.addWidget(self.frame_76)
        self.frame_77 = QtGui.QFrame(self.frame_71)
        self.frame_77.setMinimumSize(QtCore.QSize(195, 200))
        self.frame_77.setMaximumSize(QtCore.QSize(195, 200))
        self.frame_77.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.label_101 = QtGui.QLabel(self.frame_77)
        self.label_101.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_101.setObjectName("label_101")
        self.labelSnapshotThumbnail_15 = QtGui.QLabel(self.frame_77)
        self.labelSnapshotThumbnail_15.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.labelSnapshotThumbnail_15.setText("")
        self.labelSnapshotThumbnail_15.setPixmap(QtGui.QPixmap(":/samples/images/vis_gallery/example_vis_camera_13.jpg"))
        self.labelSnapshotThumbnail_15.setScaledContents(True)
        self.labelSnapshotThumbnail_15.setObjectName("labelSnapshotThumbnail_15")
        self.label_102 = QtGui.QLabel(self.frame_77)
        self.label_102.setGeometry(QtCore.QRect(13, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_102.setFont(font)
        self.label_102.setObjectName("label_102")
        self.spinBox_53 = QtGui.QSpinBox(self.frame_77)
        self.spinBox_53.setGeometry(QtCore.QRect(150, 180, 77, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_53.setFont(font)
        self.spinBox_53.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_53.setObjectName("spinBox_53")
        self.horizontalSlider_36 = QtGui.QSlider(self.frame_77)
        self.horizontalSlider_36.setGeometry(QtCore.QRect(70, 180, 71, 16))
        self.horizontalSlider_36.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_36.setObjectName("horizontalSlider_36")
        self.verticalLayout_14.addWidget(self.frame_77)
        self.horizontalLayout_8.addWidget(self.frame_71)
        self.gridLayout_16.addWidget(self.frame_66, 0, 0, 1, 1)
        self.stackedWidget_main.addWidget(self.page_main_angio_capture)
        self.page_main_angio_evaluate = QtGui.QWidget()
        self.page_main_angio_evaluate.setObjectName("page_main_angio_evaluate")
        self.label_10 = QtGui.QLabel(self.page_main_angio_evaluate)
        self.label_10.setGeometry(QtCore.QRect(70, 80, 241, 16))
        self.label_10.setObjectName("label_10")
        self.stackedWidget_main.addWidget(self.page_main_angio_evaluate)
        self.gridLayout.addWidget(self.stackedWidget_main, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox_mode.setCurrentIndex(0)
        self.comboBox_mode_2.setCurrentIndex(0)
        self.stackedWidgetHeaderNavigation.setCurrentIndex(0)
        self.stackedWidget_main.setCurrentIndex(0)
        QtCore.QObject.connect(self.comboBox_mode, QtCore.SIGNAL("currentIndexChanged(int)"), self.stackedWidget_main.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(0, QtGui.QApplication.translate("MainWindow", "HS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(1, QtGui.QApplication.translate("MainWindow", "OCTS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(2, QtGui.QApplication.translate("MainWindow", "OCTC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(3, QtGui.QApplication.translate("MainWindow", "OCTEV", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(4, QtGui.QApplication.translate("MainWindow", "AngioS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(5, QtGui.QApplication.translate("MainWindow", "AngioC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(6, QtGui.QApplication.translate("MainWindow", "AngioEV", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(7, QtGui.QApplication.translate("MainWindow", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(8, QtGui.QApplication.translate("MainWindow", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode.setItemText(9, QtGui.QApplication.translate("MainWindow", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode_2.setItemText(0, QtGui.QApplication.translate("MainWindow", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode_2.setItemText(1, QtGui.QApplication.translate("MainWindow", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mode_2.setItemText(2, QtGui.QApplication.translate("MainWindow", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_20.setText(QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_nav_oct_setup.setText(QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_nav_oct_capture.setText(QtGui.QApplication.translate("MainWindow", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("MainWindow", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Saved configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("MainWindow", "2016-04-18 07:49", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MainWindow", "Ren", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("MainWindow", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_22.setText(QtGui.QApplication.translate("MainWindow", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_24.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "OCT Camera Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Int. Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Line Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("MainWindow", "Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("MainWindow", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_15.setPrefix(QtGui.QApplication.translate("MainWindow", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Light source", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_19.setText(QtGui.QApplication.translate("MainWindow", "Off/On", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("MainWindow", "Power", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Saved configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("MainWindow", "2016-04-18 07:49", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("MainWindow", "Ren", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MainWindow", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Scan Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_28.setText(QtGui.QApplication.translate("MainWindow", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_29.setText(QtGui.QApplication.translate("MainWindow", "Spiral", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_30.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_31.setText(QtGui.QApplication.translate("MainWindow", "Rect", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_7.setText(QtGui.QApplication.translate("MainWindow", "Raw OCT data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "OCT Volume Save configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", "OCT Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_8.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_25.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_307.setText(QtGui.QApplication.translate("MainWindow", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_252.setText(QtGui.QApplication.translate("MainWindow", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_253.setText(QtGui.QApplication.translate("MainWindow", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_254.setText(QtGui.QApplication.translate("MainWindow", "Cp", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_255.setText(QtGui.QApplication.translate("MainWindow", "Ev", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_256.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_257.setText(QtGui.QApplication.translate("MainWindow", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_258.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_259.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_260.setText(QtGui.QApplication.translate("MainWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_308.setText(QtGui.QApplication.translate("MainWindow", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_261.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_262.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_184.setPrefix(QtGui.QApplication.translate("MainWindow", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_309.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_310.setText(QtGui.QApplication.translate("MainWindow", "Min. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_311.setText(QtGui.QApplication.translate("MainWindow", "Max. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_312.setText(QtGui.QApplication.translate("MainWindow", "Colormap", None, QtGui.QApplication.UnicodeUTF8))
        self.label_313.setText(QtGui.QApplication.translate("MainWindow", "Dispersion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_314.setText(QtGui.QApplication.translate("MainWindow", "Coeff. B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_315.setText(QtGui.QApplication.translate("MainWindow", "Oceff. C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_316.setText(QtGui.QApplication.translate("MainWindow", "Polarization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_317.setText(QtGui.QApplication.translate("MainWindow", "Half Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_318.setText(QtGui.QApplication.translate("MainWindow", "Quar. Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_319.setText(QtGui.QApplication.translate("MainWindow", "Scan line control", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_263.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_264.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_265.setText(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_266.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_191.setPrefix(QtGui.QApplication.translate("MainWindow", "Length: ", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_192.setPrefix(QtGui.QApplication.translate("MainWindow", "Angle: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_320.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_321.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_81.setText(QtGui.QApplication.translate("MainWindow", "OCT Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Saved configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("MainWindow", "2016-04-18 07:49", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("MainWindow", "Ren", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("MainWindow", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Scan Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_41.setText(QtGui.QApplication.translate("MainWindow", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_42.setText(QtGui.QApplication.translate("MainWindow", "Spiral", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_43.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_44.setText(QtGui.QApplication.translate("MainWindow", "Rect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Motion Correction", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_45.setText(QtGui.QApplication.translate("MainWindow", "Avg", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_46.setText(QtGui.QApplication.translate("MainWindow", "Subtract", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Angiography algorithm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_47.setText(QtGui.QApplication.translate("MainWindow", "Speckle", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_48.setText(QtGui.QApplication.translate("MainWindow", "Complex \n"
"Differntial \n"
"Variance", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_49.setText(QtGui.QApplication.translate("MainWindow", "Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Angio B-scan", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("MainWindow", "Angio Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_9.setText(QtGui.QApplication.translate("MainWindow", "Raw OCT data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("MainWindow", "Angio Projection", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_6.setText(QtGui.QApplication.translate("MainWindow", "OCT Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_10.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera image", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_11.setText(QtGui.QApplication.translate("MainWindow", "Intensity and Phase data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Save configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_267.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_82.setText(QtGui.QApplication.translate("MainWindow", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_67.setText(QtGui.QApplication.translate("MainWindow", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_68.setText(QtGui.QApplication.translate("MainWindow", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_69.setText(QtGui.QApplication.translate("MainWindow", "Cp", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_70.setText(QtGui.QApplication.translate("MainWindow", "Ev", None, QtGui.QApplication.UnicodeUTF8))
        self.label_86.setText(QtGui.QApplication.translate("MainWindow", "Angiograph preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_87.setText(QtGui.QApplication.translate("MainWindow", "Continuous scan preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_88.setText(QtGui.QApplication.translate("MainWindow", "Center B-scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_89.setText(QtGui.QApplication.translate("MainWindow", "Reference Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_71.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_72.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_44.setPrefix(QtGui.QApplication.translate("MainWindow", "Position: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_90.setText(QtGui.QApplication.translate("MainWindow", "OCT Image Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_91.setText(QtGui.QApplication.translate("MainWindow", "Min. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_92.setText(QtGui.QApplication.translate("MainWindow", "Max. Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_93.setText(QtGui.QApplication.translate("MainWindow", "Colormap", None, QtGui.QApplication.UnicodeUTF8))
        self.label_94.setText(QtGui.QApplication.translate("MainWindow", "Dispersion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_95.setText(QtGui.QApplication.translate("MainWindow", "Coeff. B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_96.setText(QtGui.QApplication.translate("MainWindow", "Oceff. C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_97.setText(QtGui.QApplication.translate("MainWindow", "Polarization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_98.setText(QtGui.QApplication.translate("MainWindow", "Half Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_99.setText(QtGui.QApplication.translate("MainWindow", "Quar. Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_100.setText(QtGui.QApplication.translate("MainWindow", "Scan line control", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_73.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_74.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_75.setText(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_76.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_51.setPrefix(QtGui.QApplication.translate("MainWindow", "Length: ", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_52.setPrefix(QtGui.QApplication.translate("MainWindow", "Angle: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_101.setText(QtGui.QApplication.translate("MainWindow", "Visible Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_102.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Angio evaluate", None, QtGui.QApplication.UnicodeUTF8))

import oct_gallery_resources_rc
import wasatch_logo_resources_rc
import vis_gallery_resources_rc
import colormap_resources_rc
import style_rc
