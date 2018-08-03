from __future__ import unicode_literals
import sys
import os
import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



class pid_plot(FigureCanvas):
    def __init__(self, width, height):
        fig = Figure(figsize=(width, height), dpi=dpi)


class ApplicationWindow( QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


        l = QtWidgets.QVBoxLayout(self)
        # sc = MyStaticMplCanvas(self.main_widget, width=5,)
        test = QtWidgets.QLabel("hello world")
        # test.setMinimum(100, 300)
        # test.setTextSize(10)
        l.addWidget(test)
        lform =QtWidgets.QGridLayout()

        labelP = QtWidgets.QLabel("KP")
        editP = QtWidgets.QLineEdit()
        # editP.sizeHeight(30)
        editI = QtWidgets.QLineEdit()
        editD = QtWidgets.QLineEdit()
        labelI = QtWidgets.QLabel("KI")
        labelD = QtWidgets.QLabel("KD")


        # lform.setMinimum(300, 200)
        # llabel.addWidget(labelP)
        # llabel.addWidget(labelI)
        # llabel.addWidget(labelD)
        # ledit.addWidget(editP)
        # ledit.addWidget(editI)
        # ledit.addWidget(editD)
        # lform.addLayout(llabel)
        #
        # lform.addLayout(ledit)


        lform.addWidget(labelP, 1,0)
        lform.addWidget(labelI, 2,0)
        lform.addWidget(labelD, 3,0)
        lform.addWidget(editP, 1,1)
        lform.addWidget(editI, 2,1)
        lform.addWidget(editD, 3,1)


        l.addLayout(lform)
        self.setLayout(l)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("PID CONTROL")
qApp = QtWidgets.QApplication(sys.argv)
aw = ApplicationWindow()
# aw.setWindowTitle("%s" % programe)
aw.show()
sys.exit(qApp.exec_())
