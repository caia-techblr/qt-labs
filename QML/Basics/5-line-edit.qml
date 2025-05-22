import QtQuick 2.6
import QtQuick.Window 2.2

Window {
    visible: true
    width: 400
    height: 300
    title: qsTr("Input Demo")
    Rectangle {
	  width: 100; 
	  height: 30
	  color: "lightsteelblue"
	  border.color: "gray"
      anchors.centerIn:parent
	  TextInput {
	  id: input
	  anchors.fill: parent
	  anchors.margins: 4
	  focus: true
	}
}
}
