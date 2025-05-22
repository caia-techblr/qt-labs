import QtQuick 2.6
import QtQuick.Window 2.2

Window {
    visible: true
    width: 320
    height: 320
    title: qsTr("Hello World")
	Rectangle {
	 id: outer
	 x: 10
	 y: 10
	 width: 300
	 height: width
	 color: "lightgreen"
	 radius: width/2
 
	 MouseArea {
  	 anchors.fill: parent
	  onClicked: {
	   Qt.quit(); //console.log("mouse clicked");		
	 }
  } 
}
}
