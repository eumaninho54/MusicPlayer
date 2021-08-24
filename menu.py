# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from settings import Ui_Dialog
from mutagen.mp3 import MP3
from PyQt5.QtMultimedia import *
import sys
from os import walk
import math


class Ui_MainWindow(object):
    global seg
    global min
    seg = 0
    min = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 588)
        MainWindow.setMinimumSize(QtCore.QSize(492, 588))
        MainWindow.setMaximumSize(QtCore.QSize(492, 588))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fundo = QtWidgets.QLabel(self.centralwidget)
        self.fundo.setGeometry(QtCore.QRect(-10, 0, 510, 621))
        self.fundo.setMaximumSize(QtCore.QSize(510, 670))
        self.fundo.setStyleSheet("background-color: rgb(0, 3, 67);\n"
"image: url(:/img/capa_00000.png);")
        self.fundo.setText("")
        self.fundo.setObjectName("fundo")
        self.MusicPlayer = QtWidgets.QLabel(self.centralwidget)
        self.MusicPlayer.setGeometry(QtCore.QRect(80, -80, 321, 221))
        self.MusicPlayer.setStyleSheet("image: url(:/img/MusicPlayer_00000.png);")
        self.MusicPlayer.setText("")
        self.MusicPlayer.setObjectName("MusicPlayer")
        self.Fundodebaixo = QtWidgets.QLabel(self.centralwidget)
        self.Fundodebaixo.setGeometry(QtCore.QRect(-80, 420, 831, 131))
        self.Fundodebaixo.setStyleSheet("background-color: rgba(0, 1, 30, 120);")
        self.Fundodebaixo.setText("")
        self.Fundodebaixo.setObjectName("Fundodebaixo")
        self.temperatura = QtWidgets.QLabel(self.centralwidget)
        self.temperatura.setGeometry(QtCore.QRect(20, 10, 31, 41))
        self.temperatura.setStyleSheet("font: 20px \"Satisfy\";\n"
"color: rgb(212, 212, 212);")
        self.temperatura.setObjectName("temperatura")
        self.celsius = QtWidgets.QLabel(self.centralwidget)
        self.celsius.setGeometry(QtCore.QRect(60, 10, 31, 41))
        self.celsius.setStyleSheet("font: 20px \"Satisfy\";\n"
"color: rgb(212, 212, 212);")
        self.celsius.setObjectName("celsius")
        self.horario = QtWidgets.QLabel(self.centralwidget)
        self.horario.setGeometry(QtCore.QRect(410, 10, 71, 41))
        self.horario.setStyleSheet("font: 20px \"Satisfy\";\n"
"color: rgb(212, 212, 212);")
        self.horario.setObjectName("horario")
        self.image_central = QtWidgets.QLabel(self.centralwidget)
        self.image_central.setGeometry(QtCore.QRect(70, 130, 371, 311))
        self.image_central.setStyleSheet("image: url(:/img/music_00000.png);")
        self.image_central.setText("")
        self.image_central.setObjectName("image_central")
        self.music_name = QtWidgets.QLabel(self.centralwidget)
        self.music_name.setGeometry(QtCore.QRect(0, 420, 491, 41))
        self.music_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.music_name.setStyleSheet("font: 20px \"Satisfy\";\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.music_name.setObjectName("music_name")
        self.FundoTop = QtWidgets.QLabel(self.centralwidget)
        self.FundoTop.setGeometry(QtCore.QRect(-90, 0, 831, 61))
        self.FundoTop.setStyleSheet("background-color: rgba(0, 1, 30, 120);")
        self.FundoTop.setText("")
        self.FundoTop.setObjectName("FundoTop")
        self.barratempo = QtWidgets.QSlider(self.centralwidget)
        self.barratempo.setGeometry(QtCore.QRect(130, 460, 231, 22))
        self.barratempo.setOrientation(QtCore.Qt.Horizontal)
        self.barratempo.setObjectName("barratempo")
        self.music_inicial = QtWidgets.QLabel(self.centralwidget)
        self.music_inicial.setGeometry(QtCore.QRect(70, 460, 61, 31))
        self.music_inicial.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.music_inicial.setStyleSheet("font: 20px \"Satisfy\";\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.music_inicial.setObjectName("music_inicial")
        self.music_final = QtWidgets.QLabel(self.centralwidget)
        self.music_final.setGeometry(QtCore.QRect(360, 460, 71, 31))
        self.music_final.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.music_final.setStyleSheet("font: 20px \"Satisfy\";\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.music_final.setObjectName("music_final")
        
        
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(220, 470, 51, 51))
        self.pause.setStyleSheet("QPushButton {\n"
"    image: url(:/img/pause_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/img/pauseHIGH_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/pause_00000.png);\n"
"}")
        self.pause.setText("")
        self.pause.setObjectName("pause")


        self.avancar = QtWidgets.QPushButton(self.centralwidget)
        self.avancar.setGeometry(QtCore.QRect(270, 500, 51, 23))
        self.avancar.setStyleSheet("QPushButton {\n"
"    image: url(:/img/right_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/img/rightHIGH_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/right_00000.png);\n"
"}")
        self.avancar.setText("")
        self.avancar.setObjectName("avancar")
        self.retroceder = QtWidgets.QPushButton(self.centralwidget)
        self.retroceder.setGeometry(QtCore.QRect(170, 500, 51, 23))
        self.retroceder.setStyleSheet("QPushButton {\n"
"    image: url(:/img/left_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/img/leftHIGH_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/left_00000.png);\n"
"}")
        self.retroceder.setText("")
        self.retroceder.setObjectName("retroceder")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(220, 470, 51, 51))
        self.play.setStyleSheet("QPushButton {\n"
"    image: url(:/img/play_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/img/playHIGH_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/play_00000.png);\n"
"}")
        self.play.setText("")
        self.play.setObjectName("play")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 50, 31, 21))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    image: url(:/img/settings_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/img/settingsHIGH_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/settings_00000.png);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.retroceder_2 = QtWidgets.QPushButton(self.centralwidget)
        self.retroceder_2.setGeometry(QtCore.QRect(230, 520, 31, 31))
        self.retroceder_2.setStyleSheet("QPushButton {\n"
"    image: url(:/img/randomoff_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/img/randomON_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/randomoff_00000.png);\n"
"}\n"
"")
        self.retroceder_2.setText("")
        self.retroceder_2.setObjectName("retroceder_2")
        self.retroceder_3 = QtWidgets.QPushButton(self.centralwidget)
        self.retroceder_3.setGeometry(QtCore.QRect(230, 520, 31, 31))
        self.retroceder_3.setStyleSheet("QPushButton {\n"
"    image: url(:/img/normal_00000.png);\n"
"    background-color: rgba(205, 205, 205, 0);\n"
"    boder-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/img/normalHIGH_00000.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/img/normal_00000.png);\n"
"}\n"
"")
        self.retroceder_3.setText("")
        self.retroceder_3.setObjectName("retroceder_3")
        self.fundo.raise_()
        self.image_central.raise_()
        self.Fundodebaixo.raise_()
        self.music_name.raise_()
        self.music_inicial.raise_()
        self.music_final.raise_()

        #self.pause.raise_()

        self.avancar.raise_()
        self.retroceder.raise_()


        self.play.raise_()
        self.barratempo.raise_()
        self.FundoTop.raise_()
        self.MusicPlayer.raise_()
        self.celsius.raise_()
        self.temperatura.raise_()
        self.horario.raise_()
        self.pushButton.raise_()
        self.retroceder_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.filenames = next(walk('musics/'), (None, None, []))[2]
        
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        for c in range(0, len(self.filenames)):
                try:
                        self.url = QtCore.QUrl.fromLocalFile("musics/"+ self.filenames[c])
                        self.playlist.addMedia(QMediaContent(self.url))
                        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
                        self.player.setPlaylist(self.playlist)
                except:
                        continue

        
        self.pushButton.clicked.connect(self.openwindow)
        self.play.clicked.connect(self.playmusic)
        self.pause.clicked.connect(self.pausemusic)
        self.avancar.clicked.connect(self.avancarmusic)
        self.retroceder_3.clicked.connect(self.random)
        self.retroceder_2.clicked.connect(self.normal)
        self.avancar.clicked.connect(self.next)
        self.retroceder.clicked.connect(self.previus)
        global seg
        global min
        seg = 0
        min = 0

    def alterar_tempo(self):
            global min
            global seg
            print(self.filenames)
            pos = self.playlist.currentIndex()
            try:
                seg = MP3('musics/' + self.filenames[pos])
                seg = seg.info.length
                min = 0
                print(min, seg)
                print(math.ceil(min), math.ceil(seg))
                while seg >= 60:
                        seg = math.ceil(seg) - 60
                        min = math.ceil(min) + 1
                seg = math.ceil(seg)
                min = math.ceil(min)
            except:
                seg = 0
                min = 0
                print('erroo')

            if seg < 10:
                seg = '0' + str(seg)
            if min < 10:
                min = '0' + str(min) 


            time = str(min) + ':' + str(seg)
            print(time)
            _translate = QtCore.QCoreApplication.translate
            self.music_final.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{time}</span></p></body></html>"))

    

    def next(self):
            self.playlist.next()
            self.alterar_tempo()
        
    def previus(self):
           self.playlist.previous()
           self.alterar_tempo()
           
        
    def normal(self):
            self.retroceder_2.hide()
            self.retroceder_3.show()
            self.play.show()
            self.pause.hide()
            self.playlist = QMediaPlaylist()
            self.alterar_tempo()

            for c in range(0, len(self.filenames)):
                try:
                        self.url = QtCore.QUrl.fromLocalFile("musics/"+ self.filenames[c])
                        self.playlist.addMedia(QMediaContent(self.url))
                        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
                        self.player.setPlaylist(self.playlist)
                except:
                        continue
            self.pausemusic

            
    def random(self):
            self.retroceder_3.hide()
            self.retroceder_2.raise_()
            self.retroceder_2.show()
            self.play.show()
            self.pause.hide()
            self.alterar_tempo()
            for c in range(0, len(self.filenames)):
                try:
                        self.url = QtCore.QUrl.fromLocalFile("musics/"+ self.filenames[c])
                        self.playlist.addMedia(QMediaContent(self.url))
                        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
                        self.player.setPlaylist(self.playlist)
                except:
                        continue
            self.playlist.shuffle()

            
            
 
    def playmusic(self):
            self.filenames = next(walk('musics/'), (None, None, []))[2]
            try:
                self.url = QtCore.QUrl.fromLocalFile("musics/"+ self.filenames[0])


                self.player.play()
                self.play.hide()
                self.pause.raise_()
                self.pause.show()
                self.alterar_tempo()
            except:
                error = QtWidgets.QMessageBox()
                error.setWindowTitle("Error")
                error.setIcon(QtWidgets.QMessageBox.Critical)
                error.setText("No music found, enter the settings above")
                error.exec()
                

    def avancarmusic(self):
            '''global num
            num += 1
            try:
                self.player.play()'''
                
    def pausemusic(self):
            self.filenames = next(walk('musics/'), (None, None, []))[2]
            self.player.pause()
            self.play.show()
            self.pause.hide()
          
        
        


    def openwindow(self):
            self.play.show()
            self.pause.hide()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
            self.filenames = next(walk('musics/'), (None, None, []))[2]
            for c in range(0, len(self.filenames)):
                try:
                        self.url = QtCore.QUrl.fromLocalFile("musics/"+ self.filenames[c])
                        self.playlist.addMedia(QMediaContent(self.url))
                        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
                        self.player.setPlaylist(self.playlist)
                except:
                        continue


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "@ymaninho54"))
        self.temperatura.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">29</span></p></body></html>"))
        self.celsius.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ºC</span></p></body></html>"))
        self.horario.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">16:40</span></p></body></html>"))
        self.music_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Nome da musica</span></p></body></html>"))
        self.music_inicial.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">00:00</span></p></body></html>"))
        self.music_final.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">00:00</span></p></body></html>"))



from img import img


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()
