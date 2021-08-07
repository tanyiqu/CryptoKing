import sys
from ui.Forms.MainForm import MainForm
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainForm()
    widget.show()
    sys.exit(app.exec_())
    pass
