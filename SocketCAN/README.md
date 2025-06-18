## SocketCAN steps
```
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
ip link show vcan0
```

## CAN Utils
```
sudo apt install can-utils
candump vcan0
cansend vcan0 125#41424344
```
