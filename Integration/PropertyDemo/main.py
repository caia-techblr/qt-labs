# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtCore import QObject, Property, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

class MyWeather(QObject):
    temperatureChanged = Signal(float)
    humidityChanged = Signal(float)
    def __init__(self,tval,hval):
        QObject.__init__(self)
        self.m_temperature=tval
        self.m_humidity=hval
    def getTemperature(self):
        return self.m_temperature
    def setTemperature(self, val):
        self.m_temperature=val
        self.temperatureChanged.emit(val)
        print(f"Temperature updated : {val}")
    def getHumidity(self):
        return self.m_humidity
    def setHumidity(self, val):
        self.m_humidity=val
        self.humidityChanged.emit(val)
        print(f"Humidity updated : {val}")
    temperature = Property(float,getTemperature,setTemperature, notify=temperatureChanged)
    humidity = Property(float, getHumidity, setHumidity, notify=humidityChanged)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    weather = MyWeather(24,72)
    engine.rootContext().setContextProperty("myweather", weather)
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
