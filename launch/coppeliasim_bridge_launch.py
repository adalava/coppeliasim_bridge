from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='coppeliasim_bridge',
            namespace='coppeliasim_bridge',
            executable='forcesensor',
            name='forcesensor'
        ),
        Node(
            package='coppeliasim_bridge',
            namespace='coppeliasim_bridge',
            executable='proximitysensor',
            name='proximitysensor'
        )
    ])