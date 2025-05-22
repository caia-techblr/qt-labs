import QtQuick 2.0

Rectangle {
  id:root
  width:400
  height:300
  Timer {
    interval: 500
	running: true
	repeat: true
    onTriggered: display.text = Qt.formatTime(new Date(),"hh:mm:ss")
  }
  Text { 
	id: display 
    font.family: "ubuntu"
	font.bold:true
	font.pointSize:28
    anchors.centerIn:parent
  }
}
