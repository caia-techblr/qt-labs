import QtQuick 2.6
import QtQuick.Window 2.2

Window {
    visible: true
    width: 300
    height: 200
    title: qsTr("Hello World")

    Rectangle {
        id: inner1
        x: 30; y: 20
        width: parent.width*0.8
        height: parent.height*0.8
        color: "lightsteelblue"
        radius: 8 
    }
}
