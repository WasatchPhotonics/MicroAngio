""" views for micronangio. Includes basic window mainform.
"""
from PySide import QtGui, QtCore

from PIL import Image  # for creating placeholder imagery at startup
import pyqtgraph

from .assets import prototype_microangio_layout as microangio_layout

import logging
log = logging.getLogger(__name__)

class BasicWindow(QtGui.QMainWindow):
    """ Load the QT designer created layout based on default qt WIMP controls.
    """
    def __init__(self, title="BasicWindow", layout=microangio_layout,
                 geometry=[250, 250, 1000, 700]):
        log.debug("Init of %s", self.__class__.__name__)
        super(BasicWindow, self).__init__()

        self.ui = layout.Ui_MainWindow()
        self.ui.setupUi(self)

        self.create_signals()
        # x, y, w, h
        self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])

        #self.load_placeholder_images()
        self.set_initial_state()

        app_icon = QtGui.QIcon(":ui/images/ApplicationIcon.ico")
        self.setWindowIcon(app_icon)
        self.setWindowTitle(title)
        self.show()

    def set_initial_state(self):
        """ Pre-configure the interface by clicking buttons and setting
        displayed widgets as appropriate.
        """
        NAV_HARDWARE = 0
        NAV_OCT = 1
        NAV_ANGIO = 2
        self.ui.comboBox_mode_navigation.setCurrentIndex(NAV_OCT)

        HARDWARE_SETUP = 0
        OCT_SETUP = 1
        OCT_CAPTURE = 2
        ANGIO_SETUP = 3
        ANGIO_CAPTURE = 4
        self.ui.stackedWidget_bottom.setCurrentIndex(OCT_CAPTURE)


    def create_signals(self):
        """ Create signal objects to be used by controller and internal simple
        events.
        """
        class ViewClose(QtCore.QObject):
            """ Emit a signal for control upstream.
            """
            exit = QtCore.Signal(str)

        self.exit_signal = ViewClose()

    def closeEvent(self, event):
        """ Custom signal for controller to catch when the GUI close event is
        triggered by the user.
        """
        log.debug("View level close")
        self.exit_signal.exit.emit("close event")
