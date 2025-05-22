import QtQuick 2.6
import QtQuick.Window 2.2

Window {
    visible: true
    width: 400
    height: 300
    title: qsTr("Hello World")

    Rectangle {
        id: inner1
        x: 10; y: 10
        width: parent.width-20
        height: parent.height-20
        color: "lightsteelblue"
        radius: 8 
        Text {
		    anchors.centerIn: parent
            text: "Hello QML"
            color: "#303030"
	        font.family: "Ubuntu"
            font.pixelSize: 28  
		}
    }
}
