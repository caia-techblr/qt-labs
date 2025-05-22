import QtQuick 2.6
import QtQuick.Window 2.2

Window {
    visible: true
    width: 400
    height: 300
    title: qsTr("Input Demo")
    Rectangle {
	  width: 200 
	  height: 100
	  color: "lightsteelblue"
	  border.color: "gray"
      anchors.centerIn:parent
	  TextEdit {
	  id: input
	  anchors.fill: parent
	  anchors.margins: 4
	  focus: true
	}
}
}
