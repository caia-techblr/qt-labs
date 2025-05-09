# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import QTimer, QTime
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLCDNumber

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog,self).__init__(parent)

        timer = QTimer(self)
        #timer.setTimeout(1000)
        timer.timeout.connect(self.show_time)
        timer.start(1000)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.lcdDisplay = QLCDNumber()
        self.lcdDisplay.setMinimumSize(300,200)
        self.lcdDisplay.setDigitCount(8)
        layout.addWidget(self.lcdDisplay)

        self.show()

    def show_time(self):
        print('timeout')
        now = QTime.currentTime()
        self.lcdDisplay.display(now.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mydialog = MyDialog()
    sys.exit(app.exec())
