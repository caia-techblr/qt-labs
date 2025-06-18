# This Python file uses the following encoding: utf-8
"""
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
import can

class CANReader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initCAN()

    def initUI(self):
        self.setWindowTitle('SocketCAN Reader')
        self.setGeometry(100, 100, 600, 400)

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def initCAN(self):
        self.bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
        self.notifier = can.Notifier(self.bus, [self])

    def on_message_received(self, msg):
        self.textEdit.append(f"Received: {msg}")

    def __call__(self, msg):
        self.on_message_received(msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    reader = CANReader()
    reader.show()
    sys.exit(app.exec())
