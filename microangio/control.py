""" Application level controller for demonstration program. Handles data model
and UI updates with MVC style architecture.
"""

from PySide import QtCore

from . import views, devices

import logging
log = logging.getLogger(__name__)

class Controller(object):
    def __init__(self, log_queue):
        log.debug("Control startup")

        # Create a separate process for the qt gui event loop
        self.form = views.BasicWindow(title="MicroAngio")

        self.create_styles()

        self.create_signals()

        self.bind_view_signals()

        self.device = devices.LongPollingSimulateSpectra(log_queue)
        self.total_spectra = 0

        self.set_capture_active()

        self.setup_main_event_loop()

    def create_styles(self):
        """ Location for runtime generated stylesheets. This is hideous.
        This should be done all in the view, somehow. Or even better, in the
        designer, specifying active/inactive themes - somehow

        This is also the location for various customizations specific to the
        prototype demo.

        """

        self.NAV_HARDWARE = 0
        self.NAV_OCT = 1
        self.NAV_ANGIO = 2

        self.HARDWARE_SETUP = 0
        self.OCT_SETUP = 1
        self.OCT_CAPTURE = 2
        self.ANGIO_SETUP = 3
        self.ANGIO_CAPTURE = 4


        self.form.ui.comboBox_selector.hide()
        self.form.ui.pushButton_capture_hidden_red.hide()


        self.setup_active = """QPushButton:hover
        {
                border: 1px solid #78879b;
                color: silver;
        }

        QPushButton {
                /* Red Active */
                background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.512195, y2:0, stop:0 rgba(137, 10, 10, 255), stop:1 rgba(186, 10, 10, 255));
                border-radius: 0px;
                border-top-left-radius: 12px;
                border-bottom-left-radius: 12px;
        }"""

        self.setup_inactive = """QPushButton:hover
        {
                border: 1px solid #78879b;
                color: silver;
        }

        QPushButton {
                /* Grey Inactive */
                background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));
                border-radius: 0px;
                border-top-left-radius: 12px;
                border-bottom-left-radius: 12px;
        }"""

        self.capture_active = """QPushButton:hover
        {
                border: 1px solid #78879b;
                color: silver;
        }

        QPushButton {
                /* Red Active */
                background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.512195, y2:0, stop:0 rgba(137, 10, 10, 255), stop:1 rgba(186, 10, 10, 255));
                border-radius: 0px;
        }"""

        self.capture_inactive = """QPushButton:hover
        {
                border: 1px solid #78879b;
                color: silver;
        }

        QPushButton {
                /* Grey Inactive */
                background-color: qlineargradient(spread:pad, x1:0.546341, y1:1, x2:0.512195, y2:0, stop:0 rgba(67, 67, 67, 255), stop:1 rgba(96, 96, 96, 255));
                border-radius: 0px;
        }"""

    def create_signals(self):
        """ Create signals for access by parent process.
        """
        class ControlClose(QtCore.QObject):
            exit = QtCore.Signal(str)

        self.control_exit_signal = ControlClose()

        class ControlSignals(QtCore.QObject):
            initialize = QtCore.Signal(str)
            nav_changed = QtCore.Signal(str)
            mode_select = QtCore.Signal(str)

        self.control_signals = ControlSignals()

    def bind_view_signals(self):
        """ Connect GUI form signals to control events.
        """
        self.form.exit_signal.exit.connect(self.close)


        #self.form.ui.buttonInitialize.clicked.connect(self.initialize)

        cmn = self.form.ui.comboBox_mode_navigation
        cmn.currentIndexChanged.connect(self.update_navigation)

        pbs = self.form.ui.pushButton_setup
        pbs.clicked.connect(self.update_mode_setup)

        pbc = self.form.ui.pushButton_capture
        pbc.clicked.connect(self.update_mode_capture)

    def update_mode_capture(self):
        """ Activate the appropriate controls for the currently selected main
        navigation, capture subsection.
        """

        log.info("Mode select capture")
        self.control_signals.mode_select.emit("capture")

        cmn = self.form.ui.comboBox_mode_navigation
        if cmn.currentIndex() == self.NAV_OCT:
            log.info("Switch to OCT capture")
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.OCT_CAPTURE)
            self.set_capture_active()

        elif cmn.currentIndex() == self.NAV_ANGIO:
            log.info("Switch to Angio setup")
            self.set_capture_active()
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.ANGIO_CAPTURE)

    def set_capture_active(self):
        """ Convenience function for making just the capture button have the
        red style sheet and all others have grey.
        """
        pbs = self.form.ui.pushButton_setup
        pbc = self.form.ui.pushButton_capture
        pbe = self.form.ui.pushButton_evaluate

        pbs.setStyleSheet(self.setup_inactive)
        pbc.setStyleSheet(self.capture_active)

        pbs.setEnabled(True)
        pbc.setEnabled(True)
        pbe.setEnabled(True)

    def update_mode_setup(self):
        """ Change the current mode under the currently selected main
        navigation for the appropriate setup subsection.
        """

        log.info("Mode select setup")
        self.control_signals.mode_select.emit("setup")

        # If you're in hardware mode, and you click setup, disable the other
        # buttons and set setup red
        cmn = self.form.ui.comboBox_mode_navigation
        if cmn.currentIndex() == self.NAV_HARDWARE:
            self.set_setup_active_disable_others()
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.HARDWARE_SETUP)

        elif cmn.currentIndex() == self.NAV_OCT:
            log.info("Switch to OCT setup")
            self.set_setup_active()
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.OCT_SETUP)

        elif cmn.currentIndex() == self.NAV_ANGIO:
            log.info("Switch to Angio setup")
            self.set_setup_active()
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.ANGIO_SETUP)

    def set_setup_active(self):
        """ Show the setup button as red active, the others as grey active.
        """
        pbs = self.form.ui.pushButton_setup
        pbc = self.form.ui.pushButton_capture
        pbe = self.form.ui.pushButton_evaluate

        pbs.setStyleSheet(self.setup_active)
        pbc.setStyleSheet(self.capture_inactive)

        pbs.setEnabled(True)
        pbc.setEnabled(True)
        pbe.setEnabled(True)

    def set_setup_active_disable_others(self):
        """ Used for hardware display of just the setup button
        """
        pbs = self.form.ui.pushButton_setup
        pbc = self.form.ui.pushButton_capture
        pbe = self.form.ui.pushButton_evaluate

        pbs.setStyleSheet(self.setup_active)
        pbc.setStyleSheet(self.capture_inactive)

        pbs.setEnabled(True)
        pbc.setEnabled(False)
        pbe.setEnabled(False)


    def update_navigation(self, index_changed):
        """ Change the main navigation window when the mode navigation
        combobox is updated.
        """
        log.info("Change to: %s", index_changed)
        self.control_signals.nav_changed.emit(index_changed)

        pbs = self.form.ui.pushButton_setup
        pbc = self.form.ui.pushButton_capture
        pbe = self.form.ui.pushButton_evaluate

        if index_changed == 0:
            self.set_setup_active_disable_others()
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.HARDWARE_SETUP)

        elif index_changed == 1:
            self.set_capture_active()
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.OCT_CAPTURE)

        elif index_changed == 2:
            self.set_capture_active()
            self.form.ui.stackedWidget_bottom.setCurrentIndex(self.ANGIO_CAPTURE)



    def setup_main_event_loop(self):
        """ Create a timer for a continuous event loop, trigger the start.
        """
        log.debug("Setup main event loop")
        self.continue_loop = True
        self.main_timer = QtCore.QTimer()
        self.main_timer.setSingleShot(True)
        self.main_timer.timeout.connect(self.event_loop)
        #self.main_timer.start(0)

    def event_loop(self):
        """ Process queue events, interface events, then update views.
        """
        result = self.device.read()
        if result is not None:
            self.total_spectra += 1
            self.form.txt_box.append("%s spectra read" \
                                     % self.total_spectra)

        if self.continue_loop:
            self.main_timer.start(0)

    def close(self):
        self.continue_loop = False
        self.device.close()
        log.debug("Control level close")
        self.control_exit_signal.exit.emit("Control level close")

