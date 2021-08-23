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

def settings_on():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = settings.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()

menu_on()
settings_on()