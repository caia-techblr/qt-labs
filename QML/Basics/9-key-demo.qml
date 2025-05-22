import QtQuick 2.0

Rectangle
{
	id:root
	width:400
	height:300
	Image {
		id: img
		source : "qt.png"
	}
    focus: true
    Keys.onLeftPressed: img.x -= 10
    Keys.onRightPressed: img.x += 10
    Keys.onUpPressed: img.y -= 10
    Keys.onDownPressed: img.y += 10
    Keys.onPressed: {
        switch(event.key) {
            case Qt.Key_Plus:
                img.scale += 0.2
                break;
            case Qt.Key_Minus:
                img.scale -= 0.2
                break;
        }
   }
}
