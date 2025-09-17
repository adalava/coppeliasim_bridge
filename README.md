# CoppeliaSim ROS2 Bridge

This package automatically scans CoppeliaSim looking for sensors and exposes them; on ROS.

WARNING: this is an experimental package

## Supported sensors

- Force Sensor
- Proximity Sensor

## Compile

```bash
cd ~/ros2_ws
colcon build --packages-select coppeliasim_bridge
```

## Run

Prepare the ROS environment

```bash
cd ~/ros2_ws
source install/setup.bash
```

Open CoppeliaSim, load your scene file and start the ROS launcher:

```bash
ros2 launch coppeliasim_bridge coppeliasim_bridge_launch.py
```

---

Alternativelly you can start each sensor node individually:

#### Force Sensors
```bash
ros2 run coppeliasim_bridge forcesensor
```

#### ProximitySensors
```bash
ros2 run coppeliasim_bridge proximitysensor
```



### Output examples

```bash
# ros2 run coppeliasim_bridge forcesensor git status
[INFO] [1757976965.409606383] [forcesensor_publisher]: Connecting to CoppeliaSim...
[INFO] [1757976965.410039663] [forcesensor_publisher]: Retrieving force sensor objects...
[INFO] [1757976965.549490506] [forcesensor_publisher]: Creating publisher topic "myRobot/bumperSensorFR"
[INFO] [1757976965.552000081] [forcesensor_publisher]: Creating publisher topic "myRobot/bumperSensorFL"
```


```bash
# ros2 topic list
/myRobot/bumperSensorFL
/myRobot/bumperSensorFR
/parameter_events
/rosout
```

```bash
# ros2 topic info  /myRobot/bumperSensorFL
Type: geometry_msgs/msg/Wrench
Publisher count: 1
Subscription count: 0
```

```bash
# ros2 topic echo --once /myRobot/bumperSensorFL
force:
  x: 12.466093416038394
  y: -19.495147652595655
  z: 0.21915032349592795
torque:
  x: 0.0668506171626216
  y: -0.08524148580638342
  z: 0.3254280060297572
---
```