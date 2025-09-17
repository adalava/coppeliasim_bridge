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
from coppeliasim_bridge.ProximitySensor import ProximitySensor
from rclpy.node import Node

from std_msgs.msg import Header
from sensor_msgs.msg import Range

import time

class ProximitySensorPublisher(Node):

    proximity_sensors = None
    publishers = {}

    def __init__(self):
        super().__init__('proximitysensor_publisher')

        self.get_logger().info('Connecting to CoppeliaSim...')

        #self.get_logger().info('Loading scene...')
        #self.sim.loadScene('/root/Unicamp/roomba/roomba style.ttt')

        self.get_logger().info('Retrieving proximity sensor objects...')
        self.proximity_sensors  = ProximitySensor()

        for sensor in self.proximity_sensors.get_sensors():
            self.get_logger().info('Creating publisher topic "{}"'.format(sensor))

            publisher = self.create_publisher(Range, sensor, 10)
            self.publishers[sensor] = publisher


        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0


    def timer_callback(self):
        result = self.proximity_sensors.get_data()

        for sensor in result:
            msg = Range()
            header_msg = Header()

            header_msg.stamp = self.get_clock().now().to_msg()
            msg.header = header_msg

            msg.max_range = result[sensor]['range']

            if result[sensor]['detected'] == 1:
                msg.range = result[sensor]['distance']
            else:
                msg.range = float('+Inf')

            self.publishers[sensor].publish(msg)
            #self.get_logger().info('Publishing: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)

    proximitysensor_publisher = ProximitySensorPublisher()

    rclpy.spin(proximitysensor_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    proximitysensor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
