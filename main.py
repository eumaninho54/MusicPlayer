import menu
import settings
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

menu.Ui_MainWindow
settings.Ui_Dialog

def menu_on():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = menu.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec_()
menu_on()
