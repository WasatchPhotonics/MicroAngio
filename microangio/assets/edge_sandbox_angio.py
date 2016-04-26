# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'microangio/assets/edge_sandbox_angio.ui'
#
# Created: Tue Apr 26 07:45:32 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1253, 837)
        Form.setStyleSheet("/*\n"
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
"}\n"
"")
        self.frame_center_nest = QtGui.QFrame(Form)
        self.frame_center_nest.setGeometry(QtCore.QRect(10, 230, 681, 591))
        self.frame_center_nest.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_center_nest.setStyleSheet("QFrame#frame_center_nest {\n"
"  background: rgb(80, 80, 80);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest.setLineWidth(1)
        self.frame_center_nest.setObjectName("frame_center_nest")
        self.frame_center_nest_2 = QtGui.QFrame(self.frame_center_nest)
        self.frame_center_nest_2.setGeometry(QtCore.QRect(480, 10, 91, 411))
        self.frame_center_nest_2.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_2.setLineWidth(1)
        self.frame_center_nest_2.setObjectName("frame_center_nest_2")
        self.frame_center_nest_4 = QtGui.QFrame(self.frame_center_nest)
        self.frame_center_nest_4.setGeometry(QtCore.QRect(110, 10, 351, 411))
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
        self.frame_center_nest_5 = QtGui.QFrame(self.frame_center_nest_4)
        self.frame_center_nest_5.setGeometry(QtCore.QRect(10, 10, 321, 41))
        self.frame_center_nest_5.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_5.setLineWidth(1)
        self.frame_center_nest_5.setObjectName("frame_center_nest_5")
        self.frame_center_nest_6 = QtGui.QFrame(self.frame_center_nest_4)
        self.frame_center_nest_6.setGeometry(QtCore.QRect(10, 60, 321, 331))
        self.frame_center_nest_6.setStyleSheet("QFrame {\n"
"  background: rgb(29, 29, 29);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_6.setLineWidth(1)
        self.frame_center_nest_6.setObjectName("frame_center_nest_6")
        self.label_22 = QtGui.QLabel(self.frame_center_nest_6)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 301, 311))
        self.label_22.setStyleSheet("background-color: none;\n"
"border-color: none;\n"
"border: none;")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/website/images/oct_gallery/placeholder_cat_retina36.jpg"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.frame_center_nest_7 = QtGui.QFrame(self.frame_center_nest)
        self.frame_center_nest_7.setGeometry(QtCore.QRect(10, 10, 91, 411))
        self.frame_center_nest_7.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_7.setLineWidth(1)
        self.frame_center_nest_7.setObjectName("frame_center_nest_7")
        self.pushButton_9 = QtGui.QPushButton(self.frame_center_nest)
        self.pushButton_9.setGeometry(QtCore.QRect(610, 180, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.611, fx:0.0205366, fy:0.517, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 6px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_18 = QtGui.QPushButton(self.frame_center_nest)
        self.pushButton_18.setGeometry(QtCore.QRect(250, 480, 97, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.frame_center_nest_3 = QtGui.QFrame(Form)
        self.frame_center_nest_3.setGeometry(QtCore.QRect(10, 10, 1071, 61))
        self.frame_center_nest_3.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 1px solid #ff0000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_3.setLineWidth(1)
        self.frame_center_nest_3.setObjectName("frame_center_nest_3")
        self.frame_center_nest_9 = QtGui.QFrame(self.frame_center_nest_3)
        self.frame_center_nest_9.setGeometry(QtCore.QRect(10, 10, 111, 40))
        self.frame_center_nest_9.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_9.setLineWidth(1)
        self.frame_center_nest_9.setObjectName("frame_center_nest_9")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_center_nest_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtGui.QLabel(self.frame_center_nest_9)
        self.label_5.setStyleSheet("background-color: none;\n"
"border-color: none;\n"
"border: none;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/logos/images/logos/92x30_placeholder_logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.frame_center_nest_10 = QtGui.QFrame(self.frame_center_nest_3)
        self.frame_center_nest_10.setGeometry(QtCore.QRect(170, 10, 631, 43))
        self.frame_center_nest_10.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_10.setLineWidth(1)
        self.frame_center_nest_10.setObjectName("frame_center_nest_10")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_center_nest_10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtGui.QComboBox(self.frame_center_nest_10)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_22 = QtGui.QPushButton(self.frame_center_nest_10)
        self.pushButton_22.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_22.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout.addWidget(self.pushButton_22)
        self.pushButton_23 = QtGui.QPushButton(self.frame_center_nest_10)
        self.pushButton_23.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_23.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setChecked(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout.addWidget(self.pushButton_23)
        self.pushButton_24 = QtGui.QPushButton(self.frame_center_nest_10)
        self.pushButton_24.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_24.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout.addWidget(self.pushButton_24)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(700, 220, 71, 71))
        self.toolButton_2.setObjectName("toolButton_2")
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1150, 220, 111, 71))
        self.pushButton_3.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.034, cy:0.539773, radius:0.388, fx:0.0203922, fy:0.517, stop:0 rgba(0, 0, 0, 255), stop:0.0980392 rgba(86, 86, 86, 255), stop:0.558824 rgba(164, 164, 164, 255), stop:1 rgba(195, 195, 195, 255))")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1160, 300, 111, 71))
        self.pushButton_4.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.27, fy:0.5, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(255, 255, 255, 255))")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1160, 390, 111, 71))
        self.pushButton_5.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.168, fx:0.167, fy:0.489091, stop:0 rgba(113, 113, 113, 255), stop:1 rgba(255, 255, 255, 255))")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(1160, 470, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.168, fx:0.167, fy:0.489091, stop:0 rgba(113, 113, 113, 255), stop:1 rgba(255, 255, 255, 255))")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(1160, 540, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.611, fx:0.0205366, fy:0.517, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(255, 255, 255, 255))")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(1160, 610, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.611, fx:0.0205366, fy:0.517, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 6px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtGui.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(1160, 680, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.182, cy:0.522727, radius:1.6, fx:0, fy:0.5, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 6px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtGui.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(870, 470, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 6px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_16 = QtGui.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(870, 520, 97, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtGui.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(870, 560, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_19 = QtGui.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(870, 600, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(870, 650, 131, 31))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 4, 81, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 0px;\n"
"background: transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(31, 6, 81, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 0px;\n"
"color: rgb(0, 0, 0);\n"
"background: transparent;")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(870, 690, 131, 31))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(30, 4, 81, 21))
        self.label_7.setMinimumSize(QtCore.QSize(81, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 0px;\n"
"background: transparent;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(31, 6, 81, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: 0px;\n"
"color: rgb(0, 0, 0);\n"
"background: transparent;")
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(870, 730, 130, 40))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border: 1px solid black;")
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(110, 20))
        self.frame_4.setMaximumSize(QtCore.QSize(110, 20))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_17 = QtGui.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(10, 0, 81, 21))
        self.label_17.setMinimumSize(QtCore.QSize(81, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border: 0px;\n"
"background: transparent;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtGui.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(11, 1, 81, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border: 0px;\n"
"color: rgb(0, 0, 0);\n"
"background: transparent;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.pushButton_21 = QtGui.QPushButton(Form)
        self.pushButton_21.setGeometry(QtCore.QRect(1020, 600, 130, 30))
        self.pushButton_21.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_21.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0,0,0);\n"
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
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.frame_center_nest_8 = QtGui.QFrame(Form)
        self.frame_center_nest_8.setGeometry(QtCore.QRect(10, 90, 1071, 61))
        self.frame_center_nest_8.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"/*    border: 1px solid #000000;*/\n"
"  border: transparent;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_8.setLineWidth(1)
        self.frame_center_nest_8.setObjectName("frame_center_nest_8")
        self.frame_center_nest_11 = QtGui.QFrame(self.frame_center_nest_8)
        self.frame_center_nest_11.setGeometry(QtCore.QRect(10, 10, 111, 40))
        self.frame_center_nest_11.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_11.setLineWidth(1)
        self.frame_center_nest_11.setObjectName("frame_center_nest_11")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_center_nest_11)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_21 = QtGui.QLabel(self.frame_center_nest_11)
        self.label_21.setStyleSheet("background-color: none;\n"
"border-color: none;\n"
"border: none;")
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/logos/images/logos/92x30_placeholder_logo.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21)
        self.frame_center_nest_12 = QtGui.QFrame(self.frame_center_nest_8)
        self.frame_center_nest_12.setGeometry(QtCore.QRect(170, 10, 671, 43))
        self.frame_center_nest_12.setStyleSheet("QFrame {\n"
"  background: rgb(54, 54, 54);\n"
"    border-style: solid;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_center_nest_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_center_nest_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_center_nest_12.setLineWidth(1)
        self.frame_center_nest_12.setObjectName("frame_center_nest_12")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_center_nest_12)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.comboBox_2 = QtGui.QComboBox(self.frame_center_nest_12)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButton_26 = QtGui.QPushButton(self.frame_center_nest_12)
        self.pushButton_26.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_26.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton:hover\n"
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
"border-radius: 12px;\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_5.addWidget(self.pushButton_26)
        self.pushButton_27 = QtGui.QPushButton(self.frame_center_nest_12)
        self.pushButton_27.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_27.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton:hover\n"
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
"border-radius: 12px;\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_5.addWidget(self.pushButton_27)
        self.pushButton_28 = QtGui.QPushButton(self.frame_center_nest_12)
        self.pushButton_28.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_28.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton:hover\n"
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
"border-radius: 12px;\n"
"}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_5.addWidget(self.pushButton_28)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.toolButton_4 = QtGui.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(700, 290, 71, 71))
        self.toolButton_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);")
        self.toolButton_4.setObjectName("toolButton_4")
        self.commandLinkButton = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(800, 240, 179, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(800, 300, 179, 41))
        self.commandLinkButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));\n"
"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(930, 360, 90, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_25 = QtGui.QPushButton(Form)
        self.pushButton_25.setGeometry(QtCore.QRect(1020, 640, 130, 30))
        self.pushButton_25.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_25.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton:hover\n"
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
"border-radius: 12px;\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 160, 104, 23))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_23 = QtGui.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(20, 150, 109, 38))
        self.label_23.setStyleSheet("background-color: none;\n"
"border-color: none;\n"
"border: none;")
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/logos/images/logos/92x30_placeholder_logo.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Form", "t", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "OCT 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_22.setText(QtGui.QApplication.translate("Form", "Setup ->", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_23.setText(QtGui.QApplication.translate("Form", "Capture ->", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_24.setText(QtGui.QApplication.translate("Form", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Setup Push", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Setup Push", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Setup Push", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "t", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "t", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form", "t", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("Form", "t", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_19.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_21.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("Form", "OCT 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_26.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_27.setText(QtGui.QApplication.translate("Form", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_28.setText(QtGui.QApplication.translate("Form", "Evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("Form", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("Form", "setup", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton_2.setText(QtGui.QApplication.translate("Form", "setup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_25.setText(QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("Form", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("Form", "OCT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("Form", "OCT 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(3, QtGui.QApplication.translate("Form", "Angiography", None, QtGui.QApplication.UnicodeUTF8))

import style_rc
import wasatch_logo_resources_rc
import oct_gallery_resources_rc
