# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Tue Apr 26 10:49:28 2016
#      by: The Resource Compiler for PySide (Qt v4.8.6)
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore

qt_resource_data = "\x00\x00b\xb9/*\x0a * The MIT License (MIT)\x0a *\x0a * Copyright (c) <2013-2014> <Colin Duquesnoy>\x0a *\x0a * Permission is hereby granted, free of charge, to any person obtaining\x0a * a copy\x0a * of this software and associated documentation files (the \x22Software\x22),\x0a * to deal\x0a * in the Software without restriction, including without limitation the\x0a * rights\x0a * to use, copy, modify, merge, publish, distribute, sublicense, and/or\x0a * sell\x0a * copies of the Software, and to permit persons to whom the Software is\x0a * furnished to do so, subject to the following conditions:\x0a\x0a * The above copyright notice and this permission notice shall be\x0a * included in\x0a * all copies or substantial portions of the Software.\x0a\x0a * THE SOFTWARE IS PROVIDED \x22AS IS\x22, WITHOUT WARRANTY OF ANY KIND,\x0a * EXPRESS OR\x0a * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF\x0a * MERCHANTABILITY,\x0a * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT\x0a * SHALL THE\x0a * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR\x0a * OTHER\x0a * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\x0a * ARISING FROM,\x0a * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\x0a * DEALINGS IN\x0a * THE SOFTWARE.\x0a */\x0a\x0aQProgressBar:horizontal {\x0a    border: 1px solid #3A3939;\x0a    text-align: center;\x0a    padding: 1px;\x0a    background: #201F1F;\x0a}\x0aQProgressBar::chunk:horizontal {\x0a    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545,\x0ax2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146,\x0a255));\x0a}\x0a\x0aQToolTip\x0a{\x0a    border: 1px solid #3A3939;\x0a    background-color: rgb(90, 102, 117);;\x0a    color: white;\x0a    padding: 1px;\x0a    opacity: 200;\x0a}\x0a\x0aQWidget\x0a{\x0a    color: silver;\x0a    background-color: #302F2F;\x0a    selection-background-color:#3d8ec9;\x0a    selection-color: black;\x0a    background-clip: border;\x0a    border-image: none;\x0a    outline: 0;\x0a}\x0a\x0aQWidget:item:hover\x0a{\x0a    background-color: #78879b;\x0a    color: black;\x0a}\x0a\x0aQWidget:item:selected\x0a{\x0a    background-color: #3d8ec9;\x0a}\x0a\x0aQCheckBox\x0a{\x0a    spacing: 5px;\x0a    outline: none;\x0a    color: #bbb;\x0a    margin-bottom: 2px;\x0a}\x0a\x0aQCheckBox:disabled\x0a{\x0a    color: #777777;\x0a}\x0aQCheckBox::indicator,\x0aQGroupBox::indicator\x0a{\x0a    width: 18px;\x0a    height: 18px;\x0a}\x0aQGroupBox::indicator\x0a{\x0a    margin-left: 2px;\x0a}\x0a\x0aQCheckBox::indicator:unchecked,\x0aQCheckBox::indicator:unchecked:hover,\x0aQGroupBox::indicator:unchecked,\x0aQGroupBox::indicator:unchecked:hover\x0a{\x0a    image: url(:/qss_icons/rc/checkbox_unchecked.png);\x0a}\x0a\x0aQCheckBox::indicator:unchecked:focus,\x0aQCheckBox::indicator:unchecked:pressed,\x0aQGroupBox::indicator:unchecked:focus,\x0aQGroupBox::indicator:unchecked:pressed\x0a{\x0a  border: none;\x0a    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\x0a}\x0a\x0aQCheckBox::indicator:checked,\x0aQCheckBox::indicator:checked:hover,\x0aQGroupBox::indicator:checked,\x0aQGroupBox::indicator:checked:hover\x0a{\x0a    image: url(:/qss_icons/rc/checkbox_checked.png);\x0a}\x0a\x0aQCheckBox::indicator:checked:focus,\x0aQCheckBox::indicator:checked:pressed,\x0aQGroupBox::indicator:checked:focus,\x0aQGroupBox::indicator:checked:pressed\x0a{\x0a  border: none;\x0a    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\x0a}\x0a\x0aQCheckBox::indicator:indeterminate,\x0aQCheckBox::indicator:indeterminate:hover,\x0aQCheckBox::indicator:indeterminate:pressed\x0aQGroupBox::indicator:indeterminate,\x0aQGroupBox::indicator:indeterminate:hover,\x0aQGroupBox::indicator:indeterminate:pressed\x0a{\x0a    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\x0a}\x0a\x0aQCheckBox::indicator:indeterminate:focus,\x0aQGroupBox::indicator:indeterminate:focus\x0a{\x0a    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\x0a}\x0a\x0aQCheckBox::indicator:checked:disabled,\x0aQGroupBox::indicator:checked:disabled\x0a{\x0a    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\x0a}\x0a\x0aQCheckBox::indicator:unchecked:disabled,\x0aQGroupBox::indicator:unchecked:disabled\x0a{\x0a    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\x0a}\x0a\x0aQRadioButton\x0a{\x0a    spacing: 5px;\x0a    outline: none;\x0a    color: #bbb;\x0a    margin-bottom: 2px;\x0a}\x0a\x0aQRadioButton:disabled\x0a{\x0a    color: #777777;\x0a}\x0aQRadioButton::indicator\x0a{\x0a    width: 21px;\x0a    height: 21px;\x0a}\x0a\x0aQRadioButton::indicator:unchecked,\x0aQRadioButton::indicator:unchecked:hover\x0a{\x0a    image: url(:/qss_icons/rc/radio_unchecked.png);\x0a}\x0a\x0aQRadioButton::indicator:unchecked:focus,\x0aQRadioButton::indicator:unchecked:pressed\x0a{\x0a  border: none;\x0a  outline: none;\x0a    image: url(:/qss_icons/rc/radio_unchecked_focus.png);\x0a}\x0a\x0aQRadioButton::indicator:checked,\x0aQRadioButton::indicator:checked:hover\x0a{\x0a  border: none;\x0a  outline: none;\x0a    image: url(:/qss_icons/rc/radio_checked.png);\x0a}\x0a\x0aQRadioButton::indicator:checked:focus,\x0aQRadioButton::indicato::menu-arrowr:checked:pressed\x0a{\x0a  border: none;\x0a  outline: none;\x0a    image: url(:/qss_icons/rc/radio_checked_focus.png);\x0a}\x0a\x0aQRadioButton::indicator:indeterminate,\x0aQRadioButton::indicator:indeterminate:hover,\x0aQRadioButton::indicator:indeterminate:pressed\x0a{\x0a        image: url(:/qss_icons/rc/radio_indeterminate.png);\x0a}\x0a\x0aQRadioButton::indicator:checked:disabled\x0a{\x0a  outline: none;\x0a  image: url(:/qss_icons/rc/radio_checked_disabled.png);\x0a}\x0a\x0aQRadioButton::indicator:unchecked:disabled\x0a{\x0a    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\x0a}\x0a\x0a\x0aQMenuBar\x0a{\x0a    background-color: #302F2F;\x0a    color: silver;\x0a}\x0a\x0aQMenuBar::item\x0a{\x0a    background: transparent;\x0a}\x0a\x0aQMenuBar::item:selected\x0a{\x0a    background: transparent;\x0a    border: 1px solid #3A3939;\x0a}\x0a\x0aQMenuBar::item:pressed\x0a{\x0a    border: 1px solid #3A3939;\x0a    background-color: #3d8ec9;\x0a    color: black;\x0a    margin-bottom:-1px;\x0a    padding-bottom:1px;\x0a}\x0a\x0aQMenu\x0a{\x0a    border: 1px solid #3A3939;\x0a    color: silver;\x0a    margin: 2px;\x0a}\x0a\x0aQMenu::icon\x0a{\x0a    margin: 5px;\x0a}\x0a\x0aQMenu::item\x0a{\x0a    padding: 5px 30px 5px 30px;\x0a    margin-left: 5px;\x0a    border: 1px solid transparent; /* reserve space for selection border\x0a*/\x0a}\x0a\x0aQMenu::item:selected\x0a{\x0a    color: black;\x0a}\x0a\x0aQMenu::separator {\x0a    height: 2px;\x0a    background: lightblue;\x0a    margin-left: 10px;\x0a    margin-right: 5px;\x0a}\x0a\x0aQMenu::indicator {\x0a    width: 18px;\x0a    height: 18px;\x0a}\x0a\x0a/* non-exclusive indicator = check box style indicator\x0a   (see QActionGroup::setExclusive) */\x0aQMenu::indicator:non-exclusive:unchecked {\x0a    image: url(:/qss_icons/rc/checkbox_unchecked.png);\x0a}\x0a\x0aQMenu::indicator:non-exclusive:unchecked:selected {\x0a    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\x0a}\x0a\x0aQMenu::indicator:non-exclusive:checked {\x0a    image: url(:/qss_icons/rc/checkbox_checked.png);\x0a}\x0a\x0aQMenu::indicator:non-exclusive:checked:selected {\x0a    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\x0a}\x0a\x0a/* exclusive indicator = radio button style indicator (see\x0a * QActionGroup::setExclusive) */\x0aQMenu::indicator:exclusive:unchecked {\x0a    image: url(:/qss_icons/rc/radio_unchecked.png);\x0a}\x0a\x0aQMenu::indicator:exclusive:unchecked:selected {\x0a    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\x0a}\x0a\x0aQMenu::indicator:exclusive:checked {\x0a    image: url(:/qss_icons/rc/radio_checked.png);\x0a}\x0a\x0aQMenu::indicator:exclusive:checked:selected {\x0a    image: url(:/qss_icons/rc/radio_checked_disabled.png);\x0a}\x0a\x0aQMenu::right-arrow {\x0a    margin: 5px;\x0a    image: url(:/qss_icons/rc/right_arrow.png)\x0a}\x0a\x0a\x0aQWidget:disabled\x0a{\x0a    color: #404040;\x0a    background-color: #302F2F;\x0a}\x0a\x0aQAbstractItemView\x0a{\x0a    alternate-background-color: #3A3939;\x0a    color: silver;\x0a    border: 1px solid 3A3939;\x0a    border-radius: 2px;\x0a    padding: 1px;\x0a}\x0a\x0aQWidget:focus, QMenuBar:focus\x0a{\x0a    border: 1px solid #78879b;\x0a}\x0a\x0aQTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\x0a{\x0a    border: none;\x0a}\x0a\x0aQLineEdit\x0a{\x0a    background-color: #201F1F;\x0a    padding: 2px;\x0a    border-style: solid;\x0a    border: 1px solid #3A3939;\x0a    border-radius: 2px;\x0a    color: silver;\x0a}\x0a\x0aQGroupBox {\x0a    border:1px solid #3A3939;\x0a    border-radius: 2px;\x0a    margin-top: 20px;\x0a}\x0a\x0aQGroupBox::title {\x0a    subcontrol-origin: margin;\x0a    subcontrol-position: top center;\x0a    padding-left: 10px;\x0a    padding-right: 10px;\x0a    padding-top: 10px;\x0a}\x0a\x0aQAbstractScrollArea\x0a{\x0a    border-radius: 2px;\x0a    border: 1px solid #3A3939;\x0a    background-color: transparent;\x0a}\x0a\x0aQScrollBar:horizontal\x0a{\x0a    height: 15px;\x0a    margin: 3px 15px 3px 15px;\x0a    border: 1px transparent #2A2929;\x0a    border-radius: 4px;\x0a    background-color: #2A2929;\x0a}\x0a\x0aQScrollBar::handle:horizontal\x0a{\x0a    background-color: #605F5F;\x0a    min-width: 5px;\x0a    border-radius: 4px;\x0a}\x0a\x0aQScrollBar::add-line:horizontal\x0a{\x0a    margin: 0px 3px 0px 3px;\x0a    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\x0a    width: 10px;\x0a    height: 10px;\x0a    subcontrol-position: right;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0aQScrollBar::sub-line:horizontal\x0a{\x0a    margin: 0px 3px 0px 3px;\x0a    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\x0a    height: 10px;\x0a    width: 10px;\x0a    subcontrol-position: left;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0aQScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\x0a{\x0a    border-image: url(:/qss_icons/rc/right_arrow.png);\x0a    height: 10px;\x0a    width: 10px;\x0a    subcontrol-position: right;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0a\x0aQScrollBar::sub-line:horizontal:hover,\x0aQScrollBar::sub-line:horizontal:on\x0a{\x0a    border-image: url(:/qss_icons/rc/left_arrow.png);\x0a    height: 10px;\x0a    width: 10px;\x0a    subcontrol-position: left;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0aQScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\x0a{\x0a    background: none;\x0a}\x0a\x0a\x0aQScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\x0a{\x0a    background: none;\x0a}\x0a\x0aQScrollBar:vertical\x0a{\x0a    background-color: #2A2929;\x0a    width: 15px;\x0a    margin: 15px 3px 15px 3px;\x0a    border: 1px transparent #2A2929;\x0a    border-radius: 4px;\x0a}\x0a\x0aQScrollBar::handle:vertical\x0a{\x0a    background-color: #605F5F;\x0a    min-height: 5px;\x0a    border-radius: 4px;\x0a}\x0a\x0aQScrollBar::sub-line:vertical\x0a{\x0a    margin: 3px 0px 3px 0px;\x0a    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\x0a    height: 10px;\x0a    width: 10px;\x0a    subcontrol-position: top;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0aQScrollBar::add-line:vertical\x0a{\x0a    margin: 3px 0px 3px 0px;\x0a    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\x0a    height: 10px;\x0a    width: 10px;\x0a    subcontrol-position: bottom;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0aQScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\x0a{\x0a\x0a    border-image: url(:/qss_icons/rc/up_arrow.png);\x0a    height: 10px;\x0a    width: 10px;\x0a    subcontrol-position: top;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0a\x0aQScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\x0a{\x0a    border-image: url(:/qss_icons/rc/down_arrow.png);\x0a    height: 10px;\x0a    width: 10px;\x0a    subcontrol-position: bottom;\x0a    subcontrol-origin: margin;\x0a}\x0a\x0aQScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\x0a{\x0a    background: none;\x0a}\x0a\x0a\x0aQScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\x0a{\x0a    background: none;\x0a}\x0a\x0aQTextEdit\x0a{\x0a    background-color: #201F1F;\x0a    color: silver;\x0a    border: 1px solid #3A3939;\x0a}\x0a\x0aQPlainTextEdit\x0a{\x0a    background-color: #201F1F;;\x0a    color: silver;\x0a    border-radius: 2px;\x0a    border: 1px solid #3A3939;\x0a}\x0a\x0aQHeaderView::section\x0a{\x0a    background-color: #3A3939;\x0a    color: silver;\x0a    padding-left: 4px;\x0a    border: 1px solid #6c6c6c;\x0a}\x0a\x0aQSizeGrip {\x0a    image: url(:/qss_icons/rc/sizegrip.png);\x0a    width: 12px;\x0a    height: 12px;\x0a}\x0a\x0a\x0aQMainWindow::separator\x0a{\x0a    background-color: #302F2F;\x0a    color: white;\x0a    padding-left: 4px;\x0a    spacing: 2px;\x0a    border: 1px dashed #3A3939;\x0a}\x0a\x0aQMainWindow::separator:hover\x0a{\x0a\x0a    background-color: #787876;\x0a    color: white;\x0a    padding-left: 4px;\x0a    border: 1px solid #3A3939;\x0a    spacing: 2px;\x0a}\x0a\x0a\x0aQMenu::separator\x0a{\x0a    height: 1px;\x0a    background-color: #3A3939;\x0a    color: white;\x0a    padding-left: 4px;\x0a    margin-left: 10px;\x0a    margin-right: 5px;\x0a}\x0a\x0a\x0aQFrame\x0a{\x0a    border-radius: 2px;\x0a    border: 1px solid #444;\x0a}\x0a\x0aQFrame[frameShape=\x220\x22]\x0a{\x0a    border-radius: 2px;\x0a    border: 1px transparent #444;\x0a}\x0a\x0aQStackedWidget\x0a{\x0a    border: 1px transparent black;\x0a}\x0a\x0aQToolBar {\x0a    border: 1px transparent #393838;\x0a    background: 1px solid #302F2F;\x0a    font-weight: bold;\x0a}\x0a\x0aQToolBar::handle:horizontal {\x0a    image: url(:/qss_icons/rc/Hmovetoolbar.png);\x0a}\x0aQToolBar::handle:vertical {\x0a    image: url(:/qss_icons/rc/Vmovetoolbar.png);\x0a}\x0aQToolBar::separator:horizontal {\x0a    image: url(:/qss_icons/rc/Hsepartoolbar.png);\x0a}\x0aQToolBar::separator:vertical {\x0a    image: url(:/qss_icons/rc/Vsepartoolbars.png);\x0a}\x0a\x0aQPushButton\x0a{\x0a    color: silver;\x0a    background-color: #302F2F;\x0a    border-width: 1px;\x0a    border-color: #4A4949;\x0a    border-style: solid;\x0a    padding-top: 5px;\x0a    padding-bottom: 5px;\x0a    padding-left: 5px;\x0a    padding-right: 5px;\x0a    border-radius: 2px;\x0a    outline: none;\x0a}\x0a\x0aQPushButton:disabled\x0a{\x0a    background-color: #302F2F;\x0a    border-width: 1px;\x0a    border-color: #3A3939;\x0a    border-style: solid;\x0a    padding-top: 5px;\x0a    padding-bottom: 5px;\x0a    padding-left: 10px;\x0a    padding-right: 10px;\x0a    /*border-radius: 2px;*/\x0a    color: #454545;\x0a}\x0a\x0aQPushButton:focus {\x0a    background-color: #3d8ec9;\x0a    color: white;\x0a}\x0a\x0aQComboBox\x0a{\x0a    selection-background-color: #3d8ec9;\x0a    background-color: #201F1F;\x0a    border-style: solid;\x0a    border: 1px solid #3A3939;\x0a    border-radius: 2px;\x0a    padding: 2px;\x0a    min-width: 75px;\x0a}\x0a\x0aQPushButton:checked{\x0a    background-color: #4A4949;\x0a    border-color: #6A6969;\x0a}\x0a\x0aQComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\x0a{\x0a    border: 1px solid #78879b;\x0a    color: silver;\x0a}\x0a\x0aQComboBox:on\x0a{\x0a    background-color: #626873;\x0a    padding-top: 3px;\x0a    padding-left: 4px;\x0a    selection-background-color: #4a4a4a;\x0a}\x0a\x0aQComboBox QAbstractItemView\x0a{\x0a    background-color: #201F1F;\x0a    border-radius: 2px;\x0a    border: 1px solid #444;\x0a    selection-background-color: #3d8ec9;\x0a}\x0a\x0aQComboBox::drop-down\x0a{\x0a    subcontrol-origin: padding;\x0a    subcontrol-position: top right;\x0a    width: 15px;\x0a\x0a    border-left-width: 0px;\x0a    border-left-color: darkgray;\x0a    border-left-style: solid;\x0a    border-top-right-radius: 3px;\x0a    border-bottom-right-radius: 3px;\x0a}\x0a\x0aQComboBox::down-arrow\x0a{\x0a    image: url(:/qss_icons/rc/down_arrow_disabled.png);\x0a}\x0a\x0aQComboBox::down-arrow:on, QComboBox::down-arrow:hover,\x0aQComboBox::down-arrow:focus\x0a{\x0a    image: url(:/qss_icons/rc/down_arrow.png);\x0a}\x0a\x0aQPushButton:pressed\x0a{\x0a    background-color: #484846;\x0a}\x0a\x0aQAbstractSpinBox {\x0a    padding-top: 2px;\x0a    padding-bottom: 2px;\x0a    border: 1px solid #3A3939;\x0a    background-color: #201F1F;\x0a    color: silver;\x0a    border-radius: 2px;\x0a    min-width: 75px;\x0a}\x0a\x0aQAbstractSpinBox:up-button\x0a{\x0a    background-color: transparent;\x0a    subcontrol-origin: border;\x0a    subcontrol-position: center right;\x0a}\x0a\x0aQAbstractSpinBox:down-button\x0a{\x0a    background-color: transparent;\x0a    subcontrol-origin: border;\x0a    subcontrol-position: center left;\x0a}\x0a\x0aQAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off\x0a{\x0a    image: url(:/qss_icons/rc/up_arrow_disabled.png);\x0a    width: 10px;\x0a    height: 10px;\x0a}\x0aQAbstractSpinBox::up-arrow:hover\x0a{\x0a    image: url(:/qss_icons/rc/up_arrow.png);\x0a}\x0a\x0a\x0aQAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\x0a{\x0a    image: url(:/qss_icons/rc/down_arrow_disabled.png);\x0a    width: 10px;\x0a    height: 10px;\x0a}\x0aQAbstractSpinBox::down-arrow:hover\x0a{\x0a    image: url(:/qss_icons/rc/down_arrow.png);\x0a}\x0a\x0a\x0aQLabel\x0a{\x0a    border: 0px solid black;\x0a}\x0a\x0aQTabWidget{\x0a    border: 1px transparent black;\x0a}\x0a\x0aQTabWidget::pane {\x0a    border: 1px solid #444;\x0a    border-radius: 3px;\x0a    padding: 3px;\x0a}\x0a\x0aQTabBar\x0a{\x0a    qproperty-drawBase: 0;\x0a    left: 5px; /* move to the right by 5px */\x0a}\x0a\x0aQTabBar:focus\x0a{\x0a    border: 0px transparent black;\x0a}\x0a\x0aQTabBar::close-button  {\x0a    image: url(:/qss_icons/rc/close.png);\x0a    background: transparent;\x0a}\x0a\x0aQTabBar::close-button:hover\x0a{\x0a    image: url(:/qss_icons/rc/close-hover.png);\x0a    background: transparent;\x0a}\x0a\x0aQTabBar::close-button:pressed {\x0a    image: url(:/qss_icons/rc/close-pressed.png);\x0a    background: transparent;\x0a}\x0a\x0a/* TOP TABS */\x0aQTabBar::tab:top {\x0a    color: #b1b1b1;\x0a    border: 1px solid #4A4949;\x0a    border-bottom: 1px transparent black;\x0a    background-color: #302F2F;\x0a    padding: 5px;\x0a    border-top-left-radius: 2px;\x0a    border-top-right-radius: 2px;\x0a}\x0a\x0aQTabBar::tab:top:!selected\x0a{\x0a    color: #b1b1b1;\x0a    background-color: #201F1F;\x0a    border: 1px transparent #4A4949;\x0a    border-bottom: 1px transparent #4A4949;\x0a    border-top-left-radius: 0px;\x0a    border-top-right-radius: 0px;\x0a}\x0a\x0aQTabBar::tab:top:!selected:hover {\x0a    background-color: #48576b;\x0a}\x0a\x0a/* BOTTOM TABS */\x0aQTabBar::tab:bottom {\x0a    color: #b1b1b1;\x0a    border: 1px solid #4A4949;\x0a    border-top: 1px transparent black;\x0a    background-color: #302F2F;\x0a    padding: 5px;\x0a    border-bottom-left-radius: 2px;\x0a    border-bottom-right-radius: 2px;\x0a}\x0a\x0aQTabBar::tab:bottom:!selected\x0a{\x0a    color: #b1b1b1;\x0a    background-color: #201F1F;\x0a    border: 1px transparent #4A4949;\x0a    border-top: 1px transparent #4A4949;\x0a    border-bottom-left-radius: 0px;\x0a    border-bottom-right-radius: 0px;\x0a}\x0a\x0aQTabBar::tab:bottom:!selected:hover {\x0a    background-color: #78879b;\x0a}\x0a\x0a/* LEFT TABS */\x0aQTabBar::tab:left {\x0a    color: #b1b1b1;\x0a    border: 1px solid #4A4949;\x0a    border-left: 1px transparent black;\x0a    background-color: #302F2F;\x0a    padding: 5px;\x0a    border-top-right-radius: 2px;\x0a    border-bottom-right-radius: 2px;\x0a}\x0a\x0aQTabBar::tab:left:!selected\x0a{\x0a    color: #b1b1b1;\x0a    background-color: #201F1F;\x0a    border: 1px transparent #4A4949;\x0a    border-right: 1px transparent #4A4949;\x0a    border-top-right-radius: 0px;\x0a    border-bottom-right-radius: 0px;\x0a}\x0a\x0aQTabBar::tab:left:!selected:hover {\x0a    background-color: #48576b;\x0a}\x0a\x0a\x0a/* RIGHT TABS */\x0aQTabBar::tab:right {\x0a    color: #b1b1b1;\x0a    border: 1px solid #4A4949;\x0a    border-right: 1px transparent black;\x0a    background-color: #302F2F;\x0a    padding: 5px;\x0a    border-top-left-radius: 2px;\x0a    border-bottom-left-radius: 2px;\x0a}\x0a\x0aQTabBar::tab:right:!selected\x0a{\x0a    color: #b1b1b1;\x0a    background-color: #201F1F;\x0a    border: 1px transparent #4A4949;\x0a    border-right: 1px transparent #4A4949;\x0a    border-top-left-radius: 0px;\x0a    border-bottom-left-radius: 0px;\x0a}\x0a\x0aQTabBar::tab:right:!selected:hover {\x0a    background-color: #48576b;\x0a}\x0a\x0aQTabBar QToolButton::right-arrow:enabled {\x0a     image: url(:/qss_icons/rc/right_arrow.png);\x0a }\x0a\x0a QTabBar QToolButton::left-arrow:enabled {\x0a     image: url(:/qss_icons/rc/left_arrow.png);\x0a }\x0a\x0aQTabBar QToolButton::right-arrow:disabled {\x0a     image: url(:/qss_icons/rc/right_arrow_disabled.png);\x0a }\x0a\x0a QTabBar QToolButton::left-arrow:disabled {\x0a     image: url(:/qss_icons/rc/left_arrow_disabled.png);\x0a }\x0a\x0a\x0aQDockWidget {\x0a    border: 1px solid #403F3F;\x0a    titlebar-close-icon: url(:/qss_icons/rc/close.png);\x0a    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\x0a}\x0a\x0aQDockWidget::close-button, QDockWidget::float-button {\x0a    border: 1px solid transparent;\x0a    border-radius: 2px;\x0a    background: transparent;\x0a}\x0a\x0aQDockWidget::close-button:hover, QDockWidget::float-button:hover {\x0a    background: rgba(255, 255, 255, 10);\x0a}\x0a\x0aQDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\x0a    padding: 1px -1px -1px 1px;\x0a    background: rgba(255, 255, 255, 10);\x0a}\x0a\x0aQTreeView, QListView\x0a{\x0a    border: 1px solid #444;\x0a    background-color: #201F1F;\x0a}\x0a\x0aQTreeView:branch:selected, QTreeView:branch:hover\x0a{\x0a    background: url(:/qss_icons/rc/transparent.png);\x0a}\x0a\x0aQTreeView::branch:has-siblings:!adjoins-item {\x0a    border-image: url(:/qss_icons/rc/transparent.png);\x0a}\x0a\x0aQTreeView::branch:has-siblings:adjoins-item {\x0a    border-image: url(:/qss_icons/rc/transparent.png);\x0a}\x0a\x0aQTreeView::branch:!has-children:!has-siblings:adjoins-item {\x0a    border-image: url(:/qss_icons/rc/transparent.png);\x0a}\x0a\x0aQTreeView::branch:has-children:!has-siblings:closed,\x0aQTreeView::branch:closed:has-children:has-siblings {\x0a    image: url(:/qss_icons/rc/branch_closed.png);\x0a}\x0a\x0aQTreeView::branch:open:has-children:!has-siblings,\x0aQTreeView::branch:open:has-children:has-siblings  {\x0a    image: url(:/qss_icons/rc/branch_open.png);\x0a}\x0a\x0aQTreeView::branch:has-children:!has-siblings:closed:hover,\x0aQTreeView::branch:closed:has-children:has-siblings:hover {\x0a    image: url(:/qss_icons/rc/branch_closed-on.png);\x0a    }\x0a\x0aQTreeView::branch:open:has-children:!has-siblings:hover,\x0aQTreeView::branch:open:has-children:has-siblings:hover  {\x0a    image: url(:/qss_icons/rc/branch_open-on.png);\x0a    }\x0a\x0aQListView::item:!selected:hover, QListView::item:!selected:hover,\x0aQTreeView::item:!selected:hover  {\x0a    background: rgba(0, 0, 0, 0);\x0a    outline: 0;\x0a    color: #FFFFFF\x0a}\x0a\x0aQListView::item:selected:hover, QListView::item:selected:hover,\x0aQTreeView::item:selected:hover  {\x0a    background: #3d8ec9;\x0a    color: #FFFFFF;\x0a}\x0a\x0aQSlider::groove:horizontal {\x0a    border: 1px solid #3A3939;\x0a    height: 8px;\x0a    background: #201F1F;\x0a    margin: 2px 0;\x0a    border-radius: 2px;\x0a}\x0a\x0aQSlider::handle:horizontal {\x0a    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\x0a      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\x0a    border: 1px solid #3A3939;\x0a    width: 14px;\x0a    height: 14px;\x0a    margin: -4px 0;\x0a    border-radius: 2px;\x0a}\x0a\x0aQSlider::groove:vertical {\x0a    border: 1px solid #3A3939;\x0a    width: 8px;\x0a    background: #201F1F;\x0a    margin: 0 0px;\x0a    border-radius: 2px;\x0a}\x0a\x0aQSlider::handle:vertical {\x0a    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0\x0asilver,\x0a      stop: 0.2 #a8a8a8, stop: 1 #727272);\x0a    border: 1px solid #3A3939;\x0a    width: 14px;\x0a    height: 14px;\x0a    margin: 0 -4px;\x0a    border-radius: 2px;\x0a}\x0a\x0aQToolButton {\x0a    background-color: transparent;\x0a    border: 1px transparent #4A4949;\x0a    border-radius: 2px;\x0a    margin: 3px;\x0a    padding: 3px;\x0a}\x0a\x0aQToolButton[popupMode=\x221\x22] { /* only for MenuButtonPopup */\x0a padding-right: 20px; /* make way for the popup button */\x0a border: 1px transparent #4A4949;\x0a border-radius: 5px;\x0a}\x0a\x0aQToolButton[popupMode=\x222\x22] { /* only for InstantPopup */\x0a padding-right: 10px; /* make way for the popup button */\x0a border: 1px transparent #4A4949;\x0a}\x0a\x0a\x0aQToolButton:hover, QToolButton::menu-button:hover {\x0a    background-color: transparent;\x0a    border: 1px solid #78879b;\x0a}\x0a\x0aQToolButton:checked, QToolButton:pressed,\x0a        QToolButton::menu-button:pressed {\x0a    background-color: #4A4949;\x0a    border: 1px solid #78879b;\x0a}\x0a\x0a/* the subcontrol below is used only in the InstantPopup or DelayedPopup\x0a * mode */\x0aQToolButton::menu-indicator {\x0a    image: url(:/qss_icons/rc/down_arrow.png);\x0a    top: -7px; left: -2px; /* shift it a bit */\x0a}\x0a\x0a/* the subcontrols below are used only in the MenuButtonPopup mode */\x0aQToolButton::menu-button {\x0a    border: 1px transparent #4A4949;\x0a    border-top-right-radius: 6px;\x0a    border-bottom-right-radius: 6px;\x0a    /* 16px width + 4px for border = 20px allocated above */\x0a    width: 16px;\x0a    outline: none;\x0a}\x0a\x0aQToolButton::menu-arrow {\x0a    image: url(:/qss_icons/rc/down_arrow.png);\x0a}\x0a\x0aQToolButton::menu-arrow:open {\x0a    top: 1px; left: 1px; /* shift it a bit */\x0a    border: 1px solid #3A3939;\x0a}\x0a\x0aQPushButton::menu-indicator  {\x0a    subcontrol-origin: padding;\x0a    subcontrol-position: bottom right;\x0a    left: 8px;\x0a}\x0a\x0aQTableView\x0a{\x0a    border: 1px solid #444;\x0a    gridline-color: #6c6c6c;\x0a    background-color: #201F1F;\x0a}\x0a\x0a\x0aQTableView, QHeaderView\x0a{\x0a    border-radius: 0px;\x0a}\x0a\x0aQTableView::item:pressed, QListView::item:pressed,\x0aQTreeView::item:pressed  {\x0a    background: #78879b;\x0a    color: #FFFFFF;\x0a}\x0a\x0aQTableView::item:selected:active, QTreeView::item:selected:active,\x0aQListView::item:selected:active  {\x0a    background: #3d8ec9;\x0a    color: #FFFFFF;\x0a}\x0a\x0a\x0aQHeaderView\x0a{\x0a    border: 1px transparent;\x0a    border-radius: 2px;\x0a    margin: 0px;\x0a    padding: 0px;\x0a}\x0a\x0aQHeaderView::section  {\x0a    background-color: #3A3939;\x0a    color: silver;\x0a    padding: 4px;\x0a    border: 1px solid #6c6c6c;\x0a    border-radius: 0px;\x0a    text-align: center;\x0a}\x0a\x0aQHeaderView::section::vertical::first,\x0aQHeaderView::section::vertical::only-one\x0a{\x0a    border-top: 1px solid #6c6c6c;\x0a}\x0a\x0aQHeaderView::section::vertical\x0a{\x0a    border-top: transparent;\x0a}\x0a\x0aQHeaderView::section::horizontal::first,\x0aQHeaderView::section::horizontal::only-one\x0a{\x0a    border-left: 1px solid #6c6c6c;\x0a}\x0a\x0aQHeaderView::section::horizontal\x0a{\x0a    border-left: transparent;\x0a}\x0a\x0a\x0aQHeaderView::section:checked\x0a {\x0a    color: white;\x0a    background-color: #5A5959;\x0a }\x0a\x0a /* style the sort indicator */\x0aQHeaderView::down-arrow {\x0a    image: url(:/qss_icons/rc/down_arrow.png);\x0a}\x0a\x0aQHeaderView::up-arrow {\x0a    image: url(:/qss_icons/rc/up_arrow.png);\x0a}\x0a\x0a\x0aQTableCornerButton::section {\x0a    background-color: #3A3939;\x0a    border: 1px solid #3A3939;\x0a    border-radius: 2px;\x0a}\x0a\x0aQToolBox  {\x0a    padding: 3px;\x0a    border: 1px transparent black;\x0a}\x0a\x0aQToolBox::tab {\x0a    color: #b1b1b1;\x0a    background-color: #302F2F;\x0a    border: 1px solid #4A4949;\x0a    border-bottom: 1px transparent #302F2F;\x0a    border-top-left-radius: 5px;\x0a    border-top-right-radius: 5px;\x0a}\x0a\x0a QToolBox::tab:selected { /* italicize selected tabs */\x0a    font: italic;\x0a    background-color: #302F2F;\x0a    border-color: #3d8ec9;\x0a }\x0a\x0aQStatusBar::item {\x0a    border: 1px solid #3A3939;\x0a    border-radius: 2px;\x0a }\x0a\x0a\x0aQFrame[height=\x223\x22], QFrame[width=\x223\x22] {\x0a    background-color: #444;\x0a}\x0a\x0a\x0aQSplitter::handle {\x0a    border: 1px dashed #3A3939;\x0a}\x0a\x0aQSplitter::handle:hover {\x0a    background-color: #787876;\x0a    border: 1px solid #3A3939;\x0a}\x0a\x0aQSplitter::handle:horizontal {\x0a    width: 1px;\x0a}\x0a\x0aQSplitter::handle:vertical {\x0a    height: 1px;\x0a}\x0a"
qt_resource_name = "\x00\x0a\x09$M%\x00q\x00d\x00a\x00r\x00k\x00s\x00t\x00y\x00l\x00e\x00\x0e\x0d6\x02#\x00q\x00d\x00a\x00r\x00k\x00s\x00t\x00y\x00l\x00e\x00.\x00c\x00s\x00s"
qt_resource_struct = "\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"
def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
