import sys
from PyQt4 import QtCore, QtGui

from code import Ui_Form


class MyForm(QtGui.QMainWindow):
    def __init__(self, offset, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self, offset)


if __name__ == "__main__":
    print "Enter Offset : "
    offset = int(raw_input())
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm(offset)
    myapp.show()
    sys.exit(app.exec_())