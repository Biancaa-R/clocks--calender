import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import time
import datetime
import winsound

class AlarmWindow(QDialog):
    def __init__(self):
        super(AlarmWindow, self).__init__()
        loadUi("alarm.ui",self)
        self.pushButton.clicked.connect(self.alarmprocess)

    def alarmprocess(self):
        if True:
            self.label_6.setText("")
        if True:
            self.label_5.setText("Alarm set successfully")
        hours=self.lineEdit.text()
        minutes=self.lineEdit.text()
        seconds=self.lineEdit.text()
        time=hours+":"+minutes+":"+seconds
        str(time)
        while True:
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            if current_time==time:
                winsound.Beep(500,500)
                self.label_5.setText("")
                if True:
                    self.label_6.setText("Alarm rung successfully")
                break

        


app = QApplication(sys.argv)
alarmwindow = AlarmWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(alarmwindow)
widget.setFixedHeight(750)
widget.setFixedWidth(1390)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")        
