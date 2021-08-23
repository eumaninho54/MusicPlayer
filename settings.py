# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from img import img
import sys
import pytube as pt
import os
import moviepy.editor as mp
import os


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 286)
        Dialog.setMinimumSize(QtCore.QSize(400, 286))
        Dialog.setMaximumSize(QtCore.QSize(400, 286))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -8, 401, 301))
        self.label.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 61))
        self.label_2.setStyleSheet("image: url(:/img/Settings2_00000.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 141, 61))
        self.label_3.setStyleSheet("image: url(:/img/AdMusic_00000.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, -40, 441, 371))
        self.label_4.setStyleSheet("image: url(:/img/settingsFundo_00000.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 110, 211, 20))
        self.lineEdit.setStyleSheet("QLineEdit {    \n"
"    border-color: rgb(85, 0, 255);\n"
"    background-color: rgb(222, 222, 222);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"    border:2px solid rgb(45, 45, 45);\n"
"}\n"
"QLineEdit:focus {\n"
"    border:2px solid rgb(0, 0, 0);\n"
"\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 140, 61, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    image: url(:/img/Add_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/img/AddHigh_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/Add_00000.png);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 210, 141, 71))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/img/viewmusic_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/img/viewmusic2_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/viewmusic_00000.png);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.add_music)
        self.pushButton_2.clicked.connect(self.view_music)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "enter the URL of the song "))

    def view_music(self):
        path = './musics'
        path = os.path.realpath(path)
        os.startfile(path)

    def add_music(self):
        try:
                # Download for Youtube
                url = self.lineEdit.text()
                stream = pt.YouTube(url = url).streams.get_audio_only()
                stream.download()
                title = str(stream.title)

                # Converter of mp4 to mp3
                clip = mp.AudioFileClip(title + '.mp4')
                clip.write_audiofile(f'musics/'+ title + '.mp3')

                # Remove mp4
                os.remove(title + '.mp4')
        except:
                error = QtWidgets.QMessageBox()
                error.setWindowTitle("Error")
                error.setIcon(QtWidgets.QMessageBox.Critical)
                error.setText("Unable to download, error found")
                error.exec()
        else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Done")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Your music was successfully downloaded")
                msg.exec()





if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()