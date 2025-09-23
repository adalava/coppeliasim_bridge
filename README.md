# CoppeliaSim ROS2 Bridge

This package automatically scans CoppeliaSim looking for sensors and exposes them on ROS.

WARNING: this is an experimental package

## Currently Supported sensors

- Force
- Proximity

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
# ros2 launch coppeliasim_bridge coppeliasim_bridge_launch.py 
[INFO] [launch]: All log files can be found below /root/.ros/log/2025-09-23-13-39-56-341622-fedora-227
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [forcesensor-1]: process started with pid [230]
[INFO] [proximitysensor-2]: process started with pid [231]
[forcesensor-1] [INFO] [1758634796.759149464] [coppeliasim_bridge.forcesensor]: Connecting to CoppeliaSim...
[forcesensor-1] [INFO] [1758634796.759617660] [coppeliasim_bridge.forcesensor]: Retrieving force sensor objects...
[proximitysensor-2] [INFO] [1758634796.818703494] [coppeliasim_bridge.proximitysensor]: Connecting to CoppeliaSim...
[proximitysensor-2] [INFO] [1758634796.819072424] [coppeliasim_bridge.proximitysensor]: Retrieving proximity sensor objects...
[proximitysensor-2] [INFO] [1758634797.143599023] [coppeliasim_bridge.proximitysensor]: Creating publisher topic "myRobot/proximitySensor"
[forcesensor-1] [INFO] [1758634797.148392851] [coppeliasim_bridge.forcesensor]: Creating publisher topic "myRobot/bumperSensorFR"
[forcesensor-1] [INFO] [1758634797.158890887] [coppeliasim_bridge.forcesensor]: Creating publisher topic "myRobot/bumperSensorFL"
```


```bash
# ros2 topic list
/coppeliasim_bridge/myRobot/bumperSensorFL
/coppeliasim_bridge/myRobot/bumperSensorFR
/coppeliasim_bridge/myRobot/proximitySensor
/parameter_events
/rosout
```

```bash
# ros2 topic info  /coppeliasim_bridge/myRobot/bumperSensorFL
Type: geometry_msgs/msg/Wrench
Publisher count: 1
Subscription count: 0
```

```bash
# ros2 topic echo --once /coppeliasim_bridge/myRobot/bumperSensorFL
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
