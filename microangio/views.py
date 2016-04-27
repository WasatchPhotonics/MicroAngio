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

        self.load_placeholder_images()
        self.set_initial_state()

        app_icon = QtGui.QIcon(":ui/images/ApplicationIcon.ico")
        self.setWindowIcon(app_icon)
        self.setWindowTitle(title)
        self.show()

    def load_placeholder_images(self):
        """ Use the example data 16 bit tiffs, make sure they can be displayed
        in the qt label. Conversion is from:
        http://blog.philippklaus.de/2011/08/handle-16bit-tiff-images-in-python/
        """
        import numpy
        img_url = "microangio/assets/images/raw_data/2048x1024_repeated.tif"

        # Open the image, convert in place
        ref_img = Image.open(img_url)
        ref_img.convert("L")

        # Assign it to a numpy array, transpose X and Y dimensions
        ref_data = numpy.asarray(ref_img, dtype=numpy.uint16).T

        # Create an imageview control, assign the data and make it visible
        self.ui.imview_reference = pyqtgraph.ImageView()
        self.ui.imview_reference.setImage(ref_data)


        #self.roi = pyqtgraph.RectROI([20, 20], [20, 20], pen=(0,9))
        #self.ui.imview_reference.addItem(self.roi)


        self.ui.stackedWidget_hardware.addWidget(self.ui.imview_reference)
        self.ui.stackedWidget_hardware.setCurrentIndex(2)

        #self.ui.imview_reference.ui.roiBtn.setChecked(True)
        # This section borrowed almost verbatim from the roiClicked function in
        # ImageView. This should probably be changed to something closer to
        # programatically clicking the roi button
        initial_roi = self.ui.imview_reference.roi
        initial_roi.setSize((2048, 20))
        initial_roi.setPos((0, 512))
        print "Size is: %s", initial_roi.size()
        print "pos is: %s", initial_roi.pos()
        initial_roi.show()
        self.ui.imview_reference.ui.roiPlot.setMouseEnabled(True, True)
        self.ui.imview_reference.ui.splitter.setSizes([self.height()*0.6, self.height()*0.4])
        self.ui.imview_reference.roiCurve.show()
        self.ui.imview_reference.roiChanged()
        self.ui.imview_reference.ui.roiPlot.showAxis('left')

        self.ui.imview_reference.ui.roiPlot.setVisible(True)


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
