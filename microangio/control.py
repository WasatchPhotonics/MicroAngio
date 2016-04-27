""" Application level controller for demonstration program. Handles data model
and UI updates with MVC style architecture.
"""

import random

import numpy

from PIL import Image

import pyqtgraph

from PySide import QtCore, QtGui

from . import views

import logging
log = logging.getLogger(__name__)

class Controller(object):
    def __init__(self, log_queue):
        log.debug("Control startup")

        # Create a separate process for the qt gui event loop
        self.form = views.BasicWindow(title="MicroAngio")

        self.create_styles()

        self.setup_simulated_imagery()
        self.load_placeholder_images()


        self.create_signals()

        self.bind_view_signals()

        self.set_capture_active()

        self.setup_main_event_loop()

    def load_placeholder_images(self):
        """ Use the example data 16 bit tiffs, make sure they can be displayed
        in the qt label. Conversion is from:
        http://blog.philippklaus.de/2011/08/handle-16bit-tiff-images-in-python/
        May actually be 8 bit tiffs for the prototype, but keep this in place
        so it doesn't bite you later.
        """
        self.ref_data = numpy.copy(self.simulated_hardware_raw).T

        # Create an imageview control, assign the data and make it visible
        self.form.ui.imview_hardware = pyqtgraph.ImageView()
        imvh = self.form.ui.imview_hardware
        imvh.setImage(self.ref_data)

        swh = self.form.ui.stackedWidget_hardware
        swh.addWidget(imvh)
        swh.setCurrentIndex(2)

        # Get the pre-created ROI, set it to full width, in the middle of the
        # image
        imvh.roi.setSize((2048, 20))
        imvh.roi.setPos((0, 512))
        imvh.roi.show()


        # This section borrowed almost verbatim from the roiClicked function in
        # ImageView. This should probably be changed to something closer to
        # programatically clicking the roi button
        imvh.ui.roiPlot.setMouseEnabled(True, True)
        imvh.ui.splitter.setSizes([imvh.height()*0.6, imvh.height()*0.4])
        imvh.roiCurve.show()
        imvh.roiChanged()
        imvh.ui.roiPlot.showAxis('left')
        imvh.ui.roiPlot.setVisible(True)


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

    def setup_simulated_imagery(self):

        img_url = ":/website/images/oct_gallery/2048x1024_repeated.tif"
        #img_url = ":/website/images/oct_gallery/cat1_retina36s.jpg"
        self.simulated_hardware_raw = self.convert_image(img_url)

        img_url = ":/website/images/oct_gallery/cat1_retina36s.jpg"
        self.simulated_center_bscan = self.convert_image(img_url)

        img_url = ":/website/images/oct_gallery/retina_angiograph_03.jpg"
        self.simulated_angio_preview = self.convert_image(img_url)

        img_url = ":/website/images/oct_gallery/square_retina11.jpg"
        self.simulated_current_bscan = self.convert_image(img_url)

    def convert_image(self, img_url):
        """ Load oct imagery from the resource file into numpy arrays for easier
        noise addition.
        """
        # Load from resource into numpy array
        incomingImage = QtGui.QImage(img_url)
        incomingImage = incomingImage.convertToFormat(QtGui.QImage.Format.Format_RGB32)

        height = incomingImage.height()
        width = incomingImage.width()

        ptr = incomingImage.constBits()

        temp_array = numpy.array(ptr).reshape(height, width, 4)
        return temp_array

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
        self.main_timer.start(100)

    def event_loop(self):
        """ Process queue events, interface events, then update views.
        """

        self.add_noise_to_imagery()

        if self.continue_loop:
            self.main_timer.start(500)


    def add_noise_to_imagery(self):
        """ For the currently displayed navigation mode, read the resource image,
        add noise to the numpy array, then display.
        """

        swb = self.form.ui.stackedWidget_bottom

        if swb.currentIndex() == self.HARDWARE_SETUP:
            #self.update_pyqtgraph_image(self.simulated_hardware_raw,
                                        #self.form.ui.imview_hardware)
            pass

        elif swb.currentIndex() == self.OCT_CAPTURE:

            display_label = self.form.ui.label_oct_image
            self.update_image(self.simulated_center_bscan, display_label)

        elif swb.currentIndex() == self.ANGIO_CAPTURE:
            display_label = self.form.ui.label_angio_preview_image
            self.update_image(self.simulated_angio_preview, display_label)

            display_label = self.form.ui.label_angio_center_bscan_image
            self.update_image(self.simulated_center_bscan, display_label)

            display_label = self.form.ui.label_angio_current_bscan_image
            self.update_image(self.simulated_current_bscan, display_label)

        else:
            log.info("Not adding noise to un-displayed imagery")
            return

    def update_pyqtgraph_image(self, input_data, display_image):
        """ Appy noise to the image, then store the data as a component
        of the pyqtgraph imageview control for permanence.
        """
        return


    def update_image(self, input_data, display_label):
        """ Apply the noise to the image, then store the data as a component
        of the label to make sure the garbage collector doesn't cause a crash.
        """
        copy_sim = numpy.copy(input_data)
        width = copy_sim.shape[1]
        height = copy_sim.shape[0]

        noise_factor = 4
        # Get random sample of width and height
        nrc = numpy.random.choice
        random_width_size = width / noise_factor
        random_height_size = height / noise_factor
        rand_width = nrc(width, size=random_width_size)

        # Assign each of the randomly selected pixels either white or black
        for width_index in rand_width:
            rand_height = nrc(height, size=random_height_size)
            for height_index in rand_height:

                # Differing shades of grade, alpha is apparently ignored
                br = random.choice([45, 50, 55, 60, 65, 70, 75, 50, 100])
                copy_sim[height_index, width_index] = [br, br, br, br]


        # recreate a qimage from the copied numpy arr
        image = QtGui.QImage(copy_sim.data,
                             width, height, QtGui.QImage.Format.Format_RGB32)
        new_pixmap = QtGui.QPixmap.fromImage(image)

        # Store the data as part of the display label to ensure the
        # garbage collector doens't cause a crash
        display_label.stored_numpy_data = copy_sim
        display_label.stored_image_data = image
        display_label.setPixmap(new_pixmap)


    def close(self):
        self.continue_loop = False
        log.debug("Control level close")
        self.control_exit_signal.exit.emit("Control level close")

