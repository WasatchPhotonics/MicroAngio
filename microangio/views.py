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

    def load_placeholder_images(self):
        """ Use the example data png files, place them in a pyqtgraph image widget.
        """
        #self.image_data = get_image_data_from_blob()
        img_url = ":/website/images/oct_gallery/placeholder_cat1_retina_bv34s.jpg"

        #self.qimg = QtGui.QImage.fromData(img_url)
        #self.pixmap = QtGui.QPixmap.fromImage(self.qimg)

        import numpy

        # Generate numpy array from scratch, set pixmap
        #spectroWidth=1000
        #spectroHeight=1000
#
#        a=numpy.random.random(spectroHeight*spectroWidth)*255
#        a=numpy.reshape(a,(spectroHeight,spectroWidth))
#        a=numpy.require(a, numpy.uint8, 'C')

#        a=numpy.roll(a,-5)
#        QI=QtGui.QImage(a.data, spectroWidth, spectroHeight, QtGui.QImage.Format_Indexed8)
#        self.pixmap = QtGui.QPixmap.fromImage(QI)


        # Load from resource, set pixmap
        #self.qimg = QtGui.QImage(img_url)
        #self.pixmap = QtGui.QPixmap.fromImage(self.qimg)


        # Load from resource into numpy array, add noise
        incomingImage = QtGui.QImage(img_url)
        #self.pixmap = QtGui.QPixmap.fromImage(incomingImage)

        incomingImage = incomingImage.convertToFormat(QtGui.QImage.Format.Format_RGB32)

        width = incomingImage.width()
        height = incomingImage.height()

        ptr = incomingImage.constBits()
        arr = numpy.array(ptr).reshape(height, width, 4)  #  Copies the data

        # Add the noise
        copy_arr = numpy.copy(arr)
        arr += copy_arr

        # recreate a qimage from the copied numpy arr
        QI = QtGui.QImage(arr.data, width, height, QtGui.QImage.Format.Format_RGB32)
        self.pixmap = QtGui.QPixmap.fromImage(QI)


        #self.pixmap = QtGui.QPixmap.fromImage(img_url)
        self.ui.label_oct_image.setPixmap(self.pixmap)


        return

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
