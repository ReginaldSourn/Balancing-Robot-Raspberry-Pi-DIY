# import pylab
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import time
import socket
import sys
import matplotlib.animation as anim
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np
import threading
import random

''' SOME TUTORIAL FROM https://pythonspot.com/pyqt5-matplotlib/ '''


data = []
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = '10.42.0.43'
# port = 2220
#
# s.connect((host, port))
# s.send('hello')
# This just simulates reading from a socket.
def data_listener():
    while True:
        data = s.recv(1024)
        print(data)


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title= "PID PLOT"
        self.left = 10
        self.top = 20
        self.width = 1300
        self.height = 640
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:#ffffff;')
        buttonstart = QPushButton('Start', self)
        buttonstop = QPushButton('STOP', self)
        pset = QLineEdit(self)
        iset = QLineEdit(self)
        dset = QLineEdit(self)
        labelp= QLabel('P SET',self)
        labeli= QLabel('I SET',self)
        labeld= QLabel('D SET',self)
        m = plotpid(self, width=15.2, height=3)
        m.move(-160,0)
        m2 = PlotInput(self, width=15.2, height=3)
        m2.move(-160,300)
        labelp.resize(40,50)
        labeli.resize(40,50)
        labeld.resize(40,50)
        labelp.move(40,600)
        labeli.move(240,600)
        labeld.move(440,600)
        pset.resize(120,50)
        iset.resize(120,50)
        dset.resize(120,50)
        pset.move(80,600)
        iset.move(280,600)
        dset.move(480,600)

        buttonstop.setToolTip('This button to kill task ')
        buttonstop.move(800,600)
        buttonstop.resize(120,50)
        buttonstart.setToolTip('Start Test PID balancing robot')
        buttonstart.move(650,600)
        buttonstart.resize(120,50)

        self.show()


class plotpid(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='rectilinear',autoscale_on=False)
        self.axes.set_ylim(-5,10)
        self.axes.set_xlim(0,200)
        # self.axes.scatter(x,y,s,c)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # anim.FuncAnimation(fig, self.plot, frames=5, interval=200, repeat=False)
        # FigureCanvas.updateGeometry(self)
        # plt.show()
        self.plot()
    def plot(self):
        #datap = [random.random() for i in range(100)]



        #datai = [random.random() for i in range(0,100)]
        datap = (10* np.random.random_sample((1,100))-3)
        datai = (10* np.random.random_sample((1,100))-3)
        datad = (10* np.random.random_sample((1,100))-3)# for i in range(0,100)
        # print(datap[][0::2])
        print(datai)
        self.axes.clear()
        self.axes.plot(datap[0], 'r-',  label="data Proportional")
        self.axes.plot(datai[0], 'g-', label="data Intergral")
        self.axes.plot(datad[0], 'b-', label="data Derivative")

        self.axes.legend(bbox_to_anchor=(1, 1),loc=2, borderaxespad=0.)
        self.axes.set_title('PID BALANCER ROBOT')
        # self.pause(0.2)
        # s.gca().set_color_cycle(['red', 'green', 'blue','yellow'])


        # self.plot.legend(['Proportional','Intergral', 'Derivative', 'ERROR'])

        self.draw()
        plt.pause(0.001)

class PlotInput(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='rectilinear',autoscale_on=False)
        self.axes.set_ylim(-5,10)
        self.axes.set_xlim(0,200)
        # self.axes.scatter(x,y,s,c)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # anim.FuncAnimation(fig, self.plot, frames=5, interval=200, repeat=False)
        # FigureCanvas.updateGeometry(self)
        # plt.show()
        self.plot()
    def plot(self):
        #datap = [random.random() for i in range(100)]



        #datai = [random.random() for i in range(0,100)]
        datap = (10* np.random.random_sample((1,100))-3)
        datai = (10* np.random.random_sample((1,100))-3)
        datad = (10* np.random.random_sample((1,100))-3)# for i in range(0,100)
        # print(datap[][0::2])
        print(datai)
        self.axes.clear()
        self.axes.plot(datap[0], 'r-',  label="data Proportional")
        self.axes.plot(datai[0], 'g-', label="data Intergral")
        self.axes.plot(datad[0], 'b-', label="data Derivative")

        self.axes.legend(bbox_to_anchor=(1, 1),loc=2, borderaxespad=0.)
        self.axes.set_title('PID BALANCER ROBOT')
        # self.pause(0.2)
        # s.gca().set_color_cycle(['red', 'green', 'blue','yellow'])


        # self.plot.legend(['Proportional','Intergral', 'Derivative', 'ERROR'])

        self.draw()
        plt.pause(0.001)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()

    sys.exit(app.exec_())
