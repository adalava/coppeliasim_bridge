# CoppeliaSim ROS2 Bridge

This package automatically scans CoppeliaSim looking from sensors and exposes it on ROS.

WARNING: this is an experimental package

## Supported sensors

- forcesensor

## Compile

```bash
cd ~/ros2_ws
colcon build --packages-select coppeliasim_bridge
```

## Run

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run coppeliasim_bridge forcesensor
```
