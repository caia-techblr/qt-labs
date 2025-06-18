
import QtQuick
import QtQuick.Window
import QtQuick.Controls 2.12


Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Column {
        Slider {
            id : tslider
            value : myweather.temperature
            from : 0
            to : 100
            onValueChanged: {
                myweather.temperature = value
            }
        }
        Slider {
            id : hslider
            value : myweather.humidity
            from : 0
            to : 100
            onValueChanged: {
                myweather.humidity = value
            }
        }
    }
}
