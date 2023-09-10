from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from manager import Handler
import time
from serial_comm import SerialComm
from tmc2130 import TMC2130
from threading import Thread

class Ui_MainWindow(object):

    def __init__(self, messager) -> None:
        self.manager_rig = None
        self.manager_iris = None
        self.rot_motor_driver = None
        self.inc_motor_driver = None
        self.messager = messager
        self.repeats = 1
        self.interval = 1
        self.cmd = 0
        self.data = []
        self.serial = SerialComm()
        self.iris_serial = SerialComm(stop_char="\r\n")
        self.ports = []
        self.serial_baud = 115200
        self.baud_list = ["9600", "19200", "115200", "921600"]
        self.messager.signal.connect(self.set_message)
        self.connected_flag = False
        self.iris_connected_flag = False
        self.stop_tx_flag = False

        self.rot_direction = 0
        self.inc_direction = 0
        self.rot_angle_hist = 0
        self.inc_angle_hist = 0
        self.inc_speed = 50
        self.rot_speed = 50
        self.messager.yaw.connect(self.set_yaw)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 835)
        MainWindow.setMinimumSize(QtCore.QSize(200, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.rot_motor_state)            # Rotation motor state change
        self.gridLayout.addWidget(self.checkBox, 2, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setMaximumSize(QtCore.QSize(200, 200))
        self.dial_2.setMaximum(100)
        self.dial_2.setObjectName("dial_2")
        self.gridLayout.addWidget(self.dial_2, 4, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.pressed.connect(self.rotate)
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.gridLayout.addWidget(self.pushButton_4, 11, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 3, 1, 1)
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setMaximumSize(QtCore.QSize(200, 200))
        self.dial.setMaximum(100)
        self.dial.setObjectName("dial")
        self.gridLayout.addWidget(self.dial, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 1, 5)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 11, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.scan_ports)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 9, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 9, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.pressed.connect(self.connect_toPort)          #RIG CONNECT BUTTON
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.inc_motor_state)            # Rotation motor state change
        self.gridLayout.addWidget(self.checkBox_2, 4, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 10, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 9, 4, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(200, 200))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 100, 18))
        self.radioButton_3.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.inc_setDirection)            # INC motor change direction
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 100, 18))
        self.radioButton_4.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.toggled.connect(self.inc_setDirection)            # INC motor change direction
        self.gridLayout.addWidget(self.groupBox_4, 4, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 100, 18))
        self.radioButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.rot_setDirection)            # Rot motor change direction
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 100, 18))
        self.radioButton.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.rot_setDirection)            # Rot motor change direction
        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 6, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.pressed.connect(self.connect_toIris)          # IRIS CONNECT BUTTON
        self.verticalLayout.addWidget(self.pushButton_5)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout.addWidget(self.lcdNumber_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.console = QtWidgets.QListWidget(self.centralwidget)
        self.console.setMaximumSize(QtCore.QSize(16777215, 300))
        self.console.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.console.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.console)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 22))
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
        self.checkBox.setText(_translate("MainWindow", "Rot. Motor Enabled"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pattern</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "GO"))
        self.pushButton_4.setText(_translate("MainWindow", "Go"))
        self.label_11.setText(_translate("MainWindow", "Direction"))
        self.label_7.setText(_translate("MainWindow", "          seconds X"))
        self.label_6.setText(_translate("MainWindow", "      degrees - per         "))
        self.label_5.setText(_translate("MainWindow", "Inclination Speed"))
        self.label.setText(_translate("MainWindow", "Rotation Degrees 0-360"))
        self.pushButton.setText(_translate("MainWindow", "Scan Ports"))
        self.label_2.setText(_translate("MainWindow", "Direction"))
        self.pushButton_2.setText(_translate("MainWindow", "CONNECT"))
        self.label_4.setText(_translate("MainWindow", "Rotation Speed"))
        self.label_3.setText(_translate("MainWindow", "Inclination Degrees 0-90"))
        self.checkBox_2.setText(_translate("MainWindow", "Inclin. Motor Enabled"))
        self.radioButton_3.setText(_translate("MainWindow", "Left"))
        self.radioButton_4.setText(_translate("MainWindow", "Right"))
        self.radioButton_2.setText(_translate("MainWindow", "Right"))
        self.radioButton.setText(_translate("MainWindow", "Left"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Iris Connection</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "CONNECT"))
        self.label_9.setText(_translate("MainWindow", "HEADING"))
        self.label_10.setText(_translate("MainWindow", "RIG ANGLE"))

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
        self.comboBox_3.clear()
        self.comboBox_3.addItems(self.ports)

    def connect_toIris(self):
        if self.iris_connected_flag == False:
            port = self.comboBox_3.currentText().split("|")[0][0:-1]
            self.iris_serial.device = port
            self.iris_serial.baud = self.serial_baud
            self.iris_serial.error = None
            self.iris_serial.serial_connect()
            if self.iris_serial.error is not None:
                self.log(f"Iris Connection: {self.iris_serial.error}", "red")
                self.pushButton_5.setStyleSheet("background-color: red")
                self.iris_connected_flag = False
            else:
                self.pushButton_5.setStyleSheet("background-color: green")
                self.manager_iris = Handler(self.iris_serial, self.messager, iris_flag=True)
                self.log("Connected to Iris", "green")
                self.iris_connected_flag = True
        else:
            self.log("Disconnecting from Iris", "red")
            self.iris_serial.serial_disconnect()
            self.iris_connected_flag = False
            del self.manager_iris
            self.pushButton_5.setStyleSheet("background-color: red")

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
            else:
                self.pushButton_2.setStyleSheet("background-color: green")
                self.manager_rig = Handler(self.serial, self.messager, iris_flag=False)
                self.rot_motor_driver = TMC2130(self.manager_rig, 0xB0)
                self.inc_motor_driver = TMC2130(self.manager_rig, 0xC0)
                self.log("Connected to Port", "green")
                self.connected_flag = True
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
        else:
            self.log("Disconnecting from Port", "red")
            self.messager.killsignal.emit(1)
            del self.manager_rig
            del self.rot_motor_driver
            del self.inc_motor_driver
            self.serial.serial_disconnect()
            self.connected_flag = False
            self.pushButton_2.setStyleSheet("background-color: red")
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)

    def rot_motor_state(self):
        if self.checkBox.isChecked():
            self.rot_motor_driver.enable_motor()
            self.log("Rotation Motor Enabled", "yellow")
        else:
            self.rot_motor_driver.disable_motor()
            self.log("Rotation Motor Disabled", "yellow")

    def inc_motor_state(self):
        if self.checkBox_2.isChecked():
            self.inc_motor_driver.enable_motor()
            self.log("Inclination Motor Enabled", "yellow")
        else:
            self.inc_motor_driver.disable_motor()
            self.log("Inclination Motor Disabled", "yellow")

    def rot_setDirection(self):
        if self.radioButton.isChecked():
            self.rot_direction = 0
            self.radioButton_2.setChecked(False)
        if self.radioButton_2.isChecked():
            self.rot_direction = 1
            self.radioButton.setChecked(False)

    def inc_setDirection(self):
        if self.radioButton_3.isChecked():
            self.inc_direction = 0
            self.radioButton_4.setChecked(False)
        if self.radioButton_4.isChecked():
            self.inc_direction = 1
            self.radioButton_3.setChecked(False)

    def update_history(self, rot_angle, inc_angle):
        self.rot_angle_hist += rot_angle
        self.inc_angle_hist += inc_angle
        self.lcdNumber_2.display(self.rot_angle_hist)

    def rotate(self):
        rot_angle = int(self.spinBox.value())
        inc_angle = int(self.spinBox_2.value())
        if self.rot_direction == 1:
            rot_angle *= -1
            self.rot_setDirection = 1
        else:
            self.rot_direction = 0
        if self.inc_direction == 1:
            inc_angle *= -1
            self.inc_setDirection = 1
        else:
            self.inc_setDirection = 0
        if (self.inc_angle_hist + inc_angle) in range(-40,40) and inc_angle != 0:
            self.inc_motor_driver.rotate(self.inc_speed, inc_angle)
        else:
            inc_angle = 0
        if (self.rot_angle_hist + rot_angle) in range(-360,360) and rot_angle != 0:
            self.rot_motor_driver.rotate(self.rot_speed, rot_angle)
        else:
            rot_angle = 0
        self.update_history(rot_angle, inc_angle)
        # Thread(target=self.transmit_iris_cmd,args=[]).start()

    def set_yaw(self, message):
        self.lcdNumber.display(message)
    
    def transmit_iris_cmd(self):
        if self.iris_connected_flag == True:
            st = time.time()
            while(1):
                if time.time() - st > 10:
                    break
                self.manager_iris.transmit_message("fcear\r\n")
                time.sleep(1)


    
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
    yaw = QtCore.pyqtSignal(str)
    pitch = QtCore.pyqtSignal(str)
