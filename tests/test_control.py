""" Controller tests that show the linkage between the data model, view, and
logging components.
Mimic the contents of the scripts/microangio.py setup section. Create the logger
with the queue handler as part of the test case, as opposed to having the
controller create the top level logger
"""

import time

import pytest

from PySide import QtTest, QtCore, QtGui

from microangio import control
from microangio import applog


class TestControl:
    NAV_HARDWARE = 0
    NAV_OCT = 1
    NAV_ANGIO = 2

    HARDWARE_SETUP = 0
    OCT_SETUP = 1
    OCT_CAPTURE = 2
    ANGIO_SETUP = 3
    ANGIO_CAPTURE = 4

    def test_control_logs_visible_to_caplog(self, caplog, qtbot):
        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)
        qtbot.wait(1000)

        app_control.close()
        time.sleep(1)

        main_logger.close()
        time.sleep(1)
        assert "Control startup" in caplog.text()
        applog.explicit_log_close()


    def test_view_logs_visible_to_caplog(self, caplog, qtbot):
        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)
        qtbot.wait(1000)

        app_control.close()
        time.sleep(1)

        main_logger.close()
        time.sleep(1)
        assert "Init of BasicWindow" in caplog.text()
        applog.explicit_log_close()

    def test_device_logs_in_file_only(self, caplog, qtbot):
        """ Shows the expected behavior. Demonstrates that the capturelog
        fixture on py.test does not see sub process entries.
        """
        assert applog.delete_log_file_if_exists() == True

        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)
        qtbot.wait(1000)

        app_control.close()
        time.sleep(1)

        main_logger.close()
        time.sleep(1)

        log_text = applog.get_text_from_log()
        # Temporarily removed the subprocess from the control for testing,
        # leaving these in here to remind you.
        #assert "SimulateSpectra setup" in log_text
        #assert "SimulateSpectra setup" not in caplog.text()
        applog.explicit_log_close()


    def test_close_view_emits_control_signal(self, caplog, qtbot):
        """ Control script emits an event on a close condition to be processsed
        by the parent qt application, in this case qtbot. In the scripts file,
        it's the Qapplication.
        """
        main_logger = applog.MainLogger()
        app_control = control.Controller(main_logger.log_queue)

        QtTest.QTest.qWaitForWindowShown(app_control.form)

        signal = app_control.control_exit_signal.exit
        with qtbot.wait_signal(signal, timeout=1):
            app_control.form.close()

        main_logger.close()
        time.sleep(1)
        assert "Control level close" in caplog.text()
        applog.explicit_log_close()

    @pytest.fixture(scope="function")
    def basic_window(self, qtbot, request, hardware=None):
        """ Setup the controller the same way the scripts/Application
        does at every test. Ensure that the teardown is in place
        regardless of test result.
        """
        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)

        qtbot.addWidget(app_control.form)

        def control_close():
            app_control.close()
            main_logger.close()
            applog.explicit_log_close()
            time.sleep(1) # wait for control timers to complete

        request.addfinalizer(control_close)

        return app_control

    def test_controller_sees_deafult_state_on_startup(self, basic_window,
                                                      qtbot, caplog):

        QtTest.QTest.qWaitForWindowShown(basic_window.form)
        assert basic_window.form.ui.stackedWidget_bottom.currentIndex() == 2

        qtbot.wait(1000)


    def test_nav_combobox_emits_signal(self, basic_window, qtbot):
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            nav_cmb.setCurrentIndex(0)

        qtbot.wait(3000)

    def test_view_hardware_highlights_setup(self, basic_window, qtbot):

        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            nav_cmb.setCurrentIndex(0)

        pbs = basic_window.form.ui.pushButton_setup
        assert "/* Red Active */" in pbs.styleSheet()
        qtbot.wait(2000)


    def test_view_hardware_disables_capture_and_evaluate(self, basic_window, qtbot):
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            nav_cmb.setCurrentIndex(0)

        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        assert pbc.isEnabled() == False
        assert pbe.isEnabled() == False

    def test_view_oct_highlights_capture(self, basic_window, qtbot):
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to oct to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(1)

        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        assert "/* Red Active */" not in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Red Active */" not in pbe.styleSheet()

        assert pbs.isEnabled() == True
        assert pbc.isEnabled() == True
        assert pbe.isEnabled() == True



    def test_view_angio_highlights_capture(self, basic_window, qtbot):
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to oct to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(2)

        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        assert "/* Red Active */" not in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Red Active */" not in pbe.styleSheet()

        assert pbs.isEnabled() == True
        assert pbc.isEnabled() == True
        assert pbe.isEnabled() == True


    def test_setup_button_emits_signal(self, basic_window, qtbot):
        pbs = basic_window.form.ui.pushButton_setup

        signal = basic_window.control_signals.mode_select
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(pbs, QtCore.Qt.LeftButton)

        qtbot.wait(3000)

    def test_view_oct_then_click_setup_changes_controls(self, basic_window, qtbot):

        # Change to index 0 then back to 1 to activate oct mode
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to oct to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(1)


        # verify the capture button is red, and others are gray
        assert "/* Grey Inactive */" in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

        # Click setup, verify it is now red and others are gray
        qtbot.mouseClick(pbs, QtCore.Qt.LeftButton)
        qtbot.wait(1000)
        assert "/* Red Active */" in pbs.styleSheet()
        assert "/* Grey Inactive */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

        # Verify that the bottom page changes to oct setup
        bot_wid = basic_window.form.ui.stackedWidget_bottom
        assert bot_wid.currentIndex() == 1


    def test_view_angio_then_click_setup_changes_controls(self, basic_window, qtbot):

        # Change to index 0 then back to 2 to activate angio mode
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to angio to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(2)


        # verify the capture button is red, and others are gray
        assert "/* Grey Inactive */" in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

        # Click setup, verify it is now red and others are gray
        qtbot.mouseClick(pbs, QtCore.Qt.LeftButton)
        qtbot.wait(1000)
        assert "/* Red Active */" in pbs.styleSheet()
        assert "/* Grey Inactive */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

        # Verify that the bottom page changes to angio setup
        bot_wid = basic_window.form.ui.stackedWidget_bottom
        assert bot_wid.currentIndex() == 3

    def test_capture_button_emits_signal(self, basic_window, qtbot):
        pbc = basic_window.form.ui.pushButton_capture

        signal = basic_window.control_signals.mode_select
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(pbc, QtCore.Qt.LeftButton)

        qtbot.wait(3000)

    def test_view_oct_then_click_capture_no_change(self, basic_window, qtbot):

        # Change to index 0 then back to 1 to activate oct mode
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to oct to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(1)

        # verify the capture button is red, and others are gray
        assert "/* Grey Inactive */" in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()


    def test_view_angio_then_click_capture_no_change(self, basic_window, qtbot):

        # Change to index 0 then back to 1 to activate oct mode
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to angio to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(2)

        # verify the capture button is red, and others are gray
        assert "/* Grey Inactive */" in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()


    def test_view_oct_setup_then_capture_changes_controls(self, basic_window, qtbot):

        # Change to index 0 then back to 1 to activate oct mode
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to oct to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(1)

        # Click setup, verify it is now red and others are gray
        qtbot.mouseClick(pbs, QtCore.Qt.LeftButton)
        qtbot.wait(1000)
        assert "/* Red Active */" in pbs.styleSheet()
        assert "/* Grey Inactive */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

        # Click capture, verify it is now red and others are gray
        qtbot.mouseClick(pbc, QtCore.Qt.LeftButton)
        qtbot.wait(1000)
        assert "/* Grey Inactive */" in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

    def test_view_angio_setup_then_capture_changes_controls(self, basic_window, qtbot):

        # Change to index 0 then back to 1 to activate oct mode
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            # Set it to hardware then back to oct to get over default
            nav_cmb.setCurrentIndex(0)
            qtbot.wait(1000)
            nav_cmb.setCurrentIndex(2)

        # Click setup, verify it is now red and others are gray
        qtbot.mouseClick(pbs, QtCore.Qt.LeftButton)
        qtbot.wait(1000)
        assert "/* Red Active */" in pbs.styleSheet()
        assert "/* Grey Inactive */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

        # Click capture, verify it is now red and others are gray
        qtbot.mouseClick(pbc, QtCore.Qt.LeftButton)
        qtbot.wait(1000)
        assert "/* Grey Inactive */" in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

    def test_form_starts_in_oct_capture(self, basic_window, qtbot):
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        pbs = basic_window.form.ui.pushButton_setup
        pbc = basic_window.form.ui.pushButton_capture
        pbe = basic_window.form.ui.pushButton_evaluate

        assert nav_cmb.currentIndex() == 1

        assert "/* Grey Inactive */" in pbs.styleSheet()
        assert "/* Red Active */" in pbc.styleSheet()
        assert "/* Grey Inactive */" in pbe.styleSheet()

    def test_combonav_changes_bottom_widget(self, basic_window, qtbot):
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation
        bot_wid = basic_window.form.ui.stackedWidget_bottom


        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            nav_cmb.setCurrentIndex(self.NAV_HARDWARE)
        assert bot_wid.currentIndex() == self.HARDWARE_SETUP

        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            nav_cmb.setCurrentIndex(self.NAV_OCT)
        assert bot_wid.currentIndex() == self.OCT_CAPTURE

        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            nav_cmb.setCurrentIndex(self.NAV_ANGIO)
        assert bot_wid.currentIndex() == self.ANGIO_CAPTURE


    def test_form_creates_simulation_oct_data(self, basic_window, qtbot):
        # Get the pixel value of the oct image at 0, 0
        loi = basic_window.form.ui.label_oct_image
        start_data = loi.pixmap().toImage()

        # Wait for 3 seconds
        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=3000, raising=False):
            print "Just waiting for a signal that should never happen"

        cease_data = loi.pixmap().toImage()

        assert start_data != cease_data

    def test_form_creates_simulation_angio_data(self, basic_window, qtbot):
        # Activate angio mode
        nav_cmb = basic_window.form.ui.comboBox_mode_navigation

        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            nav_cmb.setCurrentIndex(2)

        # Get the pixel value of the angio image at 0, 0
        lap = basic_window.form.ui.label_angio_preview_image
        start_data = lap.pixmap().toImage()

        # Wait for 3 seconds
        signal = basic_window.control_signals.nav_changed
        with qtbot.wait_signal(signal, timeout=3000, raising=False):
            print "Just waiting for a signal that should never happen"


        cease_data = lap.pixmap().toImage()

        assert start_data != cease_data
