""" Basic GUI tests with default qt controls for verifying functionality.
"""

import pytest

from PySide import QtCore, QtTest, QtGui

from microangio import views

class TestBasicMainWindow:

    @pytest.fixture(scope="function")
    def basic_form(self, qtbot, request):
        """ Create the view at every setup, close it on final.
        """
        new_form = views.BasicWindow()

        def form_close():
            new_form.close()
        request.addfinalizer(form_close)

        return new_form

    def test_form_has_default_setup(self, basic_form, qtbot):
        #assert basic_form.ui.labelStatus.text() == "Pre-initialization"
        assert basic_form.width() >= 1000
        assert basic_form.height() >= 700

    def test_form_has_default_setup_long(self, basic_form, qtbot):
        #assert basic_form.ui.labelStatus.text() == "Pre-initialization"
        assert basic_form.width() >= 1000
        assert basic_form.height() >= 700
        qtbot.wait(100000)

    def test_form_starts_in_oct_capture(self, basic_form, qtbot):
        assert basic_form.ui.stackedWidget_bottom.currentIndex() == 2

        nav = basic_form.ui.comboBox_mode_navigation
        assert nav.currentIndex() == 1

        pbc = basic_form.ui.pushButton_capture
        print pbc.styleSheet()

        color = pbc.palette().color(QtGui.QPalette.Background)
        print color.red(), color.green(), color.blue()
        assert "red" in pbc.styleSheet()


