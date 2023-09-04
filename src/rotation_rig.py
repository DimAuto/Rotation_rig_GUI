from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from manager import Handler
import time


class Ui_MainWindow(object):

    def __init__(self, ser, messager) -> None:
        self.manager = None
        self.messager = messager
        self.repeats = 1
        self.interval = 1
        self.cmd = 0
        self.data = []
        self.serial = ser
        self.ports = []
        self.serial_baud = 115200
        self.baud_list = ["9600", "19200", "115200", "921600"]
        self.messager.signal.connect(self.set_message)
        self.connected_flag = False
        self.stop_tx_flag = False


    class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 30, 261, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 75, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 30, 75, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 141, 20))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 300, 471, 81))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(90, 20, 81, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 20, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(250, 20, 47, 14))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 20, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(390, 20, 47, 14))
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 70, 471, 221))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(340, 30, 111, 18))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 160, 75, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 110, 91, 31))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.spinBox.setObjectName("spinBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(340, 110, 121, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.dial_2 = QtWidgets.QDial(self.groupBox_2)
        self.dial_2.setGeometry(QtCore.QRect(200, 100, 50, 64))
        self.dial_2.setMaximum(100)
        self.dial_2.setObjectName("dial_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.dial = QtWidgets.QDial(self.groupBox_2)
        self.dial.setGeometry(QtCore.QRect(200, 20, 50, 64))
        self.dial.setMaximum(100)
        self.dial.setObjectName("dial")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(190, 90, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(190, 10, 81, 16))
        self.label_4.setObjectName("label_4")
        self.console = QtWidgets.QListWidget(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(20, 390, 661, 111))
        self.console.setStyleSheet("background-color: rgb(59, 59, 59);\n"
        "font: 7pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 0, 0);")
        self.console.setObjectName("listWidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(500, 20, 181, 361))
        self.groupBox_3.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 50, 75, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 150, 101, 91))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(70, 130, 47, 14))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rotation Rig"))
        self.pushButton.setText(_translate("MainWindow", "Scan Ports"))
        self.pushButton_2.setText(_translate("MainWindow", "CONNECT"))
        self.label_2.setText(_translate("MainWindow", "Rotation Rig COM Port"))
        self.groupBox.setTitle(_translate("MainWindow", "Pattern"))
        self.label_6.setText(_translate("MainWindow", "degrees - per"))
        self.label_7.setText(_translate("MainWindow", "seconds -"))
        self.label_8.setText(_translate("MainWindow", "times"))
        self.pushButton_4.setText(_translate("MainWindow", "Go"))
        self.checkBox.setText(_translate("MainWindow", "Rot. Motor Enabled"))
        self.pushButton_3.setText(_translate("MainWindow", "GO"))
        self.checkBox_2.setText(_translate("MainWindow", "Inclin. Motor Enabled"))
        self.label.setText(_translate("MainWindow", "Rotation Degrees 0-360"))
        self.label_5.setText(_translate("MainWindow", "Inclination Speed"))
        self.label_3.setText(_translate("MainWindow", "Inclination Degrees 0-90"))
        self.label_4.setText(_translate("MainWindow", "Rotation Speed"))
        self.groupBox_3.setTitle(_translate("MainWindow", "IRIS Connection"))
        self.pushButton_5.setText(_translate("MainWindow", "CONNECT"))
        self.label_9.setText(_translate("MainWindow", "HEADING"))

    def configUI(self):
        self.comboBox_3.addItems(self.baud_list)
        self.scan_ports()
        self.comboBox.addItems(self.command_list)
        self.lineEdit.setText("00")
    
    def log(self, txt, color="yellow"):
        if "Received Message" in txt:
            if not self.checkBox_2.isChecked():
                return
        i = QtWidgets.QListWidgetItem(txt)
        i.setForeground(QColor(color))
        self.console.addItem(i)
        self.console.scrollToBottom()
        # if self.console.count() > 80:
        #     self.console.clear
        QApplication.processEvents()

    def set_message(self, message):
        self.log(str(message), "white")

    def clear_console(self):
        self.console.clear()

    def set_ports(self):
        self.ports = []
        for d in self.serial.list_ports():
            try:
                self.ports.append(" | ".join([d.device, d.serial_number]))
            except:
                pass

    def set_baud(self):
        self.serial_baud = int(self.comboBox_3.currentText())
        
    def stop_repeated_tx(self):
        self.manager.stop_tx_flag = True
    
    def start_repeated_tx(self):
        if self.manager == None:
            self.log("First Connect to a Device", "red")
        self.manager.set_max_repeats(self.repeats)
        self.manager.set_repeat_interval(self.interval)
        self.set_data()
        self.manager.set_tx_data(self.data)
        self.manager.set_tx_cmd(self.cmd)
        self.manager.repeated_tx_start()

    def repeated_tx(self):
        
        for i in range(0, self.repeats):
            if self.stop_tx_flag == True:
                break
            self.transmit_message()
            time.sleep(self.interval)
            QApplication.processEvents()

    def scan_ports(self):
        self.set_ports()
        self.comboBox_2.clear()
        self.comboBox_2.addItems(self.ports)

    def connect_toPort(self):
        if self.connected_flag == False:
            port = self.comboBox_2.currentText().split("|")[0][0:-1]
            self.serial.device = port
            self.serial.baud = self.serial_baud
            self.serial.error = None
            self.serial.serial_connect()
            if self.serial.error is not None:
                self.log(self.serial.error, "red")
                self.pushButton_2.setStyleSheet("background-color: red")
                self.connected_flag = False
                self.pushButton_3.setEnabled(False)
                self.pushButton_4.setEnabled(False)
                self.pushButton_stop.setEnabled(False)
                self.pushButton_vout.setEnabled(False)
            else:
                self.pushButton_2.setStyleSheet("background-color: green")
                self.manager = Handler(self.serial, self.messager)
                self.log("Connected to Port", "green")
                self.connected_flag = True
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_stop.setEnabled(True)
                self.pushButton_vout.setEnabled(True)
        else:
            self.log("Disconnecting from Port", "red")
            self.messager.killsignal.emit(1)
            del self.manager
            self.serial.serial_disconnect()
            self.connected_flag = False
            self.pushButton_2.setStyleSheet("background-color: red")
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_vout.setEnabled(False)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

class Messager(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    killsignal = QtCore.pyqtSignal(int)
