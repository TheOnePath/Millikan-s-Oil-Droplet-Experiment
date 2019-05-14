from PyQt4.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


Ui_MainWindow, QMainWindow = loadUiType('window.ui')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig_dict = {}

        self.mplfigs.itemClicked.connect(self.change_fig)


    def change_fig(self, item):
        text = item.text()
        self.rm_mpl()
        self.add_mpl(self.fig_dict[text])


    def add_mpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()


        self.toolbar = NavigationToolbar(self.canvas, self, coordinates=True)
        self.addToolBar(self.toolbar)


    def rm_mpl(self,):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()


    def add_fig(self, name, fig):
        self.fig_dict[name] = fig
        self.mplfigs.addItem(name)
    

if __name__ == "__main__":
    from millikan import Millikan
    from PyQt4 import QtGui
    import numpy as np
    import sys

    app = Millikan()
    x, y = app.sort()
    xfit, yfit = app.graph(x, y)

    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(x, y, 'ro', xfit, yfit)
    

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.add_mpl(fig1)
    main.add_fig('Millikan Oil Droplet', fig1)
    main.show()
    sys.exit(app.exec_())
