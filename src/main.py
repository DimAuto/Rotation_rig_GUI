from serial_comm import SerialComm
import time
import os
from PyQt5 import QtWidgets
from iris_emulator import Messager
from iris_emulator import Ui_MainWindow as UI
import sys



if __name__ == "__main__": 

    ser = SerialComm() 
    messager = Messager()
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = UI(ser, messager)
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(str(e))
        os._exit(-1)
    finally:
        os._exit(-1)
        