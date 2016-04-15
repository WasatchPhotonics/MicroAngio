""" Basic GUI tests with default qt controls for verifying functionality.
"""

import pytest

from PySide import QtCore, QtTest

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

    def test_form_has_default_setup(self, basic_form, qtbot):
        #assert basic_form.ui.labelStatus.text() == "Pre-initialization"
        assert basic_form.width() >= 1000
        assert basic_form.height() >= 700
        qtbot.wait(10000)
