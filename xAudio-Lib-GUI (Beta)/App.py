import traceback, sys, time, os
import pyaudio
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import *
from math import *
class AudioWorker(QRunnable):
    @pyqtSlot()
    def __init__(self):
        super().__init__()
        from xAudioControl import xAudio
        self.xAudio = xAudio()
        self.xAudio.__init__()
    def startStream(self):
        self.xAudio.setStreamOn()
    def stopStream(self):
        self.xAudio.setStreamOff()
    def exitStream(self):
        self.xAudio.exitStream()
        QCoreApplication.quit()
        os._exit(0)

    def setNoteMinMax(self, noteMin1, noteMax1):
        self.xAudio.setNoteMinMax(noteMin1, noteMax1)

    def run(self):
        while True:
            self.xAudio.startStream()
            if (self.xAudio.streamStatus):
                window.setKey(self.xAudio.keyz)
                window.setFreq(self.xAudio.freqz)
                window.setBars(self.xAudio.freqPure)

        time.sleep(0.005)

worker = AudioWorker()

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btnVar = 0;
        self.wdgtVar = 0;
        self.threadpool = QThreadPool()
        self.threadpool2 = QThreadPool()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)

        self.window.btnTuning.clicked.connect(lambda: self.mainBtnClick())

        self.window.btnAuto.clicked.connect(lambda: self.changeMode(0))
        self.window.btnLoFi.clicked.connect(lambda: self.changeMode(1))
        self.window.btnMiFi.clicked.connect(lambda: self.changeMode(2))
        self.window.btnHiFi.clicked.connect(lambda: self.changeMode(3))

        self.startThread()
        self.show()

    def setKey(self,key):
        self.window.lblKey.setText(str(key))

    def setFreq(self,freq):
        self.window.lblFreq.setText(str(freq))

    def setBars(self,freq):
        self.window.bar1.setMaximumHeight(freq-20)
        self.window.bar2.setMaximumHeight(freq-20)
        self.window.bar3.setMaximumHeight(freq-20)
        self.window.bar4.setMaximumHeight(freq-20)
        self.window.bar5.setMaximumHeight(freq-20)
        self.window.bar6.setMaximumHeight(freq-20)
        self.window.bar7.setMaximumHeight(freq-20)

    def changeMode(self, vari):
        self.window.wdgtvar = vari;
        if (vari == 0):
            self.window.lblAutoIcon.setPixmap(QtGui.QPixmap(":/svg/svg/cursor.svg"))
            self.window.lblLoFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblMiFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblHiFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.btnAuto.setStyleSheet("color: #ff9e0d;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnLoFi.setStyleSheet("color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnMiFi.setStyleSheet("color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnHiFi.setStyleSheet("color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")


        elif (vari == 1):
            self.window.lblAutoIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblLoFiIcon.setPixmap(QtGui.QPixmap(":/svg/svg/cursor.svg"))
            self.window.lblMiFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblHiFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.btnAuto.setStyleSheet(
                "color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnLoFi.setStyleSheet(
                "color: #ff9e0d;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnMiFi.setStyleSheet(
                "color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnHiFi.setStyleSheet(
                "color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")

        elif (vari == 2):
            self.window.lblAutoIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblLoFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblMiFiIcon.setPixmap(QtGui.QPixmap(":/svg/svg/cursor.svg"))
            self.window.lblHiFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.btnAuto.setStyleSheet(
                "color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnLoFi.setStyleSheet(
                "color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnMiFi.setStyleSheet(
                "color: #ff9e0d;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnHiFi.setStyleSheet(
                "color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")

        elif (vari == 3):
            self.window.lblAutoIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblLoFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblMiFiIcon.setPixmap(QtGui.QPixmap(""))
            self.window.lblHiFiIcon.setPixmap(QtGui.QPixmap(":/svg/svg/cursor.svg"))
            self.window.btnAuto.setStyleSheet("color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnLoFi.setStyleSheet("color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnMiFi.setStyleSheet("color: #747475;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")
            self.window.btnHiFi.setStyleSheet("color: #ff9e0d;\n""background-color: #e3e3e3;\n""border:0px solid white;\n""border-radius:15px;\n""font-size:11px;\n""padding:0 10px;\n""font-weight:300;")

    def startThread(self):
        self.threadpool.start(worker)

    def mainBtnClick(self):
        if (self.btnVar == 0):
            worker.startStream();
            self.window.btnTuning.setText("Tuning")
            self.window.lblKey.setStyleSheet("color: #ff9e0d;\n""font-size:80px;\n""font-weight:900;\n""margin:0 0;")
            self.window.btnTuning.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 166, 0, 255), stop:0.98 rgba(255, 231, 0, 255), stop:1 rgba(0, 0, 0, 0));border:0px;color:white;text-transform:uppercase;letter-spacing:10px;border-radius:5px;font-size:10px;")
            self.btnVar = 1

        elif(self.btnVar == 1):
            worker.stopStream();
            self.window.btnTuning.setText("Continue Tuning")
            self.window.lblKey.setText("N/A")
            self.window.lblFreq.setText("(Paused)")
            self.window.lblKey.setStyleSheet("color: rgba(8, 255, 68, 255);\n""font-size:80px;\n""font-weight:900;\n""margin:0 0;")
            self.window.btnTuning.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 255, 68, 255), stop:1 rgba(172, 255, 1, 255));\nfont-size:10px;\n""border:0px;\n""color:white;\n""text-transform:uppercase;\n""letter-spacing:10px;\n""border-radius:5px;")
            self.btnVar = 0



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())