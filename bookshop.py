import sys
from PySide2 import QtWidgets

from kit.main import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())