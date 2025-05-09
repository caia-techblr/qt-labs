# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel('Hello World!')
    label.show()
    sys.exit(app.exec())
