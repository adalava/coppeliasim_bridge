# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from coppeliasim_bridge.ForceSensor import ForceSensor
from rclpy.node import Node

from geometry_msgs.msg import Wrench

import time
        
class ForceSensorPublisher(Node):
    
    force_sensors = None
    publishers = {}

    def __init__(self):
        super().__init__('forcesensor_publisher')

        self.get_logger().info('Connecting to CoppeliaSim...')

        #self.get_logger().info('Loading scene...')
        #self.sim.loadScene('/root/Unicamp/roomba/roomba style.ttt')

        self.get_logger().info('Retrieving force sensor objects...')
        self.force_sensors  = ForceSensor()

        for sensor in self.force_sensors.get_sensors():
            self.get_logger().info('Creating publisher topic "{}"'.format(sensor))

            publisher = self.create_publisher(Wrench, sensor, 10)
            self.publishers[sensor] = publisher

            
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    

    def timer_callback(self):
        result = self.force_sensors.get_force_torque()

        for sensor in result:
            msg = Wrench()

            force = result[sensor]['force']
            torque = result[sensor]['torque']

            if force is None or torque is None: return
            msg.force.x = force[0]
            msg.force.y = force[1]
            msg.force.z = force[2]
            msg.torque.x = torque[0]
            msg.torque.y = torque[1]
            msg.torque.z = torque[2]

            self.publishers[sensor].publish(msg)
            #self.get_logger().info('Publishing: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)

    forcesensor_publisher = ForceSensorPublisher()

    rclpy.spin(forcesensor_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    forcesensor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
