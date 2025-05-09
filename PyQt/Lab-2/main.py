# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog,self).__init__(parent)

        self.layout = QVBoxLayout()
        self.firstInput = QLineEdit()
        self.secondInput = QLineEdit()
        self.resultDisplay = QLineEdit()
        submitButton = QPushButton("compute")
        clearButton = QPushButton("clear")

        self.layout.addWidget(self.firstInput)
        self.layout.addWidget(self.secondInput)
        self.layout.addWidget(self.resultDisplay)
        self.layout.addWidget(submitButton)
        self.layout.addWidget(clearButton)

        submitButton.clicked.connect(self.submit_button_clicked)
        clearButton.clicked.connect(self.clear_button_clicked)

        self.setLayout(self.layout)

        self.show()

    def submit_button_clicked(self):
        #print('clicked')
        first = self.firstInput.text()
        second = self.secondInput.text()
        res = int(first) + int(second)
        self.resultDisplay.setText(str(res))

    def clear_button_clicked(self):
        self.firstInput.clear()
        self.secondInput.clear()
        self.resultDisplay.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mydialog = MyDialog()
    #mydialog.show()
    #label = QLabel('Hello World!')
    #label.show()
    sys.exit(app.exec())
