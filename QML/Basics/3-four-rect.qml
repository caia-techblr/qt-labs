import QtQuick 2.0
Rectangle {
  id: root
  width: 240
  height: 240
  clip:true
  color: "lightsteelblue"
  border.color : "black"

  Rectangle {
    id:r1
    x:15
    y:15
    width: 100
    height: 100
    //color: "lightsteelblue"
    //border.color : "black"
 }
 Rectangle {
    id:r2
    x:125
    y:15
    width: 100
    height: 100
    //color: "lightsteelblue"
    //border.color : "black"
    radius : 10
 } 
 Rectangle {
    id:r3
    x:15
    y:140
    width: 80
    height: 80
    //color: "lightsteelblue"
    //border.color : "black"
    radius:25
    rotation: 45
 }
 Rectangle {
    id:r4
    x:125
    y:125
    width: 100
    height: 100
    //color: "lightsteelblue"
    //border.color : "black"
    radius: 50
 }
}
